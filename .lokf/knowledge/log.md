# Change Log

## 2026-11-07

* **Changed**: How the schema names MCP's keys says LOKF shares one meaning of `url` and of `required`, and the other takes a name of its own.
* **Changed**: The converter names all four kinds of sentence it writes where MCP gives no description.
* **Changed**: How the tests hold the schema to MCP counts about 12,000 mutations; tier 2 builds 12,011.
* **Prose**: reworded 5 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: How the schema names MCP's keys says six keys LOKF defines are slots under MCP's key, which the adapt copy renames, from `scripts/mcp_to_linkml.py`.
* **Changed**: The adapt copy renames the six slots LOKF defines with another meaning, from `.lokf/schema/mcp.yaml`.
* **Changed**: The converter reads schema.ts's `@internal` and `@deprecated` tags and the type a property names, from `scripts/mcp_to_linkml.py`.
* **Changed**: The mcp LinkML schema carries MCP's deprecations, from `src/mcp/schema/mcp.yaml`.
* **Changed**: The upstream watch reports a file added to MCP's version folder, from `scripts/check_upstream_release.py`.
* **Changed**: How the tests hold the schema to MCP says the tests add the rule to a copy of MCP's file, and that tier 2 allows the differences `parity/probes.yaml` lists.
* **Changed**: The mcp LinkML schema says the two format types map to no place in MCP's file, as `tests/test_build.py` holds.
* **Changed**: The release says which merges release, as CONTRIBUTING.md does.
* **Prose**: reworded 8 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: The Model Context Protocol, version 2026-07-28 links its specification site rather than naming it bare.
* **Added**: The Model Context Protocol, version 2026-07-28, from NOTICE and MCP's repository.
* **Added**: The copy of the upstream, from `upstream/`.
* **Added**: The converter, from `scripts/mcp_to_linkml.py`.
* **Added**: The mcp LinkML schema, from `src/mcp/schema/mcp.yaml`.
* **Added**: The writer of meta/, from `scripts/mcp_meta.py`.
* **Added**: MCP's schema.json, written from the schema, from `meta/schema.json`.
* **Added**: How the tests hold the schema to MCP, from `tests/test_parity.py` and `docs/about.md`.
* **Added**: The parity allowances, from `parity/`.
* **Added**: How the schema names MCP's keys, from `docs/about.md`.
* **Added**: The rule the schema adds to MCP's file, from `scripts/mcp_to_linkml.py` and `parity/probes.yaml`.
* **Added**: The adapt copy, from `.lokf/schema/mcp.yaml`.
* **Added**: The neighbours' copies, from `tests/neighbours/`.
* **Added**: The example messages, from `tests/data/problem/`.
* **Added**: The upstream watch, from `scripts/check_upstream_release.py`.
* **Added**: Regenerate after a change, from `CONTRIBUTING.md`.
* **Added**: The release, from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge sources map, from the repository root.
* **Initialization**: Scaffolded the LOKF bundle for mcp. Real concepts to follow.
