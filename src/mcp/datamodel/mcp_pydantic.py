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


metamodel_version = "1.12.0"
version = "2026-07-28"


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
     'description': 'The messages and objects of the Model Context Protocol, '
                    'version 2026-07-28, as its schema.json states them: JSON-RPC '
                    'requests, results, notifications and errors, and the tools, '
                    'resources, prompts, content and capabilities they carry. '
                    "Generated from MCP's own files by scripts/mcp_to_linkml.py.",
     'id': 'https://w3id.org/lmodel/mcp',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'mcp',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mcp': {'prefix_prefix': 'mcp',
                          'prefix_reference': 'https://w3id.org/lmodel/mcp/'},
                  'mcp_schema': {'prefix_prefix': 'mcp_schema',
                                 'prefix_reference': 'https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/2026-07-28/schema/2026-07-28/schema.json#/$defs/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/mcp',
                  'https://modelcontextprotocol.io/specification/2026-07-28'],
     'source': 'https://github.com/modelcontextprotocol/modelcontextprotocol/tree/2026-07-28/schema/2026-07-28',
     'source_file': 'src/mcp/schema/mcp.yaml',
     'subsets': {'common_types': {'description': 'The definitions schema.ts files '
                                                 'under Common Types.',
                                  'from_schema': 'https://w3id.org/lmodel/mcp',
                                  'name': 'common_types',
                                  'title': 'Common Types'},
                 'completion_complete': {'description': 'The definitions schema.ts '
                                                        'files under '
                                                        '`completion/complete`.',
                                         'from_schema': 'https://w3id.org/lmodel/mcp',
                                         'name': 'completion_complete',
                                         'title': 'completion/complete'},
                 'content': {'description': 'The definitions schema.ts files under '
                                            'Content.',
                             'from_schema': 'https://w3id.org/lmodel/mcp',
                             'name': 'content',
                             'title': 'Content'},
                 'elicitation_create': {'description': 'The definitions schema.ts '
                                                       'files under '
                                                       '`elicitation/create`.',
                                        'from_schema': 'https://w3id.org/lmodel/mcp',
                                        'name': 'elicitation_create',
                                        'title': 'elicitation/create'},
                 'errors': {'description': 'The definitions schema.ts files under '
                                           'Errors.',
                            'from_schema': 'https://w3id.org/lmodel/mcp',
                            'name': 'errors',
                            'title': 'Errors'},
                 'json_rpc': {'description': 'The definitions schema.ts files '
                                             'under JSON-RPC.',
                              'from_schema': 'https://w3id.org/lmodel/mcp',
                              'name': 'json_rpc',
                              'title': 'JSON-RPC'},
                 'multi_round_trip': {'description': 'The definitions schema.ts '
                                                     'files under Multi '
                                                     'Round-Trip.',
                                      'from_schema': 'https://w3id.org/lmodel/mcp',
                                      'name': 'multi_round_trip',
                                      'title': 'Multi Round-Trip'},
                 'notifications_cancelled': {'description': 'The definitions '
                                                            'schema.ts files under '
                                                            '`notifications/cancelled`.',
                                             'from_schema': 'https://w3id.org/lmodel/mcp',
                                             'name': 'notifications_cancelled',
                                             'title': 'notifications/cancelled'},
                 'notifications_message': {'description': 'The definitions '
                                                          'schema.ts files under '
                                                          '`notifications/message`.',
                                           'from_schema': 'https://w3id.org/lmodel/mcp',
                                           'name': 'notifications_message',
                                           'title': 'notifications/message'},
                 'notifications_progress': {'description': 'The definitions '
                                                           'schema.ts files under '
                                                           '`notifications/progress`.',
                                            'from_schema': 'https://w3id.org/lmodel/mcp',
                                            'name': 'notifications_progress',
                                            'title': 'notifications/progress'},
                 'notifications_prompts_list_changed': {'description': 'The '
                                                                       'definitions '
                                                                       'schema.ts '
                                                                       'files '
                                                                       'under '
                                                                       '`notifications/prompts/list_changed`.',
                                                        'from_schema': 'https://w3id.org/lmodel/mcp',
                                                        'name': 'notifications_prompts_list_changed',
                                                        'title': 'notifications/prompts/list_changed'},
                 'notifications_resources_list_changed': {'description': 'The '
                                                                         'definitions '
                                                                         'schema.ts '
                                                                         'files '
                                                                         'under '
                                                                         '`notifications/resources/list_changed`.',
                                                          'from_schema': 'https://w3id.org/lmodel/mcp',
                                                          'name': 'notifications_resources_list_changed',
                                                          'title': 'notifications/resources/list_changed'},
                 'notifications_resources_updated': {'description': 'The '
                                                                    'definitions '
                                                                    'schema.ts '
                                                                    'files under '
                                                                    '`notifications/resources/updated`.',
                                                     'from_schema': 'https://w3id.org/lmodel/mcp',
                                                     'name': 'notifications_resources_updated',
                                                     'title': 'notifications/resources/updated'},
                 'notifications_subscriptions_acknowledged': {'description': 'The '
                                                                             'definitions '
                                                                             'schema.ts '
                                                                             'files '
                                                                             'under '
                                                                             '`notifications/subscriptions/acknowledged`.',
                                                              'from_schema': 'https://w3id.org/lmodel/mcp',
                                                              'name': 'notifications_subscriptions_acknowledged',
                                                              'title': 'notifications/subscriptions/acknowledged'},
                 'notifications_tools_list_changed': {'description': 'The '
                                                                     'definitions '
                                                                     'schema.ts '
                                                                     'files under '
                                                                     '`notifications/tools/list_changed`.',
                                                      'from_schema': 'https://w3id.org/lmodel/mcp',
                                                      'name': 'notifications_tools_list_changed',
                                                      'title': 'notifications/tools/list_changed'},
                 'prompts_get': {'description': 'The definitions schema.ts files '
                                                'under `prompts/get`.',
                                 'from_schema': 'https://w3id.org/lmodel/mcp',
                                 'name': 'prompts_get',
                                 'title': 'prompts/get'},
                 'prompts_list': {'description': 'The definitions schema.ts files '
                                                 'under `prompts/list`.',
                                  'from_schema': 'https://w3id.org/lmodel/mcp',
                                  'name': 'prompts_list',
                                  'title': 'prompts/list'},
                 'resources_list': {'description': 'The definitions schema.ts '
                                                   'files under `resources/list`.',
                                    'from_schema': 'https://w3id.org/lmodel/mcp',
                                    'name': 'resources_list',
                                    'title': 'resources/list'},
                 'resources_read': {'description': 'The definitions schema.ts '
                                                   'files under `resources/read`.',
                                    'from_schema': 'https://w3id.org/lmodel/mcp',
                                    'name': 'resources_read',
                                    'title': 'resources/read'},
                 'resources_templates_list': {'description': 'The definitions '
                                                             'schema.ts files '
                                                             'under '
                                                             '`resources/templates/list`.',
                                              'from_schema': 'https://w3id.org/lmodel/mcp',
                                              'name': 'resources_templates_list',
                                              'title': 'resources/templates/list'},
                 'roots_list': {'description': 'The definitions schema.ts files '
                                               'under `roots/list`.',
                                'from_schema': 'https://w3id.org/lmodel/mcp',
                                'name': 'roots_list',
                                'title': 'roots/list'},
                 'sampling_createmessage': {'description': 'The definitions '
                                                           'schema.ts files under '
                                                           '`sampling/createMessage`.',
                                            'from_schema': 'https://w3id.org/lmodel/mcp',
                                            'name': 'sampling_createmessage',
                                            'title': 'sampling/createMessage'},
                 'server_discover': {'description': 'The definitions schema.ts '
                                                    'files under '
                                                    '`server/discover`.',
                                     'from_schema': 'https://w3id.org/lmodel/mcp',
                                     'name': 'server_discover',
                                     'title': 'server/discover'},
                 'subscriptions_listen': {'description': 'The definitions '
                                                         'schema.ts files under '
                                                         '`subscriptions/listen`.',
                                          'from_schema': 'https://w3id.org/lmodel/mcp',
                                          'name': 'subscriptions_listen',
                                          'title': 'subscriptions/listen'},
                 'tools_call': {'description': 'The definitions schema.ts files '
                                               'under `tools/call`.',
                                'from_schema': 'https://w3id.org/lmodel/mcp',
                                'name': 'tools_call',
                                'title': 'tools/call'},
                 'tools_list': {'description': 'The definitions schema.ts files '
                                               'under `tools/list`.',
                                'from_schema': 'https://w3id.org/lmodel/mcp',
                                'name': 'tools_list',
                                'title': 'tools/list'}},
     'title': 'Model Context Protocol (MCP) 2026-07-28',
     'types': {'McpBase64': {'comments': ['MCP gives such a string the format '
                                          'byte.'],
                             'description': 'Binary data, written as base64 text.',
                             'from_schema': 'https://w3id.org/lmodel/mcp',
                             'name': 'McpBase64',
                             'typeof': 'string',
                             'uri': 'xsd:base64Binary'},
               'McpCursor': {'description': 'An opaque token used to represent a '
                                            'cursor for pagination.',
                             'exact_mappings': ['mcp_schema:Cursor'],
                             'from_schema': 'https://w3id.org/lmodel/mcp',
                             'name': 'McpCursor',
                             'typeof': 'string'},
               'McpProgressToken': {'comments': ["linkml 1.12.1's JSON Schema "
                                                 "generator reads a type's typeof "
                                                 'and not its union_of, so each '
                                                 'slot that takes this value '
                                                 'states the union in its own '
                                                 'any_of.'],
                                    'description': 'A progress token, used to '
                                                   'associate progress '
                                                   'notifications with the '
                                                   'original request.',
                                    'exact_mappings': ['mcp_schema:ProgressToken'],
                                    'from_schema': 'https://w3id.org/lmodel/mcp',
                                    'name': 'McpProgressToken',
                                    'typeof': 'string',
                                    'union_of': ['string', 'integer']},
               'McpRequestId': {'comments': ["linkml 1.12.1's JSON Schema "
                                             "generator reads a type's typeof and "
                                             'not its union_of, so each slot that '
                                             'takes this value states the union in '
                                             'its own any_of.'],
                                'description': 'A uniquely identifying ID for a '
                                               'request in JSON-RPC.',
                                'exact_mappings': ['mcp_schema:RequestId'],
                                'from_schema': 'https://w3id.org/lmodel/mcp',
                                'name': 'McpRequestId',
                                'typeof': 'string',
                                'union_of': ['string', 'integer']},
               'McpResultType': {'description': 'Indicates the type of a {@link '
                                                'Result} object, allowing the '
                                                'client to\n'
                                                'determine how to parse the '
                                                'response.\n'
                                                '\n'
                                                'complete - the request completed '
                                                'successfully and the result '
                                                'contains the final content.\n'
                                                'input_required - the request '
                                                'requires additional input and the '
                                                'result contains an {@link '
                                                'InputRequiredResult} object with '
                                                'instructions for the client to '
                                                'provide additional input before '
                                                'retrying the original request.',
                                 'exact_mappings': ['mcp_schema:ResultType'],
                                 'from_schema': 'https://w3id.org/lmodel/mcp',
                                 'name': 'McpResultType',
                                 'typeof': 'string'},
               'McpUriTemplate': {'comments': ['MCP gives such a string the format '
                                               'uri-template.'],
                                  'description': 'A URI template, as RFC 6570 '
                                                 'defines one.',
                                  'from_schema': 'https://w3id.org/lmodel/mcp',
                                  'name': 'McpUriTemplate',
                                  'typeof': 'string'}}} )

class McpCacheScope(str, Enum):
    """
    The values MCP allows for `cacheScope`.
    """
    private = "private"
    public = "public"


class McpCreateMessageRequestParamsIncludeContext(str, Enum):
    """
    The values MCP allows for `includeContext`.
    """
    allServers = "allServers"
    none = "none"
    thisServer = "thisServer"


class McpElicitResultAction(str, Enum):
    """
    The values MCP allows for `action`.
    """
    accept = "accept"
    cancel = "cancel"
    decline = "decline"


class McpIconTheme(str, Enum):
    """
    The values MCP allows for `theme`.
    """
    dark = "dark"
    light = "light"


class McpLoggingLevel(str, Enum):
    """
    The severity of a log message.

These map to syslog message severities, as specified in RFC-5424:
https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1
    """
    alert = "alert"
    critical = "critical"
    debug = "debug"
    emergency = "emergency"
    error = "error"
    info = "info"
    notice = "notice"
    warning = "warning"


class McpNumberSchemaType(str, Enum):
    """
    The values MCP allows for `type`.
    """
    integer = "integer"
    number = "number"


class McpRole(str, Enum):
    """
    The sender or recipient of messages and data in a conversation.
    """
    assistant = "assistant"
    user = "user"


class McpStringSchemaFormat(str, Enum):
    """
    The values MCP allows for `format`.
    """
    date = "date"
    date_time = "date-time"
    email = "email"
    uri = "uri"


class McpToolChoiceMode(str, Enum):
    """
    The values MCP allows for `mode`.
    """
    auto = "auto"
    none = "none"
    required = "required"



class McpAnnotations(ConfiguredBaseModel):
    """
    Optional annotations for the client. The client can use annotations to inform how objects are used or displayed
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Annotations'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    intended_audience: Optional[list[McpRole]] = Field(default=None, description="""Describes who the intended audience of this object or data is.

It can include multiple entries to indicate content useful for multiple audiences (e.g., `[\"user\", \"assistant\"]`).""", json_schema_extra = { "linkml_meta": {'aliases': ['audience'], 'domain_of': ['McpAnnotations']} })
    lastModified: Optional[str] = Field(default=None, description="""The moment the resource was last modified, as an ISO 8601 formatted string.

