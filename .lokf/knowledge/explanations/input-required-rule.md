---
type: Explanation
id: https://w3id.org/lmodel/mcp/knowledge/explanations/input-required-rule
genre: explanation
title: The rule the schema adds to MCP's file
description: The schema states that an InputRequiredResult holds inputRequests or requestState, as MCP's description says and its schema.json does not, which MCP's own read-resource example breaks.
resource: scripts/mcp_to_linkml.py
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
sources:
  - id: probes
    resource: parity/probes.yaml
    title: narrower
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The rule the schema adds to MCP's file

MCP's description of `InputRequiredResult` says that at least one of `inputRequests` or `requestState` must be present. The converter's `RULES` states it as the class's `any_of`.[^probes]

Without the rule, any result with a `resultType` passes as an input-required result. MCP's read-resource example passes only that way: it lacks `cacheScope` and `ttlMs`, which a read-resource result requires.

[^probes]: parity/probes.yaml, narrower
