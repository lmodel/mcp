---
type: Service
id: https://w3id.org/lmodel/mcp/knowledge/services/meta-writer
genre: reference
title: The writer of meta/
description: "`scripts/mcp_meta.py`, which runs gen-json-schema on the schema and shapes its output into MCP's form in `meta/schema.json`, with MCP's definition names and keys, and three repairs of the generator."
resource: scripts/mcp_meta.py
dependsOn:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The writer of meta/

`scripts/mcp_meta.py` gives each class, enum and type the name of the definition it maps to, and writes inline what maps to a place inside a definition. For each attribute that lists a key under `aliases`, it writes that key in place of the attribute's name.

It repairs three faults of linkml 1.12.1's JSON Schema generator: `null` admitted despite `include_null=False`, `linkml:Any` without arrays, and class conditions that name slots rather than their keys.
