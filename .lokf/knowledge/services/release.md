---
type: Service
id: https://w3id.org/lmodel/mcp/knowledge/services/release
genre: reference
title: The release
description: "`.github/workflows/semantic-release.yml`, which releases from a v0.0.0 baseline tag on a feat, fix or security merge, and dispatches the knowledge release that attaches the adapt copy and the bundle."
resource: .github/workflows/semantic-release.yml
references:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/adapt-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-07T15:08:15Z"
status: draft
---

# The release

On a merge to `main` that holds a `feat:`, `fix:` or `security:` commit or a breaking change, semantic-release retitles the changelog's `## [Unreleased]` section, tags `vX.Y.Z` and publishes the release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `knowledge-release.yaml`, which attaches `schema-<tag>-mcp.yaml` with its checksum and attestation when the bundle or the schema changed. A `v0.0.0` tag on `main` must come first, so the first release is 0.1.0.
