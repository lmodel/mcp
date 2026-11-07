---
type: Playbook
id: https://w3id.org/lmodel/mcp/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons."
resource: .
references:
  - https://w3id.org/lmodel/mcp/knowledge/datasets/mcp-linkml-schema
  - https://w3id.org/lmodel/mcp/knowledge/references/mcp-specification
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: CONTRIBUTING.md
  - resource: NOTICE
  - resource: src/mcp/schema/mcp.yaml
  - resource: meta/schema.json
  - resource: parity
  - resource: scripts
  - resource: tests
  - resource: upstream
  - resource: .lokf/schema/mcp.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: .github/workflows
exclusions:
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: AI_COVENANT.md
    reason: Governance text on AI-assisted work, with nothing about the schema.
  - resource: SECURITY.md
    reason: The security policy, with nothing about the schema.
  - resource: CHANGELOG.md
    reason: The release history, which each release writes.
  - resource: LICENSE
    reason: The licence text.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .linkml/generators.yaml
    reason: "Tooling: the generators' settings."
  - resource: .linkmllint.yaml
    reason: "Tooling: the schema linter's settings."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the hooks and the files they leave alone."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .releaserc.json
    reason: "Tooling: semantic-release's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: justfile
    reason: The template's recipes.
  - resource: project.justfile
    reason: The project's recipes, which the playbook names.
  - resource: pyproject.toml
    reason: The Python project and its tool settings.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .github/dependabot.yml
    reason: "Tooling: Dependabot's settings."
  - resource: .github/release
    reason: The release tools and their lock.
  - resource: .github/scripts
    reason: The release's changelog script and the watch's issue script.
  - resource: .lokf/schema/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder.
  - resource: project
    reason: Files generated from the schema.
  - resource: src/mcp/datamodel
    reason: Python models generated from the schema.
  - resource: website
    reason: The knowledge website, built from the README, docs, the schema and this bundle.
  - resource: docs/elements
    reason: Generated pages that git ignores, apart from a placeholder.
  - resource: docs/schema
    reason: A copy of the schema that gen-doc writes.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: examples/README.md
    reason: Text from the project template.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: src/mcp/schema/README.md
    reason: Text from the project template.
  - resource: src/mcp/__init__.py
    reason: Package plumbing.
  - resource: src/mcp/_version.py
    reason: Package plumbing.
generated:
  by: process:ktl-librarian
  at: "2026-11-07T03:33:30Z"
status: draft
---

# Knowledge sources map

The bundle derives its concepts from the paths under `sources`, each re-read when `knowledge-report.sh worklist` says it changed. Paths under `exclusions` were looked at and left out, each with its reason.

| Source | Yields | Re-check |
| --- | --- | --- |
| `upstream/`, the MCP repository | the reference and the copy of the upstream | `tests/test_upstream.py`; the watch |
| `scripts/` | the converter, the writer and the watch | their tests |
| `src/mcp/schema/mcp.yaml`, `meta/`, `.lokf/schema/mcp.yaml` | the datasets | `just check-mcp`; `just lokf-adapt-check` |
| `tests/`, `parity/` | the parity explanation, the allowances, the examples and the neighbours | `just test` |
| `README.md`, `docs/`, `CONTRIBUTING.md`, `NOTICE` | the explanations and the playbook | read the page |
| `.github/workflows/` | the watch and the release | read the file |