Should be an ISO 8601 formatted string (e.g., \"2025-01-12T15:00:58Z\").

Examples: last activity timestamp in an open file, timestamp when the resource
was attached, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAnnotations']} })
    priority: Optional[float] = Field(default=None, description="""Describes how important this data is for operating the server.

A value of 1 means \"most important,\" and indicates that the data is
effectively required, while 0 means \"least important,\" and indicates that
the data is entirely optional.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['McpAnnotations']} })


class McpAudioContent(ConfiguredBaseModel):
    """
    Audio provided to or from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:AudioContent'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    data: str = Field(default=..., description="""The base64-encoded audio data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    mimeType: str = Field(default=..., description="""The MIME type of the audio. Different providers may support different audio types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    kind: Literal["audio"] = Field(default=..., description="""The kind of object, always `audio`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'audio'} })


class McpBaseMetadata(ConfiguredBaseModel):
    """
    Base interface for metadata with name (identifier) and title (display name) properties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:BaseMetadata'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'slot_usage': {'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })


class McpBooleanSchema(ConfiguredBaseModel):
    """
    MCP's `BooleanSchema`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:BooleanSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'A description of the field for '
                                                       'the user.',
                                        'name': 'description'},
                        'title': {'description': 'A title for the field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of the field for the user.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""A title for the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[bool] = Field(default=None, description="""The value the field takes when the user gives none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    kind: Literal["boolean"] = Field(default=..., description="""The kind of object, always `boolean`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'boolean'} })


class McpClientCapabilities(ConfiguredBaseModel):
    """
    Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientCapabilities'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    elicitation: Optional[McpClientCapabilitiesElicitation] = Field(default=None, description="""Present if the client supports elicitation from the server.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities']} })
    experimental: Optional[McpClientCapabilitiesExperimental] = Field(default=None, description="""Experimental, non-standard capabilities that the client supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities', 'McpServerCapabilities']} })
    extensions: Optional[McpClientCapabilitiesExtensions] = Field(default=None, description="""Optional MCP extensions that the client supports. Keys are extension identifiers
(e.g., \"io.modelcontextprotocol/oauth-client-credentials\"), and values are
per-extension settings objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities', 'McpServerCapabilities']} })
    roots: Optional[McpClientCapabilitiesRoots] = Field(default=None, description="""Present if the client supports listing roots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities', 'McpListRootsResult']} })
    sampling: Optional[McpClientCapabilitiesSampling] = Field(default=None, description="""Present if the client supports sampling from an LLM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities']} })


class McpClientCapabilitiesElicitation(ConfiguredBaseModel):
    """
    Present if the client supports elicitation from the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientCapabilities/properties/elicitation'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    form: Optional[McpJSONObject] = Field(default=None, description="""Settings for elicitation by form.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilitiesElicitation']} })
    url_settings: Optional[McpJSONObject] = Field(default=None, description="""Settings for elicitation by URL.""", json_schema_extra = { "linkml_meta": {'aliases': ['url'], 'domain_of': ['McpClientCapabilitiesElicitation']} })


class McpClientCapabilitiesExperimental(ConfiguredBaseModel):
    """
    Experimental, non-standard capabilities that the client supports.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientCapabilities/properties/experimental'],
         'extra_slots': {'range_expression': {'range': 'McpJSONObject'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    pass


class McpClientCapabilitiesExtensions(ConfiguredBaseModel):
    """
    Optional MCP extensions that the client supports. Keys are extension identifiers
    (e.g., \"io.modelcontextprotocol/oauth-client-credentials\"), and values are
    per-extension settings objects. An empty object indicates support with no settings.

    Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
    mandatory prefix.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientCapabilities/properties/extensions'],
         'extra_slots': {'range_expression': {'range': 'McpJSONObject'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    pass


class McpClientCapabilitiesRoots(ConfiguredBaseModel):
    """
    Present if the client supports listing roots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientCapabilities/properties/roots'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    pass


class McpClientCapabilitiesSampling(ConfiguredBaseModel):
    """
    Present if the client supports sampling from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientCapabilities/properties/sampling'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    context_info: Optional[McpJSONObject] = Field(default=None, description="""Whether the client supports context inclusion via `includeContext` parameter.
If not declared, servers SHOULD only use `includeContext: \"none\"` (or omit it).""", json_schema_extra = { "linkml_meta": {'aliases': ['context'],
         'domain_of': ['McpClientCapabilitiesSampling', 'McpCompleteRequestParams']} })
    tools: Optional[McpJSONObject] = Field(default=None, description="""Whether the client supports tool use via `tools` and `toolChoice` parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilitiesSampling',
                       'McpCreateMessageRequestParams',
                       'McpListToolsResult',
                       'McpServerCapabilities']} })


class McpClientRequest(ConfiguredBaseModel):
    """
    One of `DiscoverRequest`, `ListResourcesRequest`, `ListResourceTemplatesRequest`, `ReadResourceRequest`, `SubscriptionsListenRequest`, `ListPromptsRequest`, `GetPromptRequest`, `ListToolsRequest`, `CallToolRequest`, `CompleteRequest`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpDiscoverRequest'},
                    {'is_a': 'McpListResourcesRequest'},
                    {'is_a': 'McpListResourceTemplatesRequest'},
                    {'is_a': 'McpReadResourceRequest'},
                    {'is_a': 'McpSubscriptionsListenRequest'},
                    {'is_a': 'McpListPromptsRequest'},
                    {'is_a': 'McpGetPromptRequest'},
                    {'is_a': 'McpListToolsRequest'},
                    {'is_a': 'McpCallToolRequest'},
                    {'is_a': 'McpCompleteRequest'}],
         'exact_mappings': ['mcp_schema:ClientRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpCompleteRequestParamsArgument(ConfiguredBaseModel):
    """
    The argument's information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteRequestParams/properties/argument'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete'],
         'slot_usage': {'name': {'description': 'The name of the argument',
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""The name of the argument""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    value: str = Field(default=..., description="""The value of the argument to use for completion matching.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteRequestParamsArgument']} })


class McpCompleteRequestParamsContext(ConfiguredBaseModel):
    """
    Additional, optional context for completions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteRequestParams/properties/context'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    arguments: Optional[McpCompleteRequestParamsContextArguments] = Field(default=None, description="""Previously-resolved variables in a URI template or prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpCompleteRequestParamsContext',
                       'McpGetPromptRequestParams',
                       'McpPrompt']} })


class McpCompleteRequestParamsContextArguments(ConfiguredBaseModel):
    """
    Previously-resolved variables in a URI template or prompt.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteRequestParams/properties/context/properties/arguments'],
         'extra_slots': {'range_expression': {'range': 'string'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    pass


class McpCompleteResultCompletion(ConfiguredBaseModel):
    """
    The object MCP's `CompleteResult` holds under `completion`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteResult/properties/completion'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    hasMore: Optional[bool] = Field(default=None, description="""Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteResultCompletion']} })
    total: Optional[int] = Field(default=None, description="""The total number of completion options available. This can exceed the number of values actually sent in the response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteResultCompletion', 'McpProgressNotificationParams']} })
    values: list[str] = Field(default=..., description="""An array of completion values. Must not exceed 100 items.""", max_length=100, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteResultCompletion']} })


class McpContentBlock(ConfiguredBaseModel):
    """
    One of `TextContent`, `ImageContent`, `AudioContent`, `ResourceLink`, `EmbeddedResource`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpTextContent'},
                    {'is_a': 'McpImageContent'},
                    {'is_a': 'McpAudioContent'},
                    {'is_a': 'McpResourceLink'},
                    {'is_a': 'McpEmbeddedResource'}],
         'exact_mappings': ['mcp_schema:ContentBlock'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    pass


class McpCreateMessageRequest(ConfiguredBaseModel):
    """
    A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CreateMessageRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    method: Literal["sampling/createMessage"] = Field(default=..., description="""The method's name, always `sampling/createMessage`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'sampling/createMessage'} })
    params: McpCreateMessageRequestParams = Field(default=..., description="""Parameters for a `sampling/createMessage` request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpCreateMessageRequestParams(ConfiguredBaseModel):
    """
    Parameters for a `sampling/createMessage` request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CreateMessageRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    includeContext: Optional[McpCreateMessageRequestParamsIncludeContext] = Field(default=None, description="""A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.
The client MAY ignore this request.

Default is `\"none\"`. The values `\"thisServer\"` and `\"allServers\"` are deprecated (SEP-2596): servers SHOULD
omit this field or use `\"none\"`, and SHOULD only use the deprecated values if the client declares
{@link ClientCapabilities.sampling.context}.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    maxTokens: int = Field(default=..., description="""The requested maximum number of tokens to sample (to prevent runaway completions).

The client MAY choose to sample fewer tokens than the requested maximum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    messages: list[McpSamplingMessage] = Field(default=..., description="""Describes a message issued to or received from an LLM API.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams', 'McpGetPromptResult']} })
    metadata: Optional[McpJSONObject] = Field(default=None, description="""Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    modelPreferences: Optional[McpModelPreferences] = Field(default=None, description="""The server's preferences for which model to select. The client MAY ignore these preferences.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    stopSequences: Optional[list[str]] = Field(default=None, description="""Sequences at which the model should stop generating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    systemPrompt: Optional[str] = Field(default=None, description="""An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    temperature: Optional[float] = Field(default=None, description="""The sampling temperature the server asks the model to use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    toolChoice: Optional[McpToolChoice] = Field(default=None, description="""Controls how the model uses tools.
The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared.
Default is `{ mode: \"auto\" }`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams']} })
    tools: Optional[list[McpTool]] = Field(default=None, description="""Tools that the model may use during generation.
The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilitiesSampling',
                       'McpCreateMessageRequestParams',
                       'McpListToolsResult',
                       'McpServerCapabilities']} })


class McpElicitRequest(ConfiguredBaseModel):
    """
    A request from the server to elicit additional information from the user via the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    method: Literal["elicitation/create"] = Field(default=..., description="""The method's name, always `elicitation/create`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'elicitation/create'} })
    params: McpElicitRequestParams = Field(default=..., description="""The parameters for a request to elicit additional information from the user via the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpElicitRequestFormParams(ConfiguredBaseModel):
    """
    The parameters for a request to elicit non-sensitive information from the user via a form in the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitRequestFormParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    message: str = Field(default=..., description="""The message to present to the user describing what information is being requested.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })
    mode: Optional[Literal["form"]] = Field(default=None, description="""The elicitation mode.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpToolChoice'],
         'equals_string': 'form'} })
    requestedSchema: McpElicitRequestFormParamsRequestedSchema = Field(default=..., description="""A restricted subset of JSON Schema.
Only top-level properties are allowed, without nesting.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams']} })


class McpElicitRequestFormParamsRequestedSchema(ConfiguredBaseModel):
    """
    A restricted subset of JSON Schema.
    Only top-level properties are allowed, without nesting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitRequestFormParams/properties/requestedSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    schema_dialect: Optional[str] = Field(default=None, description="""The JSON Schema dialect the schema is written in.""", json_schema_extra = { "linkml_meta": {'aliases': ['$schema'],
         'domain_of': ['McpElicitRequestFormParamsRequestedSchema',
                       'McpToolInputSchema',
                       'McpToolOutputSchema']} })
    properties: McpElicitRequestFormParamsRequestedSchemaProperties = Field(default=..., description="""The fields of the form, by name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParamsRequestedSchema']} })
    required_names: Optional[list[str]] = Field(default=None, description="""The names of the fields the user must fill in.""", json_schema_extra = { "linkml_meta": {'aliases': ['required'],
         'domain_of': ['McpElicitRequestFormParamsRequestedSchema']} })
    kind: Literal["object"] = Field(default=..., description="""The kind of object, always `object`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'object'} })


class McpElicitRequestFormParamsRequestedSchemaProperties(ConfiguredBaseModel):
    """
    The object MCP's `ElicitRequestFormParams` holds under `properties`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitRequestFormParams/properties/requestedSchema/properties/properties'],
         'extra_slots': {'range_expression': {'range': 'McpPrimitiveSchemaDefinition'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    pass


class McpElicitRequestParams(ConfiguredBaseModel):
    """
    The parameters for a request to elicit additional information from the user via the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpElicitRequestFormParams'},
                    {'is_a': 'McpElicitRequestURLParams'}],
         'exact_mappings': ['mcp_schema:ElicitRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    pass


class McpElicitRequestURLParams(ConfiguredBaseModel):
    """
    The parameters for a request to elicit information from the user via a URL in the client.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitRequestURLParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'url': {'description': 'The URL that the user should navigate '
                                               'to.',
                                'name': 'url',
                                'required': True}}})

    url: str = Field(default=..., description="""The URL that the user should navigate to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestURLParams'], 'slot_uri': 'schema:url'} })
    message: str = Field(default=..., description="""The message to present to the user explaining why the interaction is needed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })
    mode: Literal["url"] = Field(default=..., description="""The elicitation mode.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpToolChoice'],
         'equals_string': 'url'} })


class McpElicitResult(ConfiguredBaseModel):
    """
    The result returned by the client for an {@link ElicitRequestelicitation/create} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    action: McpElicitResultAction = Field(default=..., description="""The user action in response to the elicitation.
- `\"accept\"`: User submitted the form/confirmed the action
- `\"decline\"`: User explicitly declined the action
- `\"cancel\"`: User dismissed without making an explicit choice""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitResult']} })
    content: Optional[McpElicitResultContent] = Field(default=None, description="""The submitted form data, only present when action is `\"accept\"` and mode was `\"form\"`.
Contains values matching the requested schema.
Omitted for out-of-band mode responses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult',
                       'McpCreateMessageResult',
                       'McpElicitResult',
                       'McpPromptMessage',
                       'McpSamplingMessage',
                       'McpToolResultContent']} })


class McpElicitResultContent(ConfiguredBaseModel):
    """
    The submitted form data, only present when action is `\"accept\"` and mode was `\"form\"`.
    Contains values matching the requested schema.
    Omitted for out-of-band mode responses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ElicitResult/properties/content'],
         'extra_slots': {'range_expression': {'any_of': [{'multivalued': True,
                                                          'range': 'string'},
                                                         {'range': 'string'},
                                                         {'range': 'integer'},
                                                         {'range': 'boolean'}]}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    pass


class McpEmbeddedResource(ConfiguredBaseModel):
    """
    The contents of a resource, embedded into a prompt or tool call result.

    It is up to the client how best to render embedded resources for the benefit
    of the LLM and/or the user.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:EmbeddedResource'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    resource_contents: Union[McpBlobResourceContents, McpTextResourceContents] = Field(default=..., description="""The resource's contents, as text or as binary data.""", json_schema_extra = { "linkml_meta": {'aliases': ['resource'],
         'any_of': [{'range': 'McpTextResourceContents'},
                    {'range': 'McpBlobResourceContents'}],
         'domain_of': ['McpEmbeddedResource']} })
    kind: Literal["resource"] = Field(default=..., description="""The kind of object, always `resource`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'resource'} })


class McpEnumSchema(ConfiguredBaseModel):
    """
    One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`, `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`, `LegacyTitledEnumSchema`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpUntitledSingleSelectEnumSchema'},
                    {'is_a': 'McpTitledSingleSelectEnumSchema'},
                    {'is_a': 'McpUntitledMultiSelectEnumSchema'},
                    {'is_a': 'McpTitledMultiSelectEnumSchema'},
                    {'is_a': 'McpLegacyTitledEnumSchema'}],
         'exact_mappings': ['mcp_schema:EnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpError(ConfiguredBaseModel):
    """
    MCP's `Error`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Error'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error type that occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpGetPromptRequestParamsArguments(ConfiguredBaseModel):
    """
    Arguments to use for templating the prompt.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:GetPromptRequestParams/properties/arguments'],
         'extra_slots': {'range_expression': {'range': 'string'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_get']})

    pass


class McpHeaderMismatchErrorError(McpError):
    """
    MCP's `Error`, with the code and data this error carries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:HeaderMismatchError/properties/error/allOf/1'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error code, always `-32020`."""    , le=-32020, ge=-32020, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpIcon(ConfiguredBaseModel):
    """
    An optionally-sized icon that can be displayed in a user interface.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Icon'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    mimeType: Optional[str] = Field(default=None, description="""Optional MIME type override if the source MIME type is missing or generic.
For example: `\"image/png\"`, `\"image/jpeg\"`, or `\"image/svg+xml\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    sizes: Optional[list[str]] = Field(default=None, description="""Optional array of strings that specify sizes at which the icon can be used.
Each string should be in WxH format (e.g., `\"48x48\"`, `\"96x96\"`) or `\"any\"` for scalable formats like SVG.

If not provided, the client should assume that the icon can be used at any size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcon']} })
    src: str = Field(default=..., description="""A standard URI pointing to an icon resource. May be an HTTP/HTTPS URL or a
`data:` URI with Base64-encoded image data.

Consumers SHOULD take steps to ensure URLs serving icons are from the
same domain as the client/server or a trusted domain.

Consumers SHOULD take appropriate precautions when consuming SVGs as they can contain
executable JavaScript.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcon']} })
    theme: Optional[McpIconTheme] = Field(default=None, description="""Optional specifier for the theme this icon is designed for. `\"light\"` indicates
the icon is designed to be used with a light background, and `\"dark\"` indicates
the icon is designed to be used with a dark background.

If not provided, the client should assume the icon can be used with any theme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcon']} })


class McpIcons(ConfiguredBaseModel):
    """
    Base interface to add `icons` property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Icons'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })


class McpImageContent(ConfiguredBaseModel):
    """
    An image provided to or from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ImageContent'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    data: str = Field(default=..., description="""The base64-encoded image data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    mimeType: str = Field(default=..., description="""The MIME type of the image. Different providers may support different image types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    kind: Literal["image"] = Field(default=..., description="""The kind of object, always `image`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'image'} })


class McpImplementation(McpIcons, McpBaseMetadata):
    """
    Describes the MCP implementation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Implementation'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover'],
         'mixins': ['McpIcons'],
         'slot_usage': {'description': {'description': 'An optional human-readable '
                                                       'description of what this '
                                                       'implementation does.\n'
                                                       '\n'
                                                       'This can be used by clients or '
                                                       'servers to provide context '
                                                       'about their purpose\n'
                                                       'and capabilities. For example, '
                                                       'a server might describe the '
                                                       'types of resources\n'
                                                       'or tools it provides, while a '
                                                       'client might describe its '
                                                       'intended use case.',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'},
                        'version': {'description': 'The version of this '
                                                   'implementation.',
                                    'name': 'version',
                                    'required': True}}})

    description: Optional[str] = Field(default=None, description="""An optional human-readable description of what this implementation does.

This can be used by clients or servers to provide context about their purpose
and capabilities. For example, a server might describe the types of resources
or tools it provides, while a client might describe its intended use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    version: str = Field(default=..., description="""The version of this implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpImplementation'], 'slot_uri': 'schema:version'} })
    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })
    websiteUrl: Optional[str] = Field(default=None, description="""An optional URL of the website for this implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpImplementation']} })


class McpInputRequest(ConfiguredBaseModel):
    """
    One of `CreateMessageRequest`, `ListRootsRequest`, `ElicitRequest`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpCreateMessageRequest'},
                    {'is_a': 'McpListRootsRequest'},
                    {'is_a': 'McpElicitRequest'}],
         'exact_mappings': ['mcp_schema:InputRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpInputRequests(ConfiguredBaseModel):
    """
    A map of server-initiated requests that the client must fulfill.
    Keys are server-assigned identifiers; values are the request objects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:InputRequests'],
         'extra_slots': {'range_expression': {'range': 'McpInputRequest'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['multi_round_trip']})

    pass


class McpInputResponse(ConfiguredBaseModel):
    """
    One of `CreateMessageResult`, `ListRootsResult`, `ElicitResult`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpCreateMessageResult'},
                    {'is_a': 'McpListRootsResult'},
                    {'is_a': 'McpElicitResult'}],
         'exact_mappings': ['mcp_schema:InputResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpInputResponses(ConfiguredBaseModel):
    """
    A map of client responses to server-initiated requests.
    Keys correspond to the keys in the {@link InputRequests} map;
    values are the client's result for each request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:InputResponses'],
         'extra_slots': {'range_expression': {'range': 'McpInputResponse'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['multi_round_trip']})

    pass


class McpInternalError(McpError):
    """
    A JSON-RPC error indicating that an internal error occurred on the receiver. This error is returned when the receiver encounters an unexpected condition that prevents it from fulfilling the request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:InternalError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error type that occurred."""    , le=-32603, ge=-32603, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpInvalidParamsError(McpError):
    """
    A JSON-RPC error indicating that the method parameters are invalid or malformed.

    In MCP, this error is returned in various contexts when request parameters fail validation:

    - **Tools**: Unknown tool name or invalid tool arguments
    - **Prompts**: Unknown prompt name or missing required arguments
    - **Pagination**: Invalid or expired cursor values
    - **Logging**: Invalid log level
    - **Elicitation**: Server requests an elicitation mode not declared in client capabilities
    - **Sampling**: Missing tool result or tool results mixed with other content
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:InvalidParamsError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error type that occurred."""    , le=-32602, ge=-32602, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpInvalidRequestError(McpError):
    """
    A JSON-RPC error indicating that the request is not a valid request object. This error is returned when the message structure does not conform to the JSON-RPC 2.0 specification requirements for a request (e.g., missing required fields like `jsonrpc` or `method`, or using invalid types for these fields).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:InvalidRequestError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error type that occurred."""    , le=-32600, ge=-32600, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpJSONObject(ConfiguredBaseModel):
    """
    A JSON object, whose values are JSON values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:JSONObject'],
         'extra_slots': {'range_expression': {'range': 'McpJSONValue'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    pass


class McpJSONRPCErrorResponse(ConfiguredBaseModel):
    """
    A response to a request that indicates an error occurred.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:JSONRPCErrorResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['json_rpc']})

    error: McpError = Field(default=..., description="""The error the request ended with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpUnsupportedProtocolVersionError']} })
    identifier: Optional[Union[int, str]] = Field(default=None, description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })


class McpHeaderMismatchError(McpJSONRPCErrorResponse):
    """
    Returned when a server rejects a request because the values in the HTTP
    headers do not match the corresponding values in the request body, or
    because required headers are missing or malformed. For HTTP, the response
    status code MUST be `400 Bad Request`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:HeaderMismatchError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    error: McpHeaderMismatchErrorError = Field(default=..., description="""The error the request ended with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpUnsupportedProtocolVersionError']} })
    identifier: Optional[Union[int, str]] = Field(default=None, description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })


class McpJSONRPCMessage(ConfiguredBaseModel):
    """
    Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpJSONRPCRequest'},
                    {'is_a': 'McpJSONRPCNotification'},
                    {'is_a': 'McpJSONRPCResultResponse'},
                    {'is_a': 'McpJSONRPCErrorResponse'}],
         'exact_mappings': ['mcp_schema:JSONRPCMessage'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['json_rpc']})

    pass


class McpJSONRPCResponse(ConfiguredBaseModel):
    """
    A response to a request, containing either the result or error.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpJSONRPCResultResponse'},
                    {'is_a': 'McpJSONRPCErrorResponse'}],
         'exact_mappings': ['mcp_schema:JSONRPCResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['json_rpc']})

    pass


class McpJSONRPCResultResponse(ConfiguredBaseModel):
    """
    A successful (non-error) response to a request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:JSONRPCResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['json_rpc']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpResult = Field(default=..., description="""Common result fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpCallToolResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link CallToolRequesttools/call} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CallToolResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_call']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: Union[McpCallToolResult, McpInputRequiredResult] = Field(default=..., description="""What the request returned.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpInputRequiredResult'},
                    {'range': 'McpCallToolResult'}],
         'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpCompleteResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link CompleteRequestcompletion/complete} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpCompleteResult = Field(default=..., description="""The result returned by the server for a {@link CompleteRequestcompletion/complete} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpDiscoverResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link DiscoverRequestserver/discover} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:DiscoverResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpDiscoverResult = Field(default=..., description="""The result returned by the server for a {@link DiscoverRequestserver/discover} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpGetPromptResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link GetPromptRequestprompts/get} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:GetPromptResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_get']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: Union[McpGetPromptResult, McpInputRequiredResult] = Field(default=..., description="""What the request returned.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpInputRequiredResult'},
                    {'range': 'McpGetPromptResult'}],
         'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpLegacyTitledEnumSchema(ConfiguredBaseModel):
    """
    Use {@link TitledSingleSelectEnumSchema} instead.
    This interface will be removed in a future version.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:LegacyTitledEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'A description of the field for '
                                                       'the user.',
                                        'name': 'description'},
                        'title': {'description': 'A title for the field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of the field for the user.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""A title for the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[str] = Field(default=None, description="""The value the field takes when the user gives none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    enum: list[str] = Field(default=..., description="""The values the field offers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpLegacyTitledEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema']} })
    enumNames: Optional[list[str]] = Field(default=None, description="""(Legacy) Display names for enum values.
Non-standard according to JSON schema 2020-12.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpLegacyTitledEnumSchema']} })
    kind: Literal["string"] = Field(default=..., description="""The kind of object, always `string`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'string'} })


class McpListPromptsResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListPromptsRequestprompts/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListPromptsResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpListPromptsResult = Field(default=..., description="""The result returned by the server for a {@link ListPromptsRequestprompts/list} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpListResourceTemplatesResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListResourceTemplatesResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_templates_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpListResourceTemplatesResult = Field(default=..., description="""The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpListResourcesResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListResourcesRequestresources/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListResourcesResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpListResourcesResult = Field(default=..., description="""The result returned by the server for a {@link ListResourcesRequestresources/list} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpListRootsRequest(ConfiguredBaseModel):
    """
    Sent from the server to request a list of root URIs from the client. Roots allow
    servers to ask for specific directories or files to operate on. A common example
    for roots is providing a set of repositories or directories a server should operate
    on.

    This request is typically used when the server needs to understand the file system
    structure or access specific locations that the client has permission to read from.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListRootsRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['roots_list']})

    method: Literal["roots/list"] = Field(default=..., description="""The method's name, always `roots/list`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'roots/list'} })
    params: Optional[McpListRootsRequestParams] = Field(default=None, description="""The parameters the message carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpListRootsRequestParams(ConfiguredBaseModel):
    """
    The object MCP's `ListRootsRequest` holds under `params`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListRootsRequest/properties/params'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['roots_list']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })


class McpListRootsResult(ConfiguredBaseModel):
    """
    The result returned by the client for a {@link ListRootsRequestroots/list} request.
    This result contains an array of {@link Root} objects, each representing a root directory
    or file that the server can operate on.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListRootsResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['roots_list']})

    roots: list[McpRoot] = Field(default=..., description="""Represents a root directory or file that the server can operate on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities', 'McpListRootsResult']} })


class McpListToolsResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListToolsRequesttools/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListToolsResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpListToolsResult = Field(default=..., description="""The result returned by the server for a {@link ListToolsRequesttools/list} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpMetaObject(ConfiguredBaseModel):
    """
    Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

    Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

    Valid keys have two segments:

    **Prefix:**
    - Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
    - Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
    - Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
    - Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

    **Name:**
    - Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
    - Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:MetaObject'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    pass


class McpMethodNotFoundError(McpError):
    """
    A JSON-RPC error indicating that the requested method does not exist or is not available.

    In MCP, a server returns this error when a client invokes a method the server does not implement — either a genuinely unknown method, or one gated behind a server capability the server did not advertise (e.g., calling `prompts/list` when the `prompts` capability was not advertised).

    A request that requires a client capability the client did not declare is signalled instead by {@link MissingRequiredClientCapabilityError} (`-32021`).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:MethodNotFoundError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error type that occurred."""    , le=-32601, ge=-32601, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpMissingRequiredClientCapabilityError(McpJSONRPCErrorResponse):
    """
    Returned when processing a request requires a capability the client did not
    declare in `clientCapabilities`. For HTTP, the response status code MUST be
    `400 Bad Request`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:MissingRequiredClientCapabilityError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    error: McpMissingRequiredClientCapabilityErrorError = Field(default=..., description="""The error the request ended with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpUnsupportedProtocolVersionError']} })
    identifier: Optional[Union[int, str]] = Field(default=None, description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })


class McpMissingRequiredClientCapabilityErrorError(McpError):
    """
    MCP's `Error`, with the code and data this error carries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:MissingRequiredClientCapabilityError/properties/error/allOf/1'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error code, always `-32021`."""    , le=-32021, ge=-32021, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: McpMissingRequiredClientCapabilityErrorErrorData = Field(default=..., description="""Details of the error.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpMissingRequiredClientCapabilityErrorErrorData(ConfiguredBaseModel):
    """
    The object MCP's `MissingRequiredClientCapabilityError` holds under `data`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:MissingRequiredClientCapabilityError/properties/error/allOf/1/properties/data'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    requiredCapabilities: McpClientCapabilities = Field(default=..., description="""The capabilities the server requires from the client to process this request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpMissingRequiredClientCapabilityErrorErrorData']} })


class McpModelHint(ConfiguredBaseModel):
    """
    Hints to use for model selection.

    Keys not declared here are currently left unspecified by the spec and are up
    to the client to interpret.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ModelHint'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage'],
         'slot_usage': {'name': {'description': 'A hint for a model name.\n'
                                                '\n'
                                                'The client SHOULD treat this as a '
                                                'substring of a model name; for '
                                                'example:\n'
                                                ' - `claude-3-5-sonnet` should match '
                                                '`claude-3-5-sonnet-20241022`\n'
                                                ' - `sonnet` should match '
                                                '`claude-3-5-sonnet-20241022`, '
                                                '`claude-3-sonnet-20240229`, etc.\n'
                                                ' - `claude` should match any Claude '
                                                'model\n'
                                                '\n'
                                                'The client MAY also map the string to '
                                                "a different provider's model name or "
                                                'a different model family, as long as '
                                                'it fills a similar niche; for '
                                                'example:\n'
                                                ' - `gemini-1.5-flash` could match '
                                                '`claude-3-haiku-20240307`',
                                 'name': 'name'}}})

    name: Optional[str] = Field(default=None, description="""A hint for a model name.

The client SHOULD treat this as a substring of a model name; for example:
 - `claude-3-5-sonnet` should match `claude-3-5-sonnet-20241022`
 - `sonnet` should match `claude-3-5-sonnet-20241022`, `claude-3-sonnet-20240229`, etc.
 - `claude` should match any Claude model

The client MAY also map the string to a different provider's model name or a different model family, as long as it fills a similar niche; for example:
 - `gemini-1.5-flash` could match `claude-3-haiku-20240307`""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })


class McpModelPreferences(ConfiguredBaseModel):
    """
    The server's preferences for model selection, requested of the client during sampling.

    Because LLMs can vary along multiple dimensions, choosing the \"best\" model is
    rarely straightforward.  Different models excel in different areas—some are
    faster but less capable, others are more capable but more expensive, and so
    on. This interface allows servers to express their priorities across multiple
    dimensions to help clients make an appropriate selection for their use case.

    These preferences are always advisory. The client MAY ignore them. It is also
    up to the client to decide how to interpret these preferences and how to
    balance them against other considerations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ModelPreferences'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    costPriority: Optional[float] = Field(default=None, description="""How much to prioritize cost when selecting a model. A value of 0 means cost
