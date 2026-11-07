---
type: Explanation
id: https://w3id.org/lmodel/mcp/knowledge/explanations/keys
genre: explanation
title: How the schema names MCP's keys
description: Which MCP keys keep their name, which take an alias, which share LOKF's schema.org IRI (name, title, description, url, version), which the adapt copy renames, such as type, and which take a name of their own, such as url_settings.
resource: docs/about.md
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-07T11:33:51Z"
status: draft
---

# How the schema names MCP's keys

A slot's alias is MCP's key, such as `input_schema` for `inputSchema`. `$schema` and the reserved `io.modelcontextprotocol/...` keys are not valid Python names, so they are listed under `aliases`.

`name`, `title`, `description`, `url` and `version` mean what LOKF means by them, so they are slots with LOKF's schema.org IRIs. Six keys LOKF defines with another meaning are slots under MCP's key, with an IRI in this schema's namespace: `type`, `id`, `audience`, `context`, `reason` and `resource`. The adapt copy renames them, such as `type` to `mcp_type`. MCP gives two keys, `url` and `required`, two meanings each, one of them LOKF's. For the other meaning of each, the schema uses a name of its own, `url_settings` and `required_names`, with MCP's key under `aliases`.
