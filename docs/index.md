# mcp

This project is a LinkML model of the Model Context Protocol (MCP) at version 2026-07-28: the JSON-RPC messages a client and a server exchange, and the tools, resources, prompts, content and capabilities they carry. A script writes the model from MCP's own `schema.json` and `schema.ts`.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the schema reads MCP, what it adds and what it leaves out
- [`mcp.yaml`](schema/mcp.yaml): the schema

## Validating a message

`meta/schema.json` is MCP's `schema.json` written again from the model, with MCP's keys. Any JSON Schema 2020-12 validator checks a message against one of its definitions:

```python
import json
from jsonschema import Draft202012Validator

schema = json.load(open("meta/schema.json"))
validator = Draft202012Validator({**schema, "$ref": "#/$defs/CallToolRequest"})
validator.validate(json.load(open("my-request.json")))
```

`project/jsonschema/mcp.schema.json` and the Python models in `src/mcp/datamodel/` read a key listed under `aliases` by the schema's name, so `$schema` reads `schema_dialect` there ([About](about.md#keys)).

## A message

```yaml
jsonrpc: "2.0"
id: 42
method: tools/call
params:
  name: get_forecast
  arguments: {city: Galway}
  _meta:
    io.modelcontextprotocol/protocolVersion: "2026-07-28"
    io.modelcontextprotocol/clientCapabilities: {}
```

`tests/data/problem/valid/` holds an example of each class a knowledge-bundle concept may name as its type.
