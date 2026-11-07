---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/mcp/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: mcp Knowledge Bundle
description: Model Context Protocol (MCP) 2026-07-28 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/mcp/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# mcp Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for mcp. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# References

* [The Model Context Protocol, version 2026-07-28](references/mcp-specification.md) - MCP 2026-07-28, the protocol version the schema models: its specification site and the schema folder of its repository at the tag 2026-07-28, licensed under Apache-2.0 or MIT.

# Datasets

* [The copy of the upstream](datasets/upstream-copy.md) - `upstream/`: MCP 2026-07-28's schema.json, schema.ts, 129 examples and the repository's LICENSE, unchanged and pinned by git object hash in `scripts/upstream_pins.tsv`.
* [The mcp LinkML schema](datasets/mcp-linkml-schema.md) - `src/mcp/schema/mcp.yaml`, the LinkML schema of MCP 2026-07-28 that the converter writes: classes with the Mcp prefix, unions, enums, types and a subset per schema.ts category.
* [MCP's schema.json, written from the schema](datasets/meta-schema-json.md) - `meta/schema.json`: MCP's schema.json written again from the LinkML schema, with MCP's definition names and keys, which the parity tests hold to MCP's own file.
* [The parity allowances](datasets/parity-allowances.md) - `parity/probes.yaml` and `parity/structural.yaml`: the differences from MCP's schema.json the tests allow, each with its reason: the gap, the wider JSON value, the narrower rule and MCP's example its own words reject.
* [The adapt copy](datasets/adapt-copy.md) - `.lokf/schema/mcp.yaml`, the copy `just lokf-adapt` writes beside LOKF's schema, rooting McpImplementation, McpTool, McpResource, McpResourceTemplate and McpPrompt on Concept; the release attaches it.
* [The neighbours' copies](datasets/neighbour-copies.md) - `tests/neighbours/`: the adapt copies 38 other lmodel repositories released, each pinned by its checksum, against which `tests/test_schema_rules.py` keeps this copy's names apart.
* [The example messages](datasets/example-messages.md) - `tests/data/problem/`: MCP messages and objects with MCP's keys, valid under `valid/` and invalid under `invalid/`, which `tests/test_data.py` checks against meta/schema.json and MCP's file.

# Services

* [The converter](services/converter.md) - `scripts/mcp_to_linkml.py`, which writes the LinkML schema from MCP's schema.json and schema.ts: classes, unions, enums, types, is_a, subsets and deprecations from schema.ts, and an exact mapping per element.
* [The writer of meta/](services/meta-writer.md) - `scripts/mcp_meta.py`, which runs gen-json-schema on the schema and shapes its output into MCP's form in `meta/schema.json`, with MCP's definition names and keys, and three repairs of the generator.
* [The upstream watch](services/upstream-watch.md) - `scripts/check_upstream_release.py`, run weekly by `.github/workflows/upstream-watch.yaml`: it reports a new MCP tag or version folder, a moved tag, a pinned file changed or a file added, and a changed licence, and opens an issue.
* [The release](services/release.md) - `.github/workflows/semantic-release.yml`, which releases from a v0.0.0 baseline tag on a feat, fix or security merge, and dispatches the knowledge release that attaches the adapt copy and the bundle.

# Explanations

* [How the tests hold the schema to MCP](explanations/parity-tiers.md) - The three parity tiers of `tests/test_parity.py`: every MCP definition is there, MCP's examples and their mutations get the same verdicts, and the shapes differ only as `parity/structural.yaml` lists.
* [How the schema names MCP's keys](explanations/keys.md) - Which MCP keys keep their name, which take an alias, which share LOKF's schema.org IRI (name, title, description, url, version), and which take a name of their own, such as kind for type and identifier for id.
* [The rule the schema adds to MCP's file](explanations/input-required-rule.md) - The schema states that an InputRequiredResult holds inputRequests or requestState, as MCP's description says and its schema.json does not, which MCP's own read-resource example breaks.

# Playbooks

* [Regenerate after a change](playbooks/regenerate.md) - How to regenerate everything after a change to the converter: just gen-mcp, gen-project, gen-doc and lokf-adapt, then lint and test.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
