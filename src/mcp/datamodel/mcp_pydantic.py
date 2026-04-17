from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "draft"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'mcp',
     'default_range': 'string',
     'description': 'Model Context Protocol LinkML Schema',
     'id': 'https://w3id.org/lmodel/mcp',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'mcp',
     'prefixes': {'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'jsonrpc': {'prefix_prefix': 'jsonrpc',
                              'prefix_reference': 'https://www.jsonrpc.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mcp': {'prefix_prefix': 'mcp',
                          'prefix_reference': 'https://w3id.org/lmodel/mcp/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://lmodel.github.io/mcp',
                  'https://spec.modelcontextprotocol.io'],
     'source': 'https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/schema',
     'source_file': 'src/mcp/schema/mcp.yaml',
     'title': 'mcp',
     'types': {'Cursor': {'base': 'str',
                          'description': 'An opaque token used to represent a '
                                         'cursor for pagination.',
                          'from_schema': 'https://w3id.org/lmodel/mcp',
                          'name': 'Cursor',
                          'uri': 'xsd:string'},
               'JsonValue': {'aliases': ['JSONValue', 'JSONArray', 'JSONObject'],
                             'base': 'object',
                             'description': 'Any JSON-serializable value.',
                             'from_schema': 'https://w3id.org/lmodel/mcp',
                             'name': 'JsonValue',
                             'uri': 'xsd:anyType'},
               'ProgressToken': {'base': 'str',
                                 'description': 'A progress token, used to '
                                                'associate progress notifications '
                                                'with the original request.',
                                 'from_schema': 'https://w3id.org/lmodel/mcp',
                                 'name': 'ProgressToken',
                                 'uri': 'xsd:string'},
               'RequestId': {'base': 'str',
                             'description': 'A uniquely identifying ID for a '
                                            'request in JSON-RPC.',
                             'from_schema': 'https://w3id.org/lmodel/mcp',
                             'name': 'RequestId',
                             'uri': 'xsd:string'}}} )

class Role(str, Enum):
    """
    The sender or recipient of messages and data in a conversation.
    """
    assistant = "assistant"
    """
    The assistant role.
    """
    user = "user"
    """
    The user role.
    """


class LoggingLevel(str, Enum):
    """
    The severity of a log message. Maps to syslog message severities (RFC-5424).
    """
    alert = "alert"
    """
    Alert severity.
    """
    critical = "critical"
    """
    Critical severity.
    """
    debug = "debug"
    """
    Debug severity.
    """
    emergency = "emergency"
    """
    Emergency severity.
    """
    error = "error"
    """
    Error severity.
    """
    info = "info"
    """
    Informational severity.
    """
    notice = "notice"
    """
    Notice severity.
    """
    warning = "warning"
    """
    Warning severity.
    """


class TaskStatusEnum(str, Enum):
    """
    The status of a task.
    """
    cancelled = "cancelled"
    """
    Task was cancelled.
    """
    completed = "completed"
    """
    Task completed successfully.
    """
    failed = "failed"
    """
    Task failed.
    """
    input_required = "input_required"
    """
    Task requires additional input.
    """
    working = "working"
    """
    Task is currently in progress.
    """


class IncludeContextEnum(str, Enum):
    """
    Context inclusion mode for sampling requests.
    """
    allServers = "allServers"
    """
    Include context from all servers.
    """
    none = "none"
    """
    Include no context.
    """
    thisServer = "thisServer"
    """
    Include context from calling server only.
    """


class ElicitActionEnum(str, Enum):
    """
    User action in response to an elicitation.
    """
    accept = "accept"
    """
    User submitted the form/confirmed the action.
    """
    cancel = "cancel"
    """
    User dismissed without making an explicit choice.
    """
    decline = "decline"
    """
    User explicitly declined the action.
    """


class ToolChoiceModeEnum(str, Enum):
    """
    Controls tool selection behavior for sampling requests.
    """
    auto = "auto"
    """
    Model decides whether to use tools (default).
    """
    none = "none"
    """
    Model MUST NOT use any tools.
    """
    required = "required"
    """
    Model MUST use at least one tool before completing.
    """


class TaskSupportEnum(str, Enum):
    """
    Indicates whether a tool supports task-augmented execution.
    """
    forbidden = "forbidden"
    """
    Tool does not support task-augmented execution (default).
    """
    optional = "optional"
    """
    Tool may support task-augmented execution.
    """
    required = "required"
    """
    Tool requires task-augmented execution.
    """


class IconThemeEnum(str, Enum):
    """
    Theme specifier for an icon.
    """
    dark = "dark"
    """
    Icon designed for a dark background.
    """
    light = "light"
    """
    Icon designed for a light background.
    """


class NumberTypeEnum(str, Enum):
    """
    Number type discriminator.
    """
    integer = "integer"
    """
    Integer type.
    """
    number = "number"
    """
    Number type.
    """


class StringFormatEnum(str, Enum):
    """
    String format constraints.
    """
    date = "date"
    """
    Date format.
    """
    date_time = "date-time"
    """
    Date-time format.
    """
    email = "email"
    """
    Email format.
    """
    uri = "uri"
    """
    URI format.
    """



class HasMeta(ConfiguredBaseModel):
    """
    Mixin for types that carry a _meta field.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['NotificationParams', 'RequestParams'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixin': True})

    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class HasAnnotations(ConfiguredBaseModel):
    """
    Mixin for types that carry annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp', 'mixin': True})

    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })


class HasIcons(ConfiguredBaseModel):
    """
    Mixin for types that carry icons.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Icons'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixin': True})

    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class HasName(ConfiguredBaseModel):
    """
    Mixin for types that carry name and title.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['BaseMetadata'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixin': True})

    name: Optional[str] = Field(default=None, description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class Annotations(ConfiguredBaseModel):
    """
    Optional annotations for the client. The client can use annotations to inform how objects are used or displayed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    audience: Optional[list[Role]] = Field(default=None, description="""Describes who the intended audience of this object or data is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotations']} })
    lastModified: Optional[str] = Field(default=None, description="""The moment the resource was last modified, as an ISO 8601 formatted string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotations']} })
    priority: Optional[float] = Field(default=None, description="""How important this data is for operating the server. 1 means most important (required), 0 means least important (optional).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotations']} })


class Error(ConfiguredBaseModel):
    """
    A JSON-RPC error object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'code': {'name': 'code', 'required': True},
                        'data': {'inlined': True, 'name': 'data', 'range': 'ErrorData'},
                        'message': {'name': 'message', 'required': True}}})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error']} })
    data: Optional[ErrorData] = Field(default=None, description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class InternalError(Error):
    """
    A JSON-RPC error indicating that an internal error occurred on the receiver (-32603).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error']} })
    data: Optional[ErrorData] = Field(default=None, description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class InvalidParamsError(Error):
    """
    A JSON-RPC error indicating that the method parameters are invalid or malformed (-32602).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error']} })
    data: Optional[ErrorData] = Field(default=None, description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class InvalidRequestError(Error):
    """
    A JSON-RPC error indicating that the request is not a valid request object (-32600).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error']} })
    data: Optional[ErrorData] = Field(default=None, description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class MethodNotFoundError(Error):
    """
    A JSON-RPC error indicating that the requested method does not exist or is not available (-32601).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error']} })
    data: Optional[ErrorData] = Field(default=None, description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class ParseError(Error):
    """
    A JSON-RPC error indicating that invalid JSON was received by the server (-32700).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error']} })
    data: Optional[ErrorData] = Field(default=None, description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class Icon(ConfiguredBaseModel):
    """
    An optionally-sized icon that can be displayed in a user interface.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'src': {'name': 'src', 'required': True}}})

    src: str = Field(default=..., description="""A standard URI pointing to an icon resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    sizes: Optional[list[str]] = Field(default=None, description="""Optional array of strings specifying sizes (WxH format or \"any\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon']} })
    theme: Optional[IconThemeEnum] = Field(default=None, description="""Optional theme specifier for the icon.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon']} })


class Implementation(HasName, HasIcons):
    """
    Describes the MCP implementation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasName', 'HasIcons'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'version': {'name': 'version', 'required': True}}})

    version: str = Field(default=..., description="""The version of this implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    websiteUrl: Optional[str] = Field(default=None, description="""An optional URL of the website for this implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class TextContent(HasAnnotations, HasMeta):
    """
    Text provided to or from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations'],
         'slot_usage': {'text': {'name': 'text', 'required': True},
                        'type': {'equals_string': 'text',
                                 'name': 'type',
                                 'required': True}}})

    text: str = Field(default=..., description="""Text content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ContentBlock',
                       'ResourceContents',
                       'TextResourceContents']} })
    type: Literal["text"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'text'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })


class ImageContent(HasAnnotations, HasMeta):
    """
    An image provided to or from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations'],
         'slot_usage': {'data': {'name': 'data', 'required': True},
                        'mimeType': {'name': 'mimeType', 'required': True},
                        'type': {'equals_string': 'image',
                                 'name': 'type',
                                 'required': True}}})

    data: str = Field(default=..., description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    mimeType: str = Field(default=..., description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    type: Literal["image"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'image'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })


class AudioContent(HasAnnotations, HasMeta):
    """
    Audio provided to or from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations'],
         'slot_usage': {'data': {'name': 'data', 'required': True},
                        'mimeType': {'name': 'mimeType', 'required': True},
                        'type': {'equals_string': 'audio',
                                 'name': 'type',
                                 'required': True}}})

    data: str = Field(default=..., description="""Base64-encoded binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    mimeType: str = Field(default=..., description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    type: Literal["audio"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'audio'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })


class ContentBlock(ConfiguredBaseModel):
    """
    Structured text content block.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True}, 'from_schema': 'https://w3id.org/lmodel/mcp'})

    type: Optional[str] = Field(default=None, description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    text: Optional[str] = Field(default=None, description="""Text content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ContentBlock',
                       'ResourceContents',
                       'TextResourceContents']} })


class EmbeddedResource(HasAnnotations, HasMeta):
    """
    The contents of a resource, embedded into a prompt or tool call result.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations'],
         'slot_usage': {'resource': {'inlined': True,
                                     'name': 'resource',
                                     'range': 'ResourceContents',
                                     'required': True},
                        'type': {'equals_string': 'resource',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["resource"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'resource'} })
    resource: ResourceContents = Field(default=..., description="""The embedded resource contents (text or blob).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmbeddedResource']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })


class ResourceLink(HasName, HasIcons, HasAnnotations, HasMeta):
    """
    A resource that the server is capable of reading, included in a prompt or tool call result.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations', 'HasName', 'HasIcons'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'type': {'equals_string': 'resource_link',
                                 'name': 'type',
                                 'required': True},
                        'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    size: Optional[int] = Field(default=None, description="""The size of the raw resource content, in bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink', 'Resource']} })
    type: Literal["resource_link"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'resource_link'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class ToolUseContent(HasMeta):
    """
    A request from the assistant to call a tool.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'id': {'description': 'A unique identifier for this tool use.',
                               'name': 'id',
                               'range': 'string',
                               'required': True},
                        'input': {'inlined': True,
                                  'name': 'input',
                                  'range': 'ToolInput',
                                  'required': True},
                        'name': {'name': 'name', 'required': True},
                        'type': {'equals_string': 'tool_use',
                                 'name': 'type',
                                 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for this tool use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    type: Literal["tool_use"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'tool_use'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    input: ToolInput = Field(default=..., description="""The arguments to pass to the tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ToolResultContent(HasMeta):
    """
    The result of a tool use, provided by the user back to the assistant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'content': {'description': 'The unstructured result content of '
                                                   'the tool use.',
                                    'multivalued': True,
                                    'name': 'content',
                                    'range': 'ContentBlock',
                                    'required': True},
                        'toolUseId': {'name': 'toolUseId', 'required': True},
                        'type': {'equals_string': 'tool_result',
                                 'name': 'type',
                                 'required': True}}})

    content: list[ContentBlock] = Field(default=..., description="""The unstructured result content of the tool use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent',
                       'PromptMessage',
                       'SamplingMessage',
                       'CallToolResult',
                       'CreateMessageResult',
                       'ElicitResult']} })
    type: Literal["tool_result"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'tool_result'} })
    toolUseId: str = Field(default=..., description="""The ID of the tool use this result corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent']} })
    isError: Optional[bool] = Field(default=None, description="""Whether the tool call ended in an error.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent', 'CallToolResult']} })
    structuredContent: Optional[StructuredContentData] = Field(default=None, description="""An optional JSON object representing structured result of the tool call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent', 'CallToolResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ResourceContents(HasMeta):
    """
    Generic resource contents.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    text: Optional[str] = Field(default=None, description="""Text content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ContentBlock',
                       'ResourceContents',
                       'TextResourceContents']} })
    blob: Optional[str] = Field(default=None, description="""A base64-encoded string representing binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceContents', 'BlobResourceContents']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class TextResourceContents(HasMeta):
    """
    Text resource contents.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'text': {'name': 'text', 'required': True},
                        'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    text: str = Field(default=..., description="""Text content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ContentBlock',
                       'ResourceContents',
                       'TextResourceContents']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class BlobResourceContents(HasMeta):
    """
    Blob resource contents.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'blob': {'name': 'blob', 'required': True},
                        'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    blob: str = Field(default=..., description="""A base64-encoded string representing binary data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceContents', 'BlobResourceContents']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class Resource(HasName, HasIcons, HasAnnotations, HasMeta):
    """
    A known resource that the server is capable of reading.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations', 'HasName', 'HasIcons'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    size: Optional[int] = Field(default=None, description="""The size of the raw resource content, in bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink', 'Resource']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class ResourceTemplate(HasName, HasIcons, HasAnnotations, HasMeta):
    """
    A template description for resources available on the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasAnnotations', 'HasName', 'HasIcons'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'uriTemplate': {'name': 'uriTemplate', 'required': True}}})

    uriTemplate: str = Field(default=..., description="""A URI template (RFC 6570) for constructing resource URIs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceTemplate']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of a resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Icon',
                       'ImageContent',
                       'AudioContent',
                       'ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'ResourceTemplate']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    annotations: Optional[Annotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class Root(HasMeta):
    """
    Represents a root directory or file that the server can operate on.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    name: Optional[str] = Field(default=None, description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class PromptArgument(HasName):
    """
    Describes an argument that a prompt can accept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasName'],
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    required: Optional[bool] = Field(default=None, description="""Whether this argument must be provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PromptArgument']} })
    required_field: Optional[bool] = Field(default=None, description="""Whether this argument must be provided.""", json_schema_extra = { "linkml_meta": {'aliases': ['required'], 'domain_of': ['PromptArgument']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class Prompt(HasName, HasIcons, HasMeta):
    """
    A prompt or prompt template that the server offers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasName', 'HasIcons'],
         'slot_usage': {'arguments': {'description': 'A list of arguments to use for '
                                                     'templating the prompt.',
                                      'inlined_as_list': True,
                                      'multivalued': True,
                                      'name': 'arguments',
                                      'range': 'PromptArgument'},
                        'name': {'name': 'name', 'required': True}}})

    arguments: Optional[list[PromptArgument]] = Field(default=None, description="""A list of arguments to use for templating the prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prompt',
                       'CompletionContext',
                       'CallToolRequestParams',
                       'GetPromptRequestParams']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class PromptMessage(ConfiguredBaseModel):
    """
    Describes a message returned as part of a prompt.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'content': {'description': 'The content of the prompt message.',
                                    'name': 'content',
                                    'range': 'ContentBlock',
                                    'required': True},
                        'role': {'name': 'role', 'required': True}}})

    content: ContentBlock = Field(default=..., description="""The content of the prompt message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent',
                       'PromptMessage',
                       'SamplingMessage',
                       'CallToolResult',
                       'CreateMessageResult',
                       'ElicitResult']} })
    role: Role = Field(default=..., description="""The role of the sender or recipient.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PromptMessage', 'SamplingMessage', 'CreateMessageResult']} })


class PromptReference(HasName):
    """
    Identifies a prompt.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasName'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'type': {'equals_string': 'ref/prompt',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["ref/prompt"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'ref/prompt'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class ResourceTemplateReference(ConfiguredBaseModel):
    """
    A reference to a resource or resource template definition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'type': {'equals_string': 'ref/resource',
                                 'name': 'type',
                                 'required': True},
                        'uri': {'name': 'uri', 'required': True}}})

    type: Literal["ref/resource"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'ref/resource'} })
    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })


class ToolAnnotations(ConfiguredBaseModel):
    """
    Additional properties describing a Tool to clients. All properties are hints, not guarantees.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    destructiveHint: Optional[bool] = Field(default=None, description="""If true, the tool may perform destructive updates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolAnnotations']} })
    idempotentHint: Optional[bool] = Field(default=None, description="""If true, calling repeatedly with same arguments has no additional effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolAnnotations']} })
    openWorldHint: Optional[bool] = Field(default=None, description="""If true, tool may interact with an open world of external entities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolAnnotations']} })
    readOnlyHint: Optional[bool] = Field(default=None, description="""If true, the tool does not modify its environment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolAnnotations']} })


class ToolChoice(ConfiguredBaseModel):
    """
    Controls tool selection behavior for sampling requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'mode': {'description': 'Controls the tool use ability of the '
                                                'model.',
                                 'name': 'mode',
                                 'range': 'ToolChoiceModeEnum'}}})

    mode: Optional[ToolChoiceModeEnum] = Field(default=None, description="""Controls the tool use ability of the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolChoice',
                       'URLElicitation',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })


class ToolExecution(ConfiguredBaseModel):
    """
    Execution-related properties for a tool.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    taskSupport: Optional[TaskSupportEnum] = Field(default=None, description="""Whether this tool supports task-augmented execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolExecution']} })


class MetaObject(ConfiguredBaseModel):
    """
    Metadata object attached to protocol objects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['RequestMetaObject'], 'from_schema': 'https://w3id.org/lmodel/mcp'})

    progressToken: Optional[str] = Field(default=None, description="""The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaObject', 'ProgressNotificationParams']} })


class ArgumentMap(ConfiguredBaseModel):
    """
    Argument object used in prompt and tool calls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True}, 'from_schema': 'https://w3id.org/lmodel/mcp'})

    city: Optional[str] = Field(default=None, description="""City value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap', 'SchemaProperties', 'ToolInput']} })
    location: Optional[str] = Field(default=None, description="""Location value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap', 'SchemaProperties', 'ToolInput']} })
    language: Optional[str] = Field(default=None, description="""Programming language value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap']} })
    framework: Optional[str] = Field(default=None, description="""Framework value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap']} })


class CompletionArgument(ConfiguredBaseModel):
    """
    Argument descriptor for completion requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'value': {'name': 'value', 'required': True}}})

    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    value: str = Field(default=..., description="""A value string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompletionArgument']} })


class CompletionContext(ConfiguredBaseModel):
    """
    Additional context for completion requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    arguments: Optional[ArgumentMap] = Field(default=None, description="""Arguments for templating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prompt',
                       'CompletionContext',
                       'CallToolRequestParams',
                       'GetPromptRequestParams']} })


class CompletionData(ConfiguredBaseModel):
    """
    Completion result payload.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'values': {'name': 'values', 'required': True}}})

    values: list[str] = Field(default=..., description="""An array of completion values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompletionData']} })
    total: Optional[float] = Field(default=None, description="""Total number of items to process (or total progress required), if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompletionData', 'ProgressNotificationParams']} })
    hasMore: Optional[bool] = Field(default=None, description="""Indicates whether there are additional completion options.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompletionData']} })


class EnumOption(ConfiguredBaseModel):
    """
    Single enumerated option with a machine value and display title.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'const': {'name': 'const', 'required': True}}})

    const: str = Field(default=..., description="""JSON Schema const value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnumOption', 'JsonSchema']} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class SchemaItems(ConfiguredBaseModel):
    """
    JSON Schema items expression used by enum multi-select schemas.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    type: Optional[str] = Field(default=None, description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    enum: Optional[list[str]] = Field(default=None, description="""Array of enum values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaItems',
                       'JsonSchema',
                       'UntitledSingleSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    anyOf: Optional[list[EnumOption]] = Field(default=None, description="""JSON Schema anyOf entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaItems', 'JsonSchema']} })


class JsonSchema(ConfiguredBaseModel):
    """
    Restricted JSON Schema object used in MCP payloads.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True}, 'from_schema': 'https://w3id.org/lmodel/mcp'})

    schemaUri: Optional[str] = Field(default=None, description="""Optional JSON Schema dialect identifier.""", json_schema_extra = { "linkml_meta": {'aliases': ['$schema'], 'domain_of': ['JsonSchema']} })
    type: Optional[str] = Field(default=None, description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    properties: Optional[SchemaProperties] = Field(default=None, description="""JSON Schema properties map.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema']} })
    required_list: Optional[list[str]] = Field(default=None, description="""JSON Schema required property list.""", json_schema_extra = { "linkml_meta": {'aliases': ['required'], 'domain_of': ['JsonSchema']} })
    additionalProperties: Optional[bool] = Field(default=None, description="""JSON Schema additionalProperties flag.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema']} })
    minimum: Optional[int] = Field(default=None, description="""Minimum value constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'NumberSchema']} })
    maximum: Optional[int] = Field(default=None, description="""Maximum value constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'NumberSchema']} })
    minLength: Optional[int] = Field(default=None, description="""Minimum length constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'StringSchema']} })
    maxLength: Optional[int] = Field(default=None, description="""Maximum length constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'StringSchema']} })
    format: Optional[StringFormatEnum] = Field(default=None, description="""String format constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'StringSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    oneOf: Optional[list[EnumOption]] = Field(default=None, description="""JSON Schema oneOf entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'TitledSingleSelectEnumSchema']} })
    anyOf: Optional[list[EnumOption]] = Field(default=None, description="""JSON Schema anyOf entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaItems', 'JsonSchema']} })
    items: Optional[SchemaItems] = Field(default=None, description="""JSON Schema items definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema']} })
    enum: Optional[list[str]] = Field(default=None, description="""Array of enum values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaItems',
                       'JsonSchema',
                       'UntitledSingleSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    const: Optional[str] = Field(default=None, description="""JSON Schema const value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnumOption', 'JsonSchema']} })
    default: Optional[object] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })


class SchemaProperties(ConfiguredBaseModel):
    """
    Named JSON Schema property map used by vendor fixtures.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'a': {'inlined': True, 'name': 'a', 'range': 'JsonSchema'},
                        'age': {'inlined': True, 'name': 'age', 'range': 'JsonSchema'},
                        'b': {'inlined': True, 'name': 'b', 'range': 'JsonSchema'},
                        'city': {'inlined': True,
                                 'name': 'city',
                                 'range': 'JsonSchema'},
                        'conditions': {'inlined': True,
                                       'name': 'conditions',
                                       'range': 'JsonSchema'},
                        'email': {'inlined': True,
                                  'name': 'email',
                                  'range': 'JsonSchema'},
                        'humidity': {'inlined': True,
                                     'name': 'humidity',
                                     'range': 'JsonSchema'},
                        'location': {'inlined': True,
                                     'name': 'location',
                                     'range': 'JsonSchema'},
                        'name': {'inlined': True,
                                 'name': 'name',
                                 'range': 'JsonSchema'},
                        'temperature': {'inlined': True,
                                        'name': 'temperature',
                                        'range': 'JsonSchema'}}})

    name: Optional[JsonSchema] = Field(default=None, description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    email: Optional[JsonSchema] = Field(default=None, description="""Email value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'ElicitationContent']} })
    age: Optional[JsonSchema] = Field(default=None, description="""Age value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'ElicitationContent']} })
    city: Optional[JsonSchema] = Field(default=None, description="""City value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap', 'SchemaProperties', 'ToolInput']} })
    location: Optional[JsonSchema] = Field(default=None, description="""Location value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap', 'SchemaProperties', 'ToolInput']} })
    a: Optional[JsonSchema] = Field(default=None, description="""JSON Schema property for key a.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties']} })
    b: Optional[JsonSchema] = Field(default=None, description="""JSON Schema property for key b.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties']} })
    temperature: Optional[JsonSchema] = Field(default=None, description="""Sampling temperature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties',
                       'StructuredContentData',
                       'CreateMessageRequestParams']} })
    conditions: Optional[JsonSchema] = Field(default=None, description="""Weather conditions description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'StructuredContentData']} })
    humidity: Optional[JsonSchema] = Field(default=None, description="""Humidity percentage value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'StructuredContentData']} })


