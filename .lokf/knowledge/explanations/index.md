# Explanations

* [How the tests hold the schema to MCP](parity-tiers.md) - The three parity tiers of `tests/test_parity.py`: every MCP definition is there, MCP's examples and their mutations get the same verdicts, and the shapes differ only as `parity/structural.yaml` lists.
* [How the schema names MCP's keys](keys.md) - Which MCP keys keep their name, which take an alias, which share LOKF's schema.org IRI (name, title, description, url, version), which the adapt copy renames, such as type, and which take a name of their own, such as url_settings.
* [The rule the schema adds to MCP's file](input-required-rule.md) - The schema states that an InputRequiredResult holds inputRequests or requestState, as MCP's description says and its schema.json does not, which MCP's own read-resource example breaks.
