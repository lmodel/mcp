#!/usr/bin/env python3
"""Write the LinkML schema of MCP from the version's schema.json and schema.ts.

MCP publishes each version's schema as TypeScript (schema.ts), which is the source, and as
JSON Schema 2020-12 (schema.json), which is generated from it. This script reads the pinned
copy of both under upstream/ and writes src/mcp/schema/mcp.yaml:

- Each definition in schema.json becomes the element that states it. An object becomes
  a class, a union of objects a class whose ``any_of`` names each member through ``is_a``,
  a string list an enum, and a string or a string-or-integer a type. Every object MCP
  publishes is open, so every class allows extra slots.
- Each property becomes an attribute of its class, with MCP's description, so a class
  states every key the definition has, inherited or not, as schema.json does. An
  inline object becomes a class of its own, named after its owner and key.
- schema.ts gives the rest: each interface's ``extends`` becomes ``is_a`` and
  ``mixins``, and its ``@category`` becomes a subset.
- Each class, enum and type maps exactly to the definition or the inline schema it
  renders, by a JSON pointer into the published file.

A key that is no Python name, such as ``$schema`` or ``io.modelcontextprotocol/clientInfo``,
goes under the attribute's ``aliases``, because gen-python writes an ``alias`` as an
attribute name. So does a key LOKF defines with another meaning, such as ``type`` or
``id`` (OWN_NAMES and lokf_naming below). scripts/mcp_meta.py writes each such key in
place of the attribute's name when it writes MCP's form.
Description text MCP leaves out is this project's, from DESCRIPTIONS below.

Usage::

    python scripts/mcp_to_linkml.py [--check]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
VERSION = "2026-07-28"
UPSTREAM = ROOT / "upstream" / "modelcontextprotocol" / "schema" / VERSION
OUTPUT = ROOT / "src" / "mcp" / "schema" / "mcp.yaml"
PREFIX = "Mcp"
MAPPING_PREFIX = "mcp_schema"
MAPPING_BASE = (
    "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/"
    f"{VERSION}/schema/{VERSION}/schema.json#/$defs/"
)

# Definitions that name a scalar: a type each, with the datatype its values take.
SCALAR_TYPES = {"Cursor", "ResultType"}
UNION_TYPES = {"RequestId", "ProgressToken"}
# JSON values: any JSON in this schema, which is wider than MCP's form (see
# parity/structural.yaml), since LinkML states no recursive union of a value's kinds.
ANY_VALUE = "JSONValue"
# An array definition: LinkML has no element for it, and no MCP definition names it.
SKIPPED = {"JSONArray"}

# Rules MCP's own words state and its schema.json does not: by definition, the keys of
# which at least one must be present, and the sentence that says so. Each becomes the
# class's any_of, and parity/probes.yaml lists it as narrower than MCP's file.
RULES = {
    "InputRequiredResult": (
        ("inputRequests", "requestState"),
        "At least one of `inputRequests` or `requestState` MUST be present.",
    ),
}

# String formats MCP uses, and the type that carries each.
FORMAT_TYPES = {
    "uri": "uri",
    "byte": f"{PREFIX}Base64",
    "uri-template": f"{PREFIX}UriTemplate",
}

# This project's words, where MCP gives an element none: by "Definition.key" first, then
# by key. MCP's own text is carried unchanged everywhere else.
DESCRIPTIONS = {
    "jsonrpc": "The JSON-RPC version, always `2.0`.",
    "method": "The name of the method.",
    "type": "The kind of value the field takes.",
    "params": "The parameters the message carries.",
    "result": "What the request returned.",
    "error": "The error the request ended with.",
    "requestState": (
        "State the server returned with an input-required result, sent back unchanged "
        "when the request is retried."
    ),
    "InputRequiredResult.requestState": (
        "State for the client to send back unchanged when it retries the request."
    ),
    "content": "The content the message carries.",
    "resource": "The resource's contents, as text or as binary data.",
    "contents": "The contents of the resource that was read.",
    "ref": "What the completion is for: a prompt or a resource template.",
    "completion": "The completion values and whether more are available.",
    "stopSequences": "Sequences at which the model should stop generating.",
    "temperature": "The sampling temperature the server asks the model to use.",
    "default": "The value the field takes when the user gives none.",
    "description": "A description of the field for the user.",
    "title": "A title for the field.",
    "minimum": "The smallest value the field accepts.",
    "maximum": "The largest value the field accepts.",
    "minLength": "The fewest characters the field accepts.",
    "maxLength": "The most characters the field accepts.",
    "format": "The format the string must have.",
    "enum": "The values the field offers.",
    "$schema": "The JSON Schema dialect the schema is written in.",
    "properties": "The fields of the form, by name.",
    "required": "The names of the fields the user must fill in.",
    "form": "Settings for elicitation by form.",
    "url": "Settings for elicitation by URL.",
    "data": "Details of the error.",
}
CONST_DESCRIPTIONS = {
    "method": "The method's name, always `{}`.",
    "type": "The kind of object, always `{}`.",
    "code": "The error code, always `{}`.",
    "jsonrpc": "The JSON-RPC version, always `{}`.",
}


def pascal(key: str) -> str:
    """anyOf -> AnyOf, io.modelcontextprotocol/clientInfo -> ClientInfo."""
    key = key.split("/")[-1].lstrip("_$")
    return key[:1].upper() + key[1:]


def snake(key: str) -> str:
    """The attribute name for a key: inputSchema -> input_schema, _meta -> meta,
    io.modelcontextprotocol/clientInfo -> mcp_client_info."""
    if key == "_meta":
        return "meta"
    if key == "$schema":
        return "schema_dialect"
    if key.startswith("io.modelcontextprotocol/"):
        return "mcp_" + snake(key.split("/", 1)[1])
    return re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", key).lower()


# Keys that LOKF also defines. Where MCP's meaning is LOKF's, the key is a slot of the
# schema's own with the schema.org IRI LOKF gives it. Every class whose key has that
# meaning shares the slot, as lmodel/calm's name and description are shared, and each
# class states its own description of the key in slot_usage. Where the meaning differs,
# the attribute takes a name of its own and lists MCP's key under aliases, so a
# composite with LOKF never projects MCP's key under LOKF's IRI.
SHARED_SLOTS = {
    "name": {
        "slot_uri": "schema:name",
        "description": "The name a program uses to refer to the thing.",
    },
    "title": {
        "slot_uri": "schema:name",
        "description": "A name for people to read.",
    },
    "description": {
        "slot_uri": "schema:description",
        "description": "A description for people to read.",
    },
    "url": {
        "slot_uri": "schema:url",
        "range": "uri",
        "description": "A URL.",
    },
    "version": {
        "slot_uri": "schema:version",
        "description": "A version string.",
    },
}
OWN_NAMES = {
    "type": "kind",
    "id": "identifier",
    "audience": "intended_audience",
    "context": "context_info",
    "reason": "reason_text",
    "resource": "resource_contents",
}


def shared_slot(key: str, prop: dict) -> bool:
    """Whether a property is one of SHARED_SLOTS: the key, as a plain string, or as a
    URL where the slot's range is uri."""
    if key not in SHARED_SLOTS or set(prop) - {"type", "description", "format"}:
        return False
    wanted = "uri" if SHARED_SLOTS[key].get("range") == "uri" else None
    return prop.get("type") == "string" and prop.get("format") == wanted


