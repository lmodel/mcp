## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Directory containing vendor (third-party) test data
vendor_data_dir := "tests/data/third_party/mcp/draft"

# Validate vendor MCP draft data against the LinkML schema
[group('model development')]
test-vendor:
  #!/usr/bin/env bash
  set -euo pipefail
  echo "Validating: 'tests/data/third_party/mcp/schema/draft/examples/*/*.json' ..."
  failed=0
  while IFS= read -r file; do
    class_name=$(basename "$(dirname "$file")")
    output=$(uv run python tests/validate_vendor.py --target-class "$class_name" "$file" 2>&1)
    if echo "$output" | grep -q '^\[ERROR\]'; then
      echo "$output"
      failed=1
    fi
  done < <(find {{vendor_data_dir}} -type f -name '*.json' | sort)
  if [ "$failed" -eq 0 ]; then
    echo "All 'upstream example data' fixtures passed."
  else
    exit 1
  fi
