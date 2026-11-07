#!/usr/bin/env python3
"""Write MCP's schema.json from the LinkML model.

gen-json-schema writes definitions under the model's names, and MCP's file carries MCP's.
This script runs the generator once and shapes its output into MCP's form, in
meta/schema.json:

- A class, enum or type whose exact mapping names a definition of MCP's takes that name
  (``McpCallToolRequest`` maps to ``mcp_schema:CallToolRequest``). One whose mapping names a
  place inside a definition (an inline object or value list) is written inline wherever it
  is used, as MCP writes it.
- A key that an attribute lists under ``aliases``, such as ``$schema`` or
  ``io.modelcontextprotocol/clientInfo``, is the property's key in meta/schema.json.
- A string type gives its format: ``McpBase64`` is ``byte``, ``McpUriTemplate``
  ``uri-template``, and each type that maps to a definition becomes that definition.
- A class that is a union of others is written as MCP writes one, an ``anyOf`` of
  references and nothing else.
- ``$schema`` is draft 2020-12.

linkml 1.12.1's generator needs three repairs here, each a fault of the generator:

- an ``any_of`` of classes and an ``extra_slots`` range still admit ``null`` despite
  ``include_null=False``;
- ``linkml:Any`` leaves out arrays;
- a class's ``any_of`` conditions name slots, not the keys their aliases give.

MCP's files never allow ``null``, so every ``null`` the generator writes is removed, the
any-value class becomes ``{}``, and each condition names the key. Usage::

    python scripts/mcp_meta.py [--output FILE] [--check]
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "mcp" / "schema" / "mcp.yaml"
OUTPUT = ROOT / "meta" / "schema.json"
DRAFT = "https://json-schema.org/draft/2020-12/schema"
MAPPING_PREFIX = "mcp_schema:"
FORMATS = {"McpBase64": "byte", "McpUriTemplate": "uri-template"}
DEFS = "#/$defs/"


SUBSCHEMA_LISTS = ("anyOf", "oneOf", "allOf")
SUBSCHEMAS = ("items", "additionalProperties", "not", "if", "then", "else")
SUBSCHEMA_MAPS = ("properties", "$defs", "patternProperties")


def _walk(node, visit):
    """Call visit on every schema in a JSON Schema tree, children first. A key of
    ``properties`` is a name, never a keyword, even when it reads ``anyOf``."""
    if not isinstance(node, dict):
        return
    for keyword in SUBSCHEMA_LISTS:
        for branch in node.get(keyword) or []:
            _walk(branch, visit)
    for keyword in SUBSCHEMAS:
        if isinstance(node.get(keyword), dict):
            _walk(node[keyword], visit)
    for keyword in SUBSCHEMA_MAPS:
        for child in (node.get(keyword) or {}).values():
            _walk(child, visit)
    visit(node)


def published_name(element) -> str | None:
    """The MCP definition an element renders, or None when it renders a place inside one."""
    for mapping in element.exact_mappings or []:
        if mapping.startswith(MAPPING_PREFIX):
            local = mapping[len(MAPPING_PREFIX) :]
            return None if "/" in local else local
    return None


def _drop_null(node: dict) -> None:
    if isinstance(node.get("type"), list):
        kinds = [k for k in node["type"] if k != "null"]
        node["type"] = kinds[0] if len(kinds) == 1 else kinds
    for keyword in ("anyOf", "oneOf"):
        if keyword in node:
            branches = [b for b in node[keyword] if b != {"type": "null"}]
            for i, branch in enumerate(branches):
                # {"anyOf": [X]} left by a dropped null branch is X.
                if set(branch) == {"anyOf"} and len(branch["anyOf"]) == 1:
                    branches[i] = branch["anyOf"][0]
            node[keyword] = branches
    if set(node) == {"anyOf"} and len(node["anyOf"]) == 1:
        only = node.pop("anyOf")[0]
        node.update(only)


def build() -> dict:
    view = SchemaView(str(SCHEMA))
    generated = json.loads(
        JsonSchemaGenerator(
            str(SCHEMA), include_null=False, mergeimports=True
        ).serialize()
    )
    defs = generated["$defs"]

    # Keys an attribute lists under aliases, by the attribute's name.
    keys: dict[str, str] = {}
    for cls in view.all_classes().values():
        for attr in (cls.attributes or {}).values():
            if attr.aliases:
                (key,) = attr.aliases
                if keys.setdefault(attr.name, key) != key:
                    raise ValueError(
                        f"{attr.name} lists two keys: {keys[attr.name]}, {key}"
                    )

    # Formats, by class and property key.
    formats: dict[tuple[str, str], str] = {}
    for name in view.all_classes():
        for slot in view.class_induced_slots(name):
            if slot.range in FORMATS:
                formats[(name, slot.alias or slot.name)] = FORMATS[slot.range]

    # Each class's key for each of its slots, for the conditions of its any_of.
    class_keys: dict[str, dict[str, str]] = {}
    for name in view.all_classes():
        class_keys[name] = {}
        for slot in view.class_induced_slots(name):
            key = slot.alias or (slot.aliases[0] if slot.aliases else slot.name)
            class_keys[name][slot.name] = key

    names: dict[str, str | None] = {}
    for element in list(view.all_classes().values()) + list(view.all_enums().values()):
        names[element.name] = published_name(element)

    for name, body in defs.items():
        body.pop("title", None)
        if body.get("description") == "":
            body.pop("description")
        if body.get("additionalProperties") is True:
            body.pop("additionalProperties")
        if (
            body.get("type") == "object"
            and "anyOf" in body
            and "properties" not in body
        ):
            body.pop("type")
        for (cls, key), fmt in formats.items():
            if cls == name and key in body.get("properties", {}):
                body["properties"][key]["format"] = fmt
        props = body.get("properties", {})
        for slot, key in keys.items():
            if slot in props:
                props[key] = props.pop(slot)
            if slot in body.get("required", []):
                body["required"] = [key if r == slot else r for r in body["required"]]
        for keyword in ("anyOf", "oneOf", "allOf"):
            for branch in body.get(keyword) or []:
                if "required" in branch and name in class_keys:
                    rename = class_keys[name]
                    branch["required"] = [rename.get(r, r) for r in branch["required"]]
                    branch["properties"] = {
                        rename.get(k, k): v
                        for k, v in branch.get("properties", {}).items()
                    }
        if "properties" in body:
            body["properties"] = dict(sorted(body["properties"].items()))
        if "required" in body:
            body["required"] = sorted(body["required"])

    any_value = [
        n for n, c in view.all_classes().items() if c.class_uri == "linkml:Any"
    ]
    for name in any_value:
        defs[name] = (
            {"description": defs[name]["description"]}
            if defs[name].get("description")
            else {}
        )

    for body in defs.values():
        _walk(body, _drop_null)

    # Rename the published definitions and inline the rest.
    inline = {
        n: defs[n] for n, published in names.items() if published is None and n in defs
    }

    def resolve(node: dict) -> None:
        ref = node.get("$ref", "")
        if ref.startswith(DEFS):
            target = ref[len(DEFS) :]
            if target in inline:
                del node["$ref"]
                body = copy.deepcopy(inline[target])
                for key, value in body.items():
                    node.setdefault(key, value)
            elif names.get(target):
                node["$ref"] = DEFS + names[target]

    # An inline class may hold another, so inline until nothing changes.
    for _ in range(10):
        before = json.dumps(defs, sort_keys=True)
        for body in defs.values():
            _walk(body, resolve)
        if json.dumps(defs, sort_keys=True) == before:
            break
    else:
        raise ValueError("inlining did not settle")

    out = {names[n]: body for n, body in defs.items() if names.get(n)}
    for name, element in view.all_types().items():
        published = published_name(element)
        if published and name in view.all_types(imports=False):
            kinds = element.union_of or [element.typeof]
            types = ["string" if k == "string" else "integer" for k in kinds]
            out[published] = {"description": element.description} | {
                "type": types[0] if len(types) == 1 else types
            }
    return {"$schema": DRAFT, "$defs": dict(sorted(out.items()))}


def render() -> str:
    return json.dumps(build(), indent=4, ensure_ascii=False) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument(
        "--check", action="store_true", help="Exit 1 if the file is stale"
    )
    args = parser.parse_args(argv)
    text = render()
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != text:
            print(f"{args.output} is stale: run `just gen-mcp`", file=sys.stderr)
            return 1
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