class ToolInput(ConfiguredBaseModel):
    """
    Tool input payload.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    city: Optional[str] = Field(default=None, description="""City value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap', 'SchemaProperties', 'ToolInput']} })
    location: Optional[str] = Field(default=None, description="""Location value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ArgumentMap', 'SchemaProperties', 'ToolInput']} })


class StructuredContentData(ConfiguredBaseModel):
    """
    Structured content object returned by tools.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    temperature: Optional[float] = Field(default=None, description="""Sampling temperature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties',
                       'StructuredContentData',
                       'CreateMessageRequestParams']} })
    conditions: Optional[str] = Field(default=None, description="""Weather conditions description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'StructuredContentData']} })
    humidity: Optional[float] = Field(default=None, description="""Humidity percentage value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'StructuredContentData']} })


class LogDetails(ConfiguredBaseModel):
    """
    Structured details attached to log data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    host: Optional[str] = Field(default=None, description="""Host value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LogDetails']} })
    port: Optional[int] = Field(default=None, description="""Port value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LogDetails']} })


class LogData(ConfiguredBaseModel):
    """
    Structured log data payload.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'details': {'inlined': True,
                                    'name': 'details',
                                    'range': 'LogDetails'},
                        'error': {'name': 'error', 'range': 'string'}}})

    error: Optional[str] = Field(default=None, description="""The error object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LogData', 'JSONRPCErrorResponse']} })
    details: Optional[LogDetails] = Field(default=None, description="""Nested log details object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LogData']} })


class ErrorData(ConfiguredBaseModel):
    """
    Structured JSON-RPC error data payload.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'elicitations': {'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'elicitations',
                                         'range': 'URLElicitation'}}})

    reason: Optional[str] = Field(default=None, description="""An optional string describing the reason.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ErrorData', 'CancelledNotificationParams']} })
    elicitations: Optional[list[URLElicitation]] = Field(default=None, description="""URL elicitation entries included in error data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ErrorData']} })


class ElicitationContent(ConfiguredBaseModel):
    """
    Form values returned by an elicitation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    name: Optional[str] = Field(default=None, description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    email: Optional[str] = Field(default=None, description="""Email value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'ElicitationContent']} })
    age: Optional[int] = Field(default=None, description="""Age value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties', 'ElicitationContent']} })


class URLElicitation(ConfiguredBaseModel):
    """
    URL-based elicitation request payload carried in error data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    mode: Optional[str] = Field(default=None, description="""The elicitation mode.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolChoice',
                       'URLElicitation',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })
    elicitationId: Optional[str] = Field(default=None, description="""The ID of the elicitation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['URLElicitation',
                       'ElicitationCompleteNotificationParams',
                       'ElicitRequestURLParams']} })
    message: Optional[str] = Field(default=None, description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })
    url: Optional[str] = Field(default=None, description="""The URL that the user should navigate to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['URLElicitation', 'ElicitRequestURLParams']} })


class ElicitationCapability(ConfiguredBaseModel):
    """
    Client elicitation capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class SamplingCapability(ConfiguredBaseModel):
    """
    Client sampling capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class RootsCapability(ConfiguredBaseModel):
    """
    Client roots capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    listChanged: Optional[bool] = Field(default=None, description="""Whether notifications for list changes are supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RootsCapability',
                       'PromptsCapability',
                       'ResourcesCapability',
                       'ToolsCapability']} })


class PromptsCapability(ConfiguredBaseModel):
    """
    Server prompts capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    listChanged: Optional[bool] = Field(default=None, description="""Whether notifications for list changes are supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RootsCapability',
                       'PromptsCapability',
                       'ResourcesCapability',
                       'ToolsCapability']} })


class ResourcesCapability(ConfiguredBaseModel):
    """
    Server resources capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    listChanged: Optional[bool] = Field(default=None, description="""Whether notifications for list changes are supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RootsCapability',
                       'PromptsCapability',
                       'ResourcesCapability',
                       'ToolsCapability']} })
    subscribe: Optional[bool] = Field(default=None, description="""Whether subscribing to resource updates is supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourcesCapability']} })


class ToolsCapability(ConfiguredBaseModel):
    """
    Server tools capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    listChanged: Optional[bool] = Field(default=None, description="""Whether notifications for list changes are supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RootsCapability',
                       'PromptsCapability',
                       'ResourcesCapability',
                       'ToolsCapability']} })


class TaskRequestCapabilities(ConfiguredBaseModel):
    """
    Task request capability map.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'elicitation': {'inlined': True,
                                        'name': 'elicitation',
                                        'range': 'ElicitationCapability'},
                        'sampling': {'inlined': True,
                                     'name': 'sampling',
                                     'range': 'SamplingCapability'},
                        'tools': {'inlined': True,
                                  'multivalued': False,
                                  'name': 'tools',
                                  'range': 'ToolsCapability'}}})

    elicitation: Optional[ElicitationCapability] = Field(default=None, description="""Elicitation capability object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities', 'ClientCapabilities']} })
    sampling: Optional[SamplingCapability] = Field(default=None, description="""Sampling capability object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities', 'ClientCapabilities']} })
    tools: Optional[ToolsCapability] = Field(default=None, description="""The list of tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities',
                       'ServerCapabilities',
                       'CreateMessageRequestParams',
                       'ListToolsResult']} })


class TasksCapability(ConfiguredBaseModel):
    """
    Task capability object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'requests': {'inlined': True,
                                     'name': 'requests',
                                     'range': 'TaskRequestCapabilities'}}})

    requests: Optional[TaskRequestCapabilities] = Field(default=None, description="""Task request capabilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TasksCapability']} })


class ExtensionsCapability(ConfiguredBaseModel):
    """
    Server/client extension capability object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'apps_extension': {'inlined': True,
                                           'name': 'apps_extension',
                                           'range': 'ExtensionAppCapability'}}})

    apps_extension: Optional[ExtensionAppCapability] = Field(default=None, description="""Extension capability entry for app mime types.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/apps'],
         'domain_of': ['ExtensionsCapability']} })


class ExtensionAppCapability(ConfiguredBaseModel):
    """
    Extension payload for app mime type declarations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'mimeTypes': {'inlined_as_list': True,
                                      'multivalued': True,
                                      'name': 'mimeTypes'}}})

    mimeTypes: Optional[list[str]] = Field(default=None, description="""MIME types supported by an extension capability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionAppCapability']} })


