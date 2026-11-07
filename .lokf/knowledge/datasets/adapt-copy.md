---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/adapt-copy
genre: reference
title: The adapt copy
description: "`.lokf/schema/mcp.yaml`, the copy `just lokf-adapt` writes beside LOKF's schema, rooting McpImplementation, McpTool, McpResource, McpResourceTemplate and McpPrompt on Concept; the release attaches it."
resource: .lokf/schema/mcp.yaml
derivedFrom:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The adapt copy

`just lokf-adapt` writes the copy from the schema, and `just lokf-adapt-check` fails when it is stale. The copy folds MCP's `description`, `title` and `version` into LOKF's, and keeps `name` and `url` as `mcp_name` and `mcp_url`.

A concept may name `McpImplementation`, `McpPrompt`, `McpResource`, `McpResourceLink`, `McpResourceTemplate` or `McpTool` as its type.
