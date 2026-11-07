---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/meta-schema-json
genre: reference
title: MCP's schema.json, written from the schema
description: "`meta/schema.json`: MCP's schema.json written again from the LinkML schema, with MCP's definition names and keys, which the parity tests hold to MCP's own file."
resource: meta/schema.json
derivedFrom:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
references:
  - https://w3id.org/lmodel/mcp/knowledge/services/meta-writer
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# MCP's schema.json, written from the schema

`meta/schema.json` is a JSON Schema 2020-12 document whose `$defs` carry MCP's definition names. Any validator of that draft checks a message against one of them. `just check-mcp` fails when the file differs from the writer's output.
