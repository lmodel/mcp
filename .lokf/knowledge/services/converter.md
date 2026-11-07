---
type: Service
id: https://w3id.org/lmodel/mcp/knowledge/services/converter
genre: reference
title: The converter
description: "`scripts/mcp_to_linkml.py`, which writes the LinkML schema from MCP's schema.json and schema.ts: classes, unions, enums, types, is_a, subsets and deprecations from schema.ts, and an exact mapping per element."
resource: scripts/mcp_to_linkml.py
dependsOn:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/upstream-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-07T11:33:51Z"
status: draft
---

# The converter

`scripts/mcp_to_linkml.py` reads the pinned `schema.json` for structure and descriptions, and `schema.ts` for each interface's `extends`, each `@category`, `@internal` and `@deprecated` tag, and the type a property names. It writes `src/mcp/schema/mcp.yaml`. `just gen-mcp` runs it, and `--check` fails when the schema differs from what it writes.

An object definition becomes a class with the `Mcp` prefix, open to extra keys. A union of definitions becomes a class whose `any_of` names each member. A list of strings becomes an enum, and a string or a string-or-integer becomes a type. An inline object becomes a class named after its owner and key.

Where MCP gives no description, the project's words come from the converter's tables: `CLASS_DESCRIPTIONS` for a definition, `CONST_DESCRIPTIONS` for a constant and `DESCRIPTIONS` for a property. Other sentences name a union's members, where MCP holds an inline object, the key of an inline value list, or the code and data an error carries.