class Tool(HasName, HasIcons, HasMeta):
    """
    Definition for a tool the client can call.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta', 'HasName', 'HasIcons'],
         'slot_usage': {'annotations': {'description': 'Optional additional tool '
                                                       'information.',
                                        'inlined': True,
                                        'name': 'annotations',
                                        'range': 'ToolAnnotations'},
                        'execution': {'description': 'Execution-related properties for '
                                                     'this tool.',
                                      'inlined': True,
                                      'name': 'execution',
                                      'range': 'ToolExecution'},
                        'inputSchema': {'name': 'inputSchema', 'required': True},
                        'name': {'name': 'name', 'required': True}}})

    annotations: Optional[ToolAnnotations] = Field(default=None, description="""Optional additional tool information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasAnnotations', 'Tool']} })
    execution: Optional[ToolExecution] = Field(default=None, description="""Execution-related properties for this tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Tool']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    inputSchema: JsonSchema = Field(default=..., description="""A JSON Schema object defining the expected parameters for the tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Tool']} })
    outputSchema: Optional[JsonSchema] = Field(default=None, description="""An optional JSON Schema object defining the structure of the tool's output.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Tool']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    icons: Optional[list[Icon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasIcons']} })


class ModelHint(ConfiguredBaseModel):
    """
    Hints to use for model selection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    name: Optional[str] = Field(default=None, description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })


class ModelPreferences(ConfiguredBaseModel):
    """
    The server's preferences for model selection, requested of the client during sampling.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    costPriority: Optional[float] = Field(default=None, description="""How much to prioritize cost when selecting a model (0-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelPreferences']} })
    intelligencePriority: Optional[float] = Field(default=None, description="""How much to prioritize intelligence when selecting a model (0-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelPreferences']} })
    speedPriority: Optional[float] = Field(default=None, description="""How much to prioritize sampling speed when selecting a model (0-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelPreferences']} })
    hints: Optional[list[ModelHint]] = Field(default=None, description="""Optional hints to use for model selection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelPreferences']} })


class SamplingMessage(HasMeta):
    """
    Describes a message issued to or received from an LLM API.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'content': {'any_of': [{'range': 'ContentBlock'},
                                               {'multivalued': True,
                                                'range': 'ContentBlock'}],
                                    'description': 'The message content.',
                                    'name': 'content',
                                    'range': 'ContentBlock',
                                    'required': True},
                        'role': {'name': 'role', 'required': True}}})

    content: ContentBlock = Field(default=..., description="""The message content.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'ContentBlock'},
                    {'multivalued': True, 'range': 'ContentBlock'}],
         'domain_of': ['ToolResultContent',
                       'PromptMessage',
                       'SamplingMessage',
                       'CallToolResult',
                       'CreateMessageResult',
                       'ElicitResult']} })
    role: Role = Field(default=..., description="""The role of the sender or recipient.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PromptMessage', 'SamplingMessage', 'CreateMessageResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class Task(ConfiguredBaseModel):
    """
    Data associated with a task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'createdAt': {'name': 'createdAt', 'required': True},
                        'lastUpdatedAt': {'name': 'lastUpdatedAt', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'taskId': {'name': 'taskId', 'required': True},
                        'ttl': {'name': 'ttl', 'required': True}}})

    taskId: str = Field(default=..., description="""The task identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'RelatedTaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    status: TaskStatusEnum = Field(default=..., description="""Current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    createdAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    lastUpdatedAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    ttl: int = Field(default=..., description="""Actual retention duration from creation in milliseconds, null for unlimited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    statusMessage: Optional[str] = Field(default=None, description="""Optional human-readable message describing the current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    pollInterval: Optional[int] = Field(default=None, description="""Suggested polling interval in milliseconds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })


class TaskMetadata(ConfiguredBaseModel):
    """
    Metadata for augmenting a request with task execution.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    ttl: Optional[int] = Field(default=None, description="""Actual retention duration from creation in milliseconds, null for unlimited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })


class RelatedTaskMetadata(ConfiguredBaseModel):
    """
    Metadata for associating messages with a task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'taskId': {'name': 'taskId', 'required': True}}})

    taskId: str = Field(default=..., description="""The task identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'RelatedTaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })


class ClientCapabilities(ConfiguredBaseModel):
    """
    Capabilities a client may support. Known capabilities are defined here, but this is not a closed set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'elicitation': {'inlined': True,
                                        'name': 'elicitation',
                                        'range': 'ElicitationCapability'},
                        'extensions': {'inlined': True,
                                       'name': 'extensions',
                                       'range': 'ExtensionsCapability'},
                        'roots': {'inlined': True,
                                  'multivalued': False,
                                  'name': 'roots',
                                  'range': 'RootsCapability'},
                        'sampling': {'inlined': True,
                                     'name': 'sampling',
                                     'range': 'SamplingCapability'},
                        'tasks': {'inlined': True,
                                  'multivalued': False,
                                  'name': 'tasks',
                                  'range': 'TasksCapability'}}})

    elicitation: Optional[ElicitationCapability] = Field(default=None, description="""Elicitation capability object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities', 'ClientCapabilities']} })
    experimental: Optional[object] = Field(default=None, description="""Experimental capability extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities']} })
    extensions: Optional[ExtensionsCapability] = Field(default=None, description="""Implementation-specific extension capabilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities']} })
    roots: Optional[RootsCapability] = Field(default=None, description="""The list of roots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ListRootsResult']} })
    sampling: Optional[SamplingCapability] = Field(default=None, description="""Sampling capability object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities', 'ClientCapabilities']} })
    tasks: Optional[TasksCapability] = Field(default=None, description="""The list of tasks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities', 'ListTasksResult']} })


class ServerCapabilities(ConfiguredBaseModel):
    """
    Capabilities that a server may support. Known capabilities are defined here, but this is not a closed set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'extensions': {'inlined': True,
                                       'name': 'extensions',
                                       'range': 'ExtensionsCapability'},
                        'prompts': {'inlined': True,
                                    'multivalued': False,
                                    'name': 'prompts',
                                    'range': 'PromptsCapability'},
                        'resources': {'inlined': True,
                                      'multivalued': False,
                                      'name': 'resources',
                                      'range': 'ResourcesCapability'},
                        'tasks': {'inlined': True,
                                  'multivalued': False,
                                  'name': 'tasks',
                                  'range': 'TasksCapability'},
                        'tools': {'inlined': True,
                                  'multivalued': False,
                                  'name': 'tools',
                                  'range': 'ToolsCapability'}}})

    experimental: Optional[object] = Field(default=None, description="""Experimental capability extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities']} })
    extensions: Optional[ExtensionsCapability] = Field(default=None, description="""Implementation-specific extension capabilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities']} })
    prompts: Optional[PromptsCapability] = Field(default=None, description="""The list of prompts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ServerCapabilities', 'ListPromptsResult']} })
    resources: Optional[ResourcesCapability] = Field(default=None, description="""The list of resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ServerCapabilities', 'ListResourcesResult']} })
    tools: Optional[ToolsCapability] = Field(default=None, description="""The list of tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities',
                       'ServerCapabilities',
                       'CreateMessageRequestParams',
                       'ListToolsResult']} })
    tasks: Optional[TasksCapability] = Field(default=None, description="""The list of tasks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities', 'ListTasksResult']} })


class StringSchema(ConfiguredBaseModel):
    """
    String schema definition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'type': {'equals_string': 'string',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["string"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'string'} })
    default: Optional[object] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    format: Optional[StringFormatEnum] = Field(default=None, description="""String format constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'StringSchema']} })
    minLength: Optional[int] = Field(default=None, description="""Minimum length constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'StringSchema']} })
    maxLength: Optional[int] = Field(default=None, description="""Maximum length constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'StringSchema']} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class NumberSchema(ConfiguredBaseModel):
    """
    Number schema definition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'default': {'name': 'default', 'range': 'integer'},
                        'type': {'name': 'type', 'required': True}}})

    type: str = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default: Optional[int] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    minimum: Optional[int] = Field(default=None, description="""Minimum value constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'NumberSchema']} })
    maximum: Optional[int] = Field(default=None, description="""Maximum value constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'NumberSchema']} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class BooleanSchema(ConfiguredBaseModel):
    """
    Boolean schema definition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'default': {'name': 'default', 'range': 'boolean'},
                        'default_value': {'description': 'Default boolean value.',
                                          'name': 'default_value',
                                          'range': 'boolean'},
                        'type': {'equals_string': 'boolean',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["boolean"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'boolean'} })
    default: Optional[bool] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[bool] = Field(default=None, description="""Default boolean value.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })


class UntitledSingleSelectEnumSchema(ConfiguredBaseModel):
    """
    Single-selection enum without display titles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'type': {'equals_string': 'string',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["string"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'string'} })
    enum: Optional[list[str]] = Field(default=None, description="""Array of enum values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaItems',
                       'JsonSchema',
                       'UntitledSingleSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    enum_values: Optional[list[str]] = Field(default=None, description="""Array of enum values.""", json_schema_extra = { "linkml_meta": {'aliases': ['enum'],
         'domain_of': ['UntitledSingleSelectEnumSchema', 'LegacyTitledEnumSchema']} })
    default: Optional[object] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class TitledSingleSelectEnumSchema(ConfiguredBaseModel):
    """
    Single-selection enum with display titles for each option.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'oneOf': {'multivalued': True,
                                  'name': 'oneOf',
                                  'range': 'EnumOption'},
                        'type': {'equals_string': 'string',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["string"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'string'} })
    oneOf: Optional[list[EnumOption]] = Field(default=None, description="""JSON Schema oneOf entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema', 'TitledSingleSelectEnumSchema']} })
    default: Optional[object] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class UntitledMultiSelectEnumSchema(ConfiguredBaseModel):
    """
    Multi-selection enum without display titles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'default': {'multivalued': True,
                                    'name': 'default',
                                    'range': 'string'},
                        'items': {'name': 'items', 'range': 'SchemaItems'},
                        'type': {'equals_string': 'array',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["array"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'array'} })
    items: Optional[SchemaItems] = Field(default=None, description="""JSON Schema items definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema']} })
    default: Optional[list[str]] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    minItems: Optional[int] = Field(default=None, description="""Minimum number of items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UntitledMultiSelectEnumSchema', 'TitledMultiSelectEnumSchema']} })
    maxItems: Optional[int] = Field(default=None, description="""Maximum number of items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UntitledMultiSelectEnumSchema', 'TitledMultiSelectEnumSchema']} })


class TitledMultiSelectEnumSchema(ConfiguredBaseModel):
    """
    Multi-selection enum with display titles for each option.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'default': {'multivalued': True,
                                    'name': 'default',
                                    'range': 'string'},
                        'items': {'name': 'items', 'range': 'SchemaItems'},
                        'type': {'equals_string': 'array',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["array"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'array'} })
    items: Optional[SchemaItems] = Field(default=None, description="""JSON Schema items definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema']} })
    default: Optional[list[str]] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })
    minItems: Optional[int] = Field(default=None, description="""Minimum number of items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UntitledMultiSelectEnumSchema', 'TitledMultiSelectEnumSchema']} })
    maxItems: Optional[int] = Field(default=None, description="""Maximum number of items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UntitledMultiSelectEnumSchema', 'TitledMultiSelectEnumSchema']} })


class LegacyTitledEnumSchema(ConfiguredBaseModel):
    """
    Legacy titled enum schema. Use TitledSingleSelectEnumSchema instead.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'deprecated': 'Use TitledSingleSelectEnumSchema instead. Will be removed in a '
                       'future version.',
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'type': {'equals_string': 'string',
                                 'name': 'type',
                                 'required': True}}})

    type: Literal["string"] = Field(default=..., description="""Type discriminator field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextContent',
                       'ImageContent',
                       'AudioContent',
                       'ContentBlock',
                       'EmbeddedResource',
                       'ResourceLink',
                       'ToolUseContent',
                       'ToolResultContent',
                       'PromptReference',
                       'ResourceTemplateReference',
                       'SchemaItems',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'equals_string': 'string'} })
    enum: Optional[list[str]] = Field(default=None, description="""Array of enum values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaItems',
                       'JsonSchema',
                       'UntitledSingleSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    enum_values: Optional[list[str]] = Field(default=None, description="""Array of enum values.""", json_schema_extra = { "linkml_meta": {'aliases': ['enum'],
         'domain_of': ['UntitledSingleSelectEnumSchema', 'LegacyTitledEnumSchema']} })
    enumNames: Optional[list[str]] = Field(default=None, description="""Display names for enum values (legacy).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LegacyTitledEnumSchema']} })
    default: Optional[object] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    default_value: Optional[str] = Field(default=None, description="""Default value for a schema field.""", json_schema_extra = { "linkml_meta": {'aliases': ['default'],
         'domain_of': ['StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolAnnotations',
                       'EnumOption',
                       'JsonSchema',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema'],
         'slot_uri': 'dct:title'} })


class JSONRPCRequest(ConfiguredBaseModel):
    """
    A request that expects a response.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'aliases': ['Request', 'PaginatedRequest'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'id': {'name': 'id', 'required': True},
                        'jsonrpc': {'name': 'jsonrpc', 'required': True},
                        'method': {'name': 'method', 'required': True}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: str = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification']} })


class JSONRPCNotification(ConfiguredBaseModel):
    """
    A notification which does not expect a response.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'aliases': ['Notification'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'jsonrpc': {'name': 'jsonrpc', 'required': True},
                        'method': {'name': 'method', 'required': True}}})

    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: str = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification']} })


class JSONRPCResultResponse(ConfiguredBaseModel):
    """
    A successful (non-error) response to a request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'id': {'name': 'id', 'required': True},
                        'jsonrpc': {'name': 'jsonrpc', 'required': True}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class JSONRPCErrorResponse(ConfiguredBaseModel):
    """
    A response to a request that indicates an error occurred.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'error': {'name': 'error', 'required': True},
                        'id': {'any_of': [{'range': 'RequestId'}, {'range': 'integer'}],
                               'name': 'id'},
                        'jsonrpc': {'name': 'jsonrpc', 'required': True}}})

    id: Optional[Union[int, str]] = Field(default=None, description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RequestId'}, {'range': 'integer'}],
         'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    error: Error = Field(default=..., description="""The error object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LogData', 'JSONRPCErrorResponse']} })


class URLElicitationRequiredError(JSONRPCErrorResponse):
    """
    A response indicating that additional information is required via URL elicitation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    id: Optional[Union[int, str]] = Field(default=None, description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RequestId'}, {'range': 'integer'}],
         'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    error: Error = Field(default=..., description="""The error object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LogData', 'JSONRPCErrorResponse']} })


class Result(HasMeta):
    """
    Common result fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['EmptyResult', 'PaginatedResult'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta']})

    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CancelledNotificationParams(HasMeta):
    """
    Parameters for a notifications/cancelled notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp', 'mixins': ['HasMeta']})

    requestId: Optional[str] = Field(default=None, description="""The ID of a request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotificationParams']} })
    reason: Optional[str] = Field(default=None, description="""An optional string describing the reason.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ErrorData', 'CancelledNotificationParams']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ProgressNotificationParams(HasMeta):
    """
    Parameters for a notifications/progress notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'progress': {'name': 'progress', 'required': True},
                        'progressToken': {'name': 'progressToken', 'required': True}}})

    progress: float = Field(default=..., description="""The progress thus far.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressNotificationParams']} })
    progressToken: str = Field(default=..., description="""The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaObject', 'ProgressNotificationParams']} })
    total: Optional[float] = Field(default=None, description="""Total number of items to process (or total progress required), if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompletionData', 'ProgressNotificationParams']} })
    message: Optional[str] = Field(default=None, description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ElicitationCompleteNotificationParams(ConfiguredBaseModel):
    """
    Parameters for a notifications/elicitation/complete notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'elicitationId': {'name': 'elicitationId', 'required': True}}})

    elicitationId: str = Field(default=..., description="""The ID of the elicitation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['URLElicitation',
                       'ElicitationCompleteNotificationParams',
                       'ElicitRequestURLParams']} })


class LoggingMessageNotificationParams(HasMeta):
    """
    Parameters for a notifications/message notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'data': {'description': 'The data to be logged.',
                                 'inlined': True,
                                 'name': 'data',
                                 'range': 'LogData',
                                 'required': True},
                        'level': {'name': 'level', 'required': True}}})

    data: LogData = Field(default=..., description="""The data to be logged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'ImageContent',
                       'AudioContent',
                       'LoggingMessageNotificationParams']} })
    level: LoggingLevel = Field(default=..., description="""The severity of a log message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LoggingMessageNotificationParams', 'SetLevelRequestParams']} })
    logger: Optional[str] = Field(default=None, description="""An optional name of the logger issuing this message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LoggingMessageNotificationParams']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ResourceUpdatedNotificationParams(HasMeta):
    """
    Parameters for a notifications/resources/updated notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class TaskStatusNotificationParams(HasMeta):
    """
    Parameters for a notifications/tasks/status notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'createdAt': {'name': 'createdAt', 'required': True},
                        'lastUpdatedAt': {'name': 'lastUpdatedAt', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'taskId': {'name': 'taskId', 'required': True},
                        'ttl': {'name': 'ttl', 'required': True}}})

    taskId: str = Field(default=..., description="""The task identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'RelatedTaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    status: TaskStatusEnum = Field(default=..., description="""Current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    createdAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    lastUpdatedAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    ttl: int = Field(default=..., description="""Actual retention duration from creation in milliseconds, null for unlimited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    statusMessage: Optional[str] = Field(default=None, description="""Optional human-readable message describing the current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    pollInterval: Optional[int] = Field(default=None, description="""Suggested polling interval in milliseconds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CancelledNotification(JSONRPCNotification):
    """
    Notification to indicate that a previously-issued request is being cancelled.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/cancelled',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'CancelledNotificationParams',
                                   'required': True}}})

    params: CancelledNotificationParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/cancelled"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/cancelled'} })


