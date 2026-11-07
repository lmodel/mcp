<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# mcp

Model Context Protocol (MCP) 2026-07-28 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/mcp](https://lmodel.github.io/mcp)

## What it models

The schema renders the [Model Context Protocol](https://modelcontextprotocol.io/specification/2026-07-28) at version 2026-07-28, as its `schema.json` states it: the JSON-RPC requests, results, notifications and errors, and the tools, resources, prompts, content and capabilities they carry.

[scripts/mcp_to_linkml.py](scripts/mcp_to_linkml.py) writes the schema from MCP's own files in [upstream/](upstream), which are pinned by hash and watched weekly. [meta/schema.json](meta/schema.json) is MCP's `schema.json` written again from the schema, and [tests/test_parity.py](tests/test_parity.py) checks it against MCP's. [docs/about.md](docs/about.md) says how the schema reads MCP and what it adds or leaves out.

## Mappings

* **MCP's own definitions**: the `exact_mappings` of each class and enum, and of each type but the two format types, name the place in MCP's `schema.json` it renders, such as `mcp_schema:Tool`. [tests/test_build.py](tests/test_build.py) resolves each one in the pinned copy.

## Repository Structure

* [docs/](docs/): the website's own pages
* [meta/](meta): MCP's `schema.json`, written from the schema by [scripts/mcp_meta.py](scripts/mcp_meta.py)
* [parity/](parity): the differences from MCP's file that the tests allow, each with its reason
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter, the writer of `meta/` and the upstream watch
* [src/mcp/schema/](src/mcp/schema): the LinkML schema, which the converter writes
* [src/mcp/datamodel/](src/mcp/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example messages in [data/problem/](tests/data/problem) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): MCP 2026-07-28's schema files, examples and licence, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes. `just gen-mcp` rewrites the schema and `meta/` from `upstream/`, and `just check-mcp` says when either is stale.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/schema/mcp.yaml`, is the copy `just lokf-adapt` writes from `src/mcp/schema/mcp.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the converter, never the copy.

In the copy, the classes a person documents about an MCP server descend from `Concept`: the implementation, and the tools, resources, resource templates and prompts it offers. Messages stay values. In Obsidian, add these to the KTL plugins' *Known LOKF types* setting:

```text
McpImplementation, McpPrompt, McpResource, McpResourceLink, McpResourceTemplate, McpTool
```

MCP's `description`, `title` and `version` fold into LOKF's, which mean the same. `name` and `url` keep their own meaning in the copy as `mcp_name` and `mcp_url`. Eight keys LOKF defines with another meaning take a name of their own in the schema, such as `kind` for `type`. [docs/about.md](docs/about.md#keys) lists them. `tests/test_schema_rules.py` keeps the copy's keys apart from LOKF and the released copies in `tests/neighbours/`.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

MCP's files in `upstream/`, and MCP's descriptions the schema carries, keep MCP's licence, the Apache License 2.0 or the MIT License. [NOTICE](NOTICE) states the position, and this project is not endorsed by the MCP project or LF Projects, LLC.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