is not important, while a value of 1 means cost is the most important
factor.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['McpModelPreferences']} })
    hints: Optional[list[McpModelHint]] = Field(default=None, description="""Optional hints to use for model selection.

If multiple hints are specified, the client MUST evaluate them in order
(such that the first match is taken).

The client SHOULD prioritize these hints over the numeric priorities, but
MAY still use the priorities to select from ambiguous matches.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpModelPreferences']} })
    intelligencePriority: Optional[float] = Field(default=None, description="""How much to prioritize intelligence and capabilities when selecting a
model. A value of 0 means intelligence is not important, while a value of 1
means intelligence is the most important factor.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['McpModelPreferences']} })
    speedPriority: Optional[float] = Field(default=None, description="""How much to prioritize sampling speed (latency) when selecting a model. A
value of 0 means speed is not important, while a value of 1 means speed is
the most important factor.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['McpModelPreferences']} })


class McpMultiSelectEnumSchema(ConfiguredBaseModel):
    """
    One of `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpUntitledMultiSelectEnumSchema'},
                    {'is_a': 'McpTitledMultiSelectEnumSchema'}],
         'exact_mappings': ['mcp_schema:MultiSelectEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpNotification(ConfiguredBaseModel):
    """
    MCP's `Notification`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Notification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    method: str = Field(default=..., description="""The name of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })
    params: Optional[McpJSONObject] = Field(default=None, description="""The parameters the message carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpJSONRPCNotification(McpNotification):
    """
    A notification which does not expect a response.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:JSONRPCNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['json_rpc']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: str = Field(default=..., description="""The name of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })
    params: Optional[McpJSONObject] = Field(default=None, description="""The parameters the message carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpCancelledNotification(McpJSONRPCNotification):
    """
    This notification is sent by the client to indicate that it is cancelling a request it previously issued.

    On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

    The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

    This notification indicates that the result will be unused, so any associated processing SHOULD cease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CancelledNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_cancelled']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/cancelled"] = Field(default=..., description="""The method's name, always `notifications/cancelled`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/cancelled'} })
    params: McpCancelledNotificationParams = Field(default=..., description="""Parameters for a `notifications/cancelled` notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpClientNotification(McpCancelledNotification):
    """
    This notification is sent by the client to indicate that it is cancelling a request it previously issued.

    On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

    The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

    This notification indicates that the result will be unused, so any associated processing SHOULD cease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/cancelled"] = Field(default=..., description="""The method's name, always `notifications/cancelled`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/cancelled'} })
    params: McpCancelledNotificationParams = Field(default=..., description="""Parameters for a `notifications/cancelled` notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpLoggingMessageNotification(McpJSONRPCNotification):
    """
    JSONRPCNotification of a log message passed from server to client. The client opts in by setting `\"io.modelcontextprotocol/logLevel\"` in a request's `_meta`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:LoggingMessageNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_message']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/message"] = Field(default=..., description="""The method's name, always `notifications/message`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/message'} })
    params: McpLoggingMessageNotificationParams = Field(default=..., description="""Parameters for a `notifications/message` notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpNotificationMetaObject(McpMetaObject):
    """
    Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:NotificationMetaObject'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    mcp_subscription_id: Optional[Union[int, str]] = Field(default=None, description="""Identifies the subscription stream a notification was delivered on. The
server MUST include this key on every notification delivered via a
{@link SubscriptionsListenRequestsubscriptions/listen} stream, so the
client can correlate the notification with the originating subscription.
The key is absent on notifications not delivered via a subscription
stream (e.g. progress notifications for an in-flight request), which is
why it is optional here.

The value is the JSON-RPC ID of the `subscriptions/listen` request that
opened the stream.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/subscriptionId'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpNotificationMetaObject',
                       'McpSubscriptionsListenResultMetaObject']} })


class McpNotificationParams(ConfiguredBaseModel):
    """
    Common params for any notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:NotificationParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    meta: Optional[McpNotificationMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })


class McpCancelledNotificationParams(McpNotificationParams):
    """
    Parameters for a `notifications/cancelled` notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CancelledNotificationParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_cancelled']})

    meta: Optional[McpNotificationMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    reason_text: Optional[str] = Field(default=None, description="""An optional string describing the reason for the cancellation. This MAY be logged or presented to the user.""", json_schema_extra = { "linkml_meta": {'aliases': ['reason'], 'domain_of': ['McpCancelledNotificationParams']} })
    requestId: Union[int, str] = Field(default=..., description="""The ID of the request to cancel.

This MUST correspond to the ID of a request the client previously issued.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCancelledNotificationParams']} })


class McpLoggingMessageNotificationParams(McpNotificationParams):
    """
    Parameters for a `notifications/message` notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:LoggingMessageNotificationParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_message']})

    meta: Optional[McpNotificationMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    data: Any = Field(default=..., description="""The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    level: McpLoggingLevel = Field(default=..., description="""The severity of this log message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpLoggingMessageNotificationParams']} })
    logger: Optional[str] = Field(default=None, description="""An optional name of the logger issuing this message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpLoggingMessageNotificationParams']} })


class McpNumberSchema(ConfiguredBaseModel):
    """
    MCP's `NumberSchema`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:NumberSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'A description of the field for '
                                                       'the user.',
                                        'name': 'description'},
                        'title': {'description': 'A title for the field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of the field for the user.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""A title for the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[float] = Field(default=None, description="""The value the field takes when the user gives none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    maximum: Optional[float] = Field(default=None, description="""The largest value the field accepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpNumberSchema']} })
    minimum: Optional[float] = Field(default=None, description="""The smallest value the field accepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpNumberSchema']} })
    kind: McpNumberSchemaType = Field(default=..., description="""The kind of value the field takes.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema']} })


class McpParseError(McpError):
    """
    A JSON-RPC error indicating that invalid JSON was received by the server. This error is returned when the server cannot parse the JSON text of a message.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ParseError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error type that occurred."""    , le=-32700, ge=-32700, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: Optional[Any] = Field(default=None, description="""Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpPrimitiveSchemaDefinition(ConfiguredBaseModel):
    """
    Restricted schema definitions that only allow primitive types
    without nested objects or arrays.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpStringSchema'},
                    {'is_a': 'McpNumberSchema'},
                    {'is_a': 'McpBooleanSchema'},
                    {'is_a': 'McpUntitledSingleSelectEnumSchema'},
                    {'is_a': 'McpTitledSingleSelectEnumSchema'},
                    {'is_a': 'McpUntitledMultiSelectEnumSchema'},
                    {'is_a': 'McpTitledMultiSelectEnumSchema'},
                    {'is_a': 'McpLegacyTitledEnumSchema'}],
         'exact_mappings': ['mcp_schema:PrimitiveSchemaDefinition'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    pass


class McpProgressNotification(McpJSONRPCNotification):
    """
    An out-of-band notification used to inform the receiver of a progress update for a long-running request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ProgressNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_progress']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/progress"] = Field(default=..., description="""The method's name, always `notifications/progress`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/progress'} })
    params: McpProgressNotificationParams = Field(default=..., description="""Parameters for a {@link ProgressNotificationnotifications/progress} notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpProgressNotificationParams(McpNotificationParams):
    """
    Parameters for a {@link ProgressNotificationnotifications/progress} notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ProgressNotificationParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_progress']})

    meta: Optional[McpNotificationMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    message: Optional[str] = Field(default=None, description="""An optional message describing the current progress.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })
    progress: float = Field(default=..., description="""The progress thus far. This should increase every time progress is made, even if the total is unknown.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpProgressNotificationParams']} })
    progressToken: Union[int, str] = Field(default=..., description="""The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpProgressNotificationParams', 'McpRequestMetaObject']} })
    total: Optional[float] = Field(default=None, description="""Total number of items to process (or total progress required), if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteResultCompletion', 'McpProgressNotificationParams']} })


class McpPrompt(McpIcons, McpBaseMetadata):
    """
    A prompt or prompt template that the server offers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Prompt'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_list'],
         'mixins': ['McpIcons'],
         'slot_usage': {'description': {'description': 'An optional description of '
                                                       'what this prompt provides',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""An optional description of what this prompt provides""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    arguments: Optional[list[McpPromptArgument]] = Field(default=None, description="""A list of arguments to use for templating the prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpCompleteRequestParamsContext',
                       'McpGetPromptRequestParams',
                       'McpPrompt']} })
    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })


class McpPromptArgument(McpBaseMetadata):
    """
    Describes an argument that a prompt can accept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PromptArgument'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_list'],
         'slot_usage': {'description': {'description': 'A human-readable description '
                                                       'of the argument.',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A human-readable description of the argument.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    required: Optional[bool] = Field(default=None, description="""Whether this argument must be provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpPromptArgument'], 'slot_uri': 'schema:valueRequired'} })


class McpPromptListChangedNotification(McpJSONRPCNotification):
    """
    An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `promptsListChanged` filter field.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PromptListChangedNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_prompts_list_changed']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/prompts/list_changed"] = Field(default=..., description="""The method's name, always `notifications/prompts/list_changed`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/prompts/list_changed'} })
    params: Optional[McpNotificationParams] = Field(default=None, description="""Common params for any notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpPromptMessage(ConfiguredBaseModel):
    """
    Describes a message returned as part of a prompt.

    This is similar to {@link SamplingMessage}, but also supports the embedding of
    resources from the MCP server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PromptMessage'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_get']})

    content: McpContentBlock = Field(default=..., description="""The content the message carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult',
                       'McpCreateMessageResult',
                       'McpElicitResult',
                       'McpPromptMessage',
                       'McpSamplingMessage',
                       'McpToolResultContent']} })
    role: McpRole = Field(default=..., description="""The sender or recipient of messages and data in a conversation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageResult',
                       'McpPromptMessage',
                       'McpSamplingMessage']} })


class McpPromptReference(McpBaseMetadata):
    """
    Identifies a prompt.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PromptReference'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete'],
         'slot_usage': {'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    kind: Literal["ref/prompt"] = Field(default=..., description="""The kind of object, always `ref/prompt`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'ref/prompt'} })


class McpReadResourceResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ReadResourceRequestresources/read} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ReadResourceResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_read']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: Union[McpInputRequiredResult, McpReadResourceResult] = Field(default=..., description="""What the request returned.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpInputRequiredResult'},
                    {'range': 'McpReadResourceResult'}],
         'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpRequest(ConfiguredBaseModel):
    """
    MCP's `Request`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Request'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    method: str = Field(default=..., description="""The name of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })
    params: Optional[McpJSONObject] = Field(default=None, description="""The parameters the message carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpJSONRPCRequest(McpRequest):
    """
    A request that expects a response.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:JSONRPCRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['json_rpc']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: str = Field(default=..., description="""The name of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })
    params: Optional[McpJSONObject] = Field(default=None, description="""The parameters the message carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpCallToolRequest(McpJSONRPCRequest):
    """
    Used by the client to invoke a tool provided by the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CallToolRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_call']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["tools/call"] = Field(default=..., description="""The method's name, always `tools/call`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'tools/call'} })
    params: McpCallToolRequestParams = Field(default=..., description="""Parameters for a `tools/call` request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpCompleteRequest(McpJSONRPCRequest):
    """
    A request from the client to the server, to ask for completion options.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["completion/complete"] = Field(default=..., description="""The method's name, always `completion/complete`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'completion/complete'} })
    params: McpCompleteRequestParams = Field(default=..., description="""Parameters for a `completion/complete` request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpDiscoverRequest(McpJSONRPCRequest):
    """
    A request from the client asking the server to advertise its supported
    protocol versions, capabilities, and other metadata. Servers **MUST**
    implement `server/discover`. Clients **MAY** call it but are not required
    to — version negotiation can also happen inline via per-request `_meta`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:DiscoverRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["server/discover"] = Field(default=..., description="""The method's name, always `server/discover`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'server/discover'} })
    params: McpRequestParams = Field(default=..., description="""Common params for any request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpGetPromptRequest(McpJSONRPCRequest):
    """
    Used by the client to get a prompt provided by the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:GetPromptRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_get']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["prompts/get"] = Field(default=..., description="""The method's name, always `prompts/get`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'prompts/get'} })
    params: McpGetPromptRequestParams = Field(default=..., description="""Parameters for a `prompts/get` request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpPaginatedRequest(McpJSONRPCRequest):
    """
    MCP's `PaginatedRequest`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PaginatedRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: str = Field(default=..., description="""The name of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })
    params: McpPaginatedRequestParams = Field(default=..., description="""Common params for paginated requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpListPromptsRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of prompts and prompt templates the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListPromptsRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["prompts/list"] = Field(default=..., description="""The method's name, always `prompts/list`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'prompts/list'} })
    params: McpPaginatedRequestParams = Field(default=..., description="""Common params for paginated requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpListResourceTemplatesRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of resource templates the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListResourceTemplatesRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_templates_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["resources/templates/list"] = Field(default=..., description="""The method's name, always `resources/templates/list`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'resources/templates/list'} })
    params: McpPaginatedRequestParams = Field(default=..., description="""Common params for paginated requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpListResourcesRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of resources the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListResourcesRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["resources/list"] = Field(default=..., description="""The method's name, always `resources/list`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'resources/list'} })
    params: McpPaginatedRequestParams = Field(default=..., description="""Common params for paginated requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpListToolsRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of tools the server has.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListToolsRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["tools/list"] = Field(default=..., description="""The method's name, always `tools/list`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'tools/list'} })
    params: McpPaginatedRequestParams = Field(default=..., description="""Common params for paginated requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpReadResourceRequest(McpJSONRPCRequest):
    """
    Sent from the client to the server, to read a specific resource URI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ReadResourceRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_read']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["resources/read"] = Field(default=..., description="""The method's name, always `resources/read`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'resources/read'} })
    params: McpReadResourceRequestParams = Field(default=..., description="""Parameters for a `resources/read` request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpRequestMetaObject(McpMetaObject):
    """
    Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:RequestMetaObject'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    mcp_client_capabilities: McpClientCapabilities = Field(default=..., description="""The client's capabilities for this specific request. Required.

Capabilities are declared per-request rather than once at initialization;
an empty object means the client supports no optional capabilities.
Servers MUST NOT infer capabilities from prior requests.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/clientCapabilities'],
         'domain_of': ['McpRequestMetaObject']} })
    mcp_client_info: Optional[McpImplementation] = Field(default=None, description="""Identifies the client software making the request. Clients SHOULD
include this field on every request unless specifically configured not
to do so.

The {@link Implementation} schema requires `name` and `version`; other
fields are optional.

The value is self-reported by the client and is not verified by the
protocol. It is intended for display, logging, and debugging. Servers
SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
security decisions.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/clientInfo'],
         'domain_of': ['McpRequestMetaObject']} })
    mcp_log_level: Optional[McpLoggingLevel] = Field(default=None, description="""The desired log level for this request. Optional.

If absent, the server MUST NOT send any {@link LoggingMessageNotificationnotifications/message}
notifications for this request. The client opts in to log messages by
explicitly setting a level. Replaces the former `logging/setLevel` RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/logLevel'],
         'domain_of': ['McpRequestMetaObject']} })
    mcp_protocol_version: str = Field(default=..., description="""The MCP Protocol Version being used for this request. Required.

For the HTTP transport, this value MUST match the `MCP-Protocol-Version`
header; otherwise the server MUST return a `400 Bad Request`. If the
server does not support the requested version, it MUST return an
{@link UnsupportedProtocolVersionError}.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/protocolVersion'],
         'domain_of': ['McpRequestMetaObject']} })
    progressToken: Optional[Union[int, str]] = Field(default=None, description="""If specified, the caller is requesting out-of-band progress notifications for this request (as represented by {@link ProgressNotificationnotifications/progress}). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpProgressNotificationParams', 'McpRequestMetaObject']} })


class McpRequestParams(ConfiguredBaseModel):
    """
    Common params for any request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:RequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })


class McpCompleteRequestParams(McpRequestParams):
    """
    Parameters for a `completion/complete` request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    argument: McpCompleteRequestParamsArgument = Field(default=..., description="""The argument's information""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteRequestParams']} })
    context_info: Optional[McpCompleteRequestParamsContext] = Field(default=None, description="""Additional, optional context for completions""", json_schema_extra = { "linkml_meta": {'aliases': ['context'],
         'domain_of': ['McpClientCapabilitiesSampling', 'McpCompleteRequestParams']} })
    ref: Union[McpPromptReference, McpResourceTemplateReference] = Field(default=..., description="""What the completion is for: a prompt or a resource template.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpPromptReference'},
                    {'range': 'McpResourceTemplateReference'}],
         'domain_of': ['McpCompleteRequestParams']} })


