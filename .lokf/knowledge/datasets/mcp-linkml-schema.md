---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
genre: reference
title: The mcp LinkML schema
description: "`src/mcp/schema/mcp.yaml`, the LinkML schema of MCP 2026-07-28 that the converter writes: classes with the Mcp prefix, unions, enums, types and a subset per schema.ts category."
resource: src/mcp/schema/mcp.yaml
derivedFrom:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/upstream-copy
references:
  - https://w3id.org/lmodel/mcp/knowledge/services/converter
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:22:05Z"
status: draft
---

# The mcp LinkML schema

The schema is one file, `src/mcp/schema/mcp.yaml`, written by the converter and never by hand. Its header names version `2026-07-28` and the schema folder at that tag as its source.

Each class and enum, and each type but the format types `McpBase64` and `McpUriTemplate`, maps exactly to the place in MCP's `schema.json` it renders, such as `mcp_schema:Tool`. Where MCP describes an element, the schema carries MCP's words unchanged.

Each element or attribute that a `@deprecated` tag in `schema.ts` tags carries `deprecated`, with the tag's text. `schema.json` drops the tags, and MCP 2026-07-28 deprecates sampling, roots and logging.
