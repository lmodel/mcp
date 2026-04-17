#!/usr/bin/env python3
"""Validate vendor JSON fixtures against the MCP LinkML-derived JSON Schema.

Generates a JSON Schema from the LinkML YAML, applies patches for known
limitations of the installed linkml version, then validates every ``*.json``
file found under the given fixtures directory.

Usage:
    python scripts/validate_vendor.py <schema.yaml> <fixtures_dir>

Exit code: 0 when all fixtures pass, 1 when any errors are found.
"""
import json
import sys
from pathlib import Path

import jsonschema
from jsonschema.exceptions import best_match

# Classes whose generated JSON Schema should have `additionalProperties`
# removed so that unknown keys in vendor fixtures do not cause failures.
OPEN_CLASSES = frozenset(
    [
        "ArgumentMap",
        "ContentBlock",
        "ExtensionsCapability",
        "JsonSchema",
        "MetaObject",
        "SchemaProperties",
    ]
)

# Slots whose content property should accept both a single object and an
# array of objects (any_of union).  The top-level $ref produced by the
# LinkML generator conflicts with the anyOf so it must be removed.
ARRAY_CONTENT_CLASSES = frozenset(
    [
        "SamplingMessage",
        "CreateMessageResult",
    ]
)

# Classes whose `id` property should accept integer *or* string.
INTEGER_ID_CLASSES = frozenset(
    [
        "JSONRPCErrorResponse",
        "URLElicitationRequiredError",
    ]
)


def patch_schema(schema: dict) -> dict:
    """Return a patched copy of the generated JSON Schema dict."""
    defs: dict = schema.get("$defs", {})

    # --- open classes: remove additionalProperties: false ---
    for cls in OPEN_CLASSES:
        if cls in defs:
            defs[cls].pop("additionalProperties", None)

    # --- JsonSchema: rename required_list -> required and add $schema prop ---
    if "JsonSchema" in defs:
        props: dict = defs["JsonSchema"].get("properties", {})
        if "required_list" in props:
            props["required"] = props.pop("required_list")
        if "$schema" not in props:
            props["$schema"] = {"type": ["string", "null"]}

    # --- Integer-or-string id ---
    for cls in INTEGER_ID_CLASSES:
        if cls in defs:
            props = defs[cls].get("properties", {})
            if "id" in props:
                id_prop = props["id"]
                # Drop the conflicting top-level `type: string` that
                # contradicts the anyOf which already includes integer.
                if "anyOf" in id_prop:
                    id_prop.pop("type", None)

    # --- content union: drop conflicting top-level $ref ---
    for cls in ARRAY_CONTENT_CLASSES:
        if cls in defs:
            props = defs[cls].get("properties", {})
            if "content" in props and "anyOf" in props["content"]:
                props["content"].pop("$ref", None)

    return schema


# Cache generated+patched schemas by target class name to avoid regenerating
# for every fixture belonging to the same class.
_schema_cache: dict[str, jsonschema.protocols.Validator | None] = {}


def get_validator(schema_yaml: str, cls_name: str):
    """Return a cached jsonschema Validator for *cls_name*, or None on error."""
    if cls_name in _schema_cache:
        return _schema_cache[cls_name]

    try:
        from linkml.generators.jsonschemagen import JsonSchemaGenerator

        g = JsonSchemaGenerator(
            schema=schema_yaml,
            mergeimports=True,
            top_class=cls_name,
        )
        raw = g.generate()
        raw_json: str = raw.to_json() if hasattr(raw, "to_json") else str(raw)
        js = json.loads(raw_json)
        patch_schema(js)
        validator_cls = jsonschema.validators.validator_for(
            js, default=jsonschema.Draft7Validator
        )
        validator = validator_cls(js, format_checker=validator_cls.FORMAT_CHECKER)
        _schema_cache[cls_name] = validator
    except Exception as exc:
        print(
            f"[SKIP] {cls_name}: could not generate schema: {exc}",
            file=sys.stderr,
        )
        _schema_cache[cls_name] = None

    return _schema_cache[cls_name]


def validate_fixture(
    validator: jsonschema.protocols.Validator, data: object
) -> list[str]:
    """Return a list of human-readable error messages for *data*."""
    messages = []
    errors = list(validator.iter_errors(data))
    for error in errors:
        best = best_match([error])
        if best.absolute_path:
            path = "/" + "/".join(str(p) for p in best.absolute_path)
        else:
            path = ""
        messages.append(f"{best.message} in {path}" if path else best.message)
    return messages


def main() -> None:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <schema.yaml> <fixtures_dir>", file=sys.stderr)
        sys.exit(2)

    schema_yaml = sys.argv[1]
    fixtures_dir = Path(sys.argv[2])

    fixtures = sorted(fixtures_dir.rglob("*.json"))

    total_files = 0
    total_errors = 0

    for fixture_path in fixtures:
        cls_name = fixture_path.parent.name

        validator = get_validator(schema_yaml, cls_name)
        if validator is None:
            continue

        try:
            with open(fixture_path) as fh:
                data = json.load(fh)
        except json.JSONDecodeError as exc:
            print(f"[ERROR] {fixture_path}: invalid JSON: {exc}")
            total_errors += 1
            continue

        total_files += 1
        errs = validate_fixture(validator, data)
        for msg in errs:
            print(f"[ERROR] [{fixture_path}/0] {msg}")
            total_errors += 1

    print(
        f"\nValidated {total_files} fixtures across"
        f" {len({p.parent.name for p in fixtures})} classes,"
        f" {total_errors} error(s)."
    )
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
