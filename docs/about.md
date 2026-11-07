# About mcp

## One version

The schema models MCP 2026-07-28, the `schema/2026-07-28/` folder at the tag `2026-07-28` of [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol). `upstream/` holds that folder's `schema.json`, `schema.ts` and 129 examples, and the repository's licence, pinned by git object hash. The upstream watch reports a new tag or version folder, and any further edit to the pinned files on MCP's default branch. By 2026-11-07 that branch had already edited three of them: `schema.json` (a description), `schema.ts` and one example. The watch knows those edits.

Before this release, the schema was written by hand against an MCP draft. MCP 2026-07-28 drops initialization, tasks and several requests that draft had, and adds discovery, subscriptions and input-required results, so a script now writes the schema: moving to the next version takes one run of the converter.

## How the converter reads MCP

`scripts/mcp_to_linkml.py` reads `schema.json` for structure and descriptions, and `schema.ts` for what JSON Schema cannot carry.

- An object definition is a class with the `Mcp` prefix, such as `McpTool`. Every object MCP publishes is open, so every class allows extra slots.
- A union of definitions, such as `ContentBlock`, is a class whose `any_of` names each member through `is_a`.
- A list of strings is an enum, and a string or a string-or-integer is a type.
- An inline object, such as a tool's `inputSchema`, is a class named after its owner and key, such as `McpToolInputSchema`.
- Each interface's `extends` in `schema.ts` gives `is_a` and `mixins`, and each `@category` a subset.
- Each class and enum, and each type but the format types `McpBase64` and `McpUriTemplate`, maps exactly to the place in `schema.json` it renders, such as `mcp_schema:Tool`.

Each class states every key of its definition, inherited or not, as `schema.json` does. The schema carries MCP's descriptions word for word. Where MCP gives a property none, the converter takes `CONST_DESCRIPTIONS` for a constant, then the description of the definition the property refers to, then `DESCRIPTIONS`. An inline object MCP does not describe gets a sentence that names where MCP holds it.

## Keys

A slot's alias is MCP's key, such as `input_schema` for `inputSchema`. Some keys need more:

- `_meta` is `meta`, with `_meta` as its alias.
- `$schema` and the reserved `io.modelcontextprotocol/...` keys are no Python names, so they are listed under `aliases`: `schema_dialect`, and `mcp_client_capabilities` and its siblings.
- `name`, `title`, `description`, `url` and `version` mean what LOKF means by them, so they are slots with LOKF's schema.org IRIs.
- Eight keys LOKF defines with another meaning take a name of their own, with MCP's key under `aliases`. `type` is `kind`, `id` is `identifier`, `audience` is `intended_audience`, `context` is `context_info`, `reason` is `reason_text`, `resource` is `resource_contents`, a capability's `url` is `url_settings`, and a list of required names is `required_names`.

For each key listed under `aliases`, `scripts/mcp_meta.py` writes that key in place of the slot's name in `meta/schema.json`.

## What the schema adds

MCP's description of `InputRequiredResult` says "At least one of `inputRequests` or `requestState` MUST be present." The schema states this rule, and `schema.json` does not. Without it, any result with a `resultType` passes as an input-required result. That is how MCP's own read-resource example passes, though it lacks `cacheScope` and `ttlMs`.

## How the tests hold it to MCP

`tests/test_parity.py` compares `meta/schema.json` with MCP's `schema.json` in three tiers:

1. **Addresses.** `meta/schema.json` holds every definition MCP publishes except `JSONArray`, which no definition uses and LinkML cannot state.
2. **Verdicts.** Both files give the same verdict on MCP's 129 examples, the examples under `tests/data/problem/`, a smallest instance of each definition and about 11,000 mutations of them, except the differences `parity/probes.yaml` lists. For this tier, the tests compare the generated file with a copy of MCP's file that has the rule above added.
3. **Shapes.** After both files are normalised, nine definitions differ. `parity/structural.yaml` lists each with its reason.

`parity/probes.yaml` lists each difference in what the two files accept.

## What LinkML cannot state

- **A JSON value.** `schema.ts` defines it as any JSON value. `schema.json` writes it with integer in place of number and without null. The schema's `McpJSONValue` is any JSON value, as `schema.ts` defines it.
- **A named union of scalars.** `RequestId` and `ProgressToken` are types with `union_of`, but linkml 1.12.1's JSON Schema generator reads only a type's `typeof`, so each slot that takes one states the union itself.
- **The generators' gaps.** `scripts/mcp_meta.py` repairs three faults of gen-json-schema. gen-pydantic ignores `extra_slots`, so its models refuse keys MCP allows (linkml #3630). gen-owl writes a union class with no members, so the OWL keeps the classes but not the unions.
