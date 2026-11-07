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
    """Where MCP describes a definition or a property, the schema carries the same text."""
    checked = 0
    for name, element in _elements():
        pointer = (
            element["exact_mappings"][0][len(MAPPING_PREFIX) :]
            if element.get("exact_mappings")
            else None
        )
        if not pointer:
            continue
        node = _node(pointer)
        if node.get("description") and "/" not in pointer:
            assert element["description"] == node["description"], name
            checked += 1
        for slot in (element.get("attributes") or {}).values():
            key = slot.get("alias") or (slot.get("aliases") or [None])[0]
            for prop_key, prop in (node.get("properties") or {}).items():
                if prop_key == key or (
                    key is None and prop_key == _key_of(slot, element)
                ):
                    if prop.get("description"):
                        assert slot["description"] == prop["description"], (
                            name,
                            prop_key,
                        )
                        checked += 1
    assert checked > 300


def _key_of(slot, element):
    for attr_name, attr in element["attributes"].items():
        if attr is slot:
            return attr_name
    return None
