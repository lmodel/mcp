## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Write the schema from MCP's files, then MCP's form of it in meta/
[group('model development')]
gen-mcp:
  uv run python scripts/mcp_to_linkml.py
  uv run python scripts/mcp_meta.py

# Fail when the schema or meta/ no longer matches what gen-mcp writes
[group('model development')]
check-mcp:
  uv run python scripts/mcp_to_linkml.py --check
  uv run python scripts/mcp_meta.py --check

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/schema/mcp.yaml` is the copy `lokf adapt` writes from the schema so that it can sit beside
# `.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are what a person
# documents about an MCP server: the implementation, and the tools, resources, resource templates
# and prompts it offers. A concept names one of them as its `type`. Messages stay values. MCP's
# description, title and version fold into LOKF's, which mean the same. The keys name and url,
# and the six slots LOKF defines with another meaning, keep slots of their own, renamed
# mcp_name, mcp_url, and mcp_type and its siblings. The recipes run the `lokf` the sidecar's
# floor pins (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root McpImplementation --root McpTool --root McpResource --root McpResourceTemplate --root McpPrompt --keep name --keep url"

# Rewrite .lokf/schema/mcp.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/mcp.yaml

# Fail when .lokf/schema/mcp.yaml is stale against the schema or .lokf/schema/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/mcp.yaml --check