class InitializedNotification(JSONRPCNotification):
    """
    Notification sent from the client to the server after initialization has finished.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/initialized',
                                   'name': 'method'}}})

    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/initialized"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/initialized'} })


class ProgressNotification(JSONRPCNotification):
    """
    Out-of-band notification to inform the receiver of a progress update.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/progress',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'ProgressNotificationParams',
                                   'required': True}}})

    params: ProgressNotificationParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/progress"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/progress'} })


class ResourceListChangedNotification(JSONRPCNotification):
    """
    Notification that the list of resources the server can read from has changed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/resources/list_changed',
                                   'name': 'method'}}})

    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/resources/list_changed"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/resources/list_changed'} })


class ResourceUpdatedNotification(JSONRPCNotification):
    """
    Notification that a resource has changed and may need to be read again.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/resources/updated',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'ResourceUpdatedNotificationParams',
                                   'required': True}}})

    params: ResourceUpdatedNotificationParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/resources/updated"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/resources/updated'} })


class PromptListChangedNotification(JSONRPCNotification):
    """
    Notification that the list of prompts the server offers has changed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/prompts/list_changed',
                                   'name': 'method'}}})

    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/prompts/list_changed"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/prompts/list_changed'} })


class ToolListChangedNotification(JSONRPCNotification):
    """
    Notification that the list of tools the server offers has changed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/tools/list_changed',
                                   'name': 'method'}}})

    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/tools/list_changed"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/tools/list_changed'} })


class RootsListChangedNotification(JSONRPCNotification):
    """
    Notification from the client that the list of roots has changed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/roots/list_changed',
                                   'name': 'method'}}})

    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/roots/list_changed"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/roots/list_changed'} })


class LoggingMessageNotification(JSONRPCNotification):
    """
    Notification of a log message passed from server to client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/message',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'LoggingMessageNotificationParams',
                                   'required': True}}})

    params: LoggingMessageNotificationParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/message"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/message'} })


class ElicitationCompleteNotification(JSONRPCNotification):
    """
    Notification from the server that an out-of-band elicitation request completed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/elicitation/complete',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'ElicitationCompleteNotificationParams',
                                   'required': True}}})

    params: ElicitationCompleteNotificationParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/elicitation/complete"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/elicitation/complete'} })


class TaskStatusNotification(JSONRPCNotification):
    """
    Notification that a task's status has changed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'notifications/tasks/status',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'TaskStatusNotificationParams',
                                   'required': True}}})

    params: TaskStatusNotificationParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["notifications/tasks/status"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'notifications/tasks/status'} })


class CallToolRequestParams(HasMeta):
    """
    Parameters for a tools/call request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['TaskAugmentedRequestParams'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'arguments': {'description': 'Arguments to use for the tool '
                                                     'call.',
                                      'inlined': True,
                                      'name': 'arguments',
                                      'range': 'ArgumentMap'},
                        'name': {'name': 'name', 'required': True},
                        'task': {'description': 'If specified, the caller is '
                                                'requesting task-augmented execution.',
                                 'inlined': True,
                                 'name': 'task',
                                 'range': 'TaskMetadata'}}})

    arguments: Optional[ArgumentMap] = Field(default=None, description="""Arguments to use for the tool call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prompt',
                       'CompletionContext',
                       'CallToolRequestParams',
                       'GetPromptRequestParams']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })
    task: Optional[TaskMetadata] = Field(default=None, description="""If specified, the caller is requesting task-augmented execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CallToolRequestParams',
                       'CreateMessageRequestParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams',
                       'CreateTaskResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class GetPromptRequestParams(ConfiguredBaseModel):
    """
    Parameters for a prompts/get request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'arguments': {'description': 'Arguments to use for templating '
                                                     'the prompt.',
                                      'inlined': True,
                                      'name': 'arguments',
                                      'range': 'ArgumentMap'},
                        'name': {'name': 'name', 'required': True}}})

    arguments: Optional[ArgumentMap] = Field(default=None, description="""Arguments to use for templating the prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prompt',
                       'CompletionContext',
                       'CallToolRequestParams',
                       'GetPromptRequestParams']} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasName',
                       'ToolUseContent',
                       'Root',
                       'CompletionArgument',
                       'SchemaProperties',
                       'ElicitationContent',
                       'ModelHint',
                       'CallToolRequestParams',
                       'GetPromptRequestParams'],
         'slot_uri': 'schema:name'} })


class CompleteRequestParams(ConfiguredBaseModel):
    """
    Parameters for a completion/complete request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'argument': {'inlined': True,
                                     'name': 'argument',
                                     'range': 'CompletionArgument',
                                     'required': True},
                        'context': {'inlined': True,
                                    'name': 'context',
                                    'range': 'CompletionContext'},
                        'ref': {'inlined': True,
                                'name': 'ref',
                                'range': 'PromptReference',
                                'required': True}}})

    argument: CompletionArgument = Field(default=..., description="""The argument's information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompleteRequestParams']} })
    context: Optional[CompletionContext] = Field(default=None, description="""Optional completion context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompleteRequestParams']} })
    ref: PromptReference = Field(default=..., description="""A prompt or resource template reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompleteRequestParams']} })


class ReadResourceRequestParams(ConfiguredBaseModel):
    """
    Parameters for a resources/read request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['ResourceRequestParams'],
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })


class SubscribeRequestParams(ConfiguredBaseModel):
    """
    Parameters for a resources/subscribe request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })


class UnsubscribeRequestParams(ConfiguredBaseModel):
    """
    Parameters for a resources/unsubscribe request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'uri': {'name': 'uri', 'required': True}}})

    uri: str = Field(default=..., description="""A resource URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink',
                       'ResourceContents',
                       'TextResourceContents',
                       'BlobResourceContents',
                       'Resource',
                       'Root',
                       'ResourceTemplateReference',
                       'ResourceUpdatedNotificationParams',
                       'ReadResourceRequestParams',
                       'SubscribeRequestParams',
                       'UnsubscribeRequestParams']} })


class SetLevelRequestParams(ConfiguredBaseModel):
    """
    Parameters for a logging/setLevel request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'level': {'name': 'level', 'required': True}}})

    level: LoggingLevel = Field(default=..., description="""The severity of a log message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LoggingMessageNotificationParams', 'SetLevelRequestParams']} })


class InitializeRequestParams(ConfiguredBaseModel):
    """
    Parameters for an initialize request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'capabilities': {'description': 'Client capabilities.',
                                         'inlined': True,
                                         'name': 'capabilities',
                                         'range': 'ClientCapabilities',
                                         'required': True},
                        'clientInfo': {'description': 'Information about the client '
                                                      'implementation.',
                                       'inlined': True,
                                       'name': 'clientInfo',
                                       'range': 'Implementation',
                                       'required': True},
                        'protocolVersion': {'name': 'protocolVersion',
                                            'required': True}}})

    capabilities: ClientCapabilities = Field(default=..., description="""Client capabilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeRequestParams', 'InitializeResult']} })
    clientInfo: Implementation = Field(default=..., description="""Information about the client implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeRequestParams']} })
    protocolVersion: str = Field(default=..., description="""The version of the Model Context Protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeRequestParams', 'InitializeResult']} })


class CreateMessageRequestParams(ConfiguredBaseModel):
    """
    Parameters for a sampling/createMessage request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'maxTokens': {'name': 'maxTokens', 'required': True},
                        'messages': {'description': 'Messages for sampling.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'messages',
                                     'range': 'SamplingMessage',
                                     'required': True},
                        'modelPreferences': {'description': 'Model preferences for '
                                                            'sampling.',
                                             'inlined': True,
                                             'name': 'modelPreferences',
                                             'range': 'ModelPreferences'},
                        'task': {'description': 'If specified, task-augmented '
                                                'execution.',
                                 'inlined': True,
                                 'name': 'task',
                                 'range': 'TaskMetadata'},
                        'toolChoice': {'description': 'Controls how the model uses '
                                                      'tools.',
                                       'inlined': True,
                                       'name': 'toolChoice',
                                       'range': 'ToolChoice'},
                        'tools': {'description': 'Tools that the model may use during '
                                                 'generation.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'tools',
                                  'range': 'Tool'}}})

    maxTokens: int = Field(default=..., description="""The requested maximum number of tokens to sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams']} })
    messages: list[SamplingMessage] = Field(default=..., description="""Messages for sampling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams', 'GetPromptResult']} })
    modelPreferences: Optional[ModelPreferences] = Field(default=None, description="""Model preferences for sampling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams']} })
    systemPrompt: Optional[str] = Field(default=None, description="""An optional system prompt the server wants to use for sampling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams']} })
    temperature: Optional[float] = Field(default=None, description="""Sampling temperature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SchemaProperties',
                       'StructuredContentData',
                       'CreateMessageRequestParams']} })
    includeContext: Optional[IncludeContextEnum] = Field(default=None, description="""A request to include context from one or more MCP servers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams']} })
    stopSequences: Optional[list[str]] = Field(default=None, description="""Stop sequences for sampling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams']} })
    tools: Optional[list[Tool]] = Field(default=None, description="""Tools that the model may use during generation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities',
                       'ServerCapabilities',
                       'CreateMessageRequestParams',
                       'ListToolsResult']} })
    toolChoice: Optional[ToolChoice] = Field(default=None, description="""Controls how the model uses tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams']} })
    task: Optional[TaskMetadata] = Field(default=None, description="""If specified, task-augmented execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CallToolRequestParams',
                       'CreateMessageRequestParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams',
                       'CreateTaskResult']} })


