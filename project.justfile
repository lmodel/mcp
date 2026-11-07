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