class McpInputResponseRequestParams(McpRequestParams):
    """
    MCP's `InputResponseRequestParams`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:InputResponseRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    inputResponses: Optional[McpInputResponses] = Field(default=None, description="""A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })
    requestState: Optional[str] = Field(default=None, description="""State the server handed out with an input-required result, sent back unchanged when the request is retried.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })


class McpCallToolRequestParams(McpInputResponseRequestParams):
    """
    Parameters for a `tools/call` request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CallToolRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_call'],
         'slot_usage': {'name': {'description': 'The name of the tool.',
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""The name of the tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    arguments: Optional[McpJSONObject] = Field(default=None, description="""Arguments to use for the tool call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpCompleteRequestParamsContext',
                       'McpGetPromptRequestParams',
                       'McpPrompt']} })
    inputResponses: Optional[McpInputResponses] = Field(default=None, description="""A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })
    requestState: Optional[str] = Field(default=None, description="""State the server handed out with an input-required result, sent back unchanged when the request is retried.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })


class McpGetPromptRequestParams(McpInputResponseRequestParams):
    """
    Parameters for a `prompts/get` request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:GetPromptRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_get'],
         'slot_usage': {'name': {'description': 'The name of the prompt or prompt '
                                                'template.',
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""The name of the prompt or prompt template.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    arguments: Optional[McpGetPromptRequestParamsArguments] = Field(default=None, description="""Arguments to use for templating the prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpCompleteRequestParamsContext',
                       'McpGetPromptRequestParams',
                       'McpPrompt']} })
    inputResponses: Optional[McpInputResponses] = Field(default=None, description="""A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })
    requestState: Optional[str] = Field(default=None, description="""State the server handed out with an input-required result, sent back unchanged when the request is retried.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })


class McpPaginatedRequestParams(McpRequestParams):
    """
    Common params for paginated requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PaginatedRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cursor: Optional[str] = Field(default=None, description="""An opaque token representing the current pagination position.
If provided, the server should return results starting after this cursor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpPaginatedRequestParams']} })


class McpResource(McpIcons, McpBaseMetadata):
    """
    A known resource that the server is capable of reading.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Resource'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_list'],
         'mixins': ['McpIcons'],
         'slot_usage': {'description': {'description': 'A description of what this '
                                                       'resource represents.\n'
                                                       '\n'
                                                       'This can be used by clients to '
                                                       "improve the LLM's "
                                                       'understanding of available '
                                                       'resources. It can be thought '
                                                       'of like a "hint" to the model.',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of what this resource represents.

This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a \"hint\" to the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of this resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    size: Optional[int] = Field(default=None, description="""The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

This can be used by Hosts to display file sizes and estimate context window usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpResource', 'McpResourceLink']} })
    uri: str = Field(default=..., description="""The URI of this resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpResourceContents(ConfiguredBaseModel):
    """
    The contents of a specific resource or sub-resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceContents'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of this resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    uri: str = Field(default=..., description="""The URI of this resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpBlobResourceContents(McpResourceContents):
    """
    MCP's `BlobResourceContents`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:BlobResourceContents'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    blob: str = Field(default=..., description="""A base64-encoded string representing the binary data of the item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of this resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    uri: str = Field(default=..., description="""The URI of this resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpResourceLink(McpResource):
    """
    A resource that the server is capable of reading, included in a prompt or tool call result.

    Note: resource links returned by tools are not guaranteed to appear in the results of {@link ListResourcesRequestresources/list} requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceLink'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content'],
         'slot_usage': {'description': {'description': 'A description of what this '
                                                       'resource represents.\n'
                                                       '\n'
                                                       'This can be used by clients to '
                                                       "improve the LLM's "
                                                       'understanding of available '
                                                       'resources. It can be thought '
                                                       'of like a "hint" to the model.',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of what this resource represents.

This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a \"hint\" to the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of this resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    size: Optional[int] = Field(default=None, description="""The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

This can be used by Hosts to display file sizes and estimate context window usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpResource', 'McpResourceLink']} })
    kind: Literal["resource_link"] = Field(default=..., description="""The kind of object, always `resource_link`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'resource_link'} })
    uri: str = Field(default=..., description="""The URI of this resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpResourceListChangedNotification(McpJSONRPCNotification):
    """
    An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `resourcesListChanged` filter field.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceListChangedNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_resources_list_changed']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/resources/list_changed"] = Field(default=..., description="""The method's name, always `notifications/resources/list_changed`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/resources/list_changed'} })
    params: Optional[McpNotificationParams] = Field(default=None, description="""Common params for any notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpResourceRequestParams(McpRequestParams):
    """
    Common params for resource-related requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    uri: str = Field(default=..., description="""The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpReadResourceRequestParams(McpResourceRequestParams, McpInputResponseRequestParams):
    """
    Parameters for a `resources/read` request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ReadResourceRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_read'],
         'mixins': ['McpInputResponseRequestParams']})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    inputResponses: Optional[McpInputResponses] = Field(default=None, description="""A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })
    requestState: Optional[str] = Field(default=None, description="""State the server handed out with an input-required result, sent back unchanged when the request is retried.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })
    uri: str = Field(default=..., description="""The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpResourceTemplate(McpIcons, McpBaseMetadata):
    """
    A template description for resources available on the server.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceTemplate'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_templates_list'],
         'mixins': ['McpIcons'],
         'slot_usage': {'description': {'description': 'A description of what this '
                                                       'template is for.\n'
                                                       '\n'
                                                       'This can be used by clients to '
                                                       "improve the LLM's "
                                                       'understanding of available '
                                                       'resources. It can be thought '
                                                       'of like a "hint" to the model.',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of what this template is for.

This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a \"hint\" to the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    uriTemplate: str = Field(default=..., description="""A URI template (according to RFC 6570) that can be used to construct resource URIs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpResourceTemplate']} })


class McpResourceTemplateReference(ConfiguredBaseModel):
    """
    A reference to a resource or resource template definition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceTemplateReference'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    kind: Literal["ref/resource"] = Field(default=..., description="""The kind of object, always `ref/resource`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'ref/resource'} })
    uri: str = Field(default=..., description="""The URI or URI template of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpResourceUpdatedNotification(McpJSONRPCNotification):
    """
    A notification from the server to the client, informing it that a resource has changed and may need to be read again. This is only sent for resources the client opted in to via the `resourceSubscriptions` field of a {@link SubscriptionsListenRequestsubscriptions/listen} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceUpdatedNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_resources_updated']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/resources/updated"] = Field(default=..., description="""The method's name, always `notifications/resources/updated`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/resources/updated'} })
    params: McpResourceUpdatedNotificationParams = Field(default=..., description="""Parameters for a `notifications/resources/updated` notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpResourceUpdatedNotificationParams(McpNotificationParams):
    """
    Parameters for a `notifications/resources/updated` notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResourceUpdatedNotificationParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_resources_updated']})

    meta: Optional[McpNotificationMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    uri: str = Field(default=..., description="""The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpResult(ConfiguredBaseModel):
    """
    Common result fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Result'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpCacheableResult(McpResult):
    """
    A result that supports a time-to-live (TTL) hint for client-side caching.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CacheableResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpCallToolResult(McpResult):
    """
    The result returned by the server for a {@link CallToolRequesttools/call} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CallToolResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_call']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    content: list[McpContentBlock] = Field(default=..., description="""A list of content objects that represent the unstructured result of the tool call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult',
                       'McpCreateMessageResult',
                       'McpElicitResult',
                       'McpPromptMessage',
                       'McpSamplingMessage',
                       'McpToolResultContent']} })
    isError: Optional[bool] = Field(default=None, description="""Whether the tool call ended in an error.

If not set, this is assumed to be false (the call was successful).

Any errors that originate from the tool SHOULD be reported inside the result
object, with `isError` set to true, _not_ as an MCP protocol-level error
response. Otherwise, the LLM would not be able to see that an error occurred
and self-correct.

However, any errors in _finding_ the tool, an error indicating that the
server does not support tool calls, or any other exceptional conditions,
should be reported as an MCP error response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult', 'McpToolResultContent']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    structuredContent: Optional[Any] = Field(default=None, description="""An optional JSON value that represents the structured result of the tool call.

This can be any JSON value (object, array, string, number, boolean, or null)
that conforms to the tool's outputSchema if one is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult', 'McpToolResultContent']} })


class McpCompleteResult(McpResult):
    """
    The result returned by the server for a {@link CompleteRequestcompletion/complete} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CompleteResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['completion_complete']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    completion: McpCompleteResultCompletion = Field(default=..., description="""The completion values and whether more are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCompleteResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpDiscoverResult(McpCacheableResult):
    """
    The result returned by the server for a {@link DiscoverRequestserver/discover} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:DiscoverResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    capabilities: McpServerCapabilities = Field(default=..., description="""The capabilities of the server.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpDiscoverResult']} })
    instructions: Optional[str] = Field(default=None, description="""Natural-language guidance describing the server and its features.

This can be used by clients to improve an LLM's understanding of
available tools (e.g., by including it in a system prompt). It should
focus on information that helps the model use the server effectively
and should not duplicate information already in tool descriptions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpDiscoverResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    supportedVersions: list[str] = Field(default=..., description="""MCP Protocol Versions this server supports. The client should choose a
version from this list for use in subsequent requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpDiscoverResult']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpEmptyResult(McpResult):
    """
    Common result fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:EmptyResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpClientResult(McpEmptyResult):
    """
    Common result fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ClientResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpGetPromptResult(McpResult):
    """
    The result returned by the server for a {@link GetPromptRequestprompts/get} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:GetPromptResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_get'],
         'slot_usage': {'description': {'description': 'An optional description for '
                                                       'the prompt.',
                                        'name': 'description'}}})

    description: Optional[str] = Field(default=None, description="""An optional description for the prompt.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    messages: list[McpPromptMessage] = Field(default=..., description="""Describes a message returned as part of a prompt.

This is similar to {@link SamplingMessage}, but also supports the embedding of
resources from the MCP server.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageRequestParams', 'McpGetPromptResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpInputRequiredResult(McpResult):
    """
    An InputRequiredResult sent by the server to indicate that additional input is needed
    before the request can be completed.

    At least one of `inputRequests` or `requestState` MUST be present.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'input_requests': {'name': 'input_requests',
                                                            'value_presence': 'PRESENT'}}},
                    {'slot_conditions': {'request_state': {'name': 'request_state',
                                                           'value_presence': 'PRESENT'}}}],
         'comments': ["MCP's description states this rule, which its schema.json does "
                      'not: At least one of `inputRequests` or `requestState` MUST be '
                      'present.'],
         'exact_mappings': ['mcp_schema:InputRequiredResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['multi_round_trip']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    inputRequests: Optional[McpInputRequests] = Field(default=None, description="""A map of server-initiated requests that the client must fulfill.
Keys are server-assigned identifiers; values are the request objects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpInputRequiredResult']} })
    requestState: Optional[str] = Field(default=None, description="""State for the client to send back unchanged when it retries the request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequestParams',
                       'McpGetPromptRequestParams',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpReadResourceRequestParams']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpPaginatedResult(McpResult):
    """
    MCP's `PaginatedResult`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:PaginatedResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpListPromptsResult(McpPaginatedResult, McpCacheableResult):
    """
    The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListPromptsResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['prompts_list'],
         'mixins': ['McpCacheableResult']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult']} })
    prompts: list[McpPrompt] = Field(default=..., description="""A prompt or prompt template that the server offers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult', 'McpServerCapabilities']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpListResourceTemplatesResult(McpPaginatedResult, McpCacheableResult):
    """
    The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListResourceTemplatesResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_templates_list'],
         'mixins': ['McpCacheableResult']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult']} })
    resourceTemplates: list[McpResourceTemplate] = Field(default=..., description="""A template description for resources available on the server.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListResourceTemplatesResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpListResourcesResult(McpPaginatedResult, McpCacheableResult):
    """
    The result returned by the server for a {@link ListResourcesRequestresources/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListResourcesResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_list'],
         'mixins': ['McpCacheableResult']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult']} })
    resources: list[McpResource] = Field(default=..., description="""A known resource that the server is capable of reading.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListResourcesResult', 'McpServerCapabilities']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpListToolsResult(McpPaginatedResult, McpCacheableResult):
    """
    The result returned by the server for a {@link ListToolsRequesttools/list} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ListToolsResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list'],
         'mixins': ['McpCacheableResult']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    nextCursor: Optional[str] = Field(default=None, description="""An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    tools: list[McpTool] = Field(default=..., description="""Definition for a tool the client can call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilitiesSampling',
                       'McpCreateMessageRequestParams',
                       'McpListToolsResult',
                       'McpServerCapabilities']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpReadResourceResult(McpCacheableResult):
    """
    The result returned by the server for a {@link ReadResourceRequestresources/read} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ReadResourceResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['resources_read']})

    meta: Optional[McpResultMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    cacheScope: McpCacheScope = Field(default=..., description="""Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `\"public\"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `\"private\"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })
    contents: list[Union[McpBlobResourceContents, McpTextResourceContents]] = Field(default=..., description="""The contents of the resource that was read.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpTextResourceContents'},
                    {'range': 'McpBlobResourceContents'}],
         'domain_of': ['McpReadResourceResult']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })
    ttlMs: int = Field(default=..., description="""A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpDiscoverResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpReadResourceResult']} })


class McpResultMetaObject(McpMetaObject):
    """
    Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ResultMetaObject'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['common_types']})

    mcp_server_info: Optional[McpImplementation] = Field(default=None, description="""Identifies the server software producing the response. Servers SHOULD
include this field on every response unless specifically configured not
to do so.

The {@link Implementation} schema requires `name` and `version`; other
fields are optional.

The value is self-reported by the server and is not verified by the
protocol. It is intended for display, logging, and debugging. Clients
SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
security decisions.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/serverInfo'],
         'domain_of': ['McpResultMetaObject', 'McpSubscriptionsListenResultMetaObject']} })


class McpRoot(ConfiguredBaseModel):
    """
    Represents a root directory or file that the server can operate on.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Root'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['roots_list'],
         'slot_usage': {'name': {'description': 'An optional name for the root. This '
                                                'can be used to provide a '
                                                'human-readable\n'
                                                'identifier for the root, which may be '
                                                'useful for display purposes or for\n'
                                                'referencing the root in other parts '
                                                'of the application.',
                                 'name': 'name'}}})

    name: Optional[str] = Field(default=None, description="""An optional name for the root. This can be used to provide a human-readable
identifier for the root, which may be useful for display purposes or for
referencing the root in other parts of the application.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    uri: str = Field(default=..., description="""The URI identifying the root. This *must* start with `file://` for now.
This restriction may be relaxed in future versions of the protocol to allow
other URI schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpSamplingMessage(ConfiguredBaseModel):
    """
    Describes a message issued to or received from an LLM API.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SamplingMessage'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    content: Union[McpAudioContent, McpImageContent, McpSamplingMessageContentBlock, McpTextContent, McpToolResultContent, McpToolUseContent] = Field(default=..., description="""The content the message carries.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpTextContent'},
                    {'range': 'McpImageContent'},
                    {'range': 'McpAudioContent'},
                    {'range': 'McpToolUseContent'},
                    {'range': 'McpToolResultContent'},
                    {'inlined_as_list': True,
                     'multivalued': True,
                     'range': 'McpSamplingMessageContentBlock'}],
         'domain_of': ['McpCallToolResult',
                       'McpCreateMessageResult',
                       'McpElicitResult',
                       'McpPromptMessage',
                       'McpSamplingMessage',
                       'McpToolResultContent']} })
    role: McpRole = Field(default=..., description="""The sender or recipient of messages and data in a conversation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageResult',
                       'McpPromptMessage',
                       'McpSamplingMessage']} })


class McpCreateMessageResult(McpSamplingMessage):
    """
    The result returned by the client for a {@link CreateMessageRequestsampling/createMessage} request.
    The client should inform the user before returning the sampled message, to allow them
    to inspect the response (human in the loop) and decide whether to allow the server to see it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:CreateMessageResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    content: Union[McpAudioContent, McpImageContent, McpSamplingMessageContentBlock, McpTextContent, McpToolResultContent, McpToolUseContent] = Field(default=..., description="""The content the message carries.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'McpTextContent'},
                    {'range': 'McpImageContent'},
                    {'range': 'McpAudioContent'},
                    {'range': 'McpToolUseContent'},
                    {'range': 'McpToolResultContent'},
                    {'inlined_as_list': True,
                     'multivalued': True,
                     'range': 'McpSamplingMessageContentBlock'}],
         'domain_of': ['McpCallToolResult',
                       'McpCreateMessageResult',
                       'McpElicitResult',
                       'McpPromptMessage',
                       'McpSamplingMessage',
                       'McpToolResultContent']} })
    model: str = Field(default=..., description="""The name of the model that generated the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageResult']} })
    role: McpRole = Field(default=..., description="""The sender or recipient of messages and data in a conversation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageResult',
                       'McpPromptMessage',
                       'McpSamplingMessage']} })
    stopReason: Optional[str] = Field(default=None, description="""The reason why sampling stopped, if known.

Standard values:
- `\"endTurn\"`: Natural end of the assistant's turn
- `\"stopSequence\"`: A stop sequence was encountered
- `\"maxTokens\"`: Maximum token limit was reached
- `\"toolUse\"`: The model wants to use one or more tools

This field is an open string to allow for provider-specific stop reasons.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCreateMessageResult']} })


class McpSamplingMessageContentBlock(ConfiguredBaseModel):
    """
    One of `TextContent`, `ImageContent`, `AudioContent`, `ToolUseContent`, `ToolResultContent`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpTextContent'},
                    {'is_a': 'McpImageContent'},
                    {'is_a': 'McpAudioContent'},
                    {'is_a': 'McpToolUseContent'},
                    {'is_a': 'McpToolResultContent'}],
         'exact_mappings': ['mcp_schema:SamplingMessageContentBlock'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    pass


class McpServerCapabilities(ConfiguredBaseModel):
    """
    Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ServerCapabilities'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    completions: Optional[McpJSONObject] = Field(default=None, description="""Present if the server supports argument autocompletion suggestions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpServerCapabilities']} })
    experimental: Optional[McpServerCapabilitiesExperimental] = Field(default=None, description="""Experimental, non-standard capabilities that the server supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities', 'McpServerCapabilities']} })
    extensions: Optional[McpServerCapabilitiesExtensions] = Field(default=None, description="""Optional MCP extensions that the server supports. Keys are extension identifiers
(e.g., \"io.modelcontextprotocol/tasks\"), and values are per-extension settings
objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilities', 'McpServerCapabilities']} })
    logging: Optional[McpJSONObject] = Field(default=None, description="""Present if the server supports sending log messages to the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpServerCapabilities']} })
    prompts: Optional[McpServerCapabilitiesPrompts] = Field(default=None, description="""Present if the server offers any prompt templates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListPromptsResult', 'McpServerCapabilities']} })
    resources: Optional[McpServerCapabilitiesResources] = Field(default=None, description="""Present if the server offers any resources to read.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpListResourcesResult', 'McpServerCapabilities']} })
    tools: Optional[McpServerCapabilitiesTools] = Field(default=None, description="""Present if the server offers any tools to call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpClientCapabilitiesSampling',
                       'McpCreateMessageRequestParams',
                       'McpListToolsResult',
                       'McpServerCapabilities']} })