class ElicitRequestFormParams(ConfiguredBaseModel):
    """
    Parameters for a form-mode elicitation request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'message': {'name': 'message', 'required': True},
                        'requestedSchema': {'inlined': True,
                                            'name': 'requestedSchema',
                                            'range': 'JsonSchema',
                                            'required': True},
                        'task': {'description': 'If specified, task-augmented '
                                                'execution.',
                                 'inlined': True,
                                 'name': 'task',
                                 'range': 'TaskMetadata'}}})

    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })
    requestedSchema: JsonSchema = Field(default=..., description="""A restricted subset of JSON Schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElicitRequestFormParams']} })
    mode: Optional[str] = Field(default=None, description="""The elicitation mode.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolChoice',
                       'URLElicitation',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })
    task: Optional[TaskMetadata] = Field(default=None, description="""If specified, task-augmented execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CallToolRequestParams',
                       'CreateMessageRequestParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams',
                       'CreateTaskResult']} })


class ElicitRequestURLParams(ConfiguredBaseModel):
    """
    Parameters for a URL-mode elicitation request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'elicitationId': {'name': 'elicitationId', 'required': True},
                        'message': {'name': 'message', 'required': True},
                        'mode': {'equals_string': 'url',
                                 'name': 'mode',
                                 'required': True},
                        'task': {'description': 'If specified, task-augmented '
                                                'execution.',
                                 'inlined': True,
                                 'name': 'task',
                                 'range': 'TaskMetadata'},
                        'url': {'name': 'url', 'required': True}}})

    elicitationId: str = Field(default=..., description="""The ID of the elicitation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['URLElicitation',
                       'ElicitationCompleteNotificationParams',
                       'ElicitRequestURLParams']} })
    message: str = Field(default=..., description="""A message string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Error',
                       'URLElicitation',
                       'ProgressNotificationParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams']} })
    mode: Literal["url"] = Field(default=..., description="""The elicitation mode.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolChoice',
                       'URLElicitation',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams'],
         'equals_string': 'url'} })
    url: str = Field(default=..., description="""The URL that the user should navigate to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['URLElicitation', 'ElicitRequestURLParams']} })
    task: Optional[TaskMetadata] = Field(default=None, description="""If specified, task-augmented execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CallToolRequestParams',
                       'CreateMessageRequestParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams',
                       'CreateTaskResult']} })


class PaginatedRequestParams(ConfiguredBaseModel):
    """
    Common params for paginated requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    cursor: Optional[str] = Field(default=None, description="""An opaque token representing the current pagination position. If provided, the server should return results starting after this cursor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PaginatedRequestParams']} })


class InitializeRequest(JSONRPCRequest):
    """
    Request sent from the client to the server when it first connects, asking it to begin initialization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'initialize', 'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'InitializeRequestParams',
                                   'required': True}}})

    params: InitializeRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["initialize"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'initialize'} })


class PingRequest(JSONRPCRequest):
    """
    A ping, issued by either the server or the client, to check that the other party is still alive.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'ping', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["ping"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'ping'} })


class ListResourcesRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of resources the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'resources/list',
                                   'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["resources/list"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'resources/list'} })


class ListResourceTemplatesRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of resource templates the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'resources/templates/list',
                                   'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["resources/templates/list"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'resources/templates/list'} })


class ReadResourceRequest(JSONRPCRequest):
    """
    Sent from the client to the server, to read a specific resource URI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'resources/read', 'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'ReadResourceRequestParams',
                                   'required': True}}})

    params: ReadResourceRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["resources/read"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'resources/read'} })


class SubscribeRequest(JSONRPCRequest):
    """
    Sent from the client to request resource update notifications.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'resources/subscribe',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'SubscribeRequestParams',
                                   'required': True}}})

    params: SubscribeRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["resources/subscribe"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'resources/subscribe'} })


class UnsubscribeRequest(JSONRPCRequest):
    """
    Sent from the client to cancel resource update notifications.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'resources/unsubscribe',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'UnsubscribeRequestParams',
                                   'required': True}}})

    params: UnsubscribeRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["resources/unsubscribe"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'resources/unsubscribe'} })


class ListPromptsRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of prompts and prompt templates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'prompts/list', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["prompts/list"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'prompts/list'} })


class GetPromptRequest(JSONRPCRequest):
    """
    Used by the client to get a prompt provided by the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'prompts/get', 'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'GetPromptRequestParams',
                                   'required': True}}})

    params: GetPromptRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["prompts/get"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'prompts/get'} })


class ListToolsRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of tools the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'tools/list', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["tools/list"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'tools/list'} })


class CallToolRequest(JSONRPCRequest):
    """
    Used by the client to invoke a tool provided by the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'tools/call', 'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'CallToolRequestParams',
                                   'required': True}}})

    params: CallToolRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["tools/call"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'tools/call'} })


class CompleteRequest(JSONRPCRequest):
    """
    A request from the client to the server, to ask for completion options.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'completion/complete',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'CompleteRequestParams',
                                   'required': True}}})

    params: CompleteRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["completion/complete"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'completion/complete'} })


class SetLevelRequest(JSONRPCRequest):
    """
    A request from the client to the server, to enable or adjust logging.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'logging/setLevel',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'SetLevelRequestParams',
                                   'required': True}}})

    params: SetLevelRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["logging/setLevel"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'logging/setLevel'} })


class CreateMessageRequest(JSONRPCRequest):
    """
    A request from the server to sample an LLM via the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'sampling/createMessage',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'CreateMessageRequestParams',
                                   'required': True}}})

    params: CreateMessageRequestParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["sampling/createMessage"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'sampling/createMessage'} })


class ListRootsRequest(JSONRPCRequest):
    """
    Sent from the server to request a list of root URIs from the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'roots/list', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["roots/list"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'roots/list'} })


class ElicitRequest(JSONRPCRequest):
    """
    A request from the server to elicit additional information from the user via the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'elicitation/create',
                                   'name': 'method'},
                        'params': {'inlined': True,
                                   'name': 'params',
                                   'range': 'ElicitRequestFormParams',
                                   'required': True}}})

    params: ElicitRequestFormParams = Field(default=..., description="""JSON-RPC parameters payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CancelledNotification',
                       'ProgressNotification',
                       'ResourceUpdatedNotification',
                       'LoggingMessageNotification',
                       'ElicitationCompleteNotification',
                       'TaskStatusNotification',
                       'InitializeRequest',
                       'ReadResourceRequest',
                       'SubscribeRequest',
                       'UnsubscribeRequest',
                       'GetPromptRequest',
                       'CallToolRequest',
                       'CompleteRequest',
                       'SetLevelRequest',
                       'CreateMessageRequest',
                       'ElicitRequest']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["elicitation/create"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'elicitation/create'} })


class ListTasksRequest(JSONRPCRequest):
    """
    A request to retrieve a list of tasks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'tasks/list', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["tasks/list"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'tasks/list'} })


class GetTaskRequest(JSONRPCRequest):
    """
    A request to retrieve the state of a task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'tasks/get', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["tasks/get"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'tasks/get'} })


class GetTaskPayloadRequest(JSONRPCRequest):
    """
    A request to retrieve the result of a completed task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'tasks/result', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["tasks/result"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'tasks/result'} })


class CancelTaskRequest(JSONRPCRequest):
    """
    A request to cancel a task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'method': {'equals_string': 'tasks/cancel', 'name': 'method'}}})

    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    method: Literal["tasks/cancel"] = Field(default=..., description="""The JSON-RPC method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest', 'JSONRPCNotification'],
         'equals_string': 'tasks/cancel'} })


