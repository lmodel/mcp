---
type: Explanation
id: https://w3id.org/lmodel/mcp/knowledge/explanations/keys
genre: explanation
title: How the schema names MCP's keys
description: Which MCP keys keep their name, which take an alias, which share LOKF's schema.org IRI (name, title, description, url, version), and which take a name of their own, such as kind for type and identifier for id.
resource: docs/about.md
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# How the schema names MCP's keys

A slot's alias is MCP's key, such as `input_schema` for `inputSchema`. `$schema` and the reserved `io.modelcontextprotocol/...` keys are no Python names, so they are listed under `aliases`.

`name`, `title`, `description`, `url` and `version` mean what LOKF means by them, so they are slots with LOKF's schema.org IRIs. Eight keys LOKF defines with another meaning take a name of their own, with MCP's key under `aliases`: `kind`, `identifier`, `intended_audience`, `context_info`, `reason_text`, `resource_contents`, `url_settings` and `required_names`.
