# About mcp

This page says how the schema reads MCP, what it adds, and what it leaves out.

## One version

The schema models MCP 2026-07-28, the `schema/2026-07-28/` folder at the tag `2026-07-28` of [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol). `upstream/` holds that folder's `schema.json`, `schema.ts` and 129 examples, and the repository's licence, pinned by git object hash. The upstream watch reports a new tag or version folder, and any further edit to the pinned files on MCP's default branch. By 2026-11-07 that branch had already edited three of them: a description in `schema.json`, `schema.ts` and one example. The watch knows those edits.

The schema was hand-written against MCP's draft before this release. MCP 2026-07-28 drops initialization, tasks and several requests the draft had, and adds discovery, subscriptions and input-required results, so the schema is now written by a script: the next version is one run of the converter.

## How the converter reads MCP

`scripts/mcp_to_linkml.py` reads `schema.json` for structure and descriptions, and `schema.ts` for what JSON Schema cannot carry.

- An object definition is a class with the `Mcp` prefix, such as `McpTool`. Every object MCP publishes is open, so every class allows extra slots.
- A union of definitions, such as `ContentBlock`, is a class whose `any_of` names each member through `is_a`.
- A list of strings is an enum, and a string or a string-or-integer is a type.
- An inline object, such as a tool's `inputSchema`, is a class named after its owner and key, such as `McpToolInputSchema`.
- Each interface's `extends` in `schema.ts` gives `is_a` and `mixins`, and each `@category` a subset.
- Each class, enum and type maps exactly to the place in `schema.json` it renders, such as `mcp_schema:Tool`.

Each class states every key its definition has, inherited or not, as `schema.json` does. Where MCP gives a description, the schema carries it word for word. Where MCP gives none, the converter's `DESCRIPTIONS` holds this project's words.

## Keys

A slot's alias is MCP's key, such as `input_schema` for `inputSchema`. Some keys need more:

- `_meta` is `meta`, with `_meta` as its alias.
- `$schema` and the reserved `io.modelcontextprotocol/...` keys are no Python names, so they sit under `aliases`: `schema_dialect`, and `mcp_client_capabilities` and its siblings.
- `name`, `title`, `description`, `url` and `version` mean what LOKF means by them, so they are slots with LOKF's schema.org IRIs.
- Eight keys LOKF defines with another meaning take a name of their own, with MCP's key under `aliases`: `type` is `kind`, `id` is `identifier`, `audience` is `intended_audience`, `context` is `context_info`, `reason` is `reason_text`, `resource` is `resource_contents`, a capability's `url` is `url_settings`, and a list of required names is `required_names`.

`scripts/mcp_meta.py` gives each key back when it writes `meta/schema.json`.

## What the schema adds

MCP's description of `InputRequiredResult` says "At least one of `inputRequests` or `requestState` MUST be present." `schema.json` does not state this, and the schema does. Without it, any result with a `resultType` passes as an input-required result. That is how MCP's own read-resource example passes, though it lacks `cacheScope` and `ttlMs`.

## How the tests hold it to MCP

`tests/test_parity.py` compares `meta/schema.json` with MCP's `schema.json` in three tiers:

1. **Addresses.** Every definition MCP publishes is there but `JSONArray`, which no definition uses and LinkML cannot state.
2. **Verdicts.** MCP's 129 examples, the examples under `tests/data/problem/`, a smallest instance of each definition and about 11,000 mutations of them get the same verdict from both files, with the rule above added to MCP's.
3. **Shapes.** Nine definitions differ once both sides are normalised, each listed in `parity/structural.yaml` with its reason.

`parity/probes.yaml` lists each difference in what the two files accept.

## What LinkML cannot state

- **A JSON value.** `schema.ts` defines it as any JSON value, while `schema.json` writes it with integer in place of number and without null. The schema's `McpJSONValue` is any JSON value, as `schema.ts` defines it.
- **A named union of scalars.** `RequestId` and `ProgressToken` are types with `union_of`, but linkml 1.12.1's JSON Schema generator reads only a type's `typeof`, so each slot that takes one states the union itself.
- **The generators' gaps.** `scripts/mcp_meta.py` repairs three faults of gen-json-schema. gen-pydantic ignores `extra_slots`, so its models refuse keys MCP allows (linkml #3630). gen-owl writes a union class with no members, so the OWL keeps the classes but not the unions.
