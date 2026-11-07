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
  ``mixins``, each ``@category`` a subset, ``@internal`` the subset internal, and each
  ``@deprecated`` tag the ``deprecated`` of what it tags. Where schema.ts gives a
  property a type MCP defines and schema.json writes the type out, the type is the range.
- Each class and enum, and each type but the two format types, maps exactly to the
  definition or the inline schema it renders, by a JSON pointer into the published file.

A key that is no Python name, such as ``$schema`` or ``io.modelcontextprotocol/clientInfo``,
goes under the attribute's ``aliases``, because gen-python writes an ``alias`` as an
attribute name. So does a key LOKF defines with another meaning, such as ``type`` or
``id`` (OWN_NAMES and lokf_naming below). scripts/mcp_meta.py writes each such key in
place of the attribute's name when it writes MCP's form.
Where MCP gives no description, the words are this project's: CLASS_DESCRIPTIONS,
CONST_DESCRIPTIONS and DESCRIPTIONS below, and the sentences that name a union's members
or where MCP holds an inline object.

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

# Deprecations MCP states in words. A definition's description that says to use another
# in its place, by definition: the replacement and the sentence. And the values a
# property's @deprecated tag names, by the property's place in schema.json; each value
# takes the tag's text.
CLASS_DEPRECATIONS = {
    "LegacyTitledEnumSchema": (
        "TitledSingleSelectEnumSchema",
        "Use {@link TitledSingleSelectEnumSchema} instead.\n"
        "This interface will be removed in a future version.",
    ),
}
VALUE_DEPRECATIONS = {
    "CreateMessageRequestParams/properties/includeContext": ("thisServer", "allServers"),
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
# This project's words for a definition MCP leaves undescribed and that is no union of
# others, which takes the names of its members.
CLASS_DESCRIPTIONS = {
    "BlobResourceContents": "A resource's contents as binary data, given as base64 text.",
    "BooleanSchema": "A field of an elicitation form that takes true or false.",
    "Error": "The error a JSON-RPC error response carries: a code, a message and any data.",
    "InputResponseRequestParams": (
        "The parameters of a request the client retries after an input-required result: "
        "its responses to the server's requests, and the state the server returned."
    ),
    "JSONObject": "A JSON object, whose values are JSON values.",
    "JSONValue": "Any JSON value: a string, a number, a boolean, null, an object or an array.",
    "Notification": "The method and the parameters a notification carries.",
    "NumberSchema": "A field of an elicitation form that takes a number or an integer.",
    "PaginatedRequest": "A request for a list that the server returns a page at a time.",
    "PaginatedResult": "A result that holds a page of a list, and the cursor of the next page.",
    "Request": "The method and the parameters a request carries.",
    "StringSchema": "A field of an elicitation form that takes text.",
    "TextResourceContents": "A resource's contents as text.",
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


class TypeScript:
    """What schema.ts says that schema.json leaves out. A declaration is named as in
    schema.ts, and an interface's own property by (interface, key)."""

    def __init__(self) -> None:
        self.categories: dict[str, str] = {}
        self.internal: set[str] = set()
        self.deprecated: dict[str, str] = {}
        self.deprecated_keys: dict[tuple[str, str], str] = {}
        # Each interface's own keys, and those whose type is one declaration's name, such as
        # resultType: ResultType.
        self.keys: dict[str, set[str]] = {}
        self.key_types: dict[tuple[str, str], str] = {}
        self.parents: dict[str, list[str]] = {}

    def of_key(self, table: dict, name: str, key: str):
        """What a table holds for a key of a declaration, read from the nearest declaration
        of the key in the declaration or the interfaces it extends."""
        queue, seen = [name], set()
        while queue:
            current = queue.pop(0)
            if (current, key) in table or key in self.keys.get(current, ()):
                return table.get((current, key))
            if current not in seen:
                seen.add(current)
                queue += self.parents.get(current, [])
        return None


def _blanked(text: str) -> tuple[str, list[tuple[int, int]]]:
    """schema.ts with every comment and the inside of every string turned to spaces, at the
    same offsets, so a brace or a colon in either counts for nothing; and the span of each
    doc comment."""
    chars = list(text)
    docs = []
    i = 0
    while i < len(text):
        if text.startswith("//", i):
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
        elif text.startswith("/*", i):
            end = text.index("*/", i + 2) + 2
            if text.startswith("/**", i) and end - i > 4:
                docs.append((i, end))
        elif text[i] in "\"'`":
            start, end = i + 1, i + 1
            while text[end] != text[i]:
                end += 2 if text[end] == "\\" else 1
            chars[start:end] = [" " if c != "\n" else c for c in text[start:end]]
            i = end + 1
            continue
        else:
            i += 1
            continue
        chars[i:end] = [" " if c != "\n" else c for c in text[i:end]]
        i = end
    return "".join(chars), docs


def _tag(doc: str, name: str) -> str | None:
    """The text of a doc comment's tag, up to the next tag, on one line; "" for a tag with
    no text, and None when the comment has no such tag."""
    lines = [re.sub(r"^\s*\*?\s?", "", line) for line in doc.splitlines()]
    for i, line in enumerate(lines):
        if re.match(rf"@{name}\b", line.strip()):
            words = [line.strip()[len(name) + 1 :]]
            for rest in lines[i + 1 :]:
                if rest.strip().startswith("@"):
                    break
                words.append(rest)
            return " ".join(" ".join(words).split())
    return None


def read_typescript(text: str) -> TypeScript:
    """Each declaration's @category, @internal and @deprecated tags, each interface
    property's @deprecated tag and the declaration its type names, and the parents an
    interface extends or a type names. A doc comment documents the declaration or the
    property that follows it, past any line comment, as TypeScript reads it. A
    @deprecated tag anywhere else, such as on a property of an inline object, stops the
    script, so no deprecation is lost."""
    ts = TypeScript()
    code, docs = _blanked(text)
    depth, level = [], 0
    for char in code:
        depth.append(level)
        level += {"{": 1, "}": -1}.get(char, 0)
    bodies = []
    for match in re.finditer(r"export\s+interface\s+(\w+)[^{]*\{", code):
        start = match.end() - 1
        end = start + 1
        while code[end] != "}" or depth[end] != depth[start] + 1:
            end += 1
        bodies.append((match.group(1), start, end))

    def interface_at(offset: int) -> str | None:
        for name, start, end in bodies:
            if start < offset < end and depth[offset] == depth[start] + 1:
                return name
        return None

    key = re.compile(r'("[^"\n]*"|[A-Za-z_$][\w$]*)\s*\??\s*:\s*')
    for name, start, end in bodies:
        for match in key.finditer(code, start + 1, end):
            if interface_at(match.start()) == name:
                prop = text[match.start(1) : match.end(1)].strip('"')
                ts.keys.setdefault(name, set()).add(prop)
                found = re.match(r"([A-Za-z_]\w*)\s*;", code[match.end() : end])
                if found:
                    ts.key_types[(name, prop)] = found.group(1)
    attached = 0
    for start, end in docs:
        doc = text[start + 3 : end - 2]
        after = re.compile(r"\s*").match(code, end).end()
        declaration = re.compile(r"export\s+(?:interface|type)\s+(\w+)").match(
            code, after
        )
        prop = key.match(code, after)
        deprecated = _tag(doc, "deprecated")
        if declaration and depth[after] == 0:
            name = declaration.group(1)
            category = _tag(doc, "category")
            if category:
                ts.categories[name] = category
            if _tag(doc, "internal") is not None:
                ts.internal.add(name)
            if deprecated is not None:
                ts.deprecated[name] = deprecated
                attached += 1
        elif prop and deprecated is not None and interface_at(after):
            owner = interface_at(after)
            ts.deprecated_keys[(owner, text[prop.start(1) : prop.end(1)].strip('"'))] = (
                deprecated
            )
            attached += 1
    if attached != len(re.findall(r"@deprecated\b", text)):
        raise ValueError("schema.ts has a @deprecated tag on something this script skips")
    for name, clause in re.findall(
        r"export\s+interface\s+(\w+)\s*(?:extends\s+([^{]+))?\{", code
    ):
        found = []
        nesting, item = 0, ""
        for char in clause + ",":
            if char == "<":
                nesting += 1
            elif char == ">":
                nesting -= 1
            if char == "," and nesting == 0:
                ident = re.search(r"(?:\w+<\s*)?(\w+)", item.strip())
                if ident:
                    found.append(ident.group(1))
                item = ""
            else:
                item += char
        ts.parents[name] = found
    for name, target in re.findall(r"export\s+type\s+(\w+)\s*=\s*(\w+)\s*;", code):
        ts.parents[name] = [target]
    return ts


class Converter:
    def __init__(self, defs: dict, ts: TypeScript):
        self.defs = defs
        self.ts = ts
        self.parents = ts.parents
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
        """The subset of a definition's @category, and internal for one schema.ts tags
        @internal."""
        found = []
        tags = [(self.ts.categories.get(name), "@category {}")]
        tags.append(("internal" if name in self.ts.internal else None, "@internal"))
        for value, tag in tags:
            if value:
                title = value.strip("`")
                self.subsets.setdefault(
                    subset_name(title),
                    {
                        "title": title,
                        "description": f"The definitions schema.ts tags `{tag.format(title)}`.",
                    },
                )
                found.append(subset_name(title))
        return found

    def deprecate(self, element: dict, text: str | None) -> None:
        if text is not None:
            element["deprecated"] = text

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
        subsets = self.subset_of(name)
        if subsets:
            element["in_subset"] = subsets
        self.deprecate(element, self.ts.deprecated.get(name))
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
        self.deprecate(element, self.ts.deprecated.get(pointer))
        element["permissible_values"] = {value: {} for value in values}
        if pointer in VALUE_DEPRECATIONS:
            owner_name, _, key = pointer.partition("/properties/")
            text = self.ts.deprecated_keys[(owner_name, key)]
            for value in VALUE_DEPRECATIONS[pointer]:
                element["permissible_values"][value]["deprecated"] = text
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
        self.deprecate(element, self.ts.deprecated.get(name))
        if name in CLASS_DEPRECATIONS:
            replacement, sentence = CLASS_DEPRECATIONS[name]
            element["deprecated"] = sentence.replace("\n", " ")
            element["deprecated_element_has_possible_replacement"] = (
                f"mcp:{PREFIX}{replacement}"
            )
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
        """This project's words for a definition MCP leaves undescribed: CLASS_DESCRIPTIONS,
        or for a union of definitions, the names of its members."""
        node = self.defs[name]
        if name in CLASS_DESCRIPTIONS:
            return CLASS_DESCRIPTIONS[name]
        members = [f"`{self.ref(b)}`" for b in node.get("anyOf", [])]
        if members and all(m != "`None`" for m in members):
            return f"One of {', '.join(members)}."
        raise ValueError(f"MCP gives {name} no description: add one to CLASS_DESCRIPTIONS")

    def order(self, element: dict) -> dict:
        keys = (
            "description",
            "comments",
            "deprecated",
            "deprecated_element_has_possible_replacement",
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
                if pointer == owner:
                    self.deprecate(
                        usage, self.ts.of_key(self.ts.deprecated_keys, owner, key)
                    )
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
        own = pointer == f"{owner}/properties/{key}"
        if own:
            self.deprecate(slot, self.ts.of_key(self.ts.deprecated_keys, owner, key))
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
        named = self.ts.of_key(self.ts.key_types, owner, key) if own else None
        if (
            named in SCALAR_TYPES
            and set(prop) <= {"type", "description"}
            and prop.get("type") == self.defs[named].get("type")
        ):
            # schema.json writes the type out in place, as for resultType: ResultType.
            slot["range"] = PREFIX + named
        else:
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
            held = " and ".join(k for k in ("code", "data") if k in part["properties"])
            text = f"MCP's `{self.ref(base)}`, with the {held} this error carries."
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
    """Indent lists under their key, as the family's YAML lint asks, and write text that
    spans lines as a literal block, so MCP's line breaks stay where MCP put them."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _text(dumper, value):
    if "\n" in value:
        return dumper.represent_scalar("tag:yaml.org,2002:str", value, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", value)


_Dumper.add_representer(str, _text)


def render() -> str:
    defs = json.loads((UPSTREAM / "schema.json").read_text(encoding="utf-8"))["$defs"]
    ts = read_typescript((UPSTREAM / "schema.ts").read_text(encoding="utf-8"))
    converter = Converter(defs, ts)
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
