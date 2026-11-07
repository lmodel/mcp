"""Checks each example against MCP's form of the schema.

An example is an MCP message or part of one, with MCP's keys, such as inputSchema or
io.modelcontextprotocol/protocolVersion. linkml-validate and the example runner read the
key a slot lists under aliases by the slot's name, so they cannot read every example;
the examples sit under tests/data/problem/, where the runner does not look, and this test
validates them against the file scripts/mcp_meta.py gives, and against MCP's own, by the
definition the class renders. `tests/data/problem/valid/<Class>-<anything>.yaml` must
pass both, and `tests/data/problem/invalid/<Class>-<anything>.yaml` must fail both.
"""

from pathlib import Path

import pytest

import mcp_parity as parity

DATA = Path(__file__).parent / "data" / "problem"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_example(path):
    name, data = parity.definition_of(path), parity._yaml(path)
    assert parity.verdict("generated", name, data)
    assert parity.verdict("published", name, data)


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_example(path):
    name, data = parity.definition_of(path), parity._yaml(path)
    assert not parity.verdict("generated", name, data)
    assert not parity.verdict("published", name, data)
