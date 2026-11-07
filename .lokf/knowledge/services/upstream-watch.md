---
type: Service
id: https://w3id.org/lmodel/mcp/knowledge/services/upstream-watch
genre: reference
title: The upstream watch
description: "`scripts/check_upstream_release.py`, run weekly by `.github/workflows/upstream-watch.yaml`: it reports a new MCP tag or version folder, a moved tag, a pinned file changed or a file added, and a changed licence, and opens an issue."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/upstream-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:22:05Z"
status: draft
---

# The upstream watch

The script lists MCP's repository through GitHub's API and compares git object hashes, so it downloads no file. MCP's default branch had already edited three pinned files, and the script holds the hash each has there. It also holds the hash of the folder's `schema.mdx`, which `upstream/` leaves out. It reports a further edit, or a file added to the folder. A failed check opens an issue, or comments on the one already open.
