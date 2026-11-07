---
type: Playbook
id: https://w3id.org/lmodel/mcp/knowledge/playbooks/regenerate
genre: how-to
title: Regenerate after a change
description: "How to regenerate everything after a change to the converter: just gen-mcp, gen-project, gen-doc and lokf-adapt, then lint and test."
resource: CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/mcp/knowledge/services/converter
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# Regenerate after a change

1. Edit `scripts/mcp_to_linkml.py`, never the schema it writes.
2. Run `just gen-mcp`, `just gen-project`, `just gen-doc` and `just lokf-adapt`.
3. Run `just lint` and `just test`.
4. Commit the output with the change.
