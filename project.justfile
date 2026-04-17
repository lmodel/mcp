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
  total=0
  passed=0
  failed=0
  skipped=0
  while IFS= read -r file; do
    total=$((total + 1))
    class_name=$(basename "$(dirname "$file")")
    output=$(uv run python tests/validate_vendor.py --target-class "$class_name" "$file" 2>&1)
    if grep -q '^\[ERROR\]' <<< "$output"; then
      echo "$output"
      failed=$((failed + 1))
    elif grep -q '^\[SKIP\]' <<< "$output"; then
      echo "$output"
      skipped=$((skipped + 1))
    else
      passed=$((passed + 1))
    fi
  done < <(find {{vendor_data_dir}} -type f -name '*.json' | sort)

  echo -e "\033[32mSummary: total=$total passed=$passed failed=$failed skipped=$skipped\033[0m"

  if [ "$failed" -ne 0 ]; then
    exit 1
  fi
