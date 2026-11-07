# Test data

Each file is an MCP message or part of one, or a broken copy of one, named
`<Class>-<what it shows>.yaml` after the class it is checked against.

- `problem/valid/` holds examples that must pass, at least one for each class a
  knowledge-bundle concept may name as its type.
- `problem/invalid/` holds examples that must fail, each breaking one rule.

The examples use MCP's keys. The example runner reads a key listed under
`aliases`, such as `io.modelcontextprotocol/protocolVersion`, by the slot's name,
so the examples are kept under `problem/`, where it does not look.
`tests/test_data.py` checks each against `meta/schema.json` and MCP's own
`schema.json`. `valid/` and `invalid/` stay empty.
