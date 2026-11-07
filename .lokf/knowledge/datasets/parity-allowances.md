---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/parity-allowances
genre: reference
title: The parity allowances
description: "`parity/probes.yaml` and `parity/structural.yaml`: the differences from MCP's schema.json the tests allow, each with its reason: the gap, the wider JSON value, the narrower rule and MCP's example its own words reject."
resource: parity
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The parity allowances

`parity/probes.yaml` lists the definition the generated file leaves out (`JSONArray`), the values it accepts where MCP's file does not (a fraction or null inside a JSON object), the rule it states that MCP's file does not, MCP's example that rule rejects, and documents written to test one claim each.

`parity/structural.yaml` lists each definition whose normalised shape differs, with its reason.
