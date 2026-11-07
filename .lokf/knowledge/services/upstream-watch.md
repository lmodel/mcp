---
type: Service
id: https://w3id.org/lmodel/mcp/knowledge/services/upstream-watch
genre: reference
title: The upstream watch
description: "`scripts/check_upstream_release.py`, run weekly by `.github/workflows/upstream-watch.yaml`: it reports a new MCP tag or version folder, a moved tag, a pinned file changed, and a changed licence, and opens an issue."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/upstream-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The upstream watch

The script lists MCP's repository through GitHub's API and compares git object hashes, so it downloads no file. It knows the three pinned files MCP's default branch had already edited, and reports only a further edit. A failed check opens an issue, or comments on the one already open.
