---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/example-messages
genre: reference
title: The example messages
description: "`tests/data/problem/`: MCP messages and objects with MCP's keys, valid under `valid/` and invalid under `invalid/`, which `tests/test_data.py` checks against meta/schema.json and MCP's file."
resource: tests/data/problem
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/meta-schema-json
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The example messages

Each file is named for the class it is an instance of, such as `McpTool-weather.yaml`. The examples sit under `problem/`, where the example runner does not look, because they carry keys the LinkML form names differently. Each class a concept may name as its type has a valid example.
