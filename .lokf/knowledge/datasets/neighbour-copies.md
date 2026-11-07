---
type: Dataset
id: https://w3id.org/lmodel/mcp/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbours' copies
description: "`tests/neighbours/`: the adapt copies 38 other lmodel repositories released, each pinned by its checksum, against which `tests/test_schema_rules.py` keeps this copy's names apart."
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/adapt-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# The neighbours' copies

Each file is the schema asset of a release, checked against its `.sha256` and its build-provenance attestation, and pinned in `NEIGHBOURS` in `tests/test_schema_rules.py`. The test fails on a class, enum, type or subset name the copy shares, and on a shared key the test does not list.
