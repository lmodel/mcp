"""Holds the schema to MCP's files, and the generated files to the schema."""

import json
import subprocess
import sys

import yaml

from mcp_parity import PUBLISHED, ROOT

SCHEMA = ROOT / "src" / "mcp" / "schema" / "mcp.yaml"
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