class InitializeResult(Result):
    """
    The result returned by the server for an initialize request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'capabilities': {'description': 'Server capabilities.',
                                         'inlined': True,
                                         'name': 'capabilities',
                                         'range': 'ServerCapabilities',
                                         'required': True},
                        'protocolVersion': {'name': 'protocolVersion',
                                            'required': True},
                        'serverInfo': {'description': 'Information about the server '
                                                      'implementation.',
                                       'inlined': True,
                                       'name': 'serverInfo',
                                       'range': 'Implementation',
                                       'required': True}}})

    capabilities: ServerCapabilities = Field(default=..., description="""Server capabilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeRequestParams', 'InitializeResult']} })
    protocolVersion: str = Field(default=..., description="""The version of the Model Context Protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeRequestParams', 'InitializeResult']} })
    serverInfo: Implementation = Field(default=..., description="""Information about the server implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResult']} })
    instructions: Optional[str] = Field(default=None, description="""Instructions describing how to use the server and its features.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CallToolResult(Result):
    """
    The result returned by the server for a tools/call request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'content': {'description': 'A list of content objects that '
                                                   'represent the result.',
                                    'multivalued': True,
                                    'name': 'content',
                                    'range': 'ContentBlock',
                                    'required': True},
                        'structuredContent': {'inlined': True,
                                              'name': 'structuredContent',
                                              'range': 'StructuredContentData'}}})

    content: list[ContentBlock] = Field(default=..., description="""A list of content objects that represent the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent',
                       'PromptMessage',
                       'SamplingMessage',
                       'CallToolResult',
                       'CreateMessageResult',
                       'ElicitResult']} })
    isError: Optional[bool] = Field(default=None, description="""Whether the tool call ended in an error.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent', 'CallToolResult']} })
    structuredContent: Optional[StructuredContentData] = Field(default=None, description="""An optional JSON object representing structured result of the tool call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent', 'CallToolResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CompleteResult(Result):
    """
    The result returned by the server for a completion/complete request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'completion': {'inlined': True,
                                       'name': 'completion',
                                       'range': 'CompletionData',
                                       'required': True}}})

    completion: CompletionData = Field(default=..., description="""The completion result object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompleteResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class GetPromptResult(Result):
    """
    The result returned by the server for a prompts/get request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'messages': {'description': 'The prompt messages.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'messages',
                                     'range': 'PromptMessage',
                                     'required': True}}})

    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Implementation',
                       'ResourceLink',
                       'Resource',
                       'ResourceTemplate',
                       'PromptArgument',
                       'Prompt',
                       'JsonSchema',
                       'Tool',
                       'StringSchema',
                       'NumberSchema',
                       'BooleanSchema',
                       'UntitledSingleSelectEnumSchema',
                       'TitledSingleSelectEnumSchema',
                       'UntitledMultiSelectEnumSchema',
                       'TitledMultiSelectEnumSchema',
                       'LegacyTitledEnumSchema',
                       'GetPromptResult'],
         'slot_uri': 'dct:description'} })
    messages: list[PromptMessage] = Field(default=..., description="""The prompt messages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageRequestParams', 'GetPromptResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ListPromptsResult(Result):
    """
    The result returned by the server for a prompts/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'prompts': {'name': 'prompts', 'required': True}}})

    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result. If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListPromptsResult',
                       'ListResourcesResult',
                       'ListResourceTemplatesResult',
                       'ListToolsResult',
                       'ListTasksResult']} })
    prompts: list[Prompt] = Field(default=..., description="""The list of prompts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ServerCapabilities', 'ListPromptsResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ListResourcesResult(Result):
    """
    The result returned by the server for a resources/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'resources': {'name': 'resources', 'required': True}}})

    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result. If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListPromptsResult',
                       'ListResourcesResult',
                       'ListResourceTemplatesResult',
                       'ListToolsResult',
                       'ListTasksResult']} })
    resources: list[Resource] = Field(default=..., description="""The list of resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ServerCapabilities', 'ListResourcesResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ListResourceTemplatesResult(Result):
    """
    The result returned by the server for a resources/templates/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'resourceTemplates': {'name': 'resourceTemplates',
                                              'required': True}}})

    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result. If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListPromptsResult',
                       'ListResourcesResult',
                       'ListResourceTemplatesResult',
                       'ListToolsResult',
                       'ListTasksResult']} })
    resourceTemplates: list[ResourceTemplate] = Field(default=..., description="""The list of resource templates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListResourceTemplatesResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ReadResourceResult(Result):
    """
    The result returned by the server for a resources/read request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'contents': {'name': 'contents', 'required': True}}})

    contents: list[ResourceContents] = Field(default=..., description="""The resource contents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReadResourceResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ListToolsResult(Result):
    """
    The result returned by the server for a tools/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'tools': {'name': 'tools', 'required': True}}})

    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result. If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListPromptsResult',
                       'ListResourcesResult',
                       'ListResourceTemplatesResult',
                       'ListToolsResult',
                       'ListTasksResult']} })
    tools: list[Tool] = Field(default=..., description="""The list of tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaskRequestCapabilities',
                       'ServerCapabilities',
                       'CreateMessageRequestParams',
                       'ListToolsResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ListRootsResult(Result):
    """
    The result returned by the client for a roots/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'roots': {'name': 'roots', 'required': True}}})

    roots: list[Root] = Field(default=..., description="""The list of roots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ListRootsResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CreateMessageResult(Result):
    """
    The result returned by the client for a sampling/createMessage request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'content': {'any_of': [{'range': 'ContentBlock'},
                                               {'multivalued': True,
                                                'range': 'ContentBlock'}],
                                    'description': 'The message content.',
                                    'name': 'content',
                                    'range': 'ContentBlock',
                                    'required': True},
                        'model': {'name': 'model', 'required': True},
                        'role': {'name': 'role', 'required': True}}})

    content: ContentBlock = Field(default=..., description="""The message content.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'ContentBlock'},
                    {'multivalued': True, 'range': 'ContentBlock'}],
         'domain_of': ['ToolResultContent',
                       'PromptMessage',
                       'SamplingMessage',
                       'CallToolResult',
                       'CreateMessageResult',
                       'ElicitResult']} })
    model: str = Field(default=..., description="""The name of the model that generated the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageResult']} })
    role: Role = Field(default=..., description="""The role of the sender or recipient.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PromptMessage', 'SamplingMessage', 'CreateMessageResult']} })
    stopReason: Optional[str] = Field(default=None, description="""The reason why sampling stopped, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreateMessageResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ElicitResult(Result):
    """
    The result returned by the client for an elicitation/create request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'action': {'name': 'action', 'required': True},
                        'content': {'inlined': True,
                                    'name': 'content',
                                    'range': 'ElicitationContent'}}})

    action: ElicitActionEnum = Field(default=..., description="""The user action in response to the elicitation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElicitResult']} })
    content: Optional[ElicitationContent] = Field(default=None, description="""Structured content block of a message or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolResultContent',
                       'PromptMessage',
                       'SamplingMessage',
                       'CallToolResult',
                       'CreateMessageResult',
                       'ElicitResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CreateTaskResult(Result):
    """
    The result returned for a task-augmented request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'task': {'name': 'task', 'required': True}}})

    task: Task = Field(default=..., description="""Task data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CallToolRequestParams',
                       'CreateMessageRequestParams',
                       'ElicitRequestFormParams',
                       'ElicitRequestURLParams',
                       'CreateTaskResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class GetTaskPayloadResult(Result):
    """
    The result returned for a tasks/result request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class ListTasksResult(Result):
    """
    The result returned for a tasks/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'tasks': {'name': 'tasks', 'required': True}}})

    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result. If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListPromptsResult',
                       'ListResourcesResult',
                       'ListResourceTemplatesResult',
                       'ListToolsResult',
                       'ListTasksResult']} })
    tasks: list[Task] = Field(default=..., description="""The list of tasks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClientCapabilities', 'ServerCapabilities', 'ListTasksResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class CancelTaskResult(Result, HasMeta):
    """
    The result returned for a tasks/cancel request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'createdAt': {'name': 'createdAt', 'required': True},
                        'lastUpdatedAt': {'name': 'lastUpdatedAt', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'taskId': {'name': 'taskId', 'required': True},
                        'ttl': {'name': 'ttl', 'required': True}}})

    taskId: str = Field(default=..., description="""The task identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'RelatedTaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    status: TaskStatusEnum = Field(default=..., description="""Current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    createdAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    lastUpdatedAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    ttl: int = Field(default=..., description="""Actual retention duration from creation in milliseconds, null for unlimited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    statusMessage: Optional[str] = Field(default=None, description="""Optional human-readable message describing the current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    pollInterval: Optional[int] = Field(default=None, description="""Suggested polling interval in milliseconds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class GetTaskResult(Result, HasMeta):
    """
    The result returned for a tasks/get request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'mixins': ['HasMeta'],
         'slot_usage': {'createdAt': {'name': 'createdAt', 'required': True},
                        'lastUpdatedAt': {'name': 'lastUpdatedAt', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'taskId': {'name': 'taskId', 'required': True},
                        'ttl': {'name': 'ttl', 'required': True}}})

    taskId: str = Field(default=..., description="""The task identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'RelatedTaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    status: TaskStatusEnum = Field(default=..., description="""Current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    createdAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    lastUpdatedAt: str = Field(default=..., description="""ISO 8601 timestamp when the task was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    ttl: int = Field(default=..., description="""Actual retention duration from creation in milliseconds, null for unlimited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskMetadata',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    statusMessage: Optional[str] = Field(default=None, description="""Optional human-readable message describing the current task state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    pollInterval: Optional[int] = Field(default=None, description="""Suggested polling interval in milliseconds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'TaskStatusNotificationParams',
                       'CancelTaskResult',
                       'GetTaskResult']} })
    meta: Optional[MetaObject] = Field(default=None, alias="_meta", description="""Optional metadata object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMeta']} })


class InitializeResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for an initialize request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'InitializeResult',
                                   'required': True}}})

    result: InitializeResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class CallToolResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a tools/call request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'CallToolResult',
                                   'required': True}}})

    result: CallToolResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class CompleteResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a completion/complete request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'CompleteResult',
                                   'required': True}}})

    result: CompleteResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class GetPromptResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a prompts/get request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'GetPromptResult',
                                   'required': True}}})

    result: GetPromptResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ListPromptsResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a prompts/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ListPromptsResult',
                                   'required': True}}})

    result: ListPromptsResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ListResourcesResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a resources/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ListResourcesResult',
                                   'required': True}}})

    result: ListResourcesResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ListResourceTemplatesResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a resources/templates/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ListResourceTemplatesResult',
                                   'required': True}}})

    result: ListResourceTemplatesResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ReadResourceResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a resources/read request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ReadResourceResult',
                                   'required': True}}})

    result: ReadResourceResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ListToolsResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a tools/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ListToolsResult',
                                   'required': True}}})

    result: ListToolsResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ListRootsResultResponse(JSONRPCResultResponse):
    """
    A successful response from the client for a roots/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ListRootsResult',
                                   'required': True}}})

    result: ListRootsResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class CreateMessageResultResponse(JSONRPCResultResponse):
    """
    A successful response from the client for a sampling/createMessage request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'CreateMessageResult',
                                   'required': True}}})

    result: CreateMessageResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ElicitResultResponse(JSONRPCResultResponse):
    """
    A successful response from the client for an elicitation/create request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ElicitResult',
                                   'required': True}}})

    result: ElicitResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class SetLevelResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a logging/setLevel request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    result: Optional[Result] = Field(default=None, description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class PingResultResponse(JSONRPCResultResponse):
    """
    A successful response for a ping request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    result: Optional[Result] = Field(default=None, description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class SubscribeResultResponse(JSONRPCResultResponse):
    """
    A successful response for a resources/subscribe request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    result: Optional[Result] = Field(default=None, description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class UnsubscribeResultResponse(JSONRPCResultResponse):
    """
    A successful response for a resources/unsubscribe request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp'})

    result: Optional[Result] = Field(default=None, description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class CreateTaskResultResponse(JSONRPCResultResponse):
    """
    A successful response for a task-augmented request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'CreateTaskResult',
                                   'required': True}}})

    result: CreateTaskResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class GetTaskResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/get request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'GetTaskResult',
                                   'required': True}}})

    result: GetTaskResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class GetTaskPayloadResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/result request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'GetTaskPayloadResult',
                                   'required': True}}})

    result: GetTaskPayloadResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class CancelTaskResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/cancel request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'CancelTaskResult',
                                   'required': True}}})

    result: CancelTaskResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


class ListTasksResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/list request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'result': {'inlined': True,
                                   'name': 'result',
                                   'range': 'ListTasksResult',
                                   'required': True}}})

    result: ListTasksResult = Field(default=..., description="""JSON-RPC successful result payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InitializeResultResponse',
                       'CallToolResultResponse',
                       'CompleteResultResponse',
                       'GetPromptResultResponse',
                       'ListPromptsResultResponse',
                       'ListResourcesResultResponse',
                       'ListResourceTemplatesResultResponse',
                       'ReadResourceResultResponse',
                       'ListToolsResultResponse',
                       'ListRootsResultResponse',
                       'CreateMessageResultResponse',
                       'ElicitResultResponse',
                       'SetLevelResultResponse',
                       'PingResultResponse',
                       'SubscribeResultResponse',
                       'UnsubscribeResultResponse',
                       'CreateTaskResultResponse',
                       'GetTaskResultResponse',
                       'GetTaskPayloadResultResponse',
                       'CancelTaskResultResponse',
                       'ListTasksResultResponse']} })
    id: str = Field(default=..., description="""Uniquely identifying ID for a JSON-RPC request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolUseContent',
                       'JSONRPCRequest',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })
    jsonrpc: str = Field(default=..., description="""JSON-RPC version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JSONRPCRequest',
                       'JSONRPCNotification',
                       'JSONRPCResultResponse',
                       'JSONRPCErrorResponse']} })


# A union of all notifications that can be sent by a client.
ClientNotification = Union["CancelledNotification", "InitializedNotification", "ProgressNotification", "RootsListChangedNotification", "TaskStatusNotification"]


# A union of all requests that can be sent by a client.
ClientRequest = Union["CallToolRequest", "CancelTaskRequest", "CompleteRequest", "GetPromptRequest", "GetTaskPayloadRequest", "GetTaskRequest", "InitializeRequest", "ListPromptsRequest", "ListResourceTemplatesRequest", "ListResourcesRequest", "ListTasksRequest", "ListToolsRequest", "PingRequest", "ReadResourceRequest", "SetLevelRequest", "SubscribeRequest", "UnsubscribeRequest"]


# A union of all result types that a client can return.
ClientResult = Union["CancelTaskResult", "CreateMessageResult", "ElicitResult", "GetTaskPayloadResult", "GetTaskResult", "ListRootsResult", "ListTasksResult", "Result"]


# A union of all notifications that can be sent by a server.
ServerNotification = Union["CancelledNotification", "ElicitationCompleteNotification", "LoggingMessageNotification", "ProgressNotification", "PromptListChangedNotification", "ResourceListChangedNotification", "ResourceUpdatedNotification", "TaskStatusNotification", "ToolListChangedNotification"]


# A union of all requests that can be sent by a server.
ServerRequest = Union["CancelTaskRequest", "CreateMessageRequest", "ElicitRequest", "GetTaskPayloadRequest", "GetTaskRequest", "ListRootsRequest", "ListTasksRequest", "PingRequest"]


# A union of all result types that a server can return.
ServerResult = Union["CallToolResult", "CancelTaskResult", "CompleteResult", "CreateTaskResult", "GetPromptResult", "GetTaskPayloadResult", "GetTaskResult", "InitializeResult", "ListPromptsResult", "ListResourceTemplatesResult", "ListResourcesResult", "ListTasksResult", "ListToolsResult", "ReadResourceResult", "Result"]


# A union of all JSON-RPC message types (requests, notifications, and responses).
JSONRPCMessage = Union["JSONRPCErrorResponse", "JSONRPCNotification", "JSONRPCRequest", "JSONRPCResultResponse"]


# A union of all JSON-RPC response types.
JSONRPCResponse = Union["JSONRPCErrorResponse", "JSONRPCResultResponse"]


# A union of all elicitation request parameter types.
ElicitRequestParams = Union["ElicitRequestFormParams", "ElicitRequestURLParams"]


# A union of all enum schema types.
EnumSchema = Union["LegacyTitledEnumSchema", "TitledMultiSelectEnumSchema", "TitledSingleSelectEnumSchema", "UntitledMultiSelectEnumSchema", "UntitledSingleSelectEnumSchema"]


# A union of single-select enum schema types.
SingleSelectEnumSchema = Union["TitledSingleSelectEnumSchema", "UntitledSingleSelectEnumSchema"]


# A union of multi-select enum schema types.
MultiSelectEnumSchema = Union["TitledMultiSelectEnumSchema", "UntitledMultiSelectEnumSchema"]


# A union of all primitive schema definition types.
PrimitiveSchemaDefinition = Union["BooleanSchema", "LegacyTitledEnumSchema", "NumberSchema", "StringSchema", "TitledMultiSelectEnumSchema", "TitledSingleSelectEnumSchema", "UntitledMultiSelectEnumSchema", "UntitledSingleSelectEnumSchema"]


# A union of all content block types. Maps to the vendor schema ContentBlock anyOf definition.
ContentBlockVariants = Union["AudioContent", "EmbeddedResource", "ImageContent", "ResourceLink", "TextContent"]


# A union of content types valid in sampling messages.
SamplingMessageContentBlock = Union["AudioContent", "ImageContent", "TextContent", "ToolResultContent", "ToolUseContent"]


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
HasMeta.model_rebuild()
HasAnnotations.model_rebuild()
HasIcons.model_rebuild()
HasName.model_rebuild()
Annotations.model_rebuild()
Error.model_rebuild()
InternalError.model_rebuild()
InvalidParamsError.model_rebuild()
InvalidRequestError.model_rebuild()
MethodNotFoundError.model_rebuild()
ParseError.model_rebuild()
Icon.model_rebuild()
Implementation.model_rebuild()
TextContent.model_rebuild()
ImageContent.model_rebuild()
AudioContent.model_rebuild()
ContentBlock.model_rebuild()
EmbeddedResource.model_rebuild()
ResourceLink.model_rebuild()
ToolUseContent.model_rebuild()
ToolResultContent.model_rebuild()
ResourceContents.model_rebuild()
TextResourceContents.model_rebuild()
BlobResourceContents.model_rebuild()
Resource.model_rebuild()
ResourceTemplate.model_rebuild()
Root.model_rebuild()
PromptArgument.model_rebuild()
Prompt.model_rebuild()
PromptMessage.model_rebuild()
PromptReference.model_rebuild()
ResourceTemplateReference.model_rebuild()
ToolAnnotations.model_rebuild()
ToolChoice.model_rebuild()
ToolExecution.model_rebuild()
MetaObject.model_rebuild()
ArgumentMap.model_rebuild()
CompletionArgument.model_rebuild()
CompletionContext.model_rebuild()
CompletionData.model_rebuild()
EnumOption.model_rebuild()
SchemaItems.model_rebuild()
JsonSchema.model_rebuild()
SchemaProperties.model_rebuild()
ToolInput.model_rebuild()
StructuredContentData.model_rebuild()
LogDetails.model_rebuild()
LogData.model_rebuild()
ErrorData.model_rebuild()
ElicitationContent.model_rebuild()
URLElicitation.model_rebuild()
ElicitationCapability.model_rebuild()
SamplingCapability.model_rebuild()
RootsCapability.model_rebuild()
PromptsCapability.model_rebuild()
ResourcesCapability.model_rebuild()
ToolsCapability.model_rebuild()
TaskRequestCapabilities.model_rebuild()
TasksCapability.model_rebuild()
ExtensionsCapability.model_rebuild()
ExtensionAppCapability.model_rebuild()
Tool.model_rebuild()
ModelHint.model_rebuild()
ModelPreferences.model_rebuild()
SamplingMessage.model_rebuild()
Task.model_rebuild()
TaskMetadata.model_rebuild()
RelatedTaskMetadata.model_rebuild()
ClientCapabilities.model_rebuild()
ServerCapabilities.model_rebuild()
StringSchema.model_rebuild()
NumberSchema.model_rebuild()
BooleanSchema.model_rebuild()
UntitledSingleSelectEnumSchema.model_rebuild()
TitledSingleSelectEnumSchema.model_rebuild()
UntitledMultiSelectEnumSchema.model_rebuild()
TitledMultiSelectEnumSchema.model_rebuild()
LegacyTitledEnumSchema.model_rebuild()
JSONRPCRequest.model_rebuild()
JSONRPCNotification.model_rebuild()
JSONRPCResultResponse.model_rebuild()
JSONRPCErrorResponse.model_rebuild()
URLElicitationRequiredError.model_rebuild()
Result.model_rebuild()
CancelledNotificationParams.model_rebuild()
ProgressNotificationParams.model_rebuild()
ElicitationCompleteNotificationParams.model_rebuild()
LoggingMessageNotificationParams.model_rebuild()
ResourceUpdatedNotificationParams.model_rebuild()
TaskStatusNotificationParams.model_rebuild()
CancelledNotification.model_rebuild()
InitializedNotification.model_rebuild()
ProgressNotification.model_rebuild()
ResourceListChangedNotification.model_rebuild()
ResourceUpdatedNotification.model_rebuild()
PromptListChangedNotification.model_rebuild()
ToolListChangedNotification.model_rebuild()
RootsListChangedNotification.model_rebuild()
LoggingMessageNotification.model_rebuild()
ElicitationCompleteNotification.model_rebuild()
TaskStatusNotification.model_rebuild()
CallToolRequestParams.model_rebuild()
GetPromptRequestParams.model_rebuild()
CompleteRequestParams.model_rebuild()
ReadResourceRequestParams.model_rebuild()
SubscribeRequestParams.model_rebuild()
UnsubscribeRequestParams.model_rebuild()
SetLevelRequestParams.model_rebuild()
InitializeRequestParams.model_rebuild()
CreateMessageRequestParams.model_rebuild()
ElicitRequestFormParams.model_rebuild()
ElicitRequestURLParams.model_rebuild()
PaginatedRequestParams.model_rebuild()
InitializeRequest.model_rebuild()
PingRequest.model_rebuild()
ListResourcesRequest.model_rebuild()
ListResourceTemplatesRequest.model_rebuild()
ReadResourceRequest.model_rebuild()
SubscribeRequest.model_rebuild()
UnsubscribeRequest.model_rebuild()
ListPromptsRequest.model_rebuild()
GetPromptRequest.model_rebuild()
ListToolsRequest.model_rebuild()
CallToolRequest.model_rebuild()
CompleteRequest.model_rebuild()
SetLevelRequest.model_rebuild()
CreateMessageRequest.model_rebuild()
ListRootsRequest.model_rebuild()
ElicitRequest.model_rebuild()
ListTasksRequest.model_rebuild()
GetTaskRequest.model_rebuild()
GetTaskPayloadRequest.model_rebuild()
CancelTaskRequest.model_rebuild()
InitializeResult.model_rebuild()
CallToolResult.model_rebuild()
CompleteResult.model_rebuild()
GetPromptResult.model_rebuild()
ListPromptsResult.model_rebuild()
ListResourcesResult.model_rebuild()
ListResourceTemplatesResult.model_rebuild()
ReadResourceResult.model_rebuild()
ListToolsResult.model_rebuild()
ListRootsResult.model_rebuild()
CreateMessageResult.model_rebuild()
ElicitResult.model_rebuild()
CreateTaskResult.model_rebuild()
GetTaskPayloadResult.model_rebuild()
ListTasksResult.model_rebuild()
CancelTaskResult.model_rebuild()
GetTaskResult.model_rebuild()
InitializeResultResponse.model_rebuild()
CallToolResultResponse.model_rebuild()
CompleteResultResponse.model_rebuild()
GetPromptResultResponse.model_rebuild()
ListPromptsResultResponse.model_rebuild()
ListResourcesResultResponse.model_rebuild()
ListResourceTemplatesResultResponse.model_rebuild()
ReadResourceResultResponse.model_rebuild()
ListToolsResultResponse.model_rebuild()
ListRootsResultResponse.model_rebuild()
CreateMessageResultResponse.model_rebuild()
ElicitResultResponse.model_rebuild()
SetLevelResultResponse.model_rebuild()
PingResultResponse.model_rebuild()
SubscribeResultResponse.model_rebuild()
UnsubscribeResultResponse.model_rebuild()
CreateTaskResultResponse.model_rebuild()
GetTaskResultResponse.model_rebuild()
GetTaskPayloadResultResponse.model_rebuild()
CancelTaskResultResponse.model_rebuild()
ListTasksResultResponse.model_rebuild()
