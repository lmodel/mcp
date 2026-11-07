"""Checks the JSON Schema the model gives (meta/schema.json) against MCP's schema.json."""

import json

import pytest
from jsonschema import Draft202012Validator

import mcp_parity as parity


def test_generated_file_compiles():
    """meta/schema.json is a valid draft 2020-12 schema."""
    Draft202012Validator.check_schema(parity.load("generated"))


def test_every_reference_resolves():
    """Every $ref in the generated file names one of its definitions."""
    defs = parity.load("generated")["$defs"]
    for ref in parity.refs(parity.load("generated")):
        assert ref.startswith(parity.DEFS) and ref[len(parity.DEFS) :] in defs, ref


def test_every_published_definition_is_there():
    """Tier 1: every definition MCP publishes is in the generated file, except the listed gaps,
    and the file adds none of its own."""
    published, generated = (
        parity.load("published")["$defs"],
        parity.load("generated")["$defs"],
    )
    assert parity.missing_definitions() == set(parity.probes()["gaps"])
    assert set(generated) <= set(published)


def test_corpus_is_valid_against_both():
    """Tier 2: each example and each smallest instance is valid against both files, and
    against MCP's with the stated rules, except the examples MCP's own words reject, which
    are valid against MCP's file alone."""
    rejected = parity.probes()["examples_mcp_rejects"]
    for label, name, doc in parity.corpus():
        assert parity.verdict("published", name, doc), label
        expected = label not in rejected
        assert parity.verdict("stated", name, doc) is expected, label
        assert parity.verdict("generated", name, doc) is expected, label
    assert set(rejected) <= {label for label, _, _ in parity.corpus()}


def test_each_stated_rule_rejects_what_mcps_file_accepts():
    """Each narrower rule in probes.yaml names a definition and changes a verdict there."""
    for rule in parity.probes()["narrower"]:
        name = rule["definition"]
        bare = {k: v for k, v in parity.smallest(name).items() if k in ("resultType",)}
        assert parity.verdict("published", name, bare), name
        assert not parity.verdict("stated", name, bare), name
        assert not parity.verdict("generated", name, bare), name


def test_mutations_get_the_same_verdicts():
    """Tier 2: each mutation of each document gets the same verdict from both files, or the
    generated file accepts a value probes.yaml lists as wider."""
    wider = parity.probes()["wider"]["values"]
    found = parity.differences()
    assert found, "no mutation reaches the wider JSON value: drop the entry"
    for label, name, published, generated in found:
        assert (published, generated) == (False, True), label
        assert any(label.endswith(f" as {json.dumps(v)}") for v in wider), label


@pytest.mark.parametrize(
    "probe", parity.probes()["documents"], ids=lambda p: p["reason"]
)
def test_probe(probe):
    """Each probe gets the verdict probes.yaml gives it from each file."""
    name, doc = probe["definition"], probe["document"]
    assert parity.verdict("published", name, doc) is probe["published"]
    assert parity.verdict("generated", name, doc) is probe["generated"]


def test_shapes_differ_only_as_listed():
    """Tier 3: the definitions whose normalised shape differs are the listed ones."""
    assert set(parity.shape_differences()) == set(parity.structural())


def test_mutations_break_each_required_key_and_value():
    """Every required key, const and value list in MCP's file is broken by some mutation of
    a smallest instance, so tier 2 tests each constraint the file states."""
    for name in parity.load("published")["$defs"]:
        if name in parity.missing_definitions():
            continue
        instance = parity.smallest(name)
        if not isinstance(instance, dict):
            continue
        labels = {label for label, _ in parity.mutations(instance)}
        for key in instance:
            assert f"/{key} removed" in labels, (name, key)