def lokf_naming(key: str, prop: dict) -> tuple[str, str | None]:
    """The attribute's name and IRI for a key LOKF also defines with another meaning,
    else (snake(key), None). A url that holds a capability's settings is not LOKF's url;
    a required flag is schema:valueRequired, as LOKF's is, and a list of required names
    is not LOKF's required."""
    if key in OWN_NAMES:
        return OWN_NAMES[key], None
    if key == "url":
        return "url_settings", None
    if key == "required":
        if prop.get("type") == "boolean":
            return key, "schema:valueRequired"
        return "required_names", None
    return snake(key), None


def subset_name(category: str) -> str:
    """`tools/list` -> tools_list, Common Types -> common_types."""
    return re.sub(r"[^a-z0-9]+", "_", category.strip("`").lower()).strip("_")


def read_typescript(text: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Each declaration's @category, and the parents an interface extends or a type names."""
    categories: dict[str, str] = {}
    parents: dict[str, list[str]] = {}
    for doc, name in re.findall(
        r"/\*\*((?:(?!\*/).)*?)\*/\s*export\s+(?:interface|type)\s+(\w+)", text, re.S
    ):
        match = re.search(r"@category\s+(.+)", doc)
        if match:
            categories[name] = match.group(1).strip()
    for name, clause in re.findall(
        r"export\s+interface\s+(\w+)\s*(?:extends\s+([^{]+))?\{", text
    ):
        found = []
        depth, item = 0, ""
        for char in clause + ",":
            if char == "<":
                depth += 1
            elif char == ">":
                depth -= 1
            if char == "," and depth == 0:
                ident = re.search(r"(?:\w+<\s*)?(\w+)", item.strip())
                if ident:
                    found.append(ident.group(1))
                item = ""
            else:
                item += char
        parents[name] = found
    for name, target in re.findall(r"export\s+type\s+(\w+)\s*=\s*(\w+)\s*;", text):
        parents[name] = [target]
    return categories, parents


class Converter:
    def __init__(
        self, defs: dict, categories: dict[str, str], parents: dict[str, list[str]]
    ):
        self.defs = defs
        self.categories = categories
        self.parents = parents
        self.classes: dict[str, dict] = {}
        self.enums: dict[str, dict] = {}
        self.types: dict[str, dict] = {}
        self.subsets: dict[str, dict] = {}
        self.enum_names = self._name_inline_enums()

    # Names -------------------------------------------------------------------------------

    def _kind(self, name: str) -> str:
        node = self.defs[name]
        if name in SKIPPED:
            return "skipped"
        if name in SCALAR_TYPES or name in UNION_TYPES:
            return "type"
        if "enum" in node:
            return "enum"
        return "class"

    def _name_inline_enums(self) -> dict[tuple[str, str], str]:
        """An inline value list takes its key's name when every owner offers the same values
        under it, and its owner's and key's names otherwise."""
        uses: dict[str, set] = {}
        found = []

        def walk(node, owner):
            for key, prop in (node.get("properties") or {}).items():
                if "enum" in prop:
                    uses.setdefault(key, set()).add(tuple(prop["enum"]))
                    found.append((owner, key))
                walk(prop, owner + pascal(key))
                walk(prop.get("items") or {}, owner + pascal(key))

        for name, node in self.defs.items():
            walk(node, name)
        owners: dict[str, set] = {}
        for owner, key in found:
            owners.setdefault(key, set()).add(owner)
        return {
            (owner, key): PREFIX
            + (
                pascal(key)
                if len(uses[key]) == 1 and len(owners[key]) > 1
                else owner + pascal(key)
            )
            for owner, key in found
        }

    def ref(self, node: dict) -> str | None:
        target = node.get("$ref")
        return target.rsplit("/", 1)[-1] if target else None

    # Elements ----------------------------------------------------------------------------

    def subset_of(self, name: str) -> list[str]:
        category = self.categories.get(name)
        if not category:
            return []
        key = subset_name(category)
        self.subsets.setdefault(
            key,
            {
                "title": category.strip("`"),
                "description": f"The definitions schema.ts files under {category}.",
            },
        )
        return [key]

    def convert(self) -> None:
        for name, node in self.defs.items():
            kind = self._kind(name)
            if kind == "type":
                self.add_type(name, node)
            elif kind == "enum":
                self.add_enum(
                    PREFIX + name, node["enum"], node.get("description"), name, name
                )
            elif kind == "class":
                self.add_class(name, node)
        self.add_format_types()

    def add_type(self, name: str, node: dict) -> None:
        element = {"description": node["description"]}
        if name in UNION_TYPES:
            element |= {
                "typeof": "string",
                "union_of": ["string", "integer"],
                "comments": [
                    "linkml 1.12.1's JSON Schema generator reads a type's typeof and not its "
                    "union_of, so each slot that takes this value states the union in its "
                    "own any_of."
                ],
            }
        else:
            element["typeof"] = "string"
        element["exact_mappings"] = [f"{MAPPING_PREFIX}:{name}"]
        self.types[PREFIX + name] = element

    def add_format_types(self) -> None:
        self.types[f"{PREFIX}Base64"] = {
            "typeof": "string",
            "uri": "xsd:base64Binary",
            "description": "Binary data, written as base64 text.",
            "comments": ["MCP gives such a string the format byte."],
        }
        self.types[f"{PREFIX}UriTemplate"] = {
            "typeof": "string",
            "description": "A URI template, as RFC 6570 defines one.",
            "comments": ["MCP gives such a string the format uri-template."],
        }

    def add_enum(self, name, values, description, pointer, owner) -> None:
        if name in self.enums:
            return
        element = {
            "description": description
            or f"The values MCP allows for `{pointer.split('/')[-1]}`.",
            "exact_mappings": [f"{MAPPING_PREFIX}:{pointer}"],
        }
        subsets = self.subset_of(owner)
        if subsets:
            element["in_subset"] = subsets
        element["permissible_values"] = {value: {} for value in values}
        self.enums[name] = element

    def add_class(self, name: str, node: dict) -> None:
        cls_name = PREFIX + name
        element: dict = {}
        description = node.get("description") or self.class_text(name)
        element["description"] = description
        parents = [
            p
            for p in self.parents.get(name, [])
            if p in self.defs and self._kind(p) == "class"
        ]
        target = self.ref(node)
        if target and not parents:
            parents = [target]
        if parents:
            element["is_a"] = PREFIX + parents[0]
            if parents[1:]:
                element["mixins"] = [PREFIX + p for p in parents[1:]]
        subsets = self.subset_of(name)
        if subsets:
            element["in_subset"] = subsets
        if name == ANY_VALUE:
            element["class_uri"] = "linkml:Any"
            element["comments"] = [
                "Any JSON value. MCP's schema.json leaves out null and numbers with a "
                "fraction, which schema.ts allows; this class takes any JSON."
            ]
        self.fill(cls_name, element, node, name, name)
        if name in RULES:
            keys, sentence = RULES[name]
            element["any_of"] = [
                {"slot_conditions": {snake(key): {"value_presence": "PRESENT"}}}
                for key in keys
            ]
            element.setdefault("comments", []).append(
                f"MCP's description states this rule, which its schema.json does not: {sentence}"
            )
        element["exact_mappings"] = [f"{MAPPING_PREFIX}:{name}"]
        self.classes[cls_name] = self.order(element)

    def class_text(self, name: str) -> str:
        node = self.defs[name]
        if "anyOf" in node:
            members = ", ".join(
                f"`{self.ref(b)}`" for b in node["anyOf"] if self.ref(b)
            )
            return f"One of {members}."
        if name == "JSONObject":
            return "A JSON object, whose values are JSON values."
        return f"MCP's `{name}`."

    def order(self, element: dict) -> dict:
        keys = (
            "description",
            "comments",
            "is_a",
            "mixins",
            "class_uri",
            "in_subset",
            "exact_mappings",
            "any_of",
            "extra_slots",
            "slots",
            "slot_usage",
            "attributes",
        )
        return {k: element[k] for k in keys if k in element} | {
            k: v for k, v in element.items() if k not in keys
        }

    def fill(
        self, cls_name: str, element: dict, node: dict, owner: str, pointer: str
    ) -> None:
        """Give a class the any_of, extra slots and attributes its node states."""
        if "anyOf" in node and all(self.ref(b) for b in node["anyOf"]):
            element["any_of"] = [{"is_a": PREFIX + self.ref(b)} for b in node["anyOf"]]
        extra = node.get("additionalProperties")
        if isinstance(extra, dict) and extra:
            element["extra_slots"] = {
                "range_expression": self.branch(
                    self.expression(
                        extra, cls_name, "value", pointer + "/additionalProperties"
                    )
                )
            }
        else:
            element["extra_slots"] = {"allowed": True}
        required = set(node.get("required") or [])
        attributes = {}
        for key, prop in (node.get("properties") or {}).items():
            if shared_slot(key, prop):
                element.setdefault("slots", []).append(key)
                usage = {"description": self.prop_text(key, prop, owner)}
                if key in required:
                    usage["required"] = True
                element.setdefault("slot_usage", {})[key] = usage
                continue
            attributes.update(
                self.attribute(
                    key,
                    prop,
                    key in required,
                    cls_name,
                    owner,
                    f"{pointer}/properties/{key}",
                )
            )
        if attributes:
            element["attributes"] = attributes

    def attribute(self, key, prop, required, cls_name, owner, pointer) -> dict:
        slot: dict = {"description": self.prop_text(key, prop, owner)}
        name, iri = lokf_naming(key, prop)
        if iri:
            slot["slot_uri"] = iri
        if name != key:
            if (
                key.isidentifier()
                and key not in OWN_NAMES
                and key not in ("url", "required")
            ):
                slot["alias"] = key
            else:
                slot["aliases"] = [key]
        slot |= self.expression(prop, cls_name, key, pointer)
        if required:
            slot["required"] = True
        return {name: slot}

    def prop_text(self, key: str, prop: dict, owner: str) -> str:
        if prop.get("description"):
            return prop["description"]
        if "const" in prop and key in CONST_DESCRIPTIONS:
            return CONST_DESCRIPTIONS[key].format(prop["const"])
        target = self.ref(prop) or self.ref(prop.get("items") or {})
        if target and self.defs[target].get("description"):
            return self.defs[target]["description"]
        return DESCRIPTIONS.get(f"{owner}.{key}") or DESCRIPTIONS[key]

    def inline_class(self, cls_name, key, node, pointer, parent=None, text=None) -> str:
        name = cls_name + pascal(key)
        if name[len(PREFIX) :] in self.defs:
            raise ValueError(f"{name} would be MCP's own definition's name")
        element: dict = {
            "description": text
            or f"The object MCP's `{pointer.split('/')[0]}` holds under `{key}`."
        }
        if parent:
            element["is_a"] = parent
        owner = pointer.split("/")[0]
        subsets = self.subset_of(owner)
        if subsets:
            element["in_subset"] = subsets
        self.fill(name, element, node, owner, pointer)
        element["exact_mappings"] = [f"{MAPPING_PREFIX}:{pointer}"]
        self.classes[name] = self.order(element)
        return name

    def expression(self, node: dict, cls_name: str, key: str, pointer: str) -> dict:
        """The slot expression that states a property's schema."""
        keywords = {"$ref", "const", "enum", "anyOf", "allOf", "type", "properties"}
        if not keywords & node.keys():
            return {"range": PREFIX + ANY_VALUE}
        target = self.ref(node)
        if target:
            if target in UNION_TYPES:
                return {"any_of": [{"range": "string"}, {"range": "integer"}]}
            return {"range": PREFIX + target}
        if "const" in node:
            if node.get("type") == "integer":
                return {"range": "integer", "equals_number": node["const"]}
            return {"equals_string": node["const"]}
        if "enum" in node:
            owner = pointer.split("/")[0]
            ancestry = cls_name[len(PREFIX) :]
            enum_name = (
                self.enum_names.get((ancestry, key)) or self.enum_names[(owner, key)]
            )
            self.add_enum(enum_name, node["enum"], None, pointer, owner)
            return {"range": enum_name}
        if "anyOf" in node:
            branches = []
            for branch in node["anyOf"]:
                if isinstance(branch.get("type"), list):
                    branches += [
                        self.expression({"type": t}, cls_name, key, pointer)
                        for t in branch["type"]
                    ]
                else:
                    branches.append(self.expression(branch, cls_name, key, pointer))
            return {"any_of": [self.branch(b) for b in branches]}
        if "allOf" in node:
            base, part = node["allOf"]
            text = (
                f"MCP's `{self.ref(base)}`, with the code and data this error carries."
            )
            return {
                "range": self.inline_class(
                    cls_name,
                    key,
                    part,
                    f"{pointer}/allOf/1",
                    PREFIX + self.ref(base),
                    text,
                )
            }
        kind = node.get("type")
        if isinstance(kind, list):
            return {
                "any_of": [
                    self.branch(self.expression({"type": t}, cls_name, key, pointer))
                    for t in kind
                ]
            }
        if kind == "array":
            items = self.expression(node["items"], cls_name, key, pointer + "/items")
            out = {"multivalued": True} | items
            if node.get("minItems") is not None:
                out["minimum_cardinality"] = node["minItems"]
            if node.get("maxItems") is not None:
                out["maximum_cardinality"] = node["maxItems"]
            if self._inlined(items):
                out["inlined_as_list"] = True
            return out
        if kind == "object":
            if "properties" in node:
                return {
                    "range": self.inline_class(
                        cls_name, key, node, pointer, text=node.get("description")
                    )
                }
            extra = node.get("additionalProperties")
            if isinstance(extra, dict) and extra:
                return {
                    "range": self.inline_class(
                        cls_name, key, node, pointer, text=node.get("description")
                    )
                }
            return {"range": f"{PREFIX}JSONObject"}
        if kind == "string":
            fmt = node.get("format")
            return {"range": FORMAT_TYPES[fmt]} if fmt else {}
        if kind in ("integer", "boolean"):
            out = {"range": kind}
        elif kind == "number":
            out = {"range": "float"}
        else:
            raise ValueError(f"no rule for {pointer}: {json.dumps(node)[:200]}")
        if "minimum" in node:
            out["minimum_value"] = node["minimum"]
        if "maximum" in node:
            out["maximum_value"] = node["maximum"]
        return out

    @staticmethod
    def branch(expression: dict) -> dict:
        """A branch of an any_of, or an extra slots range, names its range even when it is the
        default string, since a branch with no range reads as no constraint."""
        if "range" not in expression and "any_of" not in expression:
            return {"range": "string"} | expression
        return expression

    def _inlined(self, expression: dict) -> bool:
        ranges = [expression.get("range")] + [
            b.get("range") for b in expression.get("any_of", [])
        ]
        return any(
            r in self.classes
            or (
                r
                and r.startswith(PREFIX)
                and r[len(PREFIX) :] in self.defs
                and self._kind(r[len(PREFIX) :]) == "class"
            )
            for r in ranges
        )


def header() -> dict:
    return {
        "id": "https://w3id.org/lmodel/mcp",
        "name": "mcp",
        "title": f"Model Context Protocol (MCP) {VERSION}",
        "description": (
            f"The messages and objects of the Model Context Protocol, version {VERSION}, as "
            "its schema.json states them: JSON-RPC requests, results, notifications and "
            "errors, and the tools, resources, prompts, content and capabilities they carry. "
            "Generated from MCP's own files by scripts/mcp_to_linkml.py."
        ),
        "license": "Apache-2.0",
        "version": VERSION,
        "source": (
            "https://github.com/modelcontextprotocol/modelcontextprotocol/tree/"
            f"{VERSION}/schema/{VERSION}"
        ),
        "see_also": [
            "https://lmodel.github.io/mcp",
            f"https://modelcontextprotocol.io/specification/{VERSION}",
        ],
        "prefixes": {
            "mcp": "https://w3id.org/lmodel/mcp/",
            "linkml": "https://w3id.org/linkml/",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "schema": "http://schema.org/",
            MAPPING_PREFIX: MAPPING_BASE,
        },
        "default_prefix": "mcp",
        "default_range": "string",
        "imports": ["linkml:types"],
    }


class _Dumper(yaml.SafeDumper):
    """Indent lists under their key, as the family's YAML lint asks, and write long text
    as a folded block."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _text(dumper, value):
    if "\n" in value:
        return dumper.represent_scalar("tag:yaml.org,2002:str", value, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", value)


_Dumper.add_representer(str, _text)


def render() -> str:
    defs = json.loads((UPSTREAM / "schema.json").read_text(encoding="utf-8"))["$defs"]
    categories, parents = read_typescript(
        (UPSTREAM / "schema.ts").read_text(encoding="utf-8")
    )
    converter = Converter(defs, categories, parents)
    converter.convert()
    schema = header()
    schema["subsets"] = dict(sorted(converter.subsets.items()))
    schema["types"] = dict(sorted(converter.types.items()))
    schema["slots"] = {
        key: {
            k: v
            for k, v in sorted(
                SHARED_SLOTS[key].items(), key=lambda kv: kv[0] != "description"
            )
        }
        for key in sorted(SHARED_SLOTS)
    }
    schema["enums"] = dict(sorted(converter.enums.items()))
    schema["classes"] = dict(sorted(converter.classes.items()))
    body = yaml.dump(
        schema, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=88
    )
    return (
        "# Written by scripts/mcp_to_linkml.py from upstream/modelcontextprotocol/schema/"
        f"{VERSION}/.\n# Do not edit by hand: change the script and run `just gen-mcp`.\n---\n"
        + body
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="Exit 1 if the schema is stale"
    )
    args = parser.parse_args(argv)
    text = render()
    if args.check:
        if OUTPUT.read_text(encoding="utf-8") != text:
            print(
                f"{OUTPUT.relative_to(ROOT)} is stale: run `just gen-mcp`",
                file=sys.stderr,
            )
            return 1
        return 0
    OUTPUT.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
