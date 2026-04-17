#!/usr/bin/env python3
"""Validate a vendor MCP JSON fixture against the LinkML schema.

Replaces ``linkml-validate`` for vendor testing to work around limitations
in the installed linkml version:

  1. ``extra_slots: allowed: true`` is not honoured by ``JsonSchemaGenerator``
     — all classes get ``additionalProperties: false`` unless their
     ``class_uri`` is ``linkml:Any``.

  2. ``$ref`` + ``anyOf`` as siblings is invalid in JSON Schema Draft 7:
     the ``$ref`` wins and the ``anyOf`` is silently ignored.  This breaks
     any slot whose LinkML ``any_of`` union generates ``{"$ref": "...",
     "anyOf": [...]}`` in the property schema.

  3. A bare ``type: <scalar>`` alongside an ``anyOf`` that expresses multiple
     types (e.g. string | integer) over-constrains the union.
"""

import argparse
import json
import sys
from pathlib import Path

from linkml.generators.jsonschemagen import JsonSchemaGenerator
import jsonschema
from jsonschema.exceptions import best_match


# ---------------------------------------------------------------------------
# Classes that should allow additional properties beyond those declared.
# These correspond to LinkML classes that carry ``extra_slots: allowed: true``
# or are structurally open in the MCP spec.
# ---------------------------------------------------------------------------
OPEN_CLASSES = {
    "JsonSchema",         # vendor uses "required", "$schema", etc.
    "SchemaItems",        # vendor may carry arbitrary schema keywords
    "SchemaProperties",   # vendor property maps may use any key
    "ArgumentMap",        # prompt/tool arguments are free-form key→string maps
    "ContentBlock",       # tool_use / tool_result blocks carry extra keys
    # Capability classes — the spec says none of these are closed sets
    "ClientCapabilities",
    "ServerCapabilities",
    "ElicitationCapability",   # carries mode flags: form, url, etc.
    "SamplingCapability",      # carries: context, tools, etc.
    "RootsCapability",
    "PromptsCapability",
    "ResourcesCapability",
    "ToolsCapability",         # carries: call, etc.
    "TasksCapability",
    "TaskRequestCapabilities",
    "ExtensionsCapability",    # dotted extension keys like io.foo/bar
    "ExtensionAppCapability",
    # Misc open bags
    "MetaObject",
    "ElicitationContent",
    "ToolInput",
    "StructuredContentData",
    "LogData",
    "LogDetails",
    "ErrorData",
}


# ---------------------------------------------------------------------------
# Schema post-processing helpers
# ---------------------------------------------------------------------------

def _walk_and_fix(obj: object) -> None:
    """Walk *obj* in-place and apply two JSON Schema Draft-7 correctness fixes.

    Fix 1 — ``$ref`` alongside ``anyOf``:
        In Draft 7 a ``$ref`` causes all sibling keywords to be ignored.
        When LinkML emits ``{"$ref": "...", "anyOf": [...]}`` the ``anyOf``
        is never evaluated.  Remove the ``$ref`` so that ``anyOf`` takes effect.

    Fix 2 — scalar ``type`` alongside a multi-type ``anyOf``:
        When a slot has ``any_of: [{range: string}, {range: integer}]`` the
        generator produces ``{"type": "string", "anyOf": [...]}`` where the
        ``type: string`` rejects integers before ``anyOf`` can accept them.
        Remove the scalar ``type`` when ``anyOf`` already encodes multiple
        concrete types.
    """
    if isinstance(obj, list):
        for item in obj:
            _walk_and_fix(item)
        return

    if not isinstance(obj, dict):
        return

    # Fix 1
    if "$ref" in obj and "anyOf" in obj:
        del obj["$ref"]

    # Fix 2
    if "type" in obj and "anyOf" in obj and isinstance(obj["type"], str):
        any_of_non_null_types = [
            item["type"]
            for item in obj["anyOf"]
            if isinstance(item, dict) and "type" in item and item["type"] != "null"
        ]
        if len(any_of_non_null_types) > 1:
            del obj["type"]

    for v in list(obj.values()):
        _walk_and_fix(v)


def patch_schema(schema: dict, target_class: str | None = None) -> dict:
    """Post-process *schema* (generated JSON Schema dict) for vendor validation."""
    defs = schema.get("$defs", {})

    # Open classes that accept additional properties in $defs (nested references)
    for cls_name in OPEN_CLASSES:
        if cls_name in defs:
            defs[cls_name]["additionalProperties"] = True

    # When the target class is open, the top-level schema IS that class definition
    # (JsonSchemaGenerator inlines the top_class at root, not under $defs).
    # We must also open the root schema itself.
    if target_class in OPEN_CLASSES:
        schema["additionalProperties"] = True

    # Fix Draft-7 structural issues throughout
    _walk_and_fix(schema)

    return schema


# ---------------------------------------------------------------------------
# Per-class schema generation (cached between files of the same class)
# ---------------------------------------------------------------------------

_schema_cache: dict[str, dict] = {}


def _get_patched_schema(target_class: str, schema_path: str) -> dict:
    cache_key = f"{schema_path}::{target_class}"
    if cache_key in _schema_cache:
        return _schema_cache[cache_key]

    gen = JsonSchemaGenerator(
        schema=schema_path,
        mergeimports=True,
        top_class=target_class,
        not_closed=False,
        include_range_class_descendants=True,
    )
    # JsonSchemaGenerator.generate() returns a JsonSchema (dict subclass).
    # json.dumps handles dict subclasses natively.
    raw = gen.generate()
    schema_dict: dict = json.loads(json.dumps(raw))
    schema_dict = patch_schema(schema_dict, target_class)
    _schema_cache[cache_key] = schema_dict
    return schema_dict


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_file(json_path: str | Path, target_class: str, schema_path: str) -> list[str]:
    """Validate *json_path* against *target_class*.  Returns error messages."""
    with open(json_path) as f:
        instance = json.load(f)

    schema_dict = _get_patched_schema(target_class, schema_path)
    validator_cls = jsonschema.validators.validator_for(
        schema_dict, default=jsonschema.Draft7Validator
    )
    validator = validator_cls(schema_dict, format_checker=validator_cls.FORMAT_CHECKER)

    errors: list[str] = []
    for error in validator.iter_errors(instance):
        best_err = best_match([error])
        path = "/" + "/".join(str(p) for p in best_err.absolute_path)
        errors.append(f"{best_err.message} in {path}")

    return errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate a vendor MCP JSON fixture against the LinkML schema."
    )
    parser.add_argument("json_file", help="Path to the JSON fixture to validate.")
    parser.add_argument(
        "--target-class", "-C", required=True, help="LinkML class name to validate against."
    )
    parser.add_argument(
        "--schema", "-s", default="src/mcp/schema/mcp.yaml",
        help="Path to the LinkML schema YAML file."
    )
    args = parser.parse_args()

    errors = validate_file(args.json_file, args.target_class, args.schema)

    if errors:
        for msg in errors:
            print(f"[ERROR] [{args.json_file}/0] {msg}")
        sys.exit(1)
    else:
        print(f"[OK] {args.json_file}")


if __name__ == "__main__":
    main()
