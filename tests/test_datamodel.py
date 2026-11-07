"""The generated Python models import, and hold every class of the schema."""

import importlib

from linkml_runtime import SchemaView

from mcp_parity import ROOT


def test_dataclasses_and_pydantic_models_import():
    view = SchemaView(str(ROOT / "src" / "mcp" / "schema" / "mcp.yaml"))
    for module in ("mcp.datamodel.mcp", "mcp.datamodel.mcp_pydantic"):
        models = importlib.import_module(module)
        for name, cls in view.all_classes().items():
            # gen-pydantic writes a linkml:Any class as typing.Any, not as a model.
            if module.endswith("_pydantic") and cls.class_uri == "linkml:Any":
                continue
            assert hasattr(models, name), (module, name)


def test_pydantic_reads_an_mcp_key():
    """gen-pydantic names a field by its alias where the alias is a Python name, so a model
    reads MCP's key. linkml 1.12.1's gen-pydantic ignores extra_slots, so its models refuse a
    key the schema does not name, where MCP's objects are open; linkml #3630 asks for it."""
    models = importlib.import_module("mcp.datamodel.mcp_pydantic")
    tool = models.McpTool.model_validate(
        {"name": "t", "inputSchema": {"type": "object"}, "_meta": {}}
    )
    assert tool.inputSchema.type == "object"
    assert tool.meta is not None
