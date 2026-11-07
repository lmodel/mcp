# Datasets

* [The copy of the upstream](upstream-copy.md) - `upstream/`: MCP 2026-07-28's schema.json, schema.ts, 129 examples and the repository's LICENSE, unchanged and pinned by git object hash in `scripts/upstream_pins.tsv`.
* [The mcp LinkML schema](mcp-linkml-schema.md) - `src/mcp/schema/mcp.yaml`, the LinkML schema of MCP 2026-07-28 that the converter writes: classes with the Mcp prefix, unions, enums, types and a subset per schema.ts category.
* [MCP's schema.json, written from the schema](meta-schema-json.md) - `meta/schema.json`: MCP's schema.json written again from the LinkML schema, with MCP's definition names and keys, which the parity tests hold to MCP's own file.
* [The parity allowances](parity-allowances.md) - `parity/probes.yaml` and `parity/structural.yaml`: the differences from MCP's schema.json the tests allow, each with its reason: the gap, the wider JSON value, the narrower rule and MCP's example its own words reject.
* [The adapt copy](adapt-copy.md) - `.lokf/schema/mcp.yaml`, the copy `just lokf-adapt` writes beside LOKF's schema, rooting McpImplementation, McpTool, McpResource, McpResourceTemplate and McpPrompt on Concept; the release attaches it.
* [The neighbours' copies](neighbour-copies.md) - `tests/neighbours/`: the adapt copies 38 other lmodel repositories released, each pinned by its checksum, against which `tests/test_schema_rules.py` keeps this copy's names apart.
* [The example messages](example-messages.md) - `tests/data/problem/`: MCP messages and objects with MCP's keys, valid under `valid/` and invalid under `invalid/`, which `tests/test_data.py` checks against meta/schema.json and MCP's file.
