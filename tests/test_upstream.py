"""Checks that upstream/ holds the version the schema models.

upstream/ holds MCP 2026-07-28's schema files and examples and the repository's licence,
as they are published. scripts/check_upstream_release.py compares them with GitHub. These
tests make the same comparison offline, and hold the schema's header, the converter and
NOTICE to the same pins.
"""

import hashlib
import importlib.util
from functools import cache

import yaml

from mcp_parity import ROOT

UPSTREAM = ROOT / "upstream"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
CONVERTER = ROOT / "scripts" / "mcp_to_linkml.py"
SCHEMA = ROOT / "src" / "mcp" / "schema" / "mcp.yaml"


@cache
def _module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _watch():
    return _module(WATCH, "watch_pins")


def _blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_upstream_holds_only_the_pinned_files():
    found = {
        path.relative_to(UPSTREAM).as_posix()
        for path in UPSTREAM.rglob("*")
        if path.is_file()
    }
    assert found == set(_watch().pins())
    assert len(found) == 132


def test_copies_match_the_pinned_blobs():
    """Each file has the git object hash the watch pins."""
    wrong = [
        path for path, sha in _watch().pins().items() if _blob(UPSTREAM / path) != sha
    ]
    assert not wrong


def test_the_schema_names_the_pinned_version():
    watch = _watch()
    header = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    assert header["version"] == watch.VERSION
    assert header["source"].endswith(f"/tree/{watch.TAG}/{watch.FOLDER}")
    assert header["license"] == "Apache-2.0"
    assert (
        f"/{watch.TAG}/{watch.FOLDER}/schema.json#/$defs/"
        in (header["prefixes"]["mcp_schema"])
    )


def test_the_converter_reads_the_pinned_version():
    assert _module(CONVERTER, "converter_pins").VERSION == _watch().VERSION


def test_the_branch_edits_are_ones_the_pins_know():
    """The watch excuses only pinned files the default branch has edited."""
    watch = _watch()
    pinned = {p.removeprefix(f"{watch.SPEC}/") for p in watch.pins()}
    assert set(watch.EDITED_ON_BRANCH) <= pinned
    for path, sha in watch.EDITED_ON_BRANCH.items():
        assert watch.pins()[f"{watch.SPEC}/{path}"] != sha, path


def test_the_notice_carries_what_the_licences_ask():
    """Apache-2.0 and MIT ask for the copyright and licence notices, and the MCP project's
    name stays the MCP project's."""
    watch = _watch()
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    for needed in (
        "Model Context Protocol a Series of LF Projects, LLC",
        "Apache License, Version 2.0",
        "MIT License",
        f"at the tag {watch.TAG}, commit {watch.COMMIT[:7]}",
        "does not imply endorsement",
        "word for word",
    ):
        assert needed in notice.replace("\n  ", " ").replace("\n", " "), needed
    examples = sum(1 for p in watch.pins() if "/examples/" in p)
    assert f"examples/ ({examples} files)" in notice