class McpServerCapabilitiesExperimental(ConfiguredBaseModel):
    """
    Experimental, non-standard capabilities that the server supports.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ServerCapabilities/properties/experimental'],
         'extra_slots': {'range_expression': {'range': 'McpJSONObject'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    pass


class McpServerCapabilitiesExtensions(ConfiguredBaseModel):
    """
    Optional MCP extensions that the server supports. Keys are extension identifiers
    (e.g., \"io.modelcontextprotocol/tasks\"), and values are per-extension settings
    objects. An empty object indicates support with no settings.

    Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
    mandatory prefix.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ServerCapabilities/properties/extensions'],
         'extra_slots': {'range_expression': {'range': 'McpJSONObject'}},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    pass


class McpServerCapabilitiesPrompts(ConfiguredBaseModel):
    """
    Present if the server offers any prompt templates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ServerCapabilities/properties/prompts'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    listChanged: Optional[bool] = Field(default=None, description="""Whether this server supports notifications for changes to the prompt list.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpServerCapabilitiesPrompts',
                       'McpServerCapabilitiesResources',
                       'McpServerCapabilitiesTools']} })


class McpServerCapabilitiesResources(ConfiguredBaseModel):
    """
    Present if the server offers any resources to read.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ServerCapabilities/properties/resources'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    listChanged: Optional[bool] = Field(default=None, description="""Whether this server supports notifications for changes to the resource list.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpServerCapabilitiesPrompts',
                       'McpServerCapabilitiesResources',
                       'McpServerCapabilitiesTools']} })
    subscribe: Optional[bool] = Field(default=None, description="""Whether this server supports subscribing to resource updates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpServerCapabilitiesResources']} })


class McpServerCapabilitiesTools(ConfiguredBaseModel):
    """
    Present if the server offers any tools to call.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ServerCapabilities/properties/tools'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['server_discover']})

    listChanged: Optional[bool] = Field(default=None, description="""Whether this server supports notifications for changes to the tool list.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpServerCapabilitiesPrompts',
                       'McpServerCapabilitiesResources',
                       'McpServerCapabilitiesTools']} })


class McpServerNotification(ConfiguredBaseModel):
    """
    One of `CancelledNotification`, `ProgressNotification`, `ResourceListChangedNotification`, `SubscriptionsAcknowledgedNotification`, `ResourceUpdatedNotification`, `PromptListChangedNotification`, `ToolListChangedNotification`, `LoggingMessageNotification`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpCancelledNotification'},
                    {'is_a': 'McpProgressNotification'},
                    {'is_a': 'McpResourceListChangedNotification'},
                    {'is_a': 'McpSubscriptionsAcknowledgedNotification'},
                    {'is_a': 'McpResourceUpdatedNotification'},
                    {'is_a': 'McpPromptListChangedNotification'},
                    {'is_a': 'McpToolListChangedNotification'},
                    {'is_a': 'McpLoggingMessageNotification'}],
         'exact_mappings': ['mcp_schema:ServerNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpServerResult(ConfiguredBaseModel):
    """
    One of `Result`, `InputRequiredResult`, `DiscoverResult`, `ListResourcesResult`, `ListResourceTemplatesResult`, `ReadResourceResult`, `SubscriptionsListenResult`, `ListPromptsResult`, `GetPromptResult`, `ListToolsResult`, `CallToolResult`, `CompleteResult`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpResult'},
                    {'is_a': 'McpInputRequiredResult'},
                    {'is_a': 'McpDiscoverResult'},
                    {'is_a': 'McpListResourcesResult'},
                    {'is_a': 'McpListResourceTemplatesResult'},
                    {'is_a': 'McpReadResourceResult'},
                    {'is_a': 'McpSubscriptionsListenResult'},
                    {'is_a': 'McpListPromptsResult'},
                    {'is_a': 'McpGetPromptResult'},
                    {'is_a': 'McpListToolsResult'},
                    {'is_a': 'McpCallToolResult'},
                    {'is_a': 'McpCompleteResult'}],
         'exact_mappings': ['mcp_schema:ServerResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpSingleSelectEnumSchema(ConfiguredBaseModel):
    """
    One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'is_a': 'McpUntitledSingleSelectEnumSchema'},
                    {'is_a': 'McpTitledSingleSelectEnumSchema'}],
         'exact_mappings': ['mcp_schema:SingleSelectEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp'})

    pass


class McpStringSchema(ConfiguredBaseModel):
    """
    MCP's `StringSchema`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:StringSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'A description of the field for '
                                                       'the user.',
                                        'name': 'description'},
                        'title': {'description': 'A title for the field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A description of the field for the user.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""A title for the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[str] = Field(default=None, description="""The value the field takes when the user gives none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    format: Optional[McpStringSchemaFormat] = Field(default=None, description="""The format the string must have.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpStringSchema']} })
    maxLength: Optional[int] = Field(default=None, description="""The most characters the field accepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpStringSchema']} })
    minLength: Optional[int] = Field(default=None, description="""The fewest characters the field accepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpStringSchema']} })
    kind: Literal["string"] = Field(default=..., description="""The kind of object, always `string`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'string'} })


