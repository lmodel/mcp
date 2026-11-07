---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/upstream-copy
genre: reference
title: The copy of the upstream
description: "`upstream/`: MCP 2026-07-28's schema.json, schema.ts, 129 examples and the repository's LICENSE, unchanged and pinned by git object hash in `scripts/upstream_pins.tsv`."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/mcp/knowledge/references/mcp-specification
sources:
  - id: notice
    resource: NOTICE
    title: Model Context Protocol
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_upstream_holds_only_the_pinned_files
  - resource: scripts/upstream_pins.tsv
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The copy of the upstream

The files are copied whole and unchanged from the tag `2026-07-28`, commit `5f5440b`.[^notice]

The folder holds exactly the pinned files, 132 of them, and each matches its pinned hash.[^test_upstream.py]

[^notice]: NOTICE, Model Context Protocol
[^test_upstream.py]: tests/test_upstream.py, test_upstream_holds_only_the_pinned_files
