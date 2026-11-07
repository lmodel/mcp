# Services

* [The converter](converter.md) - `scripts/mcp_to_linkml.py`, which writes the LinkML schema from MCP's schema.json and schema.ts: classes, unions, enums, types, is_a from schema.ts, a subset per category and an exact mapping per element.
* [The writer of meta/](meta-writer.md) - `scripts/mcp_meta.py`, which runs gen-json-schema on the schema and shapes its output into MCP's form in `meta/schema.json`, with MCP's definition names and keys, and three repairs of the generator.
* [The upstream watch](upstream-watch.md) - `scripts/check_upstream_release.py`, run weekly by `.github/workflows/upstream-watch.yaml`: it reports a new MCP tag or version folder, a moved tag, a pinned file changed, and a changed licence, and opens an issue.
* [The release](release.md) - `.github/workflows/semantic-release.yml`, which releases from a v0.0.0 baseline tag on a feat, fix or security merge, and dispatches the knowledge release that attaches the adapt copy and the bundle.
