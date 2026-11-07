"""Checks the schema against MCP's files, and the generated files against the schema."""

import importlib.util
import json
import re
import subprocess
import sys
from functools import cache

import yaml

from mcp_parity import PUBLISHED, ROOT

SCHEMA = ROOT / "src" / "mcp" / "schema" / "mcp.yaml"
TYPESCRIPT = PUBLISHED.parent / "schema.ts"
MAPPING_PREFIX = "mcp_schema:"


def _schema():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def _published():
    return json.loads(PUBLISHED.read_text(encoding="utf-8"))["$defs"]


def _node(pointer: str):
    """The part of MCP's file a mapping names, such as Tool/properties/inputSchema."""
    node = _published()
    for part in pointer.split("/"):
        node = node[int(part)] if isinstance(node, list) else node[part]
    return node


def _elements():
    doc = _schema()
    for kind in ("classes", "enums", "types"):
        yield from (doc.get(kind) or {}).items()


def test_schema_is_what_the_converter_writes():
    """src/mcp/schema/mcp.yaml is scripts/mcp_to_linkml.py's output, unedited."""
    script = ROOT / "scripts" / "mcp_to_linkml.py"
    run = subprocess.run([sys.executable, str(script), "--check"], capture_output=True)
    assert run.returncode == 0, run.stderr.decode()


def test_meta_is_what_the_writer_writes():
    """meta/schema.json is scripts/mcp_meta.py's output for the schema."""
    script = ROOT / "scripts" / "mcp_meta.py"
    run = subprocess.run([sys.executable, str(script), "--check"], capture_output=True)
    assert run.returncode == 0, run.stderr.decode()


def test_every_element_maps_to_a_place_in_mcps_file():
    """Each class, enum and type maps exactly to one place in the pinned schema.json, and
    that place exists."""
    for name, element in _elements():
        mappings = element.get("exact_mappings") or []
        if name in ("McpBase64", "McpUriTemplate"):
            assert not mappings, name
            continue
        assert len(mappings) == 1 and mappings[0].startswith(MAPPING_PREFIX), name
        assert _node(mappings[0][len(MAPPING_PREFIX) :]) is not None, name


def test_mcps_descriptions_are_kept_word_for_word():
    """Where MCP describes a definition or a property, the schema carries the same text, on
    the element, on an attribute or in a class's slot_usage."""
    checked = 0
    for name, element in _elements():
        mappings = element.get("exact_mappings") or []
        if not mappings:
            continue
        pointer = mappings[0][len(MAPPING_PREFIX) :]
        node = _node(pointer)
        if node.get("description") and "/" not in pointer:
            assert element["description"] == node["description"], name
            checked += 1
        texts = {}
        for attr_name, slot in (element.get("attributes") or {}).items():
            key = slot.get("alias") or (slot.get("aliases") or [attr_name])[0]
            texts[key] = slot["description"]
        for key, usage in (element.get("slot_usage") or {}).items():
            texts[key] = usage["description"]
        for key, prop in (node.get("properties") or {}).items():
            if prop.get("description"):
                assert texts[key] == prop["description"], (name, key)
                checked += 1
    assert checked > 300


@cache
def _converter():
    spec = importlib.util.spec_from_file_location(
        "converter_rules", ROOT / "scripts" / "mcp_to_linkml.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _by_definition():
    """Each element that renders a definition, by the definition's name."""
    return {
        element["exact_mappings"][0][len(MAPPING_PREFIX) :]: element
        for _, element in _elements()
        if element.get("exact_mappings")
        and "/" not in element["exact_mappings"][0][len(MAPPING_PREFIX) :]
    }


def _tagged(tag: str):
    """Where schema.ts puts a doc comment's tag, read line by line, independently of the
    converter's reader: (declaration, None, text) for a declaration, and (interface, key,
    text) for a property, which is indented by two spaces."""
    lines = TYPESCRIPT.read_text(encoding="utf-8").splitlines()
    interface = None
    for i, line in enumerate(lines):
        declared = re.match(r"export (?:interface|type) (\w+)", line)
        if declared:
            interface = declared.group(1)
        found = re.search(rf"@{tag}\b(.*)", line)
        if not found:
            continue
        end = next(j for j in range(i, len(lines)) if "*/" in lines[j])
        code = next(
            text
            for text in lines[end + 1 :]
            if text.strip() and not text.strip().startswith("//")
        )
        text = found.group(1).replace("*/", "").strip()
        declared = re.match(r"export (?:interface|type|const) (\w+)", code)
        if declared:
            yield declared.group(1), None, text
        else:
            yield interface, re.match(r'  "?([\w./-]+)"?\??:', code).group(1), text


def _key_of(attribute: str, slot: dict) -> str:
    return slot.get("alias") or (slot.get("aliases") or [attribute])[0]


def test_each_deprecation_in_schema_ts_is_carried():
    """Each @deprecated tag in schema.ts, which schema.json drops, marks the element or the
    attribute it tags as deprecated, with the tag's text."""
    found = 0
    elements = _by_definition()
    for name, key, text in _tagged("deprecated"):
        element = elements[name]
        if key is None:
            assert element["deprecated"].startswith(text), name
        else:
            slots = {
                _key_of(attr, slot): slot
                for attr, slot in (element.get("attributes") or {}).items()
            } | (element.get("slot_usage") or {})
            assert slots[key]["deprecated"].startswith(text), (name, key)
        found += 1
    assert found == 21


def test_each_category_and_internal_tag_is_a_subset():
    """Each definition schema.ts tags with @category or @internal is in that subset."""
    subset_name = _converter().subset_name
    elements = _by_definition()
    for tag, subset in (("category", None), ("internal", "internal")):
        for name, key, text in _tagged(tag):
            if name in elements:
                assert key is None, name
                wanted = subset or subset_name(text)
                assert wanted in elements[name]["in_subset"], (name, wanted)


def test_the_words_a_rule_or_deprecation_rests_on_are_mcps():
    """Each rule and each deprecation the converter takes from MCP's words quotes them: the
    sentence is in the definition's description, and each deprecated value is one the
    property lists and its @deprecated tag names."""
    converter, published = _converter(), _published()
    for name, (_, sentence) in converter.RULES.items():
        assert sentence in published[name]["description"], name
    for name, (replacement, sentence) in converter.CLASS_DEPRECATIONS.items():
        assert sentence in published[name]["description"], name
        assert replacement in published, replacement
    tags = {(name, key): text for name, key, text in _tagged("deprecated") if key}
    for pointer, values in converter.VALUE_DEPRECATIONS.items():
        name, _, key = pointer.partition("/properties/")
        for value in values:
            assert value in _node(pointer)["enum"], (pointer, value)
            assert f'`"{value}"`' in tags[(name, key)], (pointer, value)


def test_a_type_schema_ts_names_is_the_range():
    """Where schema.ts gives a property a type MCP defines and schema.json writes the type
    out in place, as for resultType: ResultType, the attribute ranges over the type."""
    ranges = {}
    for _, element in _elements():
        for attr, slot in (element.get("attributes") or {}).items():
            if _key_of(attr, slot) in ("resultType", "cursor", "nextCursor"):
                ranges.setdefault(_key_of(attr, slot), set()).add(slot.get("range"))
    assert ranges == {
        "resultType": {"McpResultType"},
        "cursor": {"McpCursor"},
        "nextCursor": {"McpCursor"},
    }
