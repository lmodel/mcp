# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change raises the minor version.

## [Unreleased]

## [0.2.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

## [0.1.0] - 2026-11-07

### Added

- **`upstream/`**, holding MCP 2026-07-28's `schema.json`, `schema.ts`, examples and licence at the tag `2026-07-28`, pinned by git object hash, with a weekly watch.
- **`scripts/mcp_to_linkml.py`**, which writes the schema from MCP's files: a class per object, a union class per union, enums and types, `is_a` and subsets from `schema.ts`, and an exact mapping from each class, enum and type but the two format types to the place it renders.
- **MCP's deprecations.** `schema.json` drops the 21 `@deprecated` tags of `schema.ts`. The schema marks what each one tags, so sampling, roots and logging read as deprecated in 2026-07-28.
- **`meta/schema.json`**, MCP's `schema.json` written again from the schema, and tests that hold it to MCP's in three tiers over MCP's examples and their mutations.
- **The rule MCP's description gives `InputRequiredResult`**: at least one of `inputRequests` or `requestState`.
- **`.lokf/schema/mcp.yaml`, the schema's `lokf adapt` copy**, rooted on the implementation, tools, resources, resource templates and prompts. The knowledge release attaches it as `schema-<tag>-mcp.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.62.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, the CONTRIBUTING checklist, and a NOTICE that states the licence position.

### Changed

- **The schema models MCP 2026-07-28.** Before, it was written by hand against an earlier draft, which had initialization, tasks and the requests that 2026-07-28 drops.
- **Every class, enum and type takes the `Mcp` prefix** and MCP's definition name, such as `McpCallToolRequest`.
- **Keys LOKF defines with another meaning keep MCP's key** as slots of the schema's own, which the adapt copy renames, such as `mcp_type` for `type`. Where MCP gives a key two meanings and LOKF shares one, the other takes a name of its own, such as `url_settings`.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `mcp-linkml`.

### Removed

- **The vendored draft `schema.json`, `BUG.txt` and the scripts that patched the generated JSON Schema.** linkml 1.12.1 writes open classes and unions that need no patch.
- **The draft examples under `tests/data/third_party/`**, replaced by MCP 2026-07-28's own examples in `upstream/`.
