---
type: Explanation
id: https://w3id.org/lmodel/mcp/knowledge/explanations/parity-tiers
genre: explanation
title: How the tests hold the schema to MCP
description: "The three parity tiers of `tests/test_parity.py`: every MCP definition is there, MCP's examples and their mutations get the same verdicts, and the shapes differ only as `parity/structural.yaml` lists."
resource: tests/test_parity.py
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/meta-schema-json
references:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/parity-allowances
sources:
  - id: about
    resource: docs/about.md
    title: How the tests hold it to MCP
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:59:20Z"
status: draft
---

# How the tests hold the schema to MCP

The tests compare `meta/schema.json` with MCP's `schema.json` in three tiers.[^about]

1. Addresses: `meta/schema.json` holds every definition MCP publishes except `JSONArray`.
2. Verdicts: both files give the same verdict on MCP's 129 examples, the examples under `tests/data/problem/`, a smallest instance of each definition and about 11,000 mutations, except the differences `parity/probes.yaml` lists. For this tier, the tests compare the generated file with a copy of MCP's file that has the rule the schema adds.
3. Shapes: after both files are normalised, nine definitions differ, each listed with its reason.

[^about]: docs/about.md, How the tests hold it to MCP