class McpSubscriptionFilter(ConfiguredBaseModel):
    """
    The set of notification types a client may opt in to on a
    {@link SubscriptionsListenRequestsubscriptions/listen} request.

    Each notification type is **opt-in**; the server **MUST NOT** send
    notification types the client has not explicitly requested here.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionFilter'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['subscriptions_listen']})

    promptsListChanged: Optional[bool] = Field(default=None, description="""If true, receive {@link PromptListChangedNotificationnotifications/prompts/list_changed}.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpSubscriptionFilter']} })
    resourceSubscriptions: Optional[list[str]] = Field(default=None, description="""Subscribe to {@link ResourceUpdatedNotificationnotifications/resources/updated} for these resource URIs.
Replaces the former `resources/subscribe` RPC.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpSubscriptionFilter']} })
    resourcesListChanged: Optional[bool] = Field(default=None, description="""If true, receive {@link ResourceListChangedNotificationnotifications/resources/list_changed}.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpSubscriptionFilter']} })
    toolsListChanged: Optional[bool] = Field(default=None, description="""If true, receive {@link ToolListChangedNotificationnotifications/tools/list_changed}.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpSubscriptionFilter']} })


class McpSubscriptionsAcknowledgedNotification(McpJSONRPCNotification):
    """
    Sent by the server to acknowledge that a
    {@link SubscriptionsListenRequestsubscriptions/listen} subscription has been
    established and to report which notification types it agreed to honor.

    This notification MUST be the first message the server sends carrying the
    subscription's ID in `io.modelcontextprotocol/subscriptionId`. The server MUST
    NOT send any notification on the subscription before acknowledging it. On
    stdio, where every subscription shares one channel, this ordering is defined
    per subscription ID and not per channel: messages belonging to other
    subscriptions MAY be interleaved before it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsAcknowledgedNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_subscriptions_acknowledged']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/subscriptions/acknowledged"] = Field(default=..., description="""The method's name, always `notifications/subscriptions/acknowledged`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/subscriptions/acknowledged'} })
    params: McpSubscriptionsAcknowledgedNotificationParams = Field(default=..., description="""Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpSubscriptionsAcknowledgedNotificationParams(McpNotificationParams):
    """
    Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsAcknowledgedNotificationParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_subscriptions_acknowledged']})

    meta: Optional[McpNotificationMetaObject] = Field(default=None, alias="_meta", description="""Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    notifications: McpSubscriptionFilter = Field(default=..., description="""The subset of requested notification types the server agreed to honor.
Only includes notification types the server actually supports; if the
client requested an unsupported type (e.g., `promptsListChanged` when
the server has no prompts), it is omitted from this set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams']} })


class McpSubscriptionsListenRequest(McpJSONRPCRequest):
    """
    Sent from the client to open a long-lived channel for receiving notifications
    outside the context of a specific request. Replaces the previous HTTP GET
    endpoint and ensures consistent behavior between HTTP and STDIO.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsListenRequest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['subscriptions_listen']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["subscriptions/listen"] = Field(default=..., description="""The method's name, always `subscriptions/listen`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'subscriptions/listen'} })
    params: McpSubscriptionsListenRequestParams = Field(default=..., description="""Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpSubscriptionsListenRequestParams(McpRequestParams):
    """
    Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsListenRequestParams'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['subscriptions_listen']})

    meta: McpRequestMetaObject = Field(default=..., alias="_meta", description="""Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    notifications: McpSubscriptionFilter = Field(default=..., description="""The notifications the client opts in to on this stream. The server
**MUST NOT** send notification types the client has not explicitly
requested.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams']} })


class McpSubscriptionsListenResult(McpResult):
    """
    The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
    request, signalling that the subscription has ended gracefully (for example,
    during server shutdown). Because the listen stream is long-lived, this result
    is sent only when the server tears the subscription down; an abrupt transport
    close carries no response. The result body is otherwise empty.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsListenResult'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['subscriptions_listen']})

    meta: McpSubscriptionsListenResultMetaObject = Field(default=..., alias="_meta", description="""Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
{@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    resultType: str = Field(default=..., description="""Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `\"complete\"`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCacheableResult',
                       'McpCallToolResult',
                       'McpCompleteResult',
                       'McpDiscoverResult',
                       'McpGetPromptResult',
                       'McpInputRequiredResult',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListToolsResult',
                       'McpPaginatedResult',
                       'McpReadResourceResult',
                       'McpResult',
                       'McpSubscriptionsListenResult']} })


class McpSubscriptionsListenResultMetaObject(McpResultMetaObject):
    """
    Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
    {@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsListenResultMetaObject'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['subscriptions_listen']})

    mcp_server_info: Optional[McpImplementation] = Field(default=None, description="""Identifies the server software producing the response. Servers SHOULD
include this field on every response unless specifically configured not
to do so.

The {@link Implementation} schema requires `name` and `version`; other
fields are optional.

The value is self-reported by the server and is not verified by the
protocol. It is intended for display, logging, and debugging. Clients
SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
security decisions.""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/serverInfo'],
         'domain_of': ['McpResultMetaObject', 'McpSubscriptionsListenResultMetaObject']} })
    mcp_subscription_id: Union[int, str] = Field(default=..., description="""Identifies the subscription stream this response closes, so the client can
correlate it with the originating subscription — mirroring the same key on
the stream's notifications. The value is the JSON-RPC ID of the
`subscriptions/listen` request that opened the stream (and equals this
response's `id`).""", json_schema_extra = { "linkml_meta": {'aliases': ['io.modelcontextprotocol/subscriptionId'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpNotificationMetaObject',
                       'McpSubscriptionsListenResultMetaObject']} })


class McpSubscriptionsListenResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link SubscriptionsListenRequestsubscriptions/listen}
    request, sent when the server tears the subscription down gracefully.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:SubscriptionsListenResultResponse'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['subscriptions_listen']})

    identifier: Union[int, str] = Field(default=..., description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    result: McpSubscriptionsListenResult = Field(default=..., description="""The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
request, signalling that the subscription has ended gracefully (for example,
during server shutdown). Because the listen stream is long-lived, this result
is sent only when the server tears the subscription down; an abrupt transport
close carries no response. The result body is otherwise empty.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResultResponse',
                       'McpCompleteResultResponse',
                       'McpDiscoverResultResponse',
                       'McpGetPromptResultResponse',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesResultResponse',
                       'McpListToolsResultResponse',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenResultResponse']} })


class McpTextContent(ConfiguredBaseModel):
    """
    Text provided to or from an LLM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TextContent'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpAnnotations] = Field(default=None, description="""Optional annotations for the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    text: str = Field(default=..., description="""The text content of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTextContent', 'McpTextResourceContents']} })
    kind: Literal["text"] = Field(default=..., description="""The kind of object, always `text`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'text'} })


class McpTextResourceContents(McpResourceContents):
    """
    MCP's `TextResourceContents`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TextResourceContents'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['content']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    mimeType: Optional[str] = Field(default=None, description="""The MIME type of this resource, if known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpIcon',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextResourceContents']} })
    text: str = Field(default=..., description="""The text of the item. This must only be set if the item can actually be represented as text (not binary data).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTextContent', 'McpTextResourceContents']} })
    uri: str = Field(default=..., description="""The URI of this resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBlobResourceContents',
                       'McpReadResourceRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplateReference',
                       'McpResourceUpdatedNotificationParams',
                       'McpRoot',
                       'McpTextResourceContents']} })


class McpTitledMultiSelectEnumSchema(ConfiguredBaseModel):
    """
    Schema for multiple-selection enumeration with display titles for each option.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TitledMultiSelectEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'Optional description for the '
                                                       'enum field.',
                                        'name': 'description'},
                        'title': {'description': 'Optional title for the enum field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""Optional description for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""Optional title for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[list[str]] = Field(default=None, description="""Optional default value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    items: McpTitledMultiSelectEnumSchemaItems = Field(default=..., description="""Schema for array items with enum options and display labels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema']} })
    maxItems: Optional[int] = Field(default=None, description="""Maximum number of items to select.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema']} })
    minItems: Optional[int] = Field(default=None, description="""Minimum number of items to select.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema']} })
    kind: Literal["array"] = Field(default=..., description="""The kind of object, always `array`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'array'} })


class McpTitledMultiSelectEnumSchemaItems(ConfiguredBaseModel):
    """
    Schema for array items with enum options and display labels.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TitledMultiSelectEnumSchema/properties/items'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    anyOf: list[McpTitledMultiSelectEnumSchemaItemsAnyOf] = Field(default=..., description="""Array of enum options with values and display labels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchemaItems']} })


class McpTitledMultiSelectEnumSchemaItemsAnyOf(ConfiguredBaseModel):
    """
    The object MCP's `TitledMultiSelectEnumSchema` holds under `anyOf`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TitledMultiSelectEnumSchema/properties/items/properties/anyOf/items'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'title': {'description': 'Display title for this option.',
                                  'name': 'title',
                                  'required': True}}})

    title: str = Field(default=..., description="""Display title for this option.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    const: str = Field(default=..., description="""The constant enum value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchemaOneOf']} })


class McpTitledSingleSelectEnumSchema(ConfiguredBaseModel):
    """
    Schema for single-selection enumeration with display titles for each option.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TitledSingleSelectEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'Optional description for the '
                                                       'enum field.',
                                        'name': 'description'},
                        'title': {'description': 'Optional title for the enum field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""Optional description for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""Optional title for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[str] = Field(default=None, description="""Optional default value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    oneOf: list[McpTitledSingleSelectEnumSchemaOneOf] = Field(default=..., description="""Array of enum options with values and display labels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledSingleSelectEnumSchema']} })
    kind: Literal["string"] = Field(default=..., description="""The kind of object, always `string`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'string'} })


class McpTitledSingleSelectEnumSchemaOneOf(ConfiguredBaseModel):
    """
    The object MCP's `TitledSingleSelectEnumSchema` holds under `oneOf`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:TitledSingleSelectEnumSchema/properties/oneOf/items'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'title': {'description': 'Display label for this option.',
                                  'name': 'title',
                                  'required': True}}})

    title: str = Field(default=..., description="""Display label for this option.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    const: str = Field(default=..., description="""The enum value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchemaOneOf']} })


class McpTool(McpIcons, McpBaseMetadata):
    """
    Definition for a tool the client can call.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Tool'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list'],
         'mixins': ['McpIcons'],
         'slot_usage': {'description': {'description': 'A human-readable description '
                                                       'of the tool.\n'
                                                       '\n'
                                                       'This can be used by clients to '
                                                       "improve the LLM's "
                                                       'understanding of available '
                                                       'tools. It can be thought of '
                                                       'like a "hint" to the model.',
                                        'name': 'description'},
                        'name': {'description': 'Intended for programmatic or logical '
                                                'use, but used as a display name in '
                                                'past specs or fallback (if title '
                                                "isn't present).",
                                 'name': 'name',
                                 'required': True},
                        'title': {'description': 'Intended for UI and end-user '
                                                 'contexts — optimized to be '
                                                 'human-readable and easily '
                                                 'understood,\n'
                                                 'even by those unfamiliar with '
                                                 'domain-specific terminology.\n'
                                                 '\n'
                                                 'If not provided, the name should be '
                                                 'used for display (except for {@link '
                                                 'Tool},\n'
                                                 'where `annotations.title` should be '
                                                 'given precedence over using `name`,\n'
                                                 'if present).',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""A human-readable description of the tool.

This can be used by clients to improve the LLM's understanding of available tools. It can be thought of like a \"hint\" to the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    name: str = Field(default=..., description="""Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    title: Optional[str] = Field(default=None, description="""Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    annotations: Optional[McpToolAnnotations] = Field(default=None, description="""Optional additional tool information.

Display name precedence order is: `title`, `annotations.title`, then `name`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTextContent',
                       'McpTool']} })
    icons: Optional[list[McpIcon]] = Field(default=None, description="""Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpIcons',
                       'McpImplementation',
                       'McpPrompt',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpTool']} })
    inputSchema: McpToolInputSchema = Field(default=..., description="""A JSON Schema object defining the expected parameters for the tool.

Tool arguments are always JSON objects, so `type: \"object\"` is required at the root.
Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — including
composition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords
(`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any other
standard validation or annotation keywords.

Property schemas may carry an `x-mcp-header` annotation to mirror the
argument value into an HTTP header on the Streamable HTTP transport. See
the Streamable HTTP transport specification for the validity and
extraction rules.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTool']} })
    outputSchema: Optional[McpToolOutputSchema] = Field(default=None, description="""An optional JSON Schema object defining the structure of the tool's output returned in
the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTool']} })


class McpToolAnnotations(ConfiguredBaseModel):
    """
    Additional properties describing a {@link Tool} to clients.

    NOTE: all properties in `ToolAnnotations` are **hints**.
    They are not guaranteed to provide a faithful description of
    tool behavior (including descriptive properties like `title`).

    Clients should never make tool use decisions based on `ToolAnnotations`
    received from untrusted servers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ToolAnnotations'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list'],
         'slot_usage': {'title': {'description': 'A human-readable title for the tool.',
                                  'name': 'title'}}})

    title: Optional[str] = Field(default=None, description="""A human-readable title for the tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    destructiveHint: Optional[bool] = Field(default=None, description="""If true, the tool may perform destructive updates to its environment.
If false, the tool performs only additive updates.

(This property is meaningful only when `readOnlyHint == false`)

Default: true""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpToolAnnotations']} })
    idempotentHint: Optional[bool] = Field(default=None, description="""If true, calling the tool repeatedly with the same arguments
will have no additional effect on its environment.

(This property is meaningful only when `readOnlyHint == false`)

Default: false""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpToolAnnotations']} })
    openWorldHint: Optional[bool] = Field(default=None, description="""If true, this tool may interact with an \"open world\" of external
entities. If false, the tool's domain of interaction is closed.
For example, the world of a web search tool is open, whereas that
of a memory tool is not.

Default: true""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpToolAnnotations']} })
    readOnlyHint: Optional[bool] = Field(default=None, description="""If true, the tool does not modify its environment.

Default: false""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpToolAnnotations']} })


class McpToolChoice(ConfiguredBaseModel):
    """
    Controls tool selection behavior for sampling requests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ToolChoice'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    mode: Optional[McpToolChoiceMode] = Field(default=None, description="""Controls the tool use ability of the model:
- `\"auto\"`: Model decides whether to use tools (default)
- `\"required\"`: Model MUST use at least one tool before completing
- `\"none\"`: Model MUST NOT use any tools""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpToolChoice']} })


class McpToolInputSchema(ConfiguredBaseModel):
    """
    A JSON Schema object defining the expected parameters for the tool.

    Tool arguments are always JSON objects, so `type: \"object\"` is required at the root.
    Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — including
    composition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords
    (`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any other
    standard validation or annotation keywords.

    Property schemas may carry an `x-mcp-header` annotation to mirror the
    argument value into an HTTP header on the Streamable HTTP transport. See
    the Streamable HTTP transport specification for the validity and
    extraction rules.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Tool/properties/inputSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list']})

    schema_dialect: Optional[str] = Field(default=None, description="""The JSON Schema dialect the schema is written in.""", json_schema_extra = { "linkml_meta": {'aliases': ['$schema'],
         'domain_of': ['McpElicitRequestFormParamsRequestedSchema',
                       'McpToolInputSchema',
                       'McpToolOutputSchema']} })
    kind: Literal["object"] = Field(default=..., description="""The kind of object, always `object`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'object'} })


class McpToolListChangedNotification(McpJSONRPCNotification):
    """
    An optional notification from the server to the client, informing it that the list of tools it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `toolsListChanged` filter field.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ToolListChangedNotification'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['notifications_tools_list_changed']})

    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })
    method: Literal["notifications/tools/list_changed"] = Field(default=..., description="""The method's name, always `notifications/tools/list_changed`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification'],
         'equals_string': 'notifications/tools/list_changed'} })
    params: Optional[McpNotificationParams] = Field(default=None, description="""Common params for any notification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCreateMessageRequest',
                       'McpDiscoverRequest',
                       'McpElicitRequest',
                       'McpGetPromptRequest',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpListPromptsRequest',
                       'McpListResourceTemplatesRequest',
                       'McpListResourcesRequest',
                       'McpListRootsRequest',
                       'McpListToolsRequest',
                       'McpLoggingMessageNotification',
                       'McpNotification',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpRequest',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpToolListChangedNotification']} })


class McpToolOutputSchema(ConfiguredBaseModel):
    """
    An optional JSON Schema object defining the structure of the tool's output returned in
    the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:Tool/properties/outputSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['tools_list']})

    schema_dialect: Optional[str] = Field(default=None, description="""The JSON Schema dialect the schema is written in.""", json_schema_extra = { "linkml_meta": {'aliases': ['$schema'],
         'domain_of': ['McpElicitRequestFormParamsRequestedSchema',
                       'McpToolInputSchema',
                       'McpToolOutputSchema']} })


class McpToolResultContent(ConfiguredBaseModel):
    """
    The result of a tool use, provided by the user back to the assistant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ToolResultContent'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage']})

    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Optional metadata about the tool result. Clients SHOULD preserve this field when
including tool results in subsequent sampling requests to enable caching optimizations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    content: list[McpContentBlock] = Field(default=..., description="""The unstructured result content of the tool use.

This has the same format as {@link CallToolResult.content} and can include text, images,
audio, resource links, and embedded resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult',
                       'McpCreateMessageResult',
                       'McpElicitResult',
                       'McpPromptMessage',
                       'McpSamplingMessage',
                       'McpToolResultContent']} })
    isError: Optional[bool] = Field(default=None, description="""Whether the tool use resulted in an error.

If true, the content typically describes the error that occurred.
Default: false""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult', 'McpToolResultContent']} })
    structuredContent: Optional[Any] = Field(default=None, description="""An optional structured result value.

This can be any JSON value (object, array, string, number, boolean, or null).
If the tool defined an {@link Tool.outputSchema}, this SHOULD conform to that schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolResult', 'McpToolResultContent']} })
    toolUseId: str = Field(default=..., description="""The ID of the tool use this result corresponds to.

This MUST match the ID from a previous {@link ToolUseContent}.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpToolResultContent']} })
    kind: Literal["tool_result"] = Field(default=..., description="""The kind of object, always `tool_result`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'tool_result'} })


class McpToolUseContent(ConfiguredBaseModel):
    """
    A request from the assistant to call a tool.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:ToolUseContent'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['sampling_createmessage'],
         'slot_usage': {'name': {'description': 'The name of the tool to call.',
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""The name of the tool to call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpCallToolRequestParams',
                       'McpCompleteRequestParamsArgument',
                       'McpGetPromptRequestParams',
                       'McpImplementation',
                       'McpModelHint',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpRoot',
                       'McpTool',
                       'McpToolUseContent'],
         'slot_uri': 'schema:name'} })
    meta: Optional[McpMetaObject] = Field(default=None, alias="_meta", description="""Optional metadata about the tool use. Clients SHOULD preserve this field when
including tool uses in subsequent sampling requests to enable caching optimizations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpBlobResourceContents',
                       'McpCacheableResult',
                       'McpCallToolRequestParams',
                       'McpCallToolResult',
                       'McpCancelledNotificationParams',
                       'McpCompleteRequestParams',
                       'McpCompleteResult',
                       'McpCreateMessageResult',
                       'McpDiscoverResult',
                       'McpEmbeddedResource',
                       'McpGetPromptRequestParams',
                       'McpGetPromptResult',
                       'McpImageContent',
                       'McpInputRequiredResult',
                       'McpInputResponseRequestParams',
                       'McpListPromptsResult',
                       'McpListResourceTemplatesResult',
                       'McpListResourcesResult',
                       'McpListRootsRequestParams',
                       'McpListToolsResult',
                       'McpLoggingMessageNotificationParams',
                       'McpNotificationParams',
                       'McpPaginatedRequestParams',
                       'McpPaginatedResult',
                       'McpProgressNotificationParams',
                       'McpPrompt',
                       'McpReadResourceRequestParams',
                       'McpReadResourceResult',
                       'McpRequestParams',
                       'McpResource',
                       'McpResourceContents',
                       'McpResourceLink',
                       'McpResourceRequestParams',
                       'McpResourceTemplate',
                       'McpResourceUpdatedNotificationParams',
                       'McpResult',
                       'McpRoot',
                       'McpSamplingMessage',
                       'McpSubscriptionsAcknowledgedNotificationParams',
                       'McpSubscriptionsListenRequestParams',
                       'McpSubscriptionsListenResult',
                       'McpTextContent',
                       'McpTextResourceContents',
                       'McpTool',
                       'McpToolResultContent',
                       'McpToolUseContent']} })
    identifier: str = Field(default=..., description="""A unique identifier for this tool use.

This ID is used to match tool results to their corresponding tool uses.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    input: McpJSONObject = Field(default=..., description="""The arguments to pass to the tool, conforming to the tool's input schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpToolUseContent']} })
    kind: Literal["tool_use"] = Field(default=..., description="""The kind of object, always `tool_use`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'tool_use'} })


class McpUnsupportedProtocolVersionError(McpJSONRPCErrorResponse):
    """
    Returned when the request's protocol version is unknown to the server or
    unsupported (e.g., a known experimental or draft version the server has
    chosen not to implement). For HTTP, the response status code MUST be
    `400 Bad Request`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:UnsupportedProtocolVersionError'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    error: McpUnsupportedProtocolVersionErrorError = Field(default=..., description="""The error the request ended with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpUnsupportedProtocolVersionError']} })
    identifier: Optional[Union[int, str]] = Field(default=None, description="""A uniquely identifying ID for a request in JSON-RPC.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'any_of': [{'range': 'string'}, {'range': 'integer'}],
         'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolUseContent',
                       'McpUnsupportedProtocolVersionError']} })
    jsonrpc: Literal["2.0"] = Field(default=..., description="""The JSON-RPC version, always `2.0`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpCallToolRequest',
                       'McpCallToolResultResponse',
                       'McpCancelledNotification',
                       'McpClientNotification',
                       'McpCompleteRequest',
                       'McpCompleteResultResponse',
                       'McpDiscoverRequest',
                       'McpDiscoverResultResponse',
                       'McpGetPromptRequest',
                       'McpGetPromptResultResponse',
                       'McpHeaderMismatchError',
                       'McpJSONRPCErrorResponse',
                       'McpJSONRPCNotification',
                       'McpJSONRPCRequest',
                       'McpJSONRPCResultResponse',
                       'McpListPromptsRequest',
                       'McpListPromptsResultResponse',
                       'McpListResourceTemplatesRequest',
                       'McpListResourceTemplatesResultResponse',
                       'McpListResourcesRequest',
                       'McpListResourcesResultResponse',
                       'McpListToolsRequest',
                       'McpListToolsResultResponse',
                       'McpLoggingMessageNotification',
                       'McpMissingRequiredClientCapabilityError',
                       'McpPaginatedRequest',
                       'McpProgressNotification',
                       'McpPromptListChangedNotification',
                       'McpReadResourceRequest',
                       'McpReadResourceResultResponse',
                       'McpResourceListChangedNotification',
                       'McpResourceUpdatedNotification',
                       'McpSubscriptionsAcknowledgedNotification',
                       'McpSubscriptionsListenRequest',
                       'McpSubscriptionsListenResultResponse',
                       'McpToolListChangedNotification',
                       'McpUnsupportedProtocolVersionError'],
         'equals_string': '2.0'} })


