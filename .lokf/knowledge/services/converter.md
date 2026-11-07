---
type: Service
id: https://w3id.org/lmodel/mcp/knowledge/services/converter
genre: reference
title: The converter
description: "`scripts/mcp_to_linkml.py`, which writes the LinkML schema from MCP's schema.json and schema.ts: classes, unions, enums, types, is_a from schema.ts, a subset per category and an exact mapping per element."
resource: scripts/mcp_to_linkml.py
dependsOn:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/upstream-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The converter

`scripts/mcp_to_linkml.py` reads the pinned `schema.json` for structure and descriptions, and `schema.ts` for each interface's `extends` and `@category`. It writes `src/mcp/schema/mcp.yaml`. `just gen-mcp` runs it, and `--check` fails when the schema differs from what it writes.

An object definition becomes a class with the `Mcp` prefix, open to extra keys. A union of definitions becomes a class whose `any_of` names each member. A list of strings becomes an enum, and a string or a string-or-integer a type. An inline object becomes a class named after its owner and key.

Where MCP gives no description, the converter's `DESCRIPTIONS` holds the project's words.