class McpUnsupportedProtocolVersionErrorError(McpError):
    """
    MCP's `Error`, with the code and data this error carries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:UnsupportedProtocolVersionError/properties/error/allOf/1'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    code: int = Field(default=..., description="""The error code, always `-32022`."""    , le=-32022, ge=-32022, json_schema_extra = { "linkml_meta": {'domain_of': ['McpError',
                       'McpHeaderMismatchErrorError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    data: McpUnsupportedProtocolVersionErrorErrorData = Field(default=..., description="""Details of the error.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpAudioContent',
                       'McpError',
                       'McpImageContent',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpLoggingMessageNotificationParams',
                       'McpMethodNotFoundError',
                       'McpMissingRequiredClientCapabilityErrorError',
                       'McpParseError',
                       'McpUnsupportedProtocolVersionErrorError']} })
    message: str = Field(default=..., description="""A short description of the error. The message SHOULD be limited to a concise single sentence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpElicitRequestFormParams',
                       'McpElicitRequestURLParams',
                       'McpError',
                       'McpInternalError',
                       'McpInvalidParamsError',
                       'McpInvalidRequestError',
                       'McpMethodNotFoundError',
                       'McpParseError',
                       'McpProgressNotificationParams']} })


class McpUnsupportedProtocolVersionErrorErrorData(ConfiguredBaseModel):
    """
    The object MCP's `UnsupportedProtocolVersionError` holds under `data`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:UnsupportedProtocolVersionError/properties/error/allOf/1/properties/data'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['errors']})

    requested: str = Field(default=..., description="""The protocol version that was requested by the client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpUnsupportedProtocolVersionErrorErrorData']} })
    supported: list[str] = Field(default=..., description="""Protocol versions the server supports. The client should choose a
mutually supported version from this list and retry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpUnsupportedProtocolVersionErrorErrorData']} })


class McpUntitledMultiSelectEnumSchema(ConfiguredBaseModel):
    """
    Schema for multiple-selection enumeration without display titles for options.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:UntitledMultiSelectEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'Optional description for the '
                                                       'enum field.',
                                        'name': 'description'},
                        'title': {'description': 'Optional title for the enum field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""Optional description for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""Optional title for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[list[str]] = Field(default=None, description="""Optional default value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    items: McpUntitledMultiSelectEnumSchemaItems = Field(default=..., description="""Schema for the array items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema']} })
    maxItems: Optional[int] = Field(default=None, description="""Maximum number of items to select.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema']} })
    minItems: Optional[int] = Field(default=None, description="""Minimum number of items to select.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpTitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema']} })
    kind: Literal["array"] = Field(default=..., description="""The kind of object, always `array`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'array'} })


class McpUntitledMultiSelectEnumSchemaItems(ConfiguredBaseModel):
    """
    Schema for the array items.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:UntitledMultiSelectEnumSchema/properties/items'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create']})

    enum: list[str] = Field(default=..., description="""Array of enum values to choose from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpLegacyTitledEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema']} })
    kind: Literal["string"] = Field(default=..., description="""The kind of object, always `string`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'string'} })


class McpUntitledSingleSelectEnumSchema(ConfiguredBaseModel):
    """
    Schema for single-selection enumeration without display titles for options.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['mcp_schema:UntitledSingleSelectEnumSchema'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/mcp',
         'in_subset': ['elicitation_create'],
         'slot_usage': {'description': {'description': 'Optional description for the '
                                                       'enum field.',
                                        'name': 'description'},
                        'title': {'description': 'Optional title for the enum field.',
                                  'name': 'title'}}})

    description: Optional[str] = Field(default=None, description="""Optional description for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpGetPromptResult',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTool',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:description'} })
    title: Optional[str] = Field(default=None, description="""Optional title for the enum field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBaseMetadata',
                       'McpBooleanSchema',
                       'McpImplementation',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPrompt',
                       'McpPromptArgument',
                       'McpPromptReference',
                       'McpResource',
                       'McpResourceLink',
                       'McpResourceTemplate',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledMultiSelectEnumSchemaItemsAnyOf',
                       'McpTitledSingleSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchemaOneOf',
                       'McpTool',
                       'McpToolAnnotations',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema'],
         'slot_uri': 'schema:name'} })
    default: Optional[str] = Field(default=None, description="""Optional default value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpBooleanSchema',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpStringSchema',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledSingleSelectEnumSchema']} })
    enum: list[str] = Field(default=..., description="""Array of enum values to choose from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['McpLegacyTitledEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema']} })
    kind: Literal["string"] = Field(default=..., description="""The kind of object, always `string`.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['McpAudioContent',
                       'McpBooleanSchema',
                       'McpElicitRequestFormParamsRequestedSchema',
                       'McpEmbeddedResource',
                       'McpImageContent',
                       'McpLegacyTitledEnumSchema',
                       'McpNumberSchema',
                       'McpPromptReference',
                       'McpResourceLink',
                       'McpResourceTemplateReference',
                       'McpStringSchema',
                       'McpTextContent',
                       'McpTitledMultiSelectEnumSchema',
                       'McpTitledSingleSelectEnumSchema',
                       'McpToolInputSchema',
                       'McpToolResultContent',
                       'McpToolUseContent',
                       'McpUntitledMultiSelectEnumSchema',
                       'McpUntitledMultiSelectEnumSchemaItems',
                       'McpUntitledSingleSelectEnumSchema'],
         'equals_string': 'string'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
McpAnnotations.model_rebuild()
McpAudioContent.model_rebuild()
McpBaseMetadata.model_rebuild()
McpBooleanSchema.model_rebuild()
McpClientCapabilities.model_rebuild()
McpClientCapabilitiesElicitation.model_rebuild()
McpClientCapabilitiesExperimental.model_rebuild()
McpClientCapabilitiesExtensions.model_rebuild()
McpClientCapabilitiesRoots.model_rebuild()
McpClientCapabilitiesSampling.model_rebuild()
McpClientRequest.model_rebuild()
McpCompleteRequestParamsArgument.model_rebuild()
McpCompleteRequestParamsContext.model_rebuild()
McpCompleteRequestParamsContextArguments.model_rebuild()
McpCompleteResultCompletion.model_rebuild()
McpContentBlock.model_rebuild()
McpCreateMessageRequest.model_rebuild()
McpCreateMessageRequestParams.model_rebuild()
McpElicitRequest.model_rebuild()
McpElicitRequestFormParams.model_rebuild()
McpElicitRequestFormParamsRequestedSchema.model_rebuild()
McpElicitRequestFormParamsRequestedSchemaProperties.model_rebuild()
McpElicitRequestParams.model_rebuild()
McpElicitRequestURLParams.model_rebuild()
McpElicitResult.model_rebuild()
McpElicitResultContent.model_rebuild()
McpEmbeddedResource.model_rebuild()
McpEnumSchema.model_rebuild()
McpError.model_rebuild()
McpGetPromptRequestParamsArguments.model_rebuild()
McpHeaderMismatchErrorError.model_rebuild()
McpIcon.model_rebuild()
McpIcons.model_rebuild()
McpImageContent.model_rebuild()
McpImplementation.model_rebuild()
McpInputRequest.model_rebuild()
McpInputRequests.model_rebuild()
McpInputResponse.model_rebuild()
McpInputResponses.model_rebuild()
McpInternalError.model_rebuild()
McpInvalidParamsError.model_rebuild()
McpInvalidRequestError.model_rebuild()
McpJSONObject.model_rebuild()
McpJSONRPCErrorResponse.model_rebuild()
McpHeaderMismatchError.model_rebuild()
McpJSONRPCMessage.model_rebuild()
McpJSONRPCResponse.model_rebuild()
McpJSONRPCResultResponse.model_rebuild()
McpCallToolResultResponse.model_rebuild()
McpCompleteResultResponse.model_rebuild()
McpDiscoverResultResponse.model_rebuild()
McpGetPromptResultResponse.model_rebuild()
McpLegacyTitledEnumSchema.model_rebuild()
McpListPromptsResultResponse.model_rebuild()
McpListResourceTemplatesResultResponse.model_rebuild()
McpListResourcesResultResponse.model_rebuild()
McpListRootsRequest.model_rebuild()
McpListRootsRequestParams.model_rebuild()
McpListRootsResult.model_rebuild()
McpListToolsResultResponse.model_rebuild()
McpMetaObject.model_rebuild()
McpMethodNotFoundError.model_rebuild()
McpMissingRequiredClientCapabilityError.model_rebuild()
McpMissingRequiredClientCapabilityErrorError.model_rebuild()
McpMissingRequiredClientCapabilityErrorErrorData.model_rebuild()
McpModelHint.model_rebuild()
McpModelPreferences.model_rebuild()
McpMultiSelectEnumSchema.model_rebuild()
McpNotification.model_rebuild()
McpJSONRPCNotification.model_rebuild()
McpCancelledNotification.model_rebuild()
McpClientNotification.model_rebuild()
McpLoggingMessageNotification.model_rebuild()
McpNotificationMetaObject.model_rebuild()
McpNotificationParams.model_rebuild()
McpCancelledNotificationParams.model_rebuild()
McpLoggingMessageNotificationParams.model_rebuild()
McpNumberSchema.model_rebuild()
McpParseError.model_rebuild()
McpPrimitiveSchemaDefinition.model_rebuild()
McpProgressNotification.model_rebuild()
McpProgressNotificationParams.model_rebuild()
McpPrompt.model_rebuild()
McpPromptArgument.model_rebuild()
McpPromptListChangedNotification.model_rebuild()
McpPromptMessage.model_rebuild()
McpPromptReference.model_rebuild()
McpReadResourceResultResponse.model_rebuild()
McpRequest.model_rebuild()
McpJSONRPCRequest.model_rebuild()
McpCallToolRequest.model_rebuild()
McpCompleteRequest.model_rebuild()
McpDiscoverRequest.model_rebuild()
McpGetPromptRequest.model_rebuild()
McpPaginatedRequest.model_rebuild()
McpListPromptsRequest.model_rebuild()
McpListResourceTemplatesRequest.model_rebuild()
McpListResourcesRequest.model_rebuild()
McpListToolsRequest.model_rebuild()
McpReadResourceRequest.model_rebuild()
McpRequestMetaObject.model_rebuild()
McpRequestParams.model_rebuild()
McpCompleteRequestParams.model_rebuild()
McpInputResponseRequestParams.model_rebuild()
McpCallToolRequestParams.model_rebuild()
McpGetPromptRequestParams.model_rebuild()
McpPaginatedRequestParams.model_rebuild()
McpResource.model_rebuild()
McpResourceContents.model_rebuild()
McpBlobResourceContents.model_rebuild()
McpResourceLink.model_rebuild()
McpResourceListChangedNotification.model_rebuild()
McpResourceRequestParams.model_rebuild()
McpReadResourceRequestParams.model_rebuild()
McpResourceTemplate.model_rebuild()
McpResourceTemplateReference.model_rebuild()
McpResourceUpdatedNotification.model_rebuild()
McpResourceUpdatedNotificationParams.model_rebuild()
McpResult.model_rebuild()
McpCacheableResult.model_rebuild()
McpCallToolResult.model_rebuild()
McpCompleteResult.model_rebuild()
McpDiscoverResult.model_rebuild()
McpEmptyResult.model_rebuild()
McpClientResult.model_rebuild()
McpGetPromptResult.model_rebuild()
McpInputRequiredResult.model_rebuild()
McpPaginatedResult.model_rebuild()
McpListPromptsResult.model_rebuild()
McpListResourceTemplatesResult.model_rebuild()
McpListResourcesResult.model_rebuild()
McpListToolsResult.model_rebuild()
McpReadResourceResult.model_rebuild()
McpResultMetaObject.model_rebuild()
McpRoot.model_rebuild()
McpSamplingMessage.model_rebuild()
McpCreateMessageResult.model_rebuild()
McpSamplingMessageContentBlock.model_rebuild()
McpServerCapabilities.model_rebuild()
McpServerCapabilitiesExperimental.model_rebuild()
McpServerCapabilitiesExtensions.model_rebuild()
McpServerCapabilitiesPrompts.model_rebuild()
McpServerCapabilitiesResources.model_rebuild()
McpServerCapabilitiesTools.model_rebuild()
McpServerNotification.model_rebuild()
McpServerResult.model_rebuild()
McpSingleSelectEnumSchema.model_rebuild()
McpStringSchema.model_rebuild()
McpSubscriptionFilter.model_rebuild()
McpSubscriptionsAcknowledgedNotification.model_rebuild()
McpSubscriptionsAcknowledgedNotificationParams.model_rebuild()
McpSubscriptionsListenRequest.model_rebuild()
McpSubscriptionsListenRequestParams.model_rebuild()
McpSubscriptionsListenResult.model_rebuild()
McpSubscriptionsListenResultMetaObject.model_rebuild()
McpSubscriptionsListenResultResponse.model_rebuild()
McpTextContent.model_rebuild()
McpTextResourceContents.model_rebuild()
McpTitledMultiSelectEnumSchema.model_rebuild()
McpTitledMultiSelectEnumSchemaItems.model_rebuild()
McpTitledMultiSelectEnumSchemaItemsAnyOf.model_rebuild()
McpTitledSingleSelectEnumSchema.model_rebuild()
McpTitledSingleSelectEnumSchemaOneOf.model_rebuild()
McpTool.model_rebuild()
McpToolAnnotations.model_rebuild()
McpToolChoice.model_rebuild()
McpToolInputSchema.model_rebuild()
McpToolListChangedNotification.model_rebuild()
McpToolOutputSchema.model_rebuild()
McpToolResultContent.model_rebuild()
McpToolUseContent.model_rebuild()
McpUnsupportedProtocolVersionError.model_rebuild()
McpUnsupportedProtocolVersionErrorError.model_rebuild()
McpUnsupportedProtocolVersionErrorErrorData.model_rebuild()
McpUntitledMultiSelectEnumSchema.model_rebuild()
McpUntitledMultiSelectEnumSchemaItems.model_rebuild()
McpUntitledSingleSelectEnumSchema.model_rebuild()
