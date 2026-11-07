# Auto generated from mcp.yaml by pythongen.py version: 0.0.1
# Schema: mcp
#
# id: https://w3id.org/lmodel/mcp
# description: The messages and objects of the Model Context Protocol, version 2026-07-28, as its schema.json states them: JSON-RPC requests, results, notifications and errors, and the tools, resources, prompts, content and capabilities they carry. Generated from MCP's own files by scripts/mcp_to_linkml.py.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.12.0"
version = "2026-07-28"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MCP = CurieNamespace('mcp', 'https://w3id.org/lmodel/mcp/')
MCP_SCHEMA = CurieNamespace('mcp_schema', 'https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/2026-07-28/schema/2026-07-28/schema.json#/$defs/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MCP


# Types
class McpBase64(String):
    """ Binary data, written as base64 text. """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "McpBase64"
    type_model_uri = MCP.McpBase64


class McpCursor(String):
    """ An opaque token used to represent a cursor for pagination. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "McpCursor"
    type_model_uri = MCP.McpCursor


class McpProgressToken(String):
    """ A progress token, used to associate progress notifications with the original request. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "McpProgressToken"
    type_model_uri = MCP.McpProgressToken


class McpRequestId(String):
    """ A uniquely identifying ID for a request in JSON-RPC. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "McpRequestId"
    type_model_uri = MCP.McpRequestId


class McpResultType(String):
    """ Indicates the type of a {@link Result} object, allowing the client to
determine how to parse the response.

complete - the request completed successfully and the result contains the final content.
input_required - the request requires additional input and the result contains an {@link InputRequiredResult} object with instructions for the client to provide additional input before retrying the original request. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "McpResultType"
    type_model_uri = MCP.McpResultType


class McpUriTemplate(String):
    """ A URI template, as RFC 6570 defines one. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "McpUriTemplate"
    type_model_uri = MCP.McpUriTemplate


# Class references



@dataclass(repr=False)
class McpAnnotations(YAMLRoot):
    """
    Optional annotations for the client. The client can use annotations to inform how objects are used or displayed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpAnnotations"]
    class_class_curie: ClassVar[str] = "mcp:McpAnnotations"
    class_name: ClassVar[str] = "McpAnnotations"
    class_model_uri: ClassVar[URIRef] = MCP.McpAnnotations

    intended_audience: Optional[Union[Union[str, "McpRole"], list[Union[str, "McpRole"]]]] = empty_list()
    lastModified: Optional[str] = None
    priority: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.intended_audience, list):
            self.intended_audience = [self.intended_audience] if self.intended_audience is not None else []
        self.intended_audience = [v if isinstance(v, McpRole) else McpRole(v) for v in self.intended_audience]

        if self.lastModified is not None and not isinstance(self.lastModified, str):
            self.lastModified = str(self.lastModified)

        if self.priority is not None and not isinstance(self.priority, float):
            self.priority = float(self.priority)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpAudioContent(YAMLRoot):
    """
    Audio provided to or from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpAudioContent"]
    class_class_curie: ClassVar[str] = "mcp:McpAudioContent"
    class_name: ClassVar[str] = "McpAudioContent"
    class_model_uri: ClassVar[URIRef] = MCP.McpAudioContent

    data: Union[str, McpBase64] = None
    mimeType: str = None
    kind: str = None
    _meta: Optional[Union[dict, "McpMetaObject"]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, McpBase64):
            self.data = McpBase64(self.data)

        if self._is_empty(self.mimeType):
            self.MissingRequiredField("mimeType")
        if not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpBaseMetadata(YAMLRoot):
    """
    Base interface for metadata with name (identifier) and title (display name) properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpBaseMetadata"]
    class_class_curie: ClassVar[str] = "mcp:McpBaseMetadata"
    class_name: ClassVar[str] = "McpBaseMetadata"
    class_model_uri: ClassVar[URIRef] = MCP.McpBaseMetadata

    name: str = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpBooleanSchema(YAMLRoot):
    """
    A field of an elicitation form that takes true or false.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpBooleanSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpBooleanSchema"
    class_name: ClassVar[str] = "McpBooleanSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpBooleanSchema

    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.default is not None and not isinstance(self.default, Bool):
            self.default = Bool(self.default)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpClientCapabilities(YAMLRoot):
    """
    Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed
    set: any client can define its own, additional capabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientCapabilities"]
    class_class_curie: ClassVar[str] = "mcp:McpClientCapabilities"
    class_name: ClassVar[str] = "McpClientCapabilities"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientCapabilities

    elicitation: Optional[Union[dict, "McpClientCapabilitiesElicitation"]] = None
    experimental: Optional[Union[dict, "McpClientCapabilitiesExperimental"]] = None
    extensions: Optional[Union[dict, "McpClientCapabilitiesExtensions"]] = None
    roots: Optional[Union[dict, "McpClientCapabilitiesRoots"]] = None
    sampling: Optional[Union[dict, "McpClientCapabilitiesSampling"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elicitation is not None and not isinstance(self.elicitation, McpClientCapabilitiesElicitation):
            self.elicitation = McpClientCapabilitiesElicitation(**as_dict(self.elicitation))

        if self.experimental is not None and not isinstance(self.experimental, McpClientCapabilitiesExperimental):
            self.experimental = McpClientCapabilitiesExperimental()

        if self.extensions is not None and not isinstance(self.extensions, McpClientCapabilitiesExtensions):
            self.extensions = McpClientCapabilitiesExtensions()

        if self.roots is not None and not isinstance(self.roots, McpClientCapabilitiesRoots):
            self.roots = McpClientCapabilitiesRoots()

        if self.sampling is not None and not isinstance(self.sampling, McpClientCapabilitiesSampling):
            self.sampling = McpClientCapabilitiesSampling(**as_dict(self.sampling))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpClientCapabilitiesElicitation(YAMLRoot):
    """
    Present if the client supports elicitation from the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientCapabilitiesElicitation"]
    class_class_curie: ClassVar[str] = "mcp:McpClientCapabilitiesElicitation"
    class_name: ClassVar[str] = "McpClientCapabilitiesElicitation"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientCapabilitiesElicitation

    form: Optional[Union[dict, "McpJSONObject"]] = None
    url_settings: Optional[Union[dict, "McpJSONObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.form is not None and not isinstance(self.form, McpJSONObject):
            self.form = McpJSONObject()

        if self.url_settings is not None and not isinstance(self.url_settings, McpJSONObject):
            self.url_settings = McpJSONObject()

        super().__post_init__(**kwargs)


class McpClientCapabilitiesExperimental(YAMLRoot):
    """
    Experimental, non-standard capabilities that the client supports.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientCapabilitiesExperimental"]
    class_class_curie: ClassVar[str] = "mcp:McpClientCapabilitiesExperimental"
    class_name: ClassVar[str] = "McpClientCapabilitiesExperimental"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientCapabilitiesExperimental


class McpClientCapabilitiesExtensions(YAMLRoot):
    """
    Optional MCP extensions that the client supports. Keys are extension identifiers
    (e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values are
    per-extension settings objects. An empty object indicates support with no settings.

    Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
    mandatory prefix.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientCapabilitiesExtensions"]
    class_class_curie: ClassVar[str] = "mcp:McpClientCapabilitiesExtensions"
    class_name: ClassVar[str] = "McpClientCapabilitiesExtensions"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientCapabilitiesExtensions


class McpClientCapabilitiesRoots(YAMLRoot):
    """
    Present if the client supports listing roots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientCapabilitiesRoots"]
    class_class_curie: ClassVar[str] = "mcp:McpClientCapabilitiesRoots"
    class_name: ClassVar[str] = "McpClientCapabilitiesRoots"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientCapabilitiesRoots


@dataclass(repr=False)
class McpClientCapabilitiesSampling(YAMLRoot):
    """
    Present if the client supports sampling from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientCapabilitiesSampling"]
    class_class_curie: ClassVar[str] = "mcp:McpClientCapabilitiesSampling"
    class_name: ClassVar[str] = "McpClientCapabilitiesSampling"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientCapabilitiesSampling

    context_info: Optional[Union[dict, "McpJSONObject"]] = None
    tools: Optional[Union[dict, "McpJSONObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.context_info is not None and not isinstance(self.context_info, McpJSONObject):
            self.context_info = McpJSONObject()

        if self.tools is not None and not isinstance(self.tools, McpJSONObject):
            self.tools = McpJSONObject()

        super().__post_init__(**kwargs)


class McpClientRequest(YAMLRoot):
    """
    One of `DiscoverRequest`, `ListResourcesRequest`, `ListResourceTemplatesRequest`, `ReadResourceRequest`,
    `SubscriptionsListenRequest`, `ListPromptsRequest`, `GetPromptRequest`, `ListToolsRequest`, `CallToolRequest`,
    `CompleteRequest`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpClientRequest"
    class_name: ClassVar[str] = "McpClientRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientRequest


@dataclass(repr=False)
class McpCompleteRequestParamsArgument(YAMLRoot):
    """
    The argument's information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteRequestParamsArgument"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteRequestParamsArgument"
    class_name: ClassVar[str] = "McpCompleteRequestParamsArgument"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteRequestParamsArgument

    name: str = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCompleteRequestParamsContext(YAMLRoot):
    """
    Additional, optional context for completions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteRequestParamsContext"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteRequestParamsContext"
    class_name: ClassVar[str] = "McpCompleteRequestParamsContext"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteRequestParamsContext

    arguments: Optional[Union[dict, "McpCompleteRequestParamsContextArguments"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.arguments is not None and not isinstance(self.arguments, McpCompleteRequestParamsContextArguments):
            self.arguments = McpCompleteRequestParamsContextArguments()

        super().__post_init__(**kwargs)


class McpCompleteRequestParamsContextArguments(YAMLRoot):
    """
    Previously-resolved variables in a URI template or prompt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteRequestParamsContextArguments"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteRequestParamsContextArguments"
    class_name: ClassVar[str] = "McpCompleteRequestParamsContextArguments"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteRequestParamsContextArguments


@dataclass(repr=False)
class McpCompleteResultCompletion(YAMLRoot):
    """
    The object MCP's `CompleteResult` holds under `completion`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteResultCompletion"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteResultCompletion"
    class_name: ClassVar[str] = "McpCompleteResultCompletion"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteResultCompletion

    values: Union[str, list[str]] = None
    hasMore: Optional[Union[bool, Bool]] = None
    total: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.hasMore is not None and not isinstance(self.hasMore, Bool):
            self.hasMore = Bool(self.hasMore)

        if self.total is not None and not isinstance(self.total, int):
            self.total = int(self.total)

        super().__post_init__(**kwargs)


class McpContentBlock(YAMLRoot):
    """
    One of `TextContent`, `ImageContent`, `AudioContent`, `ResourceLink`, `EmbeddedResource`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpContentBlock"]
    class_class_curie: ClassVar[str] = "mcp:McpContentBlock"
    class_name: ClassVar[str] = "McpContentBlock"
    class_model_uri: ClassVar[URIRef] = MCP.McpContentBlock


@dataclass(repr=False)
class McpCreateMessageRequest(YAMLRoot):
    """
    A request from the server to sample an LLM via the client. The client has full discretion over which model to
    select. The client should also inform the user before beginning sampling, to allow them to inspect the request
    (human in the loop) and decide whether to approve it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCreateMessageRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpCreateMessageRequest"
    class_name: ClassVar[str] = "McpCreateMessageRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpCreateMessageRequest

    method: str = None
    params: Union[dict, "McpCreateMessageRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpCreateMessageRequestParams):
            self.params = McpCreateMessageRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCreateMessageRequestParams(YAMLRoot):
    """
    Parameters for a `sampling/createMessage` request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCreateMessageRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpCreateMessageRequestParams"
    class_name: ClassVar[str] = "McpCreateMessageRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpCreateMessageRequestParams

    maxTokens: int = None
    messages: Union[Union[dict, "McpSamplingMessage"], list[Union[dict, "McpSamplingMessage"]]] = None
    includeContext: Optional[Union[str, "McpCreateMessageRequestParamsIncludeContext"]] = None
    metadata: Optional[Union[dict, "McpJSONObject"]] = None
    modelPreferences: Optional[Union[dict, "McpModelPreferences"]] = None
    stopSequences: Optional[Union[str, list[str]]] = empty_list()
    systemPrompt: Optional[str] = None
    temperature: Optional[float] = None
    toolChoice: Optional[Union[dict, "McpToolChoice"]] = None
    tools: Optional[Union[Union[dict, "McpTool"], list[Union[dict, "McpTool"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.maxTokens):
            self.MissingRequiredField("maxTokens")
        if not isinstance(self.maxTokens, int):
            self.maxTokens = int(self.maxTokens)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=McpSamplingMessage, key_name="content", keyed=False)

        if self.includeContext is not None and not isinstance(self.includeContext, McpCreateMessageRequestParamsIncludeContext):
            self.includeContext = McpCreateMessageRequestParamsIncludeContext(self.includeContext)

        if self.metadata is not None and not isinstance(self.metadata, McpJSONObject):
            self.metadata = McpJSONObject()

        if self.modelPreferences is not None and not isinstance(self.modelPreferences, McpModelPreferences):
            self.modelPreferences = McpModelPreferences(**as_dict(self.modelPreferences))

        if not isinstance(self.stopSequences, list):
            self.stopSequences = [self.stopSequences] if self.stopSequences is not None else []
        self.stopSequences = [v if isinstance(v, str) else str(v) for v in self.stopSequences]

        if self.systemPrompt is not None and not isinstance(self.systemPrompt, str):
            self.systemPrompt = str(self.systemPrompt)

        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.toolChoice is not None and not isinstance(self.toolChoice, McpToolChoice):
            self.toolChoice = McpToolChoice(**as_dict(self.toolChoice))

        self._normalize_inlined_as_list(slot_name="tools", slot_type=McpTool, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpElicitRequest(YAMLRoot):
    """
    A request from the server to elicit additional information from the user via the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitRequest"
    class_name: ClassVar[str] = "McpElicitRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitRequest

    method: str = None
    params: Union[dict, "McpElicitRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpElicitRequestParams):
            self.params = McpElicitRequestParams()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpElicitRequestFormParams(YAMLRoot):
    """
    The parameters for a request to elicit non-sensitive information from the user via a form in the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitRequestFormParams"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitRequestFormParams"
    class_name: ClassVar[str] = "McpElicitRequestFormParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitRequestFormParams

    message: str = None
    requestedSchema: Union[dict, "McpElicitRequestFormParamsRequestedSchema"] = None
    mode: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        if self._is_empty(self.requestedSchema):
            self.MissingRequiredField("requestedSchema")
        if not isinstance(self.requestedSchema, McpElicitRequestFormParamsRequestedSchema):
            self.requestedSchema = McpElicitRequestFormParamsRequestedSchema(**as_dict(self.requestedSchema))

        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpElicitRequestFormParamsRequestedSchema(YAMLRoot):
    """
    A restricted subset of JSON Schema.
    Only top-level properties are allowed, without nesting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitRequestFormParamsRequestedSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitRequestFormParamsRequestedSchema"
    class_name: ClassVar[str] = "McpElicitRequestFormParamsRequestedSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitRequestFormParamsRequestedSchema

    properties: Union[dict, "McpElicitRequestFormParamsRequestedSchemaProperties"] = None
    kind: str = None
    schema_dialect: Optional[str] = None
    required_names: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.properties):
            self.MissingRequiredField("properties")
        if not isinstance(self.properties, McpElicitRequestFormParamsRequestedSchemaProperties):
            self.properties = McpElicitRequestFormParamsRequestedSchemaProperties()

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.schema_dialect is not None and not isinstance(self.schema_dialect, str):
            self.schema_dialect = str(self.schema_dialect)

        if not isinstance(self.required_names, list):
            self.required_names = [self.required_names] if self.required_names is not None else []
        self.required_names = [v if isinstance(v, str) else str(v) for v in self.required_names]

        super().__post_init__(**kwargs)


class McpElicitRequestFormParamsRequestedSchemaProperties(YAMLRoot):
    """
    The object MCP's `ElicitRequestFormParams` holds under `properties`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitRequestFormParamsRequestedSchemaProperties"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitRequestFormParamsRequestedSchemaProperties"
    class_name: ClassVar[str] = "McpElicitRequestFormParamsRequestedSchemaProperties"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitRequestFormParamsRequestedSchemaProperties


class McpElicitRequestParams(YAMLRoot):
    """
    The parameters for a request to elicit additional information from the user via the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitRequestParams"
    class_name: ClassVar[str] = "McpElicitRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitRequestParams


@dataclass(repr=False)
class McpElicitRequestURLParams(YAMLRoot):
    """
    The parameters for a request to elicit information from the user via a URL in the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitRequestURLParams"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitRequestURLParams"
    class_name: ClassVar[str] = "McpElicitRequestURLParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitRequestURLParams

    url: Union[str, URI] = None
    message: str = None
    mode: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        if self._is_empty(self.mode):
            self.MissingRequiredField("mode")
        if not isinstance(self.mode, str):
            self.mode = str(self.mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpElicitResult(YAMLRoot):
    """
    The result returned by the client for an {@link ElicitRequestelicitation/create} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitResult"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitResult"
    class_name: ClassVar[str] = "McpElicitResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitResult

    action: Union[str, "McpElicitResultAction"] = None
    content: Optional[Union[dict, "McpElicitResultContent"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, McpElicitResultAction):
            self.action = McpElicitResultAction(self.action)

        if self.content is not None and not isinstance(self.content, McpElicitResultContent):
            self.content = McpElicitResultContent()

        super().__post_init__(**kwargs)


class McpElicitResultContent(YAMLRoot):
    """
    The submitted form data, only present when action is `"accept"` and mode was `"form"`.
    Contains values matching the requested schema.
    Omitted for out-of-band mode responses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpElicitResultContent"]
    class_class_curie: ClassVar[str] = "mcp:McpElicitResultContent"
    class_name: ClassVar[str] = "McpElicitResultContent"
    class_model_uri: ClassVar[URIRef] = MCP.McpElicitResultContent


@dataclass(repr=False)
class McpEmbeddedResource(YAMLRoot):
    """
    The contents of a resource, embedded into a prompt or tool call result.

    It is up to the client how best to render embedded resources for the benefit
    of the LLM and/or the user.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpEmbeddedResource"]
    class_class_curie: ClassVar[str] = "mcp:McpEmbeddedResource"
    class_name: ClassVar[str] = "McpEmbeddedResource"
    class_model_uri: ClassVar[URIRef] = MCP.McpEmbeddedResource

    resource_contents: Union[dict, "McpTextResourceContents", "McpBlobResourceContents"] = None
    kind: str = None
    _meta: Optional[Union[dict, "McpMetaObject"]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resource_contents):
            self.MissingRequiredField("resource_contents")
        if not isinstance(self.resource_contents, (McpTextResourceContents, McpBlobResourceContents)):
            value = self.resource_contents
            for _coerce in (lambda: McpTextResourceContents(**as_dict(value)), lambda: McpBlobResourceContents(**as_dict(value))):
                try:
                    self.resource_contents = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpTextResourceContents, McpBlobResourceContents] could be constructed from {value!r} for slot resource_contents")

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


class McpEnumSchema(YAMLRoot):
    """
    One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`, `UntitledMultiSelectEnumSchema`,
    `TitledMultiSelectEnumSchema`, `LegacyTitledEnumSchema`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpEnumSchema"
    class_name: ClassVar[str] = "McpEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpEnumSchema


@dataclass(repr=False)
class McpError(YAMLRoot):
    """
    The error a JSON-RPC error response carries: a code, a message and any data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpError"]
    class_class_curie: ClassVar[str] = "mcp:McpError"
    class_name: ClassVar[str] = "McpError"
    class_model_uri: ClassVar[URIRef] = MCP.McpError

    code: int = None
    message: str = None
    data: Optional[Union[dict, "McpJSONValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        super().__post_init__(**kwargs)


class McpGetPromptRequestParamsArguments(YAMLRoot):
    """
    Arguments to use for templating the prompt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpGetPromptRequestParamsArguments"]
    class_class_curie: ClassVar[str] = "mcp:McpGetPromptRequestParamsArguments"
    class_name: ClassVar[str] = "McpGetPromptRequestParamsArguments"
    class_model_uri: ClassVar[URIRef] = MCP.McpGetPromptRequestParamsArguments


@dataclass(repr=False)
class McpHeaderMismatchErrorError(McpError):
    """
    MCP's `Error`, with the code this error carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpHeaderMismatchErrorError"]
    class_class_curie: ClassVar[str] = "mcp:McpHeaderMismatchErrorError"
    class_name: ClassVar[str] = "McpHeaderMismatchErrorError"
    class_model_uri: ClassVar[URIRef] = MCP.McpHeaderMismatchErrorError

    message: str = None
    code: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpIcon(YAMLRoot):
    """
    An optionally-sized icon that can be displayed in a user interface.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpIcon"]
    class_class_curie: ClassVar[str] = "mcp:McpIcon"
    class_name: ClassVar[str] = "McpIcon"
    class_model_uri: ClassVar[URIRef] = MCP.McpIcon

    src: Union[str, URI] = None
    mimeType: Optional[str] = None
    sizes: Optional[Union[str, list[str]]] = empty_list()
    theme: Optional[Union[str, "McpIconTheme"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.src):
            self.MissingRequiredField("src")
        if not isinstance(self.src, URI):
            self.src = URI(self.src)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if not isinstance(self.sizes, list):
            self.sizes = [self.sizes] if self.sizes is not None else []
        self.sizes = [v if isinstance(v, str) else str(v) for v in self.sizes]

        if self.theme is not None and not isinstance(self.theme, McpIconTheme):
            self.theme = McpIconTheme(self.theme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpIcons(YAMLRoot):
    """
    Base interface to add `icons` property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpIcons"]
    class_class_curie: ClassVar[str] = "mcp:McpIcons"
    class_name: ClassVar[str] = "McpIcons"
    class_model_uri: ClassVar[URIRef] = MCP.McpIcons

    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpImageContent(YAMLRoot):
    """
    An image provided to or from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpImageContent"]
    class_class_curie: ClassVar[str] = "mcp:McpImageContent"
    class_name: ClassVar[str] = "McpImageContent"
    class_model_uri: ClassVar[URIRef] = MCP.McpImageContent

    data: Union[str, McpBase64] = None
    mimeType: str = None
    kind: str = None
    _meta: Optional[Union[dict, "McpMetaObject"]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, McpBase64):
            self.data = McpBase64(self.data)

        if self._is_empty(self.mimeType):
            self.MissingRequiredField("mimeType")
        if not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpImplementation(McpBaseMetadata):
    """
    Describes the MCP implementation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpImplementation"]
    class_class_curie: ClassVar[str] = "mcp:McpImplementation"
    class_name: ClassVar[str] = "McpImplementation"
    class_model_uri: ClassVar[URIRef] = MCP.McpImplementation

    name: str = None
    version: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()
    websiteUrl: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        if self.websiteUrl is not None and not isinstance(self.websiteUrl, URI):
            self.websiteUrl = URI(self.websiteUrl)

        super().__post_init__(**kwargs)


class McpInputRequest(YAMLRoot):
    """
    One of `CreateMessageRequest`, `ListRootsRequest`, `ElicitRequest`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInputRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpInputRequest"
    class_name: ClassVar[str] = "McpInputRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpInputRequest


class McpInputRequests(YAMLRoot):
    """
    A map of server-initiated requests that the client must fulfill.
    Keys are server-assigned identifiers; values are the request objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInputRequests"]
    class_class_curie: ClassVar[str] = "mcp:McpInputRequests"
    class_name: ClassVar[str] = "McpInputRequests"
    class_model_uri: ClassVar[URIRef] = MCP.McpInputRequests


class McpInputResponse(YAMLRoot):
    """
    One of `CreateMessageResult`, `ListRootsResult`, `ElicitResult`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInputResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpInputResponse"
    class_name: ClassVar[str] = "McpInputResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpInputResponse


class McpInputResponses(YAMLRoot):
    """
    A map of client responses to server-initiated requests.
    Keys correspond to the keys in the {@link InputRequests} map;
    values are the client's result for each request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInputResponses"]
    class_class_curie: ClassVar[str] = "mcp:McpInputResponses"
    class_name: ClassVar[str] = "McpInputResponses"
    class_model_uri: ClassVar[URIRef] = MCP.McpInputResponses


@dataclass(repr=False)
class McpInternalError(McpError):
    """
    A JSON-RPC error indicating that an internal error occurred on the receiver. This error is returned when the
    receiver encounters an unexpected condition that prevents it from fulfilling the request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInternalError"]
    class_class_curie: ClassVar[str] = "mcp:McpInternalError"
    class_name: ClassVar[str] = "McpInternalError"
    class_model_uri: ClassVar[URIRef] = MCP.McpInternalError

    code: int = None
    message: str = None
    data: Optional[Union[dict, "McpJSONValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInvalidParamsError"]
    class_class_curie: ClassVar[str] = "mcp:McpInvalidParamsError"
    class_name: ClassVar[str] = "McpInvalidParamsError"
    class_model_uri: ClassVar[URIRef] = MCP.McpInvalidParamsError

    code: int = None
    message: str = None
    data: Optional[Union[dict, "McpJSONValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpInvalidRequestError(McpError):
    """
    A JSON-RPC error indicating that the request is not a valid request object. This error is returned when the
    message structure does not conform to the JSON-RPC 2.0 specification requirements for a request (e.g., missing
    required fields like `jsonrpc` or `method`, or using invalid types for these fields).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInvalidRequestError"]
    class_class_curie: ClassVar[str] = "mcp:McpInvalidRequestError"
    class_name: ClassVar[str] = "McpInvalidRequestError"
    class_model_uri: ClassVar[URIRef] = MCP.McpInvalidRequestError

    code: int = None
    message: str = None
    data: Optional[Union[dict, "McpJSONValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        super().__post_init__(**kwargs)


class McpJSONObject(YAMLRoot):
    """
    A JSON object, whose values are JSON values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONObject"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONObject"
    class_name: ClassVar[str] = "McpJSONObject"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONObject


@dataclass(repr=False)
class McpJSONRPCErrorResponse(YAMLRoot):
    """
    A response to a request that indicates an error occurred.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONRPCErrorResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONRPCErrorResponse"
    class_name: ClassVar[str] = "McpJSONRPCErrorResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONRPCErrorResponse

    error: Union[dict, McpError] = None
    jsonrpc: str = None
    identifier: Optional[Union[str, int]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.error):
            self.MissingRequiredField("error")
        if not isinstance(self.error, McpError):
            self.error = McpError(**as_dict(self.error))

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self.identifier is not None and not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpHeaderMismatchError(McpJSONRPCErrorResponse):
    """
    Returned when a server rejects a request because the values in the HTTP
    headers do not match the corresponding values in the request body, or
    because required headers are missing or malformed. For HTTP, the response
    status code MUST be `400 Bad Request`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpHeaderMismatchError"]
    class_class_curie: ClassVar[str] = "mcp:McpHeaderMismatchError"
    class_name: ClassVar[str] = "McpHeaderMismatchError"
    class_model_uri: ClassVar[URIRef] = MCP.McpHeaderMismatchError

    error: Union[dict, McpHeaderMismatchErrorError] = None
    jsonrpc: str = None
    identifier: Optional[Union[str, int]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.error):
            self.MissingRequiredField("error")
        if not isinstance(self.error, McpHeaderMismatchErrorError):
            self.error = McpHeaderMismatchErrorError(**as_dict(self.error))

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self.identifier is not None and not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        super().__post_init__(**kwargs)


class McpJSONRPCMessage(YAMLRoot):
    """
    Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONRPCMessage"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONRPCMessage"
    class_name: ClassVar[str] = "McpJSONRPCMessage"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONRPCMessage


class McpJSONRPCResponse(YAMLRoot):
    """
    A response to a request, containing either the result or error.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONRPCResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONRPCResponse"
    class_name: ClassVar[str] = "McpJSONRPCResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONRPCResponse


@dataclass(repr=False)
class McpJSONRPCResultResponse(YAMLRoot):
    """
    A successful (non-error) response to a request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONRPCResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONRPCResultResponse"
    class_name: ClassVar[str] = "McpJSONRPCResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONRPCResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpResult):
            self.result = McpResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCallToolResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link CallToolRequesttools/call} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCallToolResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpCallToolResultResponse"
    class_name: ClassVar[str] = "McpCallToolResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpCallToolResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpInputRequiredResult", "McpCallToolResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, (McpInputRequiredResult, McpCallToolResult)):
            value = self.result
            for _coerce in (lambda: McpInputRequiredResult(**as_dict(value)), lambda: McpCallToolResult(**as_dict(value))):
                try:
                    self.result = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpInputRequiredResult, McpCallToolResult] could be constructed from {value!r} for slot result")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCompleteResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link CompleteRequestcompletion/complete} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteResultResponse"
    class_name: ClassVar[str] = "McpCompleteResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpCompleteResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpCompleteResult):
            self.result = McpCompleteResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpDiscoverResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link DiscoverRequestserver/discover} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpDiscoverResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpDiscoverResultResponse"
    class_name: ClassVar[str] = "McpDiscoverResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpDiscoverResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpDiscoverResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpDiscoverResult):
            self.result = McpDiscoverResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpGetPromptResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link GetPromptRequestprompts/get} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpGetPromptResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpGetPromptResultResponse"
    class_name: ClassVar[str] = "McpGetPromptResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpGetPromptResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpInputRequiredResult", "McpGetPromptResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, (McpInputRequiredResult, McpGetPromptResult)):
            value = self.result
            for _coerce in (lambda: McpInputRequiredResult(**as_dict(value)), lambda: McpGetPromptResult(**as_dict(value))):
                try:
                    self.result = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpInputRequiredResult, McpGetPromptResult] could be constructed from {value!r} for slot result")

        super().__post_init__(**kwargs)


McpJSONValue = Any

@dataclass(repr=False)
class McpLegacyTitledEnumSchema(YAMLRoot):
    """
    Use {@link TitledSingleSelectEnumSchema} instead.
    This interface will be removed in a future version.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpLegacyTitledEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpLegacyTitledEnumSchema"
    class_name: ClassVar[str] = "McpLegacyTitledEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpLegacyTitledEnumSchema

    enum: Union[str, list[str]] = None
    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[str] = None
    enumNames: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.enum):
            self.MissingRequiredField("enum")
        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.default is not None and not isinstance(self.default, str):
            self.default = str(self.default)

        if not isinstance(self.enumNames, list):
            self.enumNames = [self.enumNames] if self.enumNames is not None else []
        self.enumNames = [v if isinstance(v, str) else str(v) for v in self.enumNames]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListPromptsResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListPromptsRequestprompts/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListPromptsResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpListPromptsResultResponse"
    class_name: ClassVar[str] = "McpListPromptsResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpListPromptsResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpListPromptsResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpListPromptsResult):
            self.result = McpListPromptsResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListResourceTemplatesResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListResourceTemplatesResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpListResourceTemplatesResultResponse"
    class_name: ClassVar[str] = "McpListResourceTemplatesResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpListResourceTemplatesResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpListResourceTemplatesResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpListResourceTemplatesResult):
            self.result = McpListResourceTemplatesResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListResourcesResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListResourcesRequestresources/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListResourcesResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpListResourcesResultResponse"
    class_name: ClassVar[str] = "McpListResourcesResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpListResourcesResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpListResourcesResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpListResourcesResult):
            self.result = McpListResourcesResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListRootsRequest(YAMLRoot):
    """
    Sent from the server to request a list of root URIs from the client. Roots allow
    servers to ask for specific directories or files to operate on. A common example
    for roots is providing a set of repositories or directories a server should operate
    on.

    This request is typically used when the server needs to understand the file system
    structure or access specific locations that the client has permission to read from.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListRootsRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpListRootsRequest"
    class_name: ClassVar[str] = "McpListRootsRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpListRootsRequest

    method: str = None
    params: Optional[Union[dict, "McpListRootsRequestParams"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpListRootsRequestParams):
            self.params = McpListRootsRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListRootsRequestParams(YAMLRoot):
    """
    The object MCP's `ListRootsRequest` holds under `params`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListRootsRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpListRootsRequestParams"
    class_name: ClassVar[str] = "McpListRootsRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpListRootsRequestParams

    _meta: Optional[Union[dict, "McpMetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListRootsResult(YAMLRoot):
    """
    The result returned by the client for a {@link ListRootsRequestroots/list} request.
    This result contains an array of {@link Root} objects, each representing a root directory
    or file that the server can operate on.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListRootsResult"]
    class_class_curie: ClassVar[str] = "mcp:McpListRootsResult"
    class_name: ClassVar[str] = "McpListRootsResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpListRootsResult

    roots: Union[Union[dict, "McpRoot"], list[Union[dict, "McpRoot"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.roots):
            self.MissingRequiredField("roots")
        self._normalize_inlined_as_list(slot_name="roots", slot_type=McpRoot, key_name="uri", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListToolsResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ListToolsRequesttools/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListToolsResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpListToolsResultResponse"
    class_name: ClassVar[str] = "McpListToolsResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpListToolsResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpListToolsResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpListToolsResult):
            self.result = McpListToolsResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


class McpMetaObject(YAMLRoot):
    """
    Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their
    interactions.

    Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about
    values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific
    metadata, as declared in those definitions.

    Valid keys have two segments:

    **Prefix:**
    - Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
    - Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or
    hyphens (`-`).
    - Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
    - Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example:
    `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved.
    However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

    **Name:**
    - Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
    - Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpMetaObject"]
    class_class_curie: ClassVar[str] = "mcp:McpMetaObject"
    class_name: ClassVar[str] = "McpMetaObject"
    class_model_uri: ClassVar[URIRef] = MCP.McpMetaObject


@dataclass(repr=False)
class McpMethodNotFoundError(McpError):
    """
    A JSON-RPC error indicating that the requested method does not exist or is not available.

    In MCP, a server returns this error when a client invokes a method the server does not implement — either a
    genuinely unknown method, or one gated behind a server capability the server did not advertise (e.g., calling
    `prompts/list` when the `prompts` capability was not advertised).

    A request that requires a client capability the client did not declare is signalled instead by {@link
    MissingRequiredClientCapabilityError} (`-32021`).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpMethodNotFoundError"]
    class_class_curie: ClassVar[str] = "mcp:McpMethodNotFoundError"
    class_name: ClassVar[str] = "McpMethodNotFoundError"
    class_model_uri: ClassVar[URIRef] = MCP.McpMethodNotFoundError

    code: int = None
    message: str = None
    data: Optional[Union[dict, McpJSONValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpMissingRequiredClientCapabilityError(McpJSONRPCErrorResponse):
    """
    Returned when processing a request requires a capability the client did not
    declare in `clientCapabilities`. For HTTP, the response status code MUST be
    `400 Bad Request`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpMissingRequiredClientCapabilityError"]
    class_class_curie: ClassVar[str] = "mcp:McpMissingRequiredClientCapabilityError"
    class_name: ClassVar[str] = "McpMissingRequiredClientCapabilityError"
    class_model_uri: ClassVar[URIRef] = MCP.McpMissingRequiredClientCapabilityError

    error: Union[dict, "McpMissingRequiredClientCapabilityErrorError"] = None
    jsonrpc: str = None
    identifier: Optional[Union[str, int]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.error):
            self.MissingRequiredField("error")
        if not isinstance(self.error, McpMissingRequiredClientCapabilityErrorError):
            self.error = McpMissingRequiredClientCapabilityErrorError(**as_dict(self.error))

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self.identifier is not None and not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpMissingRequiredClientCapabilityErrorError(McpError):
    """
    MCP's `Error`, with the code and data this error carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpMissingRequiredClientCapabilityErrorError"]
    class_class_curie: ClassVar[str] = "mcp:McpMissingRequiredClientCapabilityErrorError"
    class_name: ClassVar[str] = "McpMissingRequiredClientCapabilityErrorError"
    class_model_uri: ClassVar[URIRef] = MCP.McpMissingRequiredClientCapabilityErrorError

    message: str = None
    code: int = None
    data: Union[dict, "McpMissingRequiredClientCapabilityErrorErrorData"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, McpMissingRequiredClientCapabilityErrorErrorData):
            self.data = McpMissingRequiredClientCapabilityErrorErrorData(**as_dict(self.data))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpMissingRequiredClientCapabilityErrorErrorData(YAMLRoot):
    """
    The object MCP's `MissingRequiredClientCapabilityError` holds under `data`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpMissingRequiredClientCapabilityErrorErrorData"]
    class_class_curie: ClassVar[str] = "mcp:McpMissingRequiredClientCapabilityErrorErrorData"
    class_name: ClassVar[str] = "McpMissingRequiredClientCapabilityErrorErrorData"
    class_model_uri: ClassVar[URIRef] = MCP.McpMissingRequiredClientCapabilityErrorErrorData

    requiredCapabilities: Union[dict, McpClientCapabilities] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requiredCapabilities):
            self.MissingRequiredField("requiredCapabilities")
        if not isinstance(self.requiredCapabilities, McpClientCapabilities):
            self.requiredCapabilities = McpClientCapabilities(**as_dict(self.requiredCapabilities))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpModelHint(YAMLRoot):
    """
    Hints to use for model selection.

    Keys not declared here are currently left unspecified by the spec and are up
    to the client to interpret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpModelHint"]
    class_class_curie: ClassVar[str] = "mcp:McpModelHint"
    class_name: ClassVar[str] = "McpModelHint"
    class_model_uri: ClassVar[URIRef] = MCP.McpModelHint

    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpModelPreferences(YAMLRoot):
    """
    The server's preferences for model selection, requested of the client during sampling.

    Because LLMs can vary along multiple dimensions, choosing the "best" model is
    rarely straightforward.  Different models excel in different areas—some are
    faster but less capable, others are more capable but more expensive, and so
    on. This interface allows servers to express their priorities across multiple
    dimensions to help clients make an appropriate selection for their use case.

    These preferences are always advisory. The client MAY ignore them. It is also
    up to the client to decide how to interpret these preferences and how to
    balance them against other considerations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpModelPreferences"]
    class_class_curie: ClassVar[str] = "mcp:McpModelPreferences"
    class_name: ClassVar[str] = "McpModelPreferences"
    class_model_uri: ClassVar[URIRef] = MCP.McpModelPreferences

    costPriority: Optional[float] = None
    hints: Optional[Union[Union[dict, McpModelHint], list[Union[dict, McpModelHint]]]] = empty_list()
    intelligencePriority: Optional[float] = None
    speedPriority: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.costPriority is not None and not isinstance(self.costPriority, float):
            self.costPriority = float(self.costPriority)

        if not isinstance(self.hints, list):
            self.hints = [self.hints] if self.hints is not None else []
        self.hints = [v if isinstance(v, McpModelHint) else McpModelHint(**as_dict(v)) for v in self.hints]

        if self.intelligencePriority is not None and not isinstance(self.intelligencePriority, float):
            self.intelligencePriority = float(self.intelligencePriority)

        if self.speedPriority is not None and not isinstance(self.speedPriority, float):
            self.speedPriority = float(self.speedPriority)

        super().__post_init__(**kwargs)


class McpMultiSelectEnumSchema(YAMLRoot):
    """
    One of `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpMultiSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpMultiSelectEnumSchema"
    class_name: ClassVar[str] = "McpMultiSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpMultiSelectEnumSchema


@dataclass(repr=False)
class McpNotification(YAMLRoot):
    """
    The method and the parameters a notification carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpNotification"
    class_name: ClassVar[str] = "McpNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpNotification

    method: str = None
    params: Optional[Union[dict, McpJSONObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpJSONObject):
            self.params = McpJSONObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpJSONRPCNotification(McpNotification):
    """
    A notification which does not expect a response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONRPCNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONRPCNotification"
    class_name: ClassVar[str] = "McpJSONRPCNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONRPCNotification

    jsonrpc: str = None
    method: str = None
    params: Optional[Union[dict, McpJSONObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpJSONObject):
            self.params = McpJSONObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCancelledNotification(McpJSONRPCNotification):
    """
    This notification is sent by the client to indicate that it is cancelling a request it previously issued.

    On stdio, the server also sends this notification, solely to terminate a {@link
    SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request
    that opened the stream. Servers MUST NOT use this notification to cancel any other request.

    The request SHOULD still be in-flight, but due to communication latency, it is always possible that this
    notification MAY arrive after the request has already finished.

    This notification indicates that the result will be unused, so any associated processing SHOULD cease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCancelledNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpCancelledNotification"
    class_name: ClassVar[str] = "McpCancelledNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpCancelledNotification

    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpCancelledNotificationParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpCancelledNotificationParams):
            self.params = McpCancelledNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpClientNotification(McpCancelledNotification):
    """
    This notification is sent by the client to indicate that it is cancelling a request it previously issued.

    On stdio, the server also sends this notification, solely to terminate a {@link
    SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request
    that opened the stream. Servers MUST NOT use this notification to cancel any other request.

    The request SHOULD still be in-flight, but due to communication latency, it is always possible that this
    notification MAY arrive after the request has already finished.

    This notification indicates that the result will be unused, so any associated processing SHOULD cease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpClientNotification"
    class_name: ClassVar[str] = "McpClientNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientNotification

    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpCancelledNotificationParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpCancelledNotificationParams):
            self.params = McpCancelledNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpLoggingMessageNotification(McpJSONRPCNotification):
    """
    JSONRPCNotification of a log message passed from server to client. The client opts in by setting
    `"io.modelcontextprotocol/logLevel"` in a request's `_meta`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpLoggingMessageNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpLoggingMessageNotification"
    class_name: ClassVar[str] = "McpLoggingMessageNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpLoggingMessageNotification

    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpLoggingMessageNotificationParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpLoggingMessageNotificationParams):
            self.params = McpLoggingMessageNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpNotificationMetaObject(McpMetaObject):
    """
    Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject`
    apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpNotificationMetaObject"]
    class_class_curie: ClassVar[str] = "mcp:McpNotificationMetaObject"
    class_name: ClassVar[str] = "McpNotificationMetaObject"
    class_model_uri: ClassVar[URIRef] = MCP.McpNotificationMetaObject

    mcp_subscription_id: Optional[Union[str, int]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mcp_subscription_id is not None and not isinstance(self.mcp_subscription_id, (str, int)):
            value = self.mcp_subscription_id
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.mcp_subscription_id = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot mcp_subscription_id")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpNotificationParams(YAMLRoot):
    """
    Common params for any notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:McpNotificationParams"
    class_name: ClassVar[str] = "McpNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpNotificationParams

    _meta: Optional[Union[dict, McpNotificationMetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._meta is not None and not isinstance(self._meta, McpNotificationMetaObject):
            self._meta = McpNotificationMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCancelledNotificationParams(McpNotificationParams):
    """
    Parameters for a `notifications/cancelled` notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCancelledNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:McpCancelledNotificationParams"
    class_name: ClassVar[str] = "McpCancelledNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpCancelledNotificationParams

    requestId: Union[str, int] = None
    _meta: Optional[Union[dict, McpNotificationMetaObject]] = None
    reason_text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requestId):
            self.MissingRequiredField("requestId")
        if not isinstance(self.requestId, (str, int)):
            value = self.requestId
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.requestId = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot requestId")

        if self._meta is not None and not isinstance(self._meta, McpNotificationMetaObject):
            self._meta = McpNotificationMetaObject(**as_dict(self._meta))

        if self.reason_text is not None and not isinstance(self.reason_text, str):
            self.reason_text = str(self.reason_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpLoggingMessageNotificationParams(McpNotificationParams):
    """
    Parameters for a `notifications/message` notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpLoggingMessageNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:McpLoggingMessageNotificationParams"
    class_name: ClassVar[str] = "McpLoggingMessageNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpLoggingMessageNotificationParams

    data: Union[dict, McpJSONValue] = None
    level: Union[str, "McpLoggingLevel"] = None
    _meta: Optional[Union[dict, McpNotificationMetaObject]] = None
    logger: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.level):
            self.MissingRequiredField("level")
        if not isinstance(self.level, McpLoggingLevel):
            self.level = McpLoggingLevel(self.level)

        if self._meta is not None and not isinstance(self._meta, McpNotificationMetaObject):
            self._meta = McpNotificationMetaObject(**as_dict(self._meta))

        if self.logger is not None and not isinstance(self.logger, str):
            self.logger = str(self.logger)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpNumberSchema(YAMLRoot):
    """
    A field of an elicitation form that takes a number or an integer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpNumberSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpNumberSchema"
    class_name: ClassVar[str] = "McpNumberSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpNumberSchema

    kind: Union[str, "McpNumberSchemaType"] = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, McpNumberSchemaType):
            self.kind = McpNumberSchemaType(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.default is not None and not isinstance(self.default, float):
            self.default = float(self.default)

        if self.maximum is not None and not isinstance(self.maximum, float):
            self.maximum = float(self.maximum)

        if self.minimum is not None and not isinstance(self.minimum, float):
            self.minimum = float(self.minimum)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpParseError(McpError):
    """
    A JSON-RPC error indicating that invalid JSON was received by the server. This error is returned when the server
    cannot parse the JSON text of a message.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpParseError"]
    class_class_curie: ClassVar[str] = "mcp:McpParseError"
    class_name: ClassVar[str] = "McpParseError"
    class_model_uri: ClassVar[URIRef] = MCP.McpParseError

    code: int = None
    message: str = None
    data: Optional[Union[dict, McpJSONValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        super().__post_init__(**kwargs)


class McpPrimitiveSchemaDefinition(YAMLRoot):
    """
    Restricted schema definitions that only allow primitive types
    without nested objects or arrays.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPrimitiveSchemaDefinition"]
    class_class_curie: ClassVar[str] = "mcp:McpPrimitiveSchemaDefinition"
    class_name: ClassVar[str] = "McpPrimitiveSchemaDefinition"
    class_model_uri: ClassVar[URIRef] = MCP.McpPrimitiveSchemaDefinition


@dataclass(repr=False)
class McpProgressNotification(McpJSONRPCNotification):
    """
    An out-of-band notification used to inform the receiver of a progress update for a long-running request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpProgressNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpProgressNotification"
    class_name: ClassVar[str] = "McpProgressNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpProgressNotification

    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpProgressNotificationParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpProgressNotificationParams):
            self.params = McpProgressNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpProgressNotificationParams(McpNotificationParams):
    """
    Parameters for a {@link ProgressNotificationnotifications/progress} notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpProgressNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:McpProgressNotificationParams"
    class_name: ClassVar[str] = "McpProgressNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpProgressNotificationParams

    progress: float = None
    progressToken: Union[str, int] = None
    _meta: Optional[Union[dict, McpNotificationMetaObject]] = None
    message: Optional[str] = None
    total: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.progress):
            self.MissingRequiredField("progress")
        if not isinstance(self.progress, float):
            self.progress = float(self.progress)

        if self._is_empty(self.progressToken):
            self.MissingRequiredField("progressToken")
        if not isinstance(self.progressToken, (str, int)):
            value = self.progressToken
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.progressToken = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot progressToken")

        if self._meta is not None and not isinstance(self._meta, McpNotificationMetaObject):
            self._meta = McpNotificationMetaObject(**as_dict(self._meta))

        if self.message is not None and not isinstance(self.message, str):
            self.message = str(self.message)

        if self.total is not None and not isinstance(self.total, float):
            self.total = float(self.total)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPrompt(McpBaseMetadata):
    """
    A prompt or prompt template that the server offers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPrompt"]
    class_class_curie: ClassVar[str] = "mcp:McpPrompt"
    class_name: ClassVar[str] = "McpPrompt"
    class_model_uri: ClassVar[URIRef] = MCP.McpPrompt

    name: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    arguments: Optional[Union[Union[dict, "McpPromptArgument"], list[Union[dict, "McpPromptArgument"]]]] = empty_list()
    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        self._normalize_inlined_as_list(slot_name="arguments", slot_type=McpPromptArgument, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPromptArgument(McpBaseMetadata):
    """
    Describes an argument that a prompt can accept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPromptArgument"]
    class_class_curie: ClassVar[str] = "mcp:McpPromptArgument"
    class_name: ClassVar[str] = "McpPromptArgument"
    class_model_uri: ClassVar[URIRef] = MCP.McpPromptArgument

    name: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    required: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.required is not None and not isinstance(self.required, Bool):
            self.required = Bool(self.required)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPromptListChangedNotification(McpJSONRPCNotification):
    """
    An optional notification from the server to the client, informing it that the list of prompts it offers has
    changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client
    requested it via the `promptsListChanged` filter field.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPromptListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpPromptListChangedNotification"
    class_name: ClassVar[str] = "McpPromptListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpPromptListChangedNotification

    jsonrpc: str = None
    method: str = None
    params: Optional[Union[dict, McpNotificationParams]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpNotificationParams):
            self.params = McpNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPromptMessage(YAMLRoot):
    """
    Describes a message returned as part of a prompt.

    This is similar to {@link SamplingMessage}, but also supports the embedding of
    resources from the MCP server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPromptMessage"]
    class_class_curie: ClassVar[str] = "mcp:McpPromptMessage"
    class_name: ClassVar[str] = "McpPromptMessage"
    class_model_uri: ClassVar[URIRef] = MCP.McpPromptMessage

    content: Union[dict, McpContentBlock] = None
    role: Union[str, "McpRole"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, McpContentBlock):
            self.content = McpContentBlock()

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, McpRole):
            self.role = McpRole(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPromptReference(McpBaseMetadata):
    """
    Identifies a prompt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPromptReference"]
    class_class_curie: ClassVar[str] = "mcp:McpPromptReference"
    class_name: ClassVar[str] = "McpPromptReference"
    class_model_uri: ClassVar[URIRef] = MCP.McpPromptReference

    name: str = None
    kind: str = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpReadResourceResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link ReadResourceRequestresources/read} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpReadResourceResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpReadResourceResultResponse"
    class_name: ClassVar[str] = "McpReadResourceResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpReadResourceResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, "McpInputRequiredResult", "McpReadResourceResult"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, (McpInputRequiredResult, McpReadResourceResult)):
            value = self.result
            for _coerce in (lambda: McpInputRequiredResult(**as_dict(value)), lambda: McpReadResourceResult(**as_dict(value))):
                try:
                    self.result = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpInputRequiredResult, McpReadResourceResult] could be constructed from {value!r} for slot result")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpRequest(YAMLRoot):
    """
    The method and the parameters a request carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpRequest"
    class_name: ClassVar[str] = "McpRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpRequest

    method: str = None
    params: Optional[Union[dict, McpJSONObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpJSONObject):
            self.params = McpJSONObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpJSONRPCRequest(McpRequest):
    """
    A request that expects a response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpJSONRPCRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpJSONRPCRequest"
    class_name: ClassVar[str] = "McpJSONRPCRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpJSONRPCRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Optional[Union[dict, McpJSONObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpJSONObject):
            self.params = McpJSONObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCallToolRequest(McpJSONRPCRequest):
    """
    Used by the client to invoke a tool provided by the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCallToolRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpCallToolRequest"
    class_name: ClassVar[str] = "McpCallToolRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpCallToolRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpCallToolRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpCallToolRequestParams):
            self.params = McpCallToolRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCompleteRequest(McpJSONRPCRequest):
    """
    A request from the client to the server, to ask for completion options.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteRequest"
    class_name: ClassVar[str] = "McpCompleteRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpCompleteRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpCompleteRequestParams):
            self.params = McpCompleteRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpDiscoverRequest(McpJSONRPCRequest):
    """
    A request from the client asking the server to advertise its supported
    protocol versions, capabilities, and other metadata. Servers **MUST**
    implement `server/discover`. Clients **MAY** call it but are not required
    to — version negotiation can also happen inline via per-request `_meta`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpDiscoverRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpDiscoverRequest"
    class_name: ClassVar[str] = "McpDiscoverRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpDiscoverRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpRequestParams):
            self.params = McpRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpGetPromptRequest(McpJSONRPCRequest):
    """
    Used by the client to get a prompt provided by the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpGetPromptRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpGetPromptRequest"
    class_name: ClassVar[str] = "McpGetPromptRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpGetPromptRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpGetPromptRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpGetPromptRequestParams):
            self.params = McpGetPromptRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPaginatedRequest(McpJSONRPCRequest):
    """
    A request for a list that the server returns a page at a time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPaginatedRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpPaginatedRequest"
    class_name: ClassVar[str] = "McpPaginatedRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpPaginatedRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpPaginatedRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpPaginatedRequestParams):
            self.params = McpPaginatedRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListPromptsRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of prompts and prompt templates the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListPromptsRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpListPromptsRequest"
    class_name: ClassVar[str] = "McpListPromptsRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpListPromptsRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpPaginatedRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpPaginatedRequestParams):
            self.params = McpPaginatedRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListResourceTemplatesRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of resource templates the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListResourceTemplatesRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpListResourceTemplatesRequest"
    class_name: ClassVar[str] = "McpListResourceTemplatesRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpListResourceTemplatesRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpPaginatedRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpPaginatedRequestParams):
            self.params = McpPaginatedRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListResourcesRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of resources the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListResourcesRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpListResourcesRequest"
    class_name: ClassVar[str] = "McpListResourcesRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpListResourcesRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpPaginatedRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpPaginatedRequestParams):
            self.params = McpPaginatedRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListToolsRequest(McpPaginatedRequest):
    """
    Sent from the client to request a list of tools the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListToolsRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpListToolsRequest"
    class_name: ClassVar[str] = "McpListToolsRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpListToolsRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpPaginatedRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpPaginatedRequestParams):
            self.params = McpPaginatedRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpReadResourceRequest(McpJSONRPCRequest):
    """
    Sent from the client to the server, to read a specific resource URI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpReadResourceRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpReadResourceRequest"
    class_name: ClassVar[str] = "McpReadResourceRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpReadResourceRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpReadResourceRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpReadResourceRequestParams):
            self.params = McpReadResourceRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpRequestMetaObject(McpMetaObject):
    """
    Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpRequestMetaObject"]
    class_class_curie: ClassVar[str] = "mcp:McpRequestMetaObject"
    class_name: ClassVar[str] = "McpRequestMetaObject"
    class_model_uri: ClassVar[URIRef] = MCP.McpRequestMetaObject

    mcp_client_capabilities: Union[dict, McpClientCapabilities] = None
    mcp_protocol_version: str = None
    mcp_client_info: Optional[Union[dict, McpImplementation]] = None
    mcp_log_level: Optional[Union[str, "McpLoggingLevel"]] = None
    progressToken: Optional[Union[str, int]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mcp_client_capabilities):
            self.MissingRequiredField("mcp_client_capabilities")
        if not isinstance(self.mcp_client_capabilities, McpClientCapabilities):
            self.mcp_client_capabilities = McpClientCapabilities(**as_dict(self.mcp_client_capabilities))

        if self._is_empty(self.mcp_protocol_version):
            self.MissingRequiredField("mcp_protocol_version")
        if not isinstance(self.mcp_protocol_version, str):
            self.mcp_protocol_version = str(self.mcp_protocol_version)

        if self.mcp_client_info is not None and not isinstance(self.mcp_client_info, McpImplementation):
            self.mcp_client_info = McpImplementation(**as_dict(self.mcp_client_info))

        if self.mcp_log_level is not None and not isinstance(self.mcp_log_level, McpLoggingLevel):
            self.mcp_log_level = McpLoggingLevel(self.mcp_log_level)

        if self.progressToken is not None and not isinstance(self.progressToken, (str, int)):
            value = self.progressToken
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.progressToken = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot progressToken")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpRequestParams(YAMLRoot):
    """
    Common params for any request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpRequestParams"
    class_name: ClassVar[str] = "McpRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCompleteRequestParams(McpRequestParams):
    """
    Parameters for a `completion/complete` request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteRequestParams"
    class_name: ClassVar[str] = "McpCompleteRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None
    argument: Union[dict, McpCompleteRequestParamsArgument] = None
    ref: Union[dict, McpPromptReference, "McpResourceTemplateReference"] = None
    context_info: Optional[Union[dict, McpCompleteRequestParamsContext]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self._is_empty(self.argument):
            self.MissingRequiredField("argument")
        if not isinstance(self.argument, McpCompleteRequestParamsArgument):
            self.argument = McpCompleteRequestParamsArgument(**as_dict(self.argument))

        if self._is_empty(self.ref):
            self.MissingRequiredField("ref")
        if not isinstance(self.ref, (McpPromptReference, McpResourceTemplateReference)):
            value = self.ref
            for _coerce in (lambda: McpPromptReference(**as_dict(value)), lambda: McpResourceTemplateReference(**as_dict(value))):
                try:
                    self.ref = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpPromptReference, McpResourceTemplateReference] could be constructed from {value!r} for slot ref")

        if self.context_info is not None and not isinstance(self.context_info, McpCompleteRequestParamsContext):
            self.context_info = McpCompleteRequestParamsContext(**as_dict(self.context_info))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpInputResponseRequestParams(McpRequestParams):
    """
    The parameters of a request the client retries after an input-required result: its responses to the server's
    requests, and the state the server returned.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInputResponseRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpInputResponseRequestParams"
    class_name: ClassVar[str] = "McpInputResponseRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpInputResponseRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None
    inputResponses: Optional[Union[dict, McpInputResponses]] = None
    requestState: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self.inputResponses is not None and not isinstance(self.inputResponses, McpInputResponses):
            self.inputResponses = McpInputResponses()

        if self.requestState is not None and not isinstance(self.requestState, str):
            self.requestState = str(self.requestState)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCallToolRequestParams(McpInputResponseRequestParams):
    """
    Parameters for a `tools/call` request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCallToolRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpCallToolRequestParams"
    class_name: ClassVar[str] = "McpCallToolRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpCallToolRequestParams

    name: str = None
    _meta: Union[dict, McpRequestMetaObject] = None
    arguments: Optional[Union[dict, McpJSONObject]] = None
    inputResponses: Optional[Union[dict, McpInputResponses]] = None
    requestState: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self.arguments is not None and not isinstance(self.arguments, McpJSONObject):
            self.arguments = McpJSONObject()

        if self.inputResponses is not None and not isinstance(self.inputResponses, McpInputResponses):
            self.inputResponses = McpInputResponses()

        if self.requestState is not None and not isinstance(self.requestState, str):
            self.requestState = str(self.requestState)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpGetPromptRequestParams(McpInputResponseRequestParams):
    """
    Parameters for a `prompts/get` request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpGetPromptRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpGetPromptRequestParams"
    class_name: ClassVar[str] = "McpGetPromptRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpGetPromptRequestParams

    name: str = None
    _meta: Union[dict, McpRequestMetaObject] = None
    arguments: Optional[Union[dict, McpGetPromptRequestParamsArguments]] = None
    inputResponses: Optional[Union[dict, McpInputResponses]] = None
    requestState: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self.arguments is not None and not isinstance(self.arguments, McpGetPromptRequestParamsArguments):
            self.arguments = McpGetPromptRequestParamsArguments()

        if self.inputResponses is not None and not isinstance(self.inputResponses, McpInputResponses):
            self.inputResponses = McpInputResponses()

        if self.requestState is not None and not isinstance(self.requestState, str):
            self.requestState = str(self.requestState)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPaginatedRequestParams(McpRequestParams):
    """
    Common params for paginated requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPaginatedRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpPaginatedRequestParams"
    class_name: ClassVar[str] = "McpPaginatedRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpPaginatedRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None
    cursor: Optional[Union[str, McpCursor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self.cursor is not None and not isinstance(self.cursor, McpCursor):
            self.cursor = McpCursor(self.cursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResource(McpBaseMetadata):
    """
    A known resource that the server is capable of reading.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResource"]
    class_class_curie: ClassVar[str] = "mcp:McpResource"
    class_name: ClassVar[str] = "McpResource"
    class_model_uri: ClassVar[URIRef] = MCP.McpResource

    name: str = None
    uri: Union[str, URI] = None
    description: Optional[str] = None
    title: Optional[str] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None
    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()
    mimeType: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceContents(YAMLRoot):
    """
    The contents of a specific resource or sub-resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceContents"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceContents"
    class_name: ClassVar[str] = "McpResourceContents"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceContents

    uri: Union[str, URI] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    mimeType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpBlobResourceContents(McpResourceContents):
    """
    A resource's contents as binary data, given as base64 text.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpBlobResourceContents"]
    class_class_curie: ClassVar[str] = "mcp:McpBlobResourceContents"
    class_name: ClassVar[str] = "McpBlobResourceContents"
    class_model_uri: ClassVar[URIRef] = MCP.McpBlobResourceContents

    blob: Union[str, McpBase64] = None
    uri: Union[str, URI] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    mimeType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.blob):
            self.MissingRequiredField("blob")
        if not isinstance(self.blob, McpBase64):
            self.blob = McpBase64(self.blob)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceLink(McpResource):
    """
    A resource that the server is capable of reading, included in a prompt or tool call result.

    Note: resource links returned by tools are not guaranteed to appear in the results of {@link
    ListResourcesRequestresources/list} requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceLink"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceLink"
    class_name: ClassVar[str] = "McpResourceLink"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceLink

    name: str = None
    kind: str = None
    uri: Union[str, URI] = None
    description: Optional[str] = None
    title: Optional[str] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None
    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()
    mimeType: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceListChangedNotification(McpJSONRPCNotification):
    """
    An optional notification from the server to the client, informing it that the list of resources it can read from
    has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the
    client requested it via the `resourcesListChanged` filter field.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceListChangedNotification"
    class_name: ClassVar[str] = "McpResourceListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceListChangedNotification

    jsonrpc: str = None
    method: str = None
    params: Optional[Union[dict, McpNotificationParams]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpNotificationParams):
            self.params = McpNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceRequestParams(McpRequestParams):
    """
    Common params for resource-related requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceRequestParams"
    class_name: ClassVar[str] = "McpResourceRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None
    uri: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpReadResourceRequestParams(McpResourceRequestParams):
    """
    Parameters for a `resources/read` request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpReadResourceRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpReadResourceRequestParams"
    class_name: ClassVar[str] = "McpReadResourceRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpReadResourceRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None
    uri: Union[str, URI] = None
    inputResponses: Optional[Union[dict, McpInputResponses]] = None
    requestState: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self.inputResponses is not None and not isinstance(self.inputResponses, McpInputResponses):
            self.inputResponses = McpInputResponses()

        if self.requestState is not None and not isinstance(self.requestState, str):
            self.requestState = str(self.requestState)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceTemplate(McpBaseMetadata):
    """
    A template description for resources available on the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceTemplate"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceTemplate"
    class_name: ClassVar[str] = "McpResourceTemplate"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceTemplate

    name: str = None
    uriTemplate: Union[str, McpUriTemplate] = None
    description: Optional[str] = None
    title: Optional[str] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None
    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()
    mimeType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.uriTemplate):
            self.MissingRequiredField("uriTemplate")
        if not isinstance(self.uriTemplate, McpUriTemplate):
            self.uriTemplate = McpUriTemplate(self.uriTemplate)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceTemplateReference(YAMLRoot):
    """
    A reference to a resource or resource template definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceTemplateReference"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceTemplateReference"
    class_name: ClassVar[str] = "McpResourceTemplateReference"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceTemplateReference

    kind: str = None
    uri: Union[str, McpUriTemplate] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, McpUriTemplate):
            self.uri = McpUriTemplate(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceUpdatedNotification(McpJSONRPCNotification):
    """
    A notification from the server to the client, informing it that a resource has changed and may need to be read
    again. This is only sent for resources the client opted in to via the `resourceSubscriptions` field of a {@link
    SubscriptionsListenRequestsubscriptions/listen} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceUpdatedNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceUpdatedNotification"
    class_name: ClassVar[str] = "McpResourceUpdatedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceUpdatedNotification

    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpResourceUpdatedNotificationParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpResourceUpdatedNotificationParams):
            self.params = McpResourceUpdatedNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResourceUpdatedNotificationParams(McpNotificationParams):
    """
    Parameters for a `notifications/resources/updated` notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResourceUpdatedNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:McpResourceUpdatedNotificationParams"
    class_name: ClassVar[str] = "McpResourceUpdatedNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpResourceUpdatedNotificationParams

    uri: Union[str, URI] = None
    _meta: Optional[Union[dict, McpNotificationMetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._meta is not None and not isinstance(self._meta, McpNotificationMetaObject):
            self._meta = McpNotificationMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResult(YAMLRoot):
    """
    Common result fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResult"]
    class_class_curie: ClassVar[str] = "mcp:McpResult"
    class_name: ClassVar[str] = "McpResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpResult

    resultType: Union[str, McpResultType] = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCacheableResult(McpResult):
    """
    A result that supports a time-to-live (TTL) hint for client-side caching.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCacheableResult"]
    class_class_curie: ClassVar[str] = "mcp:McpCacheableResult"
    class_name: ClassVar[str] = "McpCacheableResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpCacheableResult

    cacheScope: Union[str, "McpCacheScope"] = None
    resultType: Union[str, McpResultType] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCallToolResult(McpResult):
    """
    The result returned by the server for a {@link CallToolRequesttools/call} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCallToolResult"]
    class_class_curie: ClassVar[str] = "mcp:McpCallToolResult"
    class_name: ClassVar[str] = "McpCallToolResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpCallToolResult

    content: Union[Union[dict, McpContentBlock], list[Union[dict, McpContentBlock]]] = None
    resultType: Union[str, McpResultType] = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    isError: Optional[Union[bool, Bool]] = None
    structuredContent: Optional[Union[dict, McpJSONValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, McpContentBlock) else McpContentBlock(**as_dict(v)) for v in self.content]

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.isError is not None and not isinstance(self.isError, Bool):
            self.isError = Bool(self.isError)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCompleteResult(McpResult):
    """
    The result returned by the server for a {@link CompleteRequestcompletion/complete} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCompleteResult"]
    class_class_curie: ClassVar[str] = "mcp:McpCompleteResult"
    class_name: ClassVar[str] = "McpCompleteResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpCompleteResult

    completion: Union[dict, McpCompleteResultCompletion] = None
    resultType: Union[str, McpResultType] = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.completion):
            self.MissingRequiredField("completion")
        if not isinstance(self.completion, McpCompleteResultCompletion):
            self.completion = McpCompleteResultCompletion(**as_dict(self.completion))

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpDiscoverResult(McpCacheableResult):
    """
    The result returned by the server for a {@link DiscoverRequestserver/discover} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpDiscoverResult"]
    class_class_curie: ClassVar[str] = "mcp:McpDiscoverResult"
    class_name: ClassVar[str] = "McpDiscoverResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpDiscoverResult

    cacheScope: Union[str, "McpCacheScope"] = None
    capabilities: Union[dict, "McpServerCapabilities"] = None
    resultType: Union[str, McpResultType] = None
    supportedVersions: Union[str, list[str]] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    instructions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.capabilities):
            self.MissingRequiredField("capabilities")
        if not isinstance(self.capabilities, McpServerCapabilities):
            self.capabilities = McpServerCapabilities(**as_dict(self.capabilities))

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.supportedVersions):
            self.MissingRequiredField("supportedVersions")
        if not isinstance(self.supportedVersions, list):
            self.supportedVersions = [self.supportedVersions] if self.supportedVersions is not None else []
        self.supportedVersions = [v if isinstance(v, str) else str(v) for v in self.supportedVersions]

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.instructions is not None and not isinstance(self.instructions, str):
            self.instructions = str(self.instructions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpEmptyResult(McpResult):
    """
    Common result fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpEmptyResult"]
    class_class_curie: ClassVar[str] = "mcp:McpEmptyResult"
    class_name: ClassVar[str] = "McpEmptyResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpEmptyResult

    resultType: Union[str, McpResultType] = None

@dataclass(repr=False)
class McpClientResult(McpEmptyResult):
    """
    Common result fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpClientResult"]
    class_class_curie: ClassVar[str] = "mcp:McpClientResult"
    class_name: ClassVar[str] = "McpClientResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpClientResult

    resultType: Union[str, McpResultType] = None

@dataclass(repr=False)
class McpGetPromptResult(McpResult):
    """
    The result returned by the server for a {@link GetPromptRequestprompts/get} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpGetPromptResult"]
    class_class_curie: ClassVar[str] = "mcp:McpGetPromptResult"
    class_name: ClassVar[str] = "McpGetPromptResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpGetPromptResult

    messages: Union[Union[dict, McpPromptMessage], list[Union[dict, McpPromptMessage]]] = None
    resultType: Union[str, McpResultType] = None
    description: Optional[str] = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=McpPromptMessage, key_name="role", keyed=False)

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpInputRequiredResult(McpResult):
    """
    An InputRequiredResult sent by the server to indicate that additional input is needed
    before the request can be completed.

    At least one of `inputRequests` or `requestState` MUST be present.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpInputRequiredResult"]
    class_class_curie: ClassVar[str] = "mcp:McpInputRequiredResult"
    class_name: ClassVar[str] = "McpInputRequiredResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpInputRequiredResult

    resultType: Union[str, McpResultType] = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    inputRequests: Optional[Union[dict, McpInputRequests]] = None
    requestState: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.inputRequests is not None and not isinstance(self.inputRequests, McpInputRequests):
            self.inputRequests = McpInputRequests()

        if self.requestState is not None and not isinstance(self.requestState, str):
            self.requestState = str(self.requestState)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpPaginatedResult(McpResult):
    """
    A result that holds a page of a list, and the cursor of the next page.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpPaginatedResult"]
    class_class_curie: ClassVar[str] = "mcp:McpPaginatedResult"
    class_name: ClassVar[str] = "McpPaginatedResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpPaginatedResult

    resultType: Union[str, McpResultType] = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    nextCursor: Optional[Union[str, McpCursor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.nextCursor is not None and not isinstance(self.nextCursor, McpCursor):
            self.nextCursor = McpCursor(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListPromptsResult(McpPaginatedResult):
    """
    The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListPromptsResult"]
    class_class_curie: ClassVar[str] = "mcp:McpListPromptsResult"
    class_name: ClassVar[str] = "McpListPromptsResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpListPromptsResult

    cacheScope: Union[str, "McpCacheScope"] = None
    prompts: Union[Union[dict, McpPrompt], list[Union[dict, McpPrompt]]] = None
    resultType: Union[str, McpResultType] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    nextCursor: Optional[Union[str, McpCursor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.prompts):
            self.MissingRequiredField("prompts")
        self._normalize_inlined_as_list(slot_name="prompts", slot_type=McpPrompt, key_name="name", keyed=False)

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.nextCursor is not None and not isinstance(self.nextCursor, McpCursor):
            self.nextCursor = McpCursor(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListResourceTemplatesResult(McpPaginatedResult):
    """
    The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListResourceTemplatesResult"]
    class_class_curie: ClassVar[str] = "mcp:McpListResourceTemplatesResult"
    class_name: ClassVar[str] = "McpListResourceTemplatesResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpListResourceTemplatesResult

    cacheScope: Union[str, "McpCacheScope"] = None
    resourceTemplates: Union[Union[dict, McpResourceTemplate], list[Union[dict, McpResourceTemplate]]] = None
    resultType: Union[str, McpResultType] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    nextCursor: Optional[Union[str, McpCursor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.resourceTemplates):
            self.MissingRequiredField("resourceTemplates")
        self._normalize_inlined_as_list(slot_name="resourceTemplates", slot_type=McpResourceTemplate, key_name="name", keyed=False)

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.nextCursor is not None and not isinstance(self.nextCursor, McpCursor):
            self.nextCursor = McpCursor(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListResourcesResult(McpPaginatedResult):
    """
    The result returned by the server for a {@link ListResourcesRequestresources/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListResourcesResult"]
    class_class_curie: ClassVar[str] = "mcp:McpListResourcesResult"
    class_name: ClassVar[str] = "McpListResourcesResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpListResourcesResult

    cacheScope: Union[str, "McpCacheScope"] = None
    resources: Union[Union[dict, McpResource], list[Union[dict, McpResource]]] = None
    resultType: Union[str, McpResultType] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    nextCursor: Optional[Union[str, McpCursor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.resources):
            self.MissingRequiredField("resources")
        self._normalize_inlined_as_list(slot_name="resources", slot_type=McpResource, key_name="name", keyed=False)

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.nextCursor is not None and not isinstance(self.nextCursor, McpCursor):
            self.nextCursor = McpCursor(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpListToolsResult(McpPaginatedResult):
    """
    The result returned by the server for a {@link ListToolsRequesttools/list} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpListToolsResult"]
    class_class_curie: ClassVar[str] = "mcp:McpListToolsResult"
    class_name: ClassVar[str] = "McpListToolsResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpListToolsResult

    cacheScope: Union[str, "McpCacheScope"] = None
    resultType: Union[str, McpResultType] = None
    tools: Union[Union[dict, "McpTool"], list[Union[dict, "McpTool"]]] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None
    nextCursor: Optional[Union[str, McpCursor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.tools):
            self.MissingRequiredField("tools")
        self._normalize_inlined_as_list(slot_name="tools", slot_type=McpTool, key_name="name", keyed=False)

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        if self.nextCursor is not None and not isinstance(self.nextCursor, McpCursor):
            self.nextCursor = McpCursor(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpReadResourceResult(McpCacheableResult):
    """
    The result returned by the server for a {@link ReadResourceRequestresources/read} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpReadResourceResult"]
    class_class_curie: ClassVar[str] = "mcp:McpReadResourceResult"
    class_name: ClassVar[str] = "McpReadResourceResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpReadResourceResult

    cacheScope: Union[str, "McpCacheScope"] = None
    contents: Union[str, list[str]] = None
    resultType: Union[str, McpResultType] = None
    ttlMs: int = None
    _meta: Optional[Union[dict, "McpResultMetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cacheScope):
            self.MissingRequiredField("cacheScope")
        if not isinstance(self.cacheScope, McpCacheScope):
            self.cacheScope = McpCacheScope(self.cacheScope)

        if self._is_empty(self.contents):
            self.MissingRequiredField("contents")
        if not isinstance(self.contents, list):
            self.contents = [self.contents] if self.contents is not None else []
        self.contents = [v if isinstance(v, str) else str(v) for v in self.contents]

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        if self._is_empty(self.ttlMs):
            self.MissingRequiredField("ttlMs")
        if not isinstance(self.ttlMs, int):
            self.ttlMs = int(self.ttlMs)

        if self._meta is not None and not isinstance(self._meta, McpResultMetaObject):
            self._meta = McpResultMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpResultMetaObject(McpMetaObject):
    """
    Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpResultMetaObject"]
    class_class_curie: ClassVar[str] = "mcp:McpResultMetaObject"
    class_name: ClassVar[str] = "McpResultMetaObject"
    class_model_uri: ClassVar[URIRef] = MCP.McpResultMetaObject

    mcp_server_info: Optional[Union[dict, McpImplementation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mcp_server_info is not None and not isinstance(self.mcp_server_info, McpImplementation):
            self.mcp_server_info = McpImplementation(**as_dict(self.mcp_server_info))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpRoot(YAMLRoot):
    """
    Represents a root directory or file that the server can operate on.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpRoot"]
    class_class_curie: ClassVar[str] = "mcp:McpRoot"
    class_name: ClassVar[str] = "McpRoot"
    class_model_uri: ClassVar[URIRef] = MCP.McpRoot

    uri: Union[str, URI] = None
    name: Optional[str] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSamplingMessage(YAMLRoot):
    """
    Describes a message issued to or received from an LLM API.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSamplingMessage"]
    class_class_curie: ClassVar[str] = "mcp:McpSamplingMessage"
    class_name: ClassVar[str] = "McpSamplingMessage"
    class_model_uri: ClassVar[URIRef] = MCP.McpSamplingMessage

    content: Union[dict, "McpTextContent", McpImageContent, McpAudioContent, "McpToolUseContent", "McpToolResultContent", "McpSamplingMessageContentBlock"] = None
    role: Union[str, "McpRole"] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, (McpTextContent, McpImageContent, McpAudioContent, McpToolUseContent, McpToolResultContent, McpSamplingMessageContentBlock)):
            value = self.content
            for _coerce in (lambda: McpTextContent(**as_dict(value)), lambda: McpImageContent(**as_dict(value)), lambda: McpAudioContent(**as_dict(value)), lambda: McpToolUseContent(**as_dict(value)), lambda: McpToolResultContent(**as_dict(value)), lambda: McpSamplingMessageContentBlock()):
                try:
                    self.content = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpTextContent, McpImageContent, McpAudioContent, McpToolUseContent, McpToolResultContent, McpSamplingMessageContentBlock] could be constructed from {value!r} for slot content")

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, McpRole):
            self.role = McpRole(self.role)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpCreateMessageResult(McpSamplingMessage):
    """
    The result returned by the client for a {@link CreateMessageRequestsampling/createMessage} request.
    The client should inform the user before returning the sampled message, to allow them
    to inspect the response (human in the loop) and decide whether to allow the server to see it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpCreateMessageResult"]
    class_class_curie: ClassVar[str] = "mcp:McpCreateMessageResult"
    class_name: ClassVar[str] = "McpCreateMessageResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpCreateMessageResult

    content: Union[dict, "McpTextContent", McpImageContent, McpAudioContent, "McpToolUseContent", "McpToolResultContent", "McpSamplingMessageContentBlock"] = None
    model: str = None
    role: Union[str, "McpRole"] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    stopReason: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, (McpTextContent, McpImageContent, McpAudioContent, McpToolUseContent, McpToolResultContent, McpSamplingMessageContentBlock)):
            value = self.content
            for _coerce in (lambda: McpTextContent(**as_dict(value)), lambda: McpImageContent(**as_dict(value)), lambda: McpAudioContent(**as_dict(value)), lambda: McpToolUseContent(**as_dict(value)), lambda: McpToolResultContent(**as_dict(value)), lambda: McpSamplingMessageContentBlock()):
                try:
                    self.content = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[McpTextContent, McpImageContent, McpAudioContent, McpToolUseContent, McpToolResultContent, McpSamplingMessageContentBlock] could be constructed from {value!r} for slot content")

        if self._is_empty(self.model):
            self.MissingRequiredField("model")
        if not isinstance(self.model, str):
            self.model = str(self.model)

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, McpRole):
            self.role = McpRole(self.role)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.stopReason is not None and not isinstance(self.stopReason, str):
            self.stopReason = str(self.stopReason)

        super().__post_init__(**kwargs)


class McpSamplingMessageContentBlock(YAMLRoot):
    """
    One of `TextContent`, `ImageContent`, `AudioContent`, `ToolUseContent`, `ToolResultContent`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSamplingMessageContentBlock"]
    class_class_curie: ClassVar[str] = "mcp:McpSamplingMessageContentBlock"
    class_name: ClassVar[str] = "McpSamplingMessageContentBlock"
    class_model_uri: ClassVar[URIRef] = MCP.McpSamplingMessageContentBlock


@dataclass(repr=False)
class McpServerCapabilities(YAMLRoot):
    """
    Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a
    closed set: any server can define its own, additional capabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerCapabilities"]
    class_class_curie: ClassVar[str] = "mcp:McpServerCapabilities"
    class_name: ClassVar[str] = "McpServerCapabilities"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerCapabilities

    completions: Optional[Union[dict, McpJSONObject]] = None
    experimental: Optional[Union[dict, "McpServerCapabilitiesExperimental"]] = None
    extensions: Optional[Union[dict, "McpServerCapabilitiesExtensions"]] = None
    logging: Optional[Union[dict, McpJSONObject]] = None
    prompts: Optional[Union[dict, "McpServerCapabilitiesPrompts"]] = None
    resources: Optional[Union[dict, "McpServerCapabilitiesResources"]] = None
    tools: Optional[Union[dict, "McpServerCapabilitiesTools"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.completions is not None and not isinstance(self.completions, McpJSONObject):
            self.completions = McpJSONObject()

        if self.experimental is not None and not isinstance(self.experimental, McpServerCapabilitiesExperimental):
            self.experimental = McpServerCapabilitiesExperimental()

        if self.extensions is not None and not isinstance(self.extensions, McpServerCapabilitiesExtensions):
            self.extensions = McpServerCapabilitiesExtensions()

        if self.logging is not None and not isinstance(self.logging, McpJSONObject):
            self.logging = McpJSONObject()

        if self.prompts is not None and not isinstance(self.prompts, McpServerCapabilitiesPrompts):
            self.prompts = McpServerCapabilitiesPrompts(**as_dict(self.prompts))

        if self.resources is not None and not isinstance(self.resources, McpServerCapabilitiesResources):
            self.resources = McpServerCapabilitiesResources(**as_dict(self.resources))

        if self.tools is not None and not isinstance(self.tools, McpServerCapabilitiesTools):
            self.tools = McpServerCapabilitiesTools(**as_dict(self.tools))

        super().__post_init__(**kwargs)


class McpServerCapabilitiesExperimental(YAMLRoot):
    """
    Experimental, non-standard capabilities that the server supports.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerCapabilitiesExperimental"]
    class_class_curie: ClassVar[str] = "mcp:McpServerCapabilitiesExperimental"
    class_name: ClassVar[str] = "McpServerCapabilitiesExperimental"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerCapabilitiesExperimental


class McpServerCapabilitiesExtensions(YAMLRoot):
    """
    Optional MCP extensions that the server supports. Keys are extension identifiers
    (e.g., "io.modelcontextprotocol/tasks"), and values are per-extension settings
    objects. An empty object indicates support with no settings.

    Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
    mandatory prefix.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerCapabilitiesExtensions"]
    class_class_curie: ClassVar[str] = "mcp:McpServerCapabilitiesExtensions"
    class_name: ClassVar[str] = "McpServerCapabilitiesExtensions"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerCapabilitiesExtensions


@dataclass(repr=False)
class McpServerCapabilitiesPrompts(YAMLRoot):
    """
    Present if the server offers any prompt templates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerCapabilitiesPrompts"]
    class_class_curie: ClassVar[str] = "mcp:McpServerCapabilitiesPrompts"
    class_name: ClassVar[str] = "McpServerCapabilitiesPrompts"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerCapabilitiesPrompts

    listChanged: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpServerCapabilitiesResources(YAMLRoot):
    """
    Present if the server offers any resources to read.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerCapabilitiesResources"]
    class_class_curie: ClassVar[str] = "mcp:McpServerCapabilitiesResources"
    class_name: ClassVar[str] = "McpServerCapabilitiesResources"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerCapabilitiesResources

    listChanged: Optional[Union[bool, Bool]] = None
    subscribe: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        if self.subscribe is not None and not isinstance(self.subscribe, Bool):
            self.subscribe = Bool(self.subscribe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpServerCapabilitiesTools(YAMLRoot):
    """
    Present if the server offers any tools to call.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerCapabilitiesTools"]
    class_class_curie: ClassVar[str] = "mcp:McpServerCapabilitiesTools"
    class_name: ClassVar[str] = "McpServerCapabilitiesTools"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerCapabilitiesTools

    listChanged: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        super().__post_init__(**kwargs)


class McpServerNotification(YAMLRoot):
    """
    One of `CancelledNotification`, `ProgressNotification`, `ResourceListChangedNotification`,
    `SubscriptionsAcknowledgedNotification`, `ResourceUpdatedNotification`, `PromptListChangedNotification`,
    `ToolListChangedNotification`, `LoggingMessageNotification`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpServerNotification"
    class_name: ClassVar[str] = "McpServerNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerNotification


class McpServerResult(YAMLRoot):
    """
    One of `Result`, `InputRequiredResult`, `DiscoverResult`, `ListResourcesResult`, `ListResourceTemplatesResult`,
    `ReadResourceResult`, `SubscriptionsListenResult`, `ListPromptsResult`, `GetPromptResult`, `ListToolsResult`,
    `CallToolResult`, `CompleteResult`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpServerResult"]
    class_class_curie: ClassVar[str] = "mcp:McpServerResult"
    class_name: ClassVar[str] = "McpServerResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpServerResult


class McpSingleSelectEnumSchema(YAMLRoot):
    """
    One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSingleSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpSingleSelectEnumSchema"
    class_name: ClassVar[str] = "McpSingleSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpSingleSelectEnumSchema


@dataclass(repr=False)
class McpStringSchema(YAMLRoot):
    """
    A field of an elicitation form that takes text.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpStringSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpStringSchema"
    class_name: ClassVar[str] = "McpStringSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpStringSchema

    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[str] = None
    format: Optional[Union[str, "McpStringSchemaFormat"]] = None
    maxLength: Optional[int] = None
    minLength: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.default is not None and not isinstance(self.default, str):
            self.default = str(self.default)

        if self.format is not None and not isinstance(self.format, McpStringSchemaFormat):
            self.format = McpStringSchemaFormat(self.format)

        if self.maxLength is not None and not isinstance(self.maxLength, int):
            self.maxLength = int(self.maxLength)

        if self.minLength is not None and not isinstance(self.minLength, int):
            self.minLength = int(self.minLength)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionFilter(YAMLRoot):
    """
    The set of notification types a client may opt in to on a
    {@link SubscriptionsListenRequestsubscriptions/listen} request.

    Each notification type is **opt-in**; the server **MUST NOT** send
    notification types the client has not explicitly requested here.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionFilter"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionFilter"
    class_name: ClassVar[str] = "McpSubscriptionFilter"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionFilter

    promptsListChanged: Optional[Union[bool, Bool]] = None
    resourceSubscriptions: Optional[Union[str, list[str]]] = empty_list()
    resourcesListChanged: Optional[Union[bool, Bool]] = None
    toolsListChanged: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.promptsListChanged is not None and not isinstance(self.promptsListChanged, Bool):
            self.promptsListChanged = Bool(self.promptsListChanged)

        if not isinstance(self.resourceSubscriptions, list):
            self.resourceSubscriptions = [self.resourceSubscriptions] if self.resourceSubscriptions is not None else []
        self.resourceSubscriptions = [v if isinstance(v, str) else str(v) for v in self.resourceSubscriptions]

        if self.resourcesListChanged is not None and not isinstance(self.resourcesListChanged, Bool):
            self.resourcesListChanged = Bool(self.resourcesListChanged)

        if self.toolsListChanged is not None and not isinstance(self.toolsListChanged, Bool):
            self.toolsListChanged = Bool(self.toolsListChanged)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsAcknowledgedNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsAcknowledgedNotification"
    class_name: ClassVar[str] = "McpSubscriptionsAcknowledgedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsAcknowledgedNotification

    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpSubscriptionsAcknowledgedNotificationParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpSubscriptionsAcknowledgedNotificationParams):
            self.params = McpSubscriptionsAcknowledgedNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionsAcknowledgedNotificationParams(McpNotificationParams):
    """
    Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged}
    notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsAcknowledgedNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsAcknowledgedNotificationParams"
    class_name: ClassVar[str] = "McpSubscriptionsAcknowledgedNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsAcknowledgedNotificationParams

    notifications: Union[dict, McpSubscriptionFilter] = None
    _meta: Optional[Union[dict, McpNotificationMetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.notifications):
            self.MissingRequiredField("notifications")
        if not isinstance(self.notifications, McpSubscriptionFilter):
            self.notifications = McpSubscriptionFilter(**as_dict(self.notifications))

        if self._meta is not None and not isinstance(self._meta, McpNotificationMetaObject):
            self._meta = McpNotificationMetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionsListenRequest(McpJSONRPCRequest):
    """
    Sent from the client to open a long-lived channel for receiving notifications
    outside the context of a specific request. Replaces the previous HTTP GET
    endpoint and ensures consistent behavior between HTTP and STDIO.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsListenRequest"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsListenRequest"
    class_name: ClassVar[str] = "McpSubscriptionsListenRequest"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsListenRequest

    identifier: Union[str, int] = None
    jsonrpc: str = None
    method: str = None
    params: Union[dict, "McpSubscriptionsListenRequestParams"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, McpSubscriptionsListenRequestParams):
            self.params = McpSubscriptionsListenRequestParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionsListenRequestParams(McpRequestParams):
    """
    Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsListenRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsListenRequestParams"
    class_name: ClassVar[str] = "McpSubscriptionsListenRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsListenRequestParams

    _meta: Union[dict, McpRequestMetaObject] = None
    notifications: Union[dict, McpSubscriptionFilter] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpRequestMetaObject):
            self._meta = McpRequestMetaObject(**as_dict(self._meta))

        if self._is_empty(self.notifications):
            self.MissingRequiredField("notifications")
        if not isinstance(self.notifications, McpSubscriptionFilter):
            self.notifications = McpSubscriptionFilter(**as_dict(self.notifications))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionsListenResult(McpResult):
    """
    The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
    request, signalling that the subscription has ended gracefully (for example,
    during server shutdown). Because the listen stream is long-lived, this result
    is sent only when the server tears the subscription down; an abrupt transport
    close carries no response. The result body is otherwise empty.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsListenResult"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsListenResult"
    class_name: ClassVar[str] = "McpSubscriptionsListenResult"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsListenResult

    _meta: Union[dict, "McpSubscriptionsListenResultMetaObject"] = None
    resultType: Union[str, McpResultType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._meta):
            self.MissingRequiredField("_meta")
        if not isinstance(self._meta, McpSubscriptionsListenResultMetaObject):
            self._meta = McpSubscriptionsListenResultMetaObject(**as_dict(self._meta))

        if self._is_empty(self.resultType):
            self.MissingRequiredField("resultType")
        if not isinstance(self.resultType, McpResultType):
            self.resultType = McpResultType(self.resultType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionsListenResultMetaObject(McpResultMetaObject):
    """
    Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
    {@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsListenResultMetaObject"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsListenResultMetaObject"
    class_name: ClassVar[str] = "McpSubscriptionsListenResultMetaObject"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsListenResultMetaObject

    mcp_subscription_id: Union[str, int] = None
    mcp_server_info: Optional[Union[dict, McpImplementation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mcp_subscription_id):
            self.MissingRequiredField("mcp_subscription_id")
        if not isinstance(self.mcp_subscription_id, (str, int)):
            value = self.mcp_subscription_id
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.mcp_subscription_id = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot mcp_subscription_id")

        if self.mcp_server_info is not None and not isinstance(self.mcp_server_info, McpImplementation):
            self.mcp_server_info = McpImplementation(**as_dict(self.mcp_server_info))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpSubscriptionsListenResultResponse(McpJSONRPCResultResponse):
    """
    A successful response from the server for a {@link SubscriptionsListenRequestsubscriptions/listen}
    request, sent when the server tears the subscription down gracefully.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpSubscriptionsListenResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:McpSubscriptionsListenResultResponse"
    class_name: ClassVar[str] = "McpSubscriptionsListenResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.McpSubscriptionsListenResultResponse

    identifier: Union[str, int] = None
    jsonrpc: str = None
    result: Union[dict, McpSubscriptionsListenResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, McpSubscriptionsListenResult):
            self.result = McpSubscriptionsListenResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTextContent(YAMLRoot):
    """
    Text provided to or from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTextContent"]
    class_class_curie: ClassVar[str] = "mcp:McpTextContent"
    class_name: ClassVar[str] = "McpTextContent"
    class_model_uri: ClassVar[URIRef] = MCP.McpTextContent

    text: str = None
    kind: str = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    annotations: Optional[Union[dict, McpAnnotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpAnnotations):
            self.annotations = McpAnnotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTextResourceContents(McpResourceContents):
    """
    A resource's contents as text.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTextResourceContents"]
    class_class_curie: ClassVar[str] = "mcp:McpTextResourceContents"
    class_name: ClassVar[str] = "McpTextResourceContents"
    class_model_uri: ClassVar[URIRef] = MCP.McpTextResourceContents

    text: str = None
    uri: Union[str, URI] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    mimeType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTitledMultiSelectEnumSchema(YAMLRoot):
    """
    Schema for multiple-selection enumeration with display titles for each option.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTitledMultiSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpTitledMultiSelectEnumSchema"
    class_name: ClassVar[str] = "McpTitledMultiSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpTitledMultiSelectEnumSchema

    items: Union[dict, "McpTitledMultiSelectEnumSchemaItems"] = None
    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[Union[str, list[str]]] = empty_list()
    maxItems: Optional[int] = None
    minItems: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.items):
            self.MissingRequiredField("items")
        if not isinstance(self.items, McpTitledMultiSelectEnumSchemaItems):
            self.items = McpTitledMultiSelectEnumSchemaItems(**as_dict(self.items))

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, str) else str(v) for v in self.default]

        if self.maxItems is not None and not isinstance(self.maxItems, int):
            self.maxItems = int(self.maxItems)

        if self.minItems is not None and not isinstance(self.minItems, int):
            self.minItems = int(self.minItems)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTitledMultiSelectEnumSchemaItems(YAMLRoot):
    """
    Schema for array items with enum options and display labels.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTitledMultiSelectEnumSchemaItems"]
    class_class_curie: ClassVar[str] = "mcp:McpTitledMultiSelectEnumSchemaItems"
    class_name: ClassVar[str] = "McpTitledMultiSelectEnumSchemaItems"
    class_model_uri: ClassVar[URIRef] = MCP.McpTitledMultiSelectEnumSchemaItems

    anyOf: Union[Union[dict, "McpTitledMultiSelectEnumSchemaItemsAnyOf"], list[Union[dict, "McpTitledMultiSelectEnumSchemaItemsAnyOf"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.anyOf):
            self.MissingRequiredField("anyOf")
        self._normalize_inlined_as_list(slot_name="anyOf", slot_type=McpTitledMultiSelectEnumSchemaItemsAnyOf, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTitledMultiSelectEnumSchemaItemsAnyOf(YAMLRoot):
    """
    The object MCP's `TitledMultiSelectEnumSchema` holds under `anyOf`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTitledMultiSelectEnumSchemaItemsAnyOf"]
    class_class_curie: ClassVar[str] = "mcp:McpTitledMultiSelectEnumSchemaItemsAnyOf"
    class_name: ClassVar[str] = "McpTitledMultiSelectEnumSchemaItemsAnyOf"
    class_model_uri: ClassVar[URIRef] = MCP.McpTitledMultiSelectEnumSchemaItemsAnyOf

    title: str = None
    const: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.const):
            self.MissingRequiredField("const")
        if not isinstance(self.const, str):
            self.const = str(self.const)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTitledSingleSelectEnumSchema(YAMLRoot):
    """
    Schema for single-selection enumeration with display titles for each option.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTitledSingleSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpTitledSingleSelectEnumSchema"
    class_name: ClassVar[str] = "McpTitledSingleSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpTitledSingleSelectEnumSchema

    oneOf: Union[Union[dict, "McpTitledSingleSelectEnumSchemaOneOf"], list[Union[dict, "McpTitledSingleSelectEnumSchemaOneOf"]]] = None
    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.oneOf):
            self.MissingRequiredField("oneOf")
        self._normalize_inlined_as_list(slot_name="oneOf", slot_type=McpTitledSingleSelectEnumSchemaOneOf, key_name="title", keyed=False)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.default is not None and not isinstance(self.default, str):
            self.default = str(self.default)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTitledSingleSelectEnumSchemaOneOf(YAMLRoot):
    """
    The object MCP's `TitledSingleSelectEnumSchema` holds under `oneOf`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTitledSingleSelectEnumSchemaOneOf"]
    class_class_curie: ClassVar[str] = "mcp:McpTitledSingleSelectEnumSchemaOneOf"
    class_name: ClassVar[str] = "McpTitledSingleSelectEnumSchemaOneOf"
    class_model_uri: ClassVar[URIRef] = MCP.McpTitledSingleSelectEnumSchemaOneOf

    title: str = None
    const: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.const):
            self.MissingRequiredField("const")
        if not isinstance(self.const, str):
            self.const = str(self.const)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpTool(McpBaseMetadata):
    """
    Definition for a tool the client can call.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpTool"]
    class_class_curie: ClassVar[str] = "mcp:McpTool"
    class_name: ClassVar[str] = "McpTool"
    class_model_uri: ClassVar[URIRef] = MCP.McpTool

    name: str = None
    inputSchema: Union[dict, "McpToolInputSchema"] = None
    description: Optional[str] = None
    title: Optional[str] = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    annotations: Optional[Union[dict, "McpToolAnnotations"]] = None
    icons: Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]] = empty_list()
    outputSchema: Optional[Union[dict, "McpToolOutputSchema"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.inputSchema):
            self.MissingRequiredField("inputSchema")
        if not isinstance(self.inputSchema, McpToolInputSchema):
            self.inputSchema = McpToolInputSchema(**as_dict(self.inputSchema))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.annotations is not None and not isinstance(self.annotations, McpToolAnnotations):
            self.annotations = McpToolAnnotations(**as_dict(self.annotations))

        self._normalize_inlined_as_list(slot_name="icons", slot_type=McpIcon, key_name="src", keyed=False)

        if self.outputSchema is not None and not isinstance(self.outputSchema, McpToolOutputSchema):
            self.outputSchema = McpToolOutputSchema(**as_dict(self.outputSchema))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolAnnotations(YAMLRoot):
    """
    Additional properties describing a {@link Tool} to clients.

    NOTE: all properties in `ToolAnnotations` are **hints**.
    They are not guaranteed to provide a faithful description of
    tool behavior (including descriptive properties like `title`).

    Clients should never make tool use decisions based on `ToolAnnotations`
    received from untrusted servers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolAnnotations"]
    class_class_curie: ClassVar[str] = "mcp:McpToolAnnotations"
    class_name: ClassVar[str] = "McpToolAnnotations"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolAnnotations

    title: Optional[str] = None
    destructiveHint: Optional[Union[bool, Bool]] = None
    idempotentHint: Optional[Union[bool, Bool]] = None
    openWorldHint: Optional[Union[bool, Bool]] = None
    readOnlyHint: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.destructiveHint is not None and not isinstance(self.destructiveHint, Bool):
            self.destructiveHint = Bool(self.destructiveHint)

        if self.idempotentHint is not None and not isinstance(self.idempotentHint, Bool):
            self.idempotentHint = Bool(self.idempotentHint)

        if self.openWorldHint is not None and not isinstance(self.openWorldHint, Bool):
            self.openWorldHint = Bool(self.openWorldHint)

        if self.readOnlyHint is not None and not isinstance(self.readOnlyHint, Bool):
            self.readOnlyHint = Bool(self.readOnlyHint)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolChoice(YAMLRoot):
    """
    Controls tool selection behavior for sampling requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolChoice"]
    class_class_curie: ClassVar[str] = "mcp:McpToolChoice"
    class_name: ClassVar[str] = "McpToolChoice"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolChoice

    mode: Optional[Union[str, "McpToolChoiceMode"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mode is not None and not isinstance(self.mode, McpToolChoiceMode):
            self.mode = McpToolChoiceMode(self.mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolInputSchema(YAMLRoot):
    """
    A JSON Schema object defining the expected parameters for the tool.

    Tool arguments are always JSON objects, so `type: "object"` is required at the root.
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolInputSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpToolInputSchema"
    class_name: ClassVar[str] = "McpToolInputSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolInputSchema

    kind: str = None
    schema_dialect: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.schema_dialect is not None and not isinstance(self.schema_dialect, str):
            self.schema_dialect = str(self.schema_dialect)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolListChangedNotification(McpJSONRPCNotification):
    """
    An optional notification from the server to the client, informing it that the list of tools it offers has changed.
    This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client
    requested it via the `toolsListChanged` filter field.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:McpToolListChangedNotification"
    class_name: ClassVar[str] = "McpToolListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolListChangedNotification

    jsonrpc: str = None
    method: str = None
    params: Optional[Union[dict, McpNotificationParams]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self.params is not None and not isinstance(self.params, McpNotificationParams):
            self.params = McpNotificationParams(**as_dict(self.params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolOutputSchema(YAMLRoot):
    """
    An optional JSON Schema object defining the structure of the tool's output returned in
    the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolOutputSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpToolOutputSchema"
    class_name: ClassVar[str] = "McpToolOutputSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolOutputSchema

    schema_dialect: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.schema_dialect is not None and not isinstance(self.schema_dialect, str):
            self.schema_dialect = str(self.schema_dialect)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolResultContent(YAMLRoot):
    """
    The result of a tool use, provided by the user back to the assistant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolResultContent"]
    class_class_curie: ClassVar[str] = "mcp:McpToolResultContent"
    class_name: ClassVar[str] = "McpToolResultContent"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolResultContent

    content: Union[Union[dict, McpContentBlock], list[Union[dict, McpContentBlock]]] = None
    toolUseId: str = None
    kind: str = None
    _meta: Optional[Union[dict, McpMetaObject]] = None
    isError: Optional[Union[bool, Bool]] = None
    structuredContent: Optional[Union[dict, McpJSONValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, McpContentBlock) else McpContentBlock(**as_dict(v)) for v in self.content]

        if self._is_empty(self.toolUseId):
            self.MissingRequiredField("toolUseId")
        if not isinstance(self.toolUseId, str):
            self.toolUseId = str(self.toolUseId)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        if self.isError is not None and not isinstance(self.isError, Bool):
            self.isError = Bool(self.isError)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpToolUseContent(YAMLRoot):
    """
    A request from the assistant to call a tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpToolUseContent"]
    class_class_curie: ClassVar[str] = "mcp:McpToolUseContent"
    class_name: ClassVar[str] = "McpToolUseContent"
    class_model_uri: ClassVar[URIRef] = MCP.McpToolUseContent

    name: str = None
    identifier: str = None
    input: Union[dict, McpJSONObject] = None
    kind: str = None
    _meta: Optional[Union[dict, McpMetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, McpJSONObject):
            self.input = McpJSONObject()

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self._meta is not None and not isinstance(self._meta, McpMetaObject):
            self._meta = McpMetaObject()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpUnsupportedProtocolVersionError(McpJSONRPCErrorResponse):
    """
    Returned when the request's protocol version is unknown to the server or
    unsupported (e.g., a known experimental or draft version the server has
    chosen not to implement). For HTTP, the response status code MUST be
    `400 Bad Request`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpUnsupportedProtocolVersionError"]
    class_class_curie: ClassVar[str] = "mcp:McpUnsupportedProtocolVersionError"
    class_name: ClassVar[str] = "McpUnsupportedProtocolVersionError"
    class_model_uri: ClassVar[URIRef] = MCP.McpUnsupportedProtocolVersionError

    error: Union[dict, "McpUnsupportedProtocolVersionErrorError"] = None
    jsonrpc: str = None
    identifier: Optional[Union[str, int]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.error):
            self.MissingRequiredField("error")
        if not isinstance(self.error, McpUnsupportedProtocolVersionErrorError):
            self.error = McpUnsupportedProtocolVersionErrorError(**as_dict(self.error))

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self.identifier is not None and not isinstance(self.identifier, (str, int)):
            value = self.identifier
            for _coerce in (lambda: str(value), lambda: int(value)):
                try:
                    self.identifier = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, int] could be constructed from {value!r} for slot identifier")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpUnsupportedProtocolVersionErrorError(McpError):
    """
    MCP's `Error`, with the code and data this error carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpUnsupportedProtocolVersionErrorError"]
    class_class_curie: ClassVar[str] = "mcp:McpUnsupportedProtocolVersionErrorError"
    class_name: ClassVar[str] = "McpUnsupportedProtocolVersionErrorError"
    class_model_uri: ClassVar[URIRef] = MCP.McpUnsupportedProtocolVersionErrorError

    message: str = None
    code: int = None
    data: Union[dict, "McpUnsupportedProtocolVersionErrorErrorData"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, McpUnsupportedProtocolVersionErrorErrorData):
            self.data = McpUnsupportedProtocolVersionErrorErrorData(**as_dict(self.data))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpUnsupportedProtocolVersionErrorErrorData(YAMLRoot):
    """
    The object MCP's `UnsupportedProtocolVersionError` holds under `data`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpUnsupportedProtocolVersionErrorErrorData"]
    class_class_curie: ClassVar[str] = "mcp:McpUnsupportedProtocolVersionErrorErrorData"
    class_name: ClassVar[str] = "McpUnsupportedProtocolVersionErrorErrorData"
    class_model_uri: ClassVar[URIRef] = MCP.McpUnsupportedProtocolVersionErrorErrorData

    requested: str = None
    supported: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requested):
            self.MissingRequiredField("requested")
        if not isinstance(self.requested, str):
            self.requested = str(self.requested)

        if self._is_empty(self.supported):
            self.MissingRequiredField("supported")
        if not isinstance(self.supported, list):
            self.supported = [self.supported] if self.supported is not None else []
        self.supported = [v if isinstance(v, str) else str(v) for v in self.supported]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpUntitledMultiSelectEnumSchema(YAMLRoot):
    """
    Schema for multiple-selection enumeration without display titles for options.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpUntitledMultiSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpUntitledMultiSelectEnumSchema"
    class_name: ClassVar[str] = "McpUntitledMultiSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpUntitledMultiSelectEnumSchema

    items: Union[dict, "McpUntitledMultiSelectEnumSchemaItems"] = None
    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[Union[str, list[str]]] = empty_list()
    maxItems: Optional[int] = None
    minItems: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.items):
            self.MissingRequiredField("items")
        if not isinstance(self.items, McpUntitledMultiSelectEnumSchemaItems):
            self.items = McpUntitledMultiSelectEnumSchemaItems(**as_dict(self.items))

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, str) else str(v) for v in self.default]

        if self.maxItems is not None and not isinstance(self.maxItems, int):
            self.maxItems = int(self.maxItems)

        if self.minItems is not None and not isinstance(self.minItems, int):
            self.minItems = int(self.minItems)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpUntitledMultiSelectEnumSchemaItems(YAMLRoot):
    """
    Schema for the array items.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpUntitledMultiSelectEnumSchemaItems"]
    class_class_curie: ClassVar[str] = "mcp:McpUntitledMultiSelectEnumSchemaItems"
    class_name: ClassVar[str] = "McpUntitledMultiSelectEnumSchemaItems"
    class_model_uri: ClassVar[URIRef] = MCP.McpUntitledMultiSelectEnumSchemaItems

    enum: Union[str, list[str]] = None
    kind: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.enum):
            self.MissingRequiredField("enum")
        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class McpUntitledSingleSelectEnumSchema(YAMLRoot):
    """
    Schema for single-selection enumeration without display titles for options.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["McpUntitledSingleSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:McpUntitledSingleSelectEnumSchema"
    class_name: ClassVar[str] = "McpUntitledSingleSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.McpUntitledSingleSelectEnumSchema

    enum: Union[str, list[str]] = None
    kind: str = None
    description: Optional[str] = None
    title: Optional[str] = None
    default: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.enum):
            self.MissingRequiredField("enum")
        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.default is not None and not isinstance(self.default, str):
            self.default = str(self.default)

        super().__post_init__(**kwargs)


# Enumerations
class McpCacheScope(EnumDefinitionImpl):
    """
    The values MCP allows for `cacheScope`.
    """
    private = PermissibleValue(text="private")
    public = PermissibleValue(text="public")

    _defn = EnumDefinition(
        name="McpCacheScope",
        description="The values MCP allows for `cacheScope`.",
    )

class McpCreateMessageRequestParamsIncludeContext(EnumDefinitionImpl):
    """
    The values MCP allows for `includeContext`.
    """
    allServers = PermissibleValue(text="allServers")
    none = PermissibleValue(text="none")
    thisServer = PermissibleValue(text="thisServer")

    _defn = EnumDefinition(
        name="McpCreateMessageRequestParamsIncludeContext",
        description="The values MCP allows for `includeContext`.",
    )

class McpElicitResultAction(EnumDefinitionImpl):
    """
    The values MCP allows for `action`.
    """
    accept = PermissibleValue(text="accept")
    cancel = PermissibleValue(text="cancel")
    decline = PermissibleValue(text="decline")

    _defn = EnumDefinition(
        name="McpElicitResultAction",
        description="The values MCP allows for `action`.",
    )

class McpIconTheme(EnumDefinitionImpl):
    """
    The values MCP allows for `theme`.
    """
    dark = PermissibleValue(text="dark")
    light = PermissibleValue(text="light")

    _defn = EnumDefinition(
        name="McpIconTheme",
        description="The values MCP allows for `theme`.",
    )

class McpLoggingLevel(EnumDefinitionImpl):
    """
    The severity of a log message.

    These map to syslog message severities, as specified in RFC-5424:
    https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1
    """
    alert = PermissibleValue(text="alert")
    critical = PermissibleValue(text="critical")
    debug = PermissibleValue(text="debug")
    emergency = PermissibleValue(text="emergency")
    error = PermissibleValue(text="error")
    info = PermissibleValue(text="info")
    notice = PermissibleValue(text="notice")
    warning = PermissibleValue(text="warning")

    _defn = EnumDefinition(
        name="McpLoggingLevel",
        description="""The severity of a log message.

These map to syslog message severities, as specified in RFC-5424:
https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1""",
    )

class McpNumberSchemaType(EnumDefinitionImpl):
    """
    The values MCP allows for `type`.
    """
    integer = PermissibleValue(text="integer")
    number = PermissibleValue(text="number")

    _defn = EnumDefinition(
        name="McpNumberSchemaType",
        description="The values MCP allows for `type`.",
    )

class McpRole(EnumDefinitionImpl):
    """
    The sender or recipient of messages and data in a conversation.
    """
    assistant = PermissibleValue(text="assistant")
    user = PermissibleValue(text="user")

    _defn = EnumDefinition(
        name="McpRole",
        description="The sender or recipient of messages and data in a conversation.",
    )

class McpStringSchemaFormat(EnumDefinitionImpl):
    """
    The values MCP allows for `format`.
    """
    date = PermissibleValue(text="date")
    email = PermissibleValue(text="email")
    uri = PermissibleValue(text="uri")

    _defn = EnumDefinition(
        name="McpStringSchemaFormat",
        description="The values MCP allows for `format`.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "date-time",
            PermissibleValue(text="date-time"))

class McpToolChoiceMode(EnumDefinitionImpl):
    """
    The values MCP allows for `mode`.
    """
    auto = PermissibleValue(text="auto")
    none = PermissibleValue(text="none")
    required = PermissibleValue(text="required")

    _defn = EnumDefinition(
        name="McpToolChoiceMode",
        description="The values MCP allows for `mode`.",
    )

# Slots
class slots:
    pass

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.description, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.name, domain=None, range=Optional[str])

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.title, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=MCP.url, domain=None, range=Optional[Union[str, URI]])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=MCP.version, domain=None, range=Optional[str])

slots.mcpAnnotations__intended_audience = Slot(uri=MCP.intended_audience, name="mcpAnnotations__intended_audience", curie=MCP.curie('intended_audience'),
                   model_uri=MCP.mcpAnnotations__intended_audience, domain=None, range=Optional[Union[Union[str, "McpRole"], list[Union[str, "McpRole"]]]])

slots.mcpAnnotations__last_modified = Slot(uri=MCP.lastModified, name="mcpAnnotations__last_modified", curie=MCP.curie('lastModified'),
                   model_uri=MCP.mcpAnnotations__last_modified, domain=None, range=Optional[str])

slots.mcpAnnotations__priority = Slot(uri=MCP.priority, name="mcpAnnotations__priority", curie=MCP.curie('priority'),
                   model_uri=MCP.mcpAnnotations__priority, domain=None, range=Optional[float])

slots.mcpAudioContent__meta = Slot(uri=MCP._meta, name="mcpAudioContent__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpAudioContent__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpAudioContent__annotations = Slot(uri=MCP.annotations, name="mcpAudioContent__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpAudioContent__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpAudioContent__data = Slot(uri=MCP.data, name="mcpAudioContent__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpAudioContent__data, domain=None, range=Union[str, McpBase64])

slots.mcpAudioContent__mime_type = Slot(uri=MCP.mimeType, name="mcpAudioContent__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpAudioContent__mime_type, domain=None, range=str)

slots.mcpAudioContent__kind = Slot(uri=MCP.kind, name="mcpAudioContent__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpAudioContent__kind, domain=None, range=str)

slots.mcpBlobResourceContents__meta = Slot(uri=MCP._meta, name="mcpBlobResourceContents__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpBlobResourceContents__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpBlobResourceContents__blob = Slot(uri=MCP.blob, name="mcpBlobResourceContents__blob", curie=MCP.curie('blob'),
                   model_uri=MCP.mcpBlobResourceContents__blob, domain=None, range=Union[str, McpBase64])

slots.mcpBlobResourceContents__mime_type = Slot(uri=MCP.mimeType, name="mcpBlobResourceContents__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpBlobResourceContents__mime_type, domain=None, range=Optional[str])

slots.mcpBlobResourceContents__uri = Slot(uri=MCP.uri, name="mcpBlobResourceContents__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpBlobResourceContents__uri, domain=None, range=Union[str, URI])

slots.mcpBooleanSchema__default = Slot(uri=MCP.default, name="mcpBooleanSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpBooleanSchema__default, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpBooleanSchema__kind = Slot(uri=MCP.kind, name="mcpBooleanSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpBooleanSchema__kind, domain=None, range=str)

slots.mcpCacheableResult__meta = Slot(uri=MCP._meta, name="mcpCacheableResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCacheableResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpCacheableResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpCacheableResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpCacheableResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpCacheableResult__result_type = Slot(uri=MCP.resultType, name="mcpCacheableResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpCacheableResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpCacheableResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpCacheableResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpCacheableResult__ttl_ms, domain=None, range=int)

slots.mcpCallToolRequest__identifier = Slot(uri=MCP.identifier, name="mcpCallToolRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpCallToolRequest__identifier, domain=None, range=Union[str, int])

slots.mcpCallToolRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpCallToolRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpCallToolRequest__jsonrpc, domain=None, range=str)

slots.mcpCallToolRequest__method = Slot(uri=MCP.method, name="mcpCallToolRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpCallToolRequest__method, domain=None, range=str)

slots.mcpCallToolRequest__params = Slot(uri=MCP.params, name="mcpCallToolRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpCallToolRequest__params, domain=None, range=Union[dict, McpCallToolRequestParams])

slots.mcpCallToolRequestParams__meta = Slot(uri=MCP._meta, name="mcpCallToolRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCallToolRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpCallToolRequestParams__arguments = Slot(uri=MCP.arguments, name="mcpCallToolRequestParams__arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.mcpCallToolRequestParams__arguments, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpCallToolRequestParams__input_responses = Slot(uri=MCP.inputResponses, name="mcpCallToolRequestParams__input_responses", curie=MCP.curie('inputResponses'),
                   model_uri=MCP.mcpCallToolRequestParams__input_responses, domain=None, range=Optional[Union[dict, McpInputResponses]])

slots.mcpCallToolRequestParams__request_state = Slot(uri=MCP.requestState, name="mcpCallToolRequestParams__request_state", curie=MCP.curie('requestState'),
                   model_uri=MCP.mcpCallToolRequestParams__request_state, domain=None, range=Optional[str])

slots.mcpCallToolResult__meta = Slot(uri=MCP._meta, name="mcpCallToolResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCallToolResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpCallToolResult__content = Slot(uri=MCP.content, name="mcpCallToolResult__content", curie=MCP.curie('content'),
                   model_uri=MCP.mcpCallToolResult__content, domain=None, range=Union[Union[dict, McpContentBlock], list[Union[dict, McpContentBlock]]])

slots.mcpCallToolResult__is_error = Slot(uri=MCP.isError, name="mcpCallToolResult__is_error", curie=MCP.curie('isError'),
                   model_uri=MCP.mcpCallToolResult__is_error, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpCallToolResult__result_type = Slot(uri=MCP.resultType, name="mcpCallToolResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpCallToolResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpCallToolResult__structured_content = Slot(uri=MCP.structuredContent, name="mcpCallToolResult__structured_content", curie=MCP.curie('structuredContent'),
                   model_uri=MCP.mcpCallToolResult__structured_content, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpCallToolResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpCallToolResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpCallToolResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpCallToolResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpCallToolResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpCallToolResultResponse__jsonrpc, domain=None, range=str)

slots.mcpCallToolResultResponse__result = Slot(uri=MCP.result, name="mcpCallToolResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpCallToolResultResponse__result, domain=None, range=Union[dict, McpInputRequiredResult, McpCallToolResult])

slots.mcpCancelledNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpCancelledNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpCancelledNotification__jsonrpc, domain=None, range=str)

slots.mcpCancelledNotification__method = Slot(uri=MCP.method, name="mcpCancelledNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpCancelledNotification__method, domain=None, range=str)

slots.mcpCancelledNotification__params = Slot(uri=MCP.params, name="mcpCancelledNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpCancelledNotification__params, domain=None, range=Union[dict, McpCancelledNotificationParams])

slots.mcpCancelledNotificationParams__meta = Slot(uri=MCP._meta, name="mcpCancelledNotificationParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCancelledNotificationParams__meta, domain=None, range=Optional[Union[dict, McpNotificationMetaObject]])

slots.mcpCancelledNotificationParams__reason_text = Slot(uri=MCP.reason_text, name="mcpCancelledNotificationParams__reason_text", curie=MCP.curie('reason_text'),
                   model_uri=MCP.mcpCancelledNotificationParams__reason_text, domain=None, range=Optional[str])

slots.mcpCancelledNotificationParams__request_id = Slot(uri=MCP.requestId, name="mcpCancelledNotificationParams__request_id", curie=MCP.curie('requestId'),
                   model_uri=MCP.mcpCancelledNotificationParams__request_id, domain=None, range=Union[str, int])

slots.mcpClientCapabilities__elicitation = Slot(uri=MCP.elicitation, name="mcpClientCapabilities__elicitation", curie=MCP.curie('elicitation'),
                   model_uri=MCP.mcpClientCapabilities__elicitation, domain=None, range=Optional[Union[dict, McpClientCapabilitiesElicitation]])

slots.mcpClientCapabilities__experimental = Slot(uri=MCP.experimental, name="mcpClientCapabilities__experimental", curie=MCP.curie('experimental'),
                   model_uri=MCP.mcpClientCapabilities__experimental, domain=None, range=Optional[Union[dict, McpClientCapabilitiesExperimental]])

slots.mcpClientCapabilities__extensions = Slot(uri=MCP.extensions, name="mcpClientCapabilities__extensions", curie=MCP.curie('extensions'),
                   model_uri=MCP.mcpClientCapabilities__extensions, domain=None, range=Optional[Union[dict, McpClientCapabilitiesExtensions]])

slots.mcpClientCapabilities__roots = Slot(uri=MCP.roots, name="mcpClientCapabilities__roots", curie=MCP.curie('roots'),
                   model_uri=MCP.mcpClientCapabilities__roots, domain=None, range=Optional[Union[dict, McpClientCapabilitiesRoots]])

slots.mcpClientCapabilities__sampling = Slot(uri=MCP.sampling, name="mcpClientCapabilities__sampling", curie=MCP.curie('sampling'),
                   model_uri=MCP.mcpClientCapabilities__sampling, domain=None, range=Optional[Union[dict, McpClientCapabilitiesSampling]])

slots.mcpClientCapabilitiesElicitation__form = Slot(uri=MCP.form, name="mcpClientCapabilitiesElicitation__form", curie=MCP.curie('form'),
                   model_uri=MCP.mcpClientCapabilitiesElicitation__form, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpClientCapabilitiesElicitation__url_settings = Slot(uri=MCP.url_settings, name="mcpClientCapabilitiesElicitation__url_settings", curie=MCP.curie('url_settings'),
                   model_uri=MCP.mcpClientCapabilitiesElicitation__url_settings, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpClientCapabilitiesSampling__context_info = Slot(uri=MCP.context_info, name="mcpClientCapabilitiesSampling__context_info", curie=MCP.curie('context_info'),
                   model_uri=MCP.mcpClientCapabilitiesSampling__context_info, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpClientCapabilitiesSampling__tools = Slot(uri=MCP.tools, name="mcpClientCapabilitiesSampling__tools", curie=MCP.curie('tools'),
                   model_uri=MCP.mcpClientCapabilitiesSampling__tools, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpClientNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpClientNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpClientNotification__jsonrpc, domain=None, range=str)

slots.mcpClientNotification__method = Slot(uri=MCP.method, name="mcpClientNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpClientNotification__method, domain=None, range=str)

slots.mcpClientNotification__params = Slot(uri=MCP.params, name="mcpClientNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpClientNotification__params, domain=None, range=Union[dict, McpCancelledNotificationParams])

slots.mcpCompleteRequest__identifier = Slot(uri=MCP.identifier, name="mcpCompleteRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpCompleteRequest__identifier, domain=None, range=Union[str, int])

slots.mcpCompleteRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpCompleteRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpCompleteRequest__jsonrpc, domain=None, range=str)

slots.mcpCompleteRequest__method = Slot(uri=MCP.method, name="mcpCompleteRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpCompleteRequest__method, domain=None, range=str)

slots.mcpCompleteRequest__params = Slot(uri=MCP.params, name="mcpCompleteRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpCompleteRequest__params, domain=None, range=Union[dict, McpCompleteRequestParams])

slots.mcpCompleteRequestParams__meta = Slot(uri=MCP._meta, name="mcpCompleteRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCompleteRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpCompleteRequestParams__argument = Slot(uri=MCP.argument, name="mcpCompleteRequestParams__argument", curie=MCP.curie('argument'),
                   model_uri=MCP.mcpCompleteRequestParams__argument, domain=None, range=Union[dict, McpCompleteRequestParamsArgument])

slots.mcpCompleteRequestParams__context_info = Slot(uri=MCP.context_info, name="mcpCompleteRequestParams__context_info", curie=MCP.curie('context_info'),
                   model_uri=MCP.mcpCompleteRequestParams__context_info, domain=None, range=Optional[Union[dict, McpCompleteRequestParamsContext]])

slots.mcpCompleteRequestParams__ref = Slot(uri=MCP.ref, name="mcpCompleteRequestParams__ref", curie=MCP.curie('ref'),
                   model_uri=MCP.mcpCompleteRequestParams__ref, domain=None, range=Union[dict, McpPromptReference, McpResourceTemplateReference])

slots.mcpCompleteRequestParamsArgument__value = Slot(uri=MCP.value, name="mcpCompleteRequestParamsArgument__value", curie=MCP.curie('value'),
                   model_uri=MCP.mcpCompleteRequestParamsArgument__value, domain=None, range=str)

slots.mcpCompleteRequestParamsContext__arguments = Slot(uri=MCP.arguments, name="mcpCompleteRequestParamsContext__arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.mcpCompleteRequestParamsContext__arguments, domain=None, range=Optional[Union[dict, McpCompleteRequestParamsContextArguments]])

slots.mcpCompleteResult__meta = Slot(uri=MCP._meta, name="mcpCompleteResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCompleteResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpCompleteResult__completion = Slot(uri=MCP.completion, name="mcpCompleteResult__completion", curie=MCP.curie('completion'),
                   model_uri=MCP.mcpCompleteResult__completion, domain=None, range=Union[dict, McpCompleteResultCompletion])

slots.mcpCompleteResult__result_type = Slot(uri=MCP.resultType, name="mcpCompleteResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpCompleteResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpCompleteResultCompletion__has_more = Slot(uri=MCP.hasMore, name="mcpCompleteResultCompletion__has_more", curie=MCP.curie('hasMore'),
                   model_uri=MCP.mcpCompleteResultCompletion__has_more, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpCompleteResultCompletion__total = Slot(uri=MCP.total, name="mcpCompleteResultCompletion__total", curie=MCP.curie('total'),
                   model_uri=MCP.mcpCompleteResultCompletion__total, domain=None, range=Optional[int])

slots.mcpCompleteResultCompletion__values = Slot(uri=MCP.values, name="mcpCompleteResultCompletion__values", curie=MCP.curie('values'),
                   model_uri=MCP.mcpCompleteResultCompletion__values, domain=None, range=Union[str, list[str]])

slots.mcpCompleteResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpCompleteResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpCompleteResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpCompleteResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpCompleteResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpCompleteResultResponse__jsonrpc, domain=None, range=str)

slots.mcpCompleteResultResponse__result = Slot(uri=MCP.result, name="mcpCompleteResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpCompleteResultResponse__result, domain=None, range=Union[dict, McpCompleteResult])

slots.mcpCreateMessageRequest__method = Slot(uri=MCP.method, name="mcpCreateMessageRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpCreateMessageRequest__method, domain=None, range=str)

slots.mcpCreateMessageRequest__params = Slot(uri=MCP.params, name="mcpCreateMessageRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpCreateMessageRequest__params, domain=None, range=Union[dict, McpCreateMessageRequestParams])

slots.mcpCreateMessageRequestParams__include_context = Slot(uri=MCP.includeContext, name="mcpCreateMessageRequestParams__include_context", curie=MCP.curie('includeContext'),
                   model_uri=MCP.mcpCreateMessageRequestParams__include_context, domain=None, range=Optional[Union[str, "McpCreateMessageRequestParamsIncludeContext"]])

slots.mcpCreateMessageRequestParams__max_tokens = Slot(uri=MCP.maxTokens, name="mcpCreateMessageRequestParams__max_tokens", curie=MCP.curie('maxTokens'),
                   model_uri=MCP.mcpCreateMessageRequestParams__max_tokens, domain=None, range=int)

slots.mcpCreateMessageRequestParams__messages = Slot(uri=MCP.messages, name="mcpCreateMessageRequestParams__messages", curie=MCP.curie('messages'),
                   model_uri=MCP.mcpCreateMessageRequestParams__messages, domain=None, range=Union[Union[dict, McpSamplingMessage], list[Union[dict, McpSamplingMessage]]])

slots.mcpCreateMessageRequestParams__metadata = Slot(uri=MCP.metadata, name="mcpCreateMessageRequestParams__metadata", curie=MCP.curie('metadata'),
                   model_uri=MCP.mcpCreateMessageRequestParams__metadata, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpCreateMessageRequestParams__model_preferences = Slot(uri=MCP.modelPreferences, name="mcpCreateMessageRequestParams__model_preferences", curie=MCP.curie('modelPreferences'),
                   model_uri=MCP.mcpCreateMessageRequestParams__model_preferences, domain=None, range=Optional[Union[dict, McpModelPreferences]])

slots.mcpCreateMessageRequestParams__stop_sequences = Slot(uri=MCP.stopSequences, name="mcpCreateMessageRequestParams__stop_sequences", curie=MCP.curie('stopSequences'),
                   model_uri=MCP.mcpCreateMessageRequestParams__stop_sequences, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpCreateMessageRequestParams__system_prompt = Slot(uri=MCP.systemPrompt, name="mcpCreateMessageRequestParams__system_prompt", curie=MCP.curie('systemPrompt'),
                   model_uri=MCP.mcpCreateMessageRequestParams__system_prompt, domain=None, range=Optional[str])

slots.mcpCreateMessageRequestParams__temperature = Slot(uri=MCP.temperature, name="mcpCreateMessageRequestParams__temperature", curie=MCP.curie('temperature'),
                   model_uri=MCP.mcpCreateMessageRequestParams__temperature, domain=None, range=Optional[float])

slots.mcpCreateMessageRequestParams__tool_choice = Slot(uri=MCP.toolChoice, name="mcpCreateMessageRequestParams__tool_choice", curie=MCP.curie('toolChoice'),
                   model_uri=MCP.mcpCreateMessageRequestParams__tool_choice, domain=None, range=Optional[Union[dict, McpToolChoice]])

slots.mcpCreateMessageRequestParams__tools = Slot(uri=MCP.tools, name="mcpCreateMessageRequestParams__tools", curie=MCP.curie('tools'),
                   model_uri=MCP.mcpCreateMessageRequestParams__tools, domain=None, range=Optional[Union[Union[dict, McpTool], list[Union[dict, McpTool]]]])

slots.mcpCreateMessageResult__meta = Slot(uri=MCP._meta, name="mcpCreateMessageResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpCreateMessageResult__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpCreateMessageResult__content = Slot(uri=MCP.content, name="mcpCreateMessageResult__content", curie=MCP.curie('content'),
                   model_uri=MCP.mcpCreateMessageResult__content, domain=None, range=Union[dict, McpTextContent, McpImageContent, McpAudioContent, McpToolUseContent, McpToolResultContent, McpSamplingMessageContentBlock])

slots.mcpCreateMessageResult__model = Slot(uri=MCP.model, name="mcpCreateMessageResult__model", curie=MCP.curie('model'),
                   model_uri=MCP.mcpCreateMessageResult__model, domain=None, range=str)

slots.mcpCreateMessageResult__role = Slot(uri=MCP.role, name="mcpCreateMessageResult__role", curie=MCP.curie('role'),
                   model_uri=MCP.mcpCreateMessageResult__role, domain=None, range=Union[str, "McpRole"])

slots.mcpCreateMessageResult__stop_reason = Slot(uri=MCP.stopReason, name="mcpCreateMessageResult__stop_reason", curie=MCP.curie('stopReason'),
                   model_uri=MCP.mcpCreateMessageResult__stop_reason, domain=None, range=Optional[str])

slots.mcpDiscoverRequest__identifier = Slot(uri=MCP.identifier, name="mcpDiscoverRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpDiscoverRequest__identifier, domain=None, range=Union[str, int])

slots.mcpDiscoverRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpDiscoverRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpDiscoverRequest__jsonrpc, domain=None, range=str)

slots.mcpDiscoverRequest__method = Slot(uri=MCP.method, name="mcpDiscoverRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpDiscoverRequest__method, domain=None, range=str)

slots.mcpDiscoverRequest__params = Slot(uri=MCP.params, name="mcpDiscoverRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpDiscoverRequest__params, domain=None, range=Union[dict, McpRequestParams])

slots.mcpDiscoverResult__meta = Slot(uri=MCP._meta, name="mcpDiscoverResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpDiscoverResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpDiscoverResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpDiscoverResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpDiscoverResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpDiscoverResult__capabilities = Slot(uri=MCP.capabilities, name="mcpDiscoverResult__capabilities", curie=MCP.curie('capabilities'),
                   model_uri=MCP.mcpDiscoverResult__capabilities, domain=None, range=Union[dict, McpServerCapabilities])

slots.mcpDiscoverResult__instructions = Slot(uri=MCP.instructions, name="mcpDiscoverResult__instructions", curie=MCP.curie('instructions'),
                   model_uri=MCP.mcpDiscoverResult__instructions, domain=None, range=Optional[str])

slots.mcpDiscoverResult__result_type = Slot(uri=MCP.resultType, name="mcpDiscoverResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpDiscoverResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpDiscoverResult__supported_versions = Slot(uri=MCP.supportedVersions, name="mcpDiscoverResult__supported_versions", curie=MCP.curie('supportedVersions'),
                   model_uri=MCP.mcpDiscoverResult__supported_versions, domain=None, range=Union[str, list[str]])

slots.mcpDiscoverResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpDiscoverResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpDiscoverResult__ttl_ms, domain=None, range=int)

slots.mcpDiscoverResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpDiscoverResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpDiscoverResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpDiscoverResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpDiscoverResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpDiscoverResultResponse__jsonrpc, domain=None, range=str)

slots.mcpDiscoverResultResponse__result = Slot(uri=MCP.result, name="mcpDiscoverResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpDiscoverResultResponse__result, domain=None, range=Union[dict, McpDiscoverResult])

slots.mcpElicitRequest__method = Slot(uri=MCP.method, name="mcpElicitRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpElicitRequest__method, domain=None, range=str)

slots.mcpElicitRequest__params = Slot(uri=MCP.params, name="mcpElicitRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpElicitRequest__params, domain=None, range=Union[dict, McpElicitRequestParams])

slots.mcpElicitRequestFormParams__message = Slot(uri=MCP.message, name="mcpElicitRequestFormParams__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpElicitRequestFormParams__message, domain=None, range=str)

slots.mcpElicitRequestFormParams__mode = Slot(uri=MCP.mode, name="mcpElicitRequestFormParams__mode", curie=MCP.curie('mode'),
                   model_uri=MCP.mcpElicitRequestFormParams__mode, domain=None, range=Optional[str])

slots.mcpElicitRequestFormParams__requested_schema = Slot(uri=MCP.requestedSchema, name="mcpElicitRequestFormParams__requested_schema", curie=MCP.curie('requestedSchema'),
                   model_uri=MCP.mcpElicitRequestFormParams__requested_schema, domain=None, range=Union[dict, McpElicitRequestFormParamsRequestedSchema])

slots.mcpElicitRequestFormParamsRequestedSchema__schema_dialect = Slot(uri=MCP.schema_dialect, name="mcpElicitRequestFormParamsRequestedSchema__schema_dialect", curie=MCP.curie('schema_dialect'),
                   model_uri=MCP.mcpElicitRequestFormParamsRequestedSchema__schema_dialect, domain=None, range=Optional[str])

slots.mcpElicitRequestFormParamsRequestedSchema__properties = Slot(uri=MCP.properties, name="mcpElicitRequestFormParamsRequestedSchema__properties", curie=MCP.curie('properties'),
                   model_uri=MCP.mcpElicitRequestFormParamsRequestedSchema__properties, domain=None, range=Union[dict, McpElicitRequestFormParamsRequestedSchemaProperties])

slots.mcpElicitRequestFormParamsRequestedSchema__required_names = Slot(uri=MCP.required_names, name="mcpElicitRequestFormParamsRequestedSchema__required_names", curie=MCP.curie('required_names'),
                   model_uri=MCP.mcpElicitRequestFormParamsRequestedSchema__required_names, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpElicitRequestFormParamsRequestedSchema__kind = Slot(uri=MCP.kind, name="mcpElicitRequestFormParamsRequestedSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpElicitRequestFormParamsRequestedSchema__kind, domain=None, range=str)

slots.mcpElicitRequestURLParams__message = Slot(uri=MCP.message, name="mcpElicitRequestURLParams__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpElicitRequestURLParams__message, domain=None, range=str)

slots.mcpElicitRequestURLParams__mode = Slot(uri=MCP.mode, name="mcpElicitRequestURLParams__mode", curie=MCP.curie('mode'),
                   model_uri=MCP.mcpElicitRequestURLParams__mode, domain=None, range=str)

slots.mcpElicitResult__action = Slot(uri=MCP.action, name="mcpElicitResult__action", curie=MCP.curie('action'),
                   model_uri=MCP.mcpElicitResult__action, domain=None, range=Union[str, "McpElicitResultAction"])

slots.mcpElicitResult__content = Slot(uri=MCP.content, name="mcpElicitResult__content", curie=MCP.curie('content'),
                   model_uri=MCP.mcpElicitResult__content, domain=None, range=Optional[Union[dict, McpElicitResultContent]])

slots.mcpEmbeddedResource__meta = Slot(uri=MCP._meta, name="mcpEmbeddedResource__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpEmbeddedResource__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpEmbeddedResource__annotations = Slot(uri=MCP.annotations, name="mcpEmbeddedResource__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpEmbeddedResource__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpEmbeddedResource__resource_contents = Slot(uri=MCP.resource_contents, name="mcpEmbeddedResource__resource_contents", curie=MCP.curie('resource_contents'),
                   model_uri=MCP.mcpEmbeddedResource__resource_contents, domain=None, range=Union[dict, McpTextResourceContents, McpBlobResourceContents])

slots.mcpEmbeddedResource__kind = Slot(uri=MCP.kind, name="mcpEmbeddedResource__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpEmbeddedResource__kind, domain=None, range=str)

slots.mcpError__code = Slot(uri=MCP.code, name="mcpError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpError__code, domain=None, range=int)

slots.mcpError__data = Slot(uri=MCP.data, name="mcpError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpError__data, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpError__message = Slot(uri=MCP.message, name="mcpError__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpError__message, domain=None, range=str)

slots.mcpGetPromptRequest__identifier = Slot(uri=MCP.identifier, name="mcpGetPromptRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpGetPromptRequest__identifier, domain=None, range=Union[str, int])

slots.mcpGetPromptRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpGetPromptRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpGetPromptRequest__jsonrpc, domain=None, range=str)

slots.mcpGetPromptRequest__method = Slot(uri=MCP.method, name="mcpGetPromptRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpGetPromptRequest__method, domain=None, range=str)

slots.mcpGetPromptRequest__params = Slot(uri=MCP.params, name="mcpGetPromptRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpGetPromptRequest__params, domain=None, range=Union[dict, McpGetPromptRequestParams])

slots.mcpGetPromptRequestParams__meta = Slot(uri=MCP._meta, name="mcpGetPromptRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpGetPromptRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpGetPromptRequestParams__arguments = Slot(uri=MCP.arguments, name="mcpGetPromptRequestParams__arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.mcpGetPromptRequestParams__arguments, domain=None, range=Optional[Union[dict, McpGetPromptRequestParamsArguments]])

slots.mcpGetPromptRequestParams__input_responses = Slot(uri=MCP.inputResponses, name="mcpGetPromptRequestParams__input_responses", curie=MCP.curie('inputResponses'),
                   model_uri=MCP.mcpGetPromptRequestParams__input_responses, domain=None, range=Optional[Union[dict, McpInputResponses]])

slots.mcpGetPromptRequestParams__request_state = Slot(uri=MCP.requestState, name="mcpGetPromptRequestParams__request_state", curie=MCP.curie('requestState'),
                   model_uri=MCP.mcpGetPromptRequestParams__request_state, domain=None, range=Optional[str])

slots.mcpGetPromptResult__meta = Slot(uri=MCP._meta, name="mcpGetPromptResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpGetPromptResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpGetPromptResult__messages = Slot(uri=MCP.messages, name="mcpGetPromptResult__messages", curie=MCP.curie('messages'),
                   model_uri=MCP.mcpGetPromptResult__messages, domain=None, range=Union[Union[dict, McpPromptMessage], list[Union[dict, McpPromptMessage]]])

slots.mcpGetPromptResult__result_type = Slot(uri=MCP.resultType, name="mcpGetPromptResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpGetPromptResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpGetPromptResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpGetPromptResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpGetPromptResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpGetPromptResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpGetPromptResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpGetPromptResultResponse__jsonrpc, domain=None, range=str)

slots.mcpGetPromptResultResponse__result = Slot(uri=MCP.result, name="mcpGetPromptResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpGetPromptResultResponse__result, domain=None, range=Union[dict, McpInputRequiredResult, McpGetPromptResult])

slots.mcpHeaderMismatchError__error = Slot(uri=MCP.error, name="mcpHeaderMismatchError__error", curie=MCP.curie('error'),
                   model_uri=MCP.mcpHeaderMismatchError__error, domain=None, range=Union[dict, McpHeaderMismatchErrorError])

slots.mcpHeaderMismatchError__identifier = Slot(uri=MCP.identifier, name="mcpHeaderMismatchError__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpHeaderMismatchError__identifier, domain=None, range=Optional[Union[str, int]])

slots.mcpHeaderMismatchError__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpHeaderMismatchError__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpHeaderMismatchError__jsonrpc, domain=None, range=str)

slots.mcpHeaderMismatchErrorError__code = Slot(uri=MCP.code, name="mcpHeaderMismatchErrorError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpHeaderMismatchErrorError__code, domain=None, range=int)

slots.mcpIcon__mime_type = Slot(uri=MCP.mimeType, name="mcpIcon__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpIcon__mime_type, domain=None, range=Optional[str])

slots.mcpIcon__sizes = Slot(uri=MCP.sizes, name="mcpIcon__sizes", curie=MCP.curie('sizes'),
                   model_uri=MCP.mcpIcon__sizes, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpIcon__src = Slot(uri=MCP.src, name="mcpIcon__src", curie=MCP.curie('src'),
                   model_uri=MCP.mcpIcon__src, domain=None, range=Union[str, URI])

slots.mcpIcon__theme = Slot(uri=MCP.theme, name="mcpIcon__theme", curie=MCP.curie('theme'),
                   model_uri=MCP.mcpIcon__theme, domain=None, range=Optional[Union[str, "McpIconTheme"]])

slots.mcpIcons__icons = Slot(uri=MCP.icons, name="mcpIcons__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpIcons__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpImageContent__meta = Slot(uri=MCP._meta, name="mcpImageContent__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpImageContent__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpImageContent__annotations = Slot(uri=MCP.annotations, name="mcpImageContent__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpImageContent__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpImageContent__data = Slot(uri=MCP.data, name="mcpImageContent__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpImageContent__data, domain=None, range=Union[str, McpBase64])

slots.mcpImageContent__mime_type = Slot(uri=MCP.mimeType, name="mcpImageContent__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpImageContent__mime_type, domain=None, range=str)

slots.mcpImageContent__kind = Slot(uri=MCP.kind, name="mcpImageContent__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpImageContent__kind, domain=None, range=str)

slots.mcpImplementation__icons = Slot(uri=MCP.icons, name="mcpImplementation__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpImplementation__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpImplementation__website_url = Slot(uri=MCP.websiteUrl, name="mcpImplementation__website_url", curie=MCP.curie('websiteUrl'),
                   model_uri=MCP.mcpImplementation__website_url, domain=None, range=Optional[Union[str, URI]])

slots.mcpInputRequiredResult__meta = Slot(uri=MCP._meta, name="mcpInputRequiredResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpInputRequiredResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpInputRequiredResult__input_requests = Slot(uri=MCP.inputRequests, name="mcpInputRequiredResult__input_requests", curie=MCP.curie('inputRequests'),
                   model_uri=MCP.mcpInputRequiredResult__input_requests, domain=None, range=Optional[Union[dict, McpInputRequests]])

slots.mcpInputRequiredResult__request_state = Slot(uri=MCP.requestState, name="mcpInputRequiredResult__request_state", curie=MCP.curie('requestState'),
                   model_uri=MCP.mcpInputRequiredResult__request_state, domain=None, range=Optional[str])

slots.mcpInputRequiredResult__result_type = Slot(uri=MCP.resultType, name="mcpInputRequiredResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpInputRequiredResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpInputResponseRequestParams__meta = Slot(uri=MCP._meta, name="mcpInputResponseRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpInputResponseRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpInputResponseRequestParams__input_responses = Slot(uri=MCP.inputResponses, name="mcpInputResponseRequestParams__input_responses", curie=MCP.curie('inputResponses'),
                   model_uri=MCP.mcpInputResponseRequestParams__input_responses, domain=None, range=Optional[Union[dict, McpInputResponses]])

slots.mcpInputResponseRequestParams__request_state = Slot(uri=MCP.requestState, name="mcpInputResponseRequestParams__request_state", curie=MCP.curie('requestState'),
                   model_uri=MCP.mcpInputResponseRequestParams__request_state, domain=None, range=Optional[str])

slots.mcpInternalError__code = Slot(uri=MCP.code, name="mcpInternalError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpInternalError__code, domain=None, range=int)

slots.mcpInternalError__data = Slot(uri=MCP.data, name="mcpInternalError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpInternalError__data, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpInternalError__message = Slot(uri=MCP.message, name="mcpInternalError__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpInternalError__message, domain=None, range=str)

slots.mcpInvalidParamsError__code = Slot(uri=MCP.code, name="mcpInvalidParamsError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpInvalidParamsError__code, domain=None, range=int)

slots.mcpInvalidParamsError__data = Slot(uri=MCP.data, name="mcpInvalidParamsError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpInvalidParamsError__data, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpInvalidParamsError__message = Slot(uri=MCP.message, name="mcpInvalidParamsError__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpInvalidParamsError__message, domain=None, range=str)

slots.mcpInvalidRequestError__code = Slot(uri=MCP.code, name="mcpInvalidRequestError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpInvalidRequestError__code, domain=None, range=int)

slots.mcpInvalidRequestError__data = Slot(uri=MCP.data, name="mcpInvalidRequestError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpInvalidRequestError__data, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpInvalidRequestError__message = Slot(uri=MCP.message, name="mcpInvalidRequestError__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpInvalidRequestError__message, domain=None, range=str)

slots.mcpJSONRPCErrorResponse__error = Slot(uri=MCP.error, name="mcpJSONRPCErrorResponse__error", curie=MCP.curie('error'),
                   model_uri=MCP.mcpJSONRPCErrorResponse__error, domain=None, range=Union[dict, McpError])

slots.mcpJSONRPCErrorResponse__identifier = Slot(uri=MCP.identifier, name="mcpJSONRPCErrorResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpJSONRPCErrorResponse__identifier, domain=None, range=Optional[Union[str, int]])

slots.mcpJSONRPCErrorResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpJSONRPCErrorResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpJSONRPCErrorResponse__jsonrpc, domain=None, range=str)

slots.mcpJSONRPCNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpJSONRPCNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpJSONRPCNotification__jsonrpc, domain=None, range=str)

slots.mcpJSONRPCNotification__method = Slot(uri=MCP.method, name="mcpJSONRPCNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpJSONRPCNotification__method, domain=None, range=str)

slots.mcpJSONRPCNotification__params = Slot(uri=MCP.params, name="mcpJSONRPCNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpJSONRPCNotification__params, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpJSONRPCRequest__identifier = Slot(uri=MCP.identifier, name="mcpJSONRPCRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpJSONRPCRequest__identifier, domain=None, range=Union[str, int])

slots.mcpJSONRPCRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpJSONRPCRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpJSONRPCRequest__jsonrpc, domain=None, range=str)

slots.mcpJSONRPCRequest__method = Slot(uri=MCP.method, name="mcpJSONRPCRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpJSONRPCRequest__method, domain=None, range=str)

slots.mcpJSONRPCRequest__params = Slot(uri=MCP.params, name="mcpJSONRPCRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpJSONRPCRequest__params, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpJSONRPCResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpJSONRPCResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpJSONRPCResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpJSONRPCResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpJSONRPCResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpJSONRPCResultResponse__jsonrpc, domain=None, range=str)

slots.mcpJSONRPCResultResponse__result = Slot(uri=MCP.result, name="mcpJSONRPCResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpJSONRPCResultResponse__result, domain=None, range=Union[dict, McpResult])

slots.mcpLegacyTitledEnumSchema__default = Slot(uri=MCP.default, name="mcpLegacyTitledEnumSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpLegacyTitledEnumSchema__default, domain=None, range=Optional[str])

slots.mcpLegacyTitledEnumSchema__enum = Slot(uri=MCP.enum, name="mcpLegacyTitledEnumSchema__enum", curie=MCP.curie('enum'),
                   model_uri=MCP.mcpLegacyTitledEnumSchema__enum, domain=None, range=Union[str, list[str]])

slots.mcpLegacyTitledEnumSchema__enum_names = Slot(uri=MCP.enumNames, name="mcpLegacyTitledEnumSchema__enum_names", curie=MCP.curie('enumNames'),
                   model_uri=MCP.mcpLegacyTitledEnumSchema__enum_names, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpLegacyTitledEnumSchema__kind = Slot(uri=MCP.kind, name="mcpLegacyTitledEnumSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpLegacyTitledEnumSchema__kind, domain=None, range=str)

slots.mcpListPromptsRequest__identifier = Slot(uri=MCP.identifier, name="mcpListPromptsRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListPromptsRequest__identifier, domain=None, range=Union[str, int])

slots.mcpListPromptsRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListPromptsRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListPromptsRequest__jsonrpc, domain=None, range=str)

slots.mcpListPromptsRequest__method = Slot(uri=MCP.method, name="mcpListPromptsRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpListPromptsRequest__method, domain=None, range=str)

slots.mcpListPromptsRequest__params = Slot(uri=MCP.params, name="mcpListPromptsRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpListPromptsRequest__params, domain=None, range=Union[dict, McpPaginatedRequestParams])

slots.mcpListPromptsResult__meta = Slot(uri=MCP._meta, name="mcpListPromptsResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpListPromptsResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpListPromptsResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpListPromptsResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpListPromptsResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpListPromptsResult__next_cursor = Slot(uri=MCP.nextCursor, name="mcpListPromptsResult__next_cursor", curie=MCP.curie('nextCursor'),
                   model_uri=MCP.mcpListPromptsResult__next_cursor, domain=None, range=Optional[Union[str, McpCursor]])

slots.mcpListPromptsResult__prompts = Slot(uri=MCP.prompts, name="mcpListPromptsResult__prompts", curie=MCP.curie('prompts'),
                   model_uri=MCP.mcpListPromptsResult__prompts, domain=None, range=Union[Union[dict, McpPrompt], list[Union[dict, McpPrompt]]])

slots.mcpListPromptsResult__result_type = Slot(uri=MCP.resultType, name="mcpListPromptsResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpListPromptsResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpListPromptsResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpListPromptsResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpListPromptsResult__ttl_ms, domain=None, range=int)

slots.mcpListPromptsResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpListPromptsResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListPromptsResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpListPromptsResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListPromptsResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListPromptsResultResponse__jsonrpc, domain=None, range=str)

slots.mcpListPromptsResultResponse__result = Slot(uri=MCP.result, name="mcpListPromptsResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpListPromptsResultResponse__result, domain=None, range=Union[dict, McpListPromptsResult])

slots.mcpListResourceTemplatesRequest__identifier = Slot(uri=MCP.identifier, name="mcpListResourceTemplatesRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListResourceTemplatesRequest__identifier, domain=None, range=Union[str, int])

slots.mcpListResourceTemplatesRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListResourceTemplatesRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListResourceTemplatesRequest__jsonrpc, domain=None, range=str)

slots.mcpListResourceTemplatesRequest__method = Slot(uri=MCP.method, name="mcpListResourceTemplatesRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpListResourceTemplatesRequest__method, domain=None, range=str)

slots.mcpListResourceTemplatesRequest__params = Slot(uri=MCP.params, name="mcpListResourceTemplatesRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpListResourceTemplatesRequest__params, domain=None, range=Union[dict, McpPaginatedRequestParams])

slots.mcpListResourceTemplatesResult__meta = Slot(uri=MCP._meta, name="mcpListResourceTemplatesResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpListResourceTemplatesResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpListResourceTemplatesResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpListResourceTemplatesResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpListResourceTemplatesResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpListResourceTemplatesResult__next_cursor = Slot(uri=MCP.nextCursor, name="mcpListResourceTemplatesResult__next_cursor", curie=MCP.curie('nextCursor'),
                   model_uri=MCP.mcpListResourceTemplatesResult__next_cursor, domain=None, range=Optional[Union[str, McpCursor]])

slots.mcpListResourceTemplatesResult__resource_templates = Slot(uri=MCP.resourceTemplates, name="mcpListResourceTemplatesResult__resource_templates", curie=MCP.curie('resourceTemplates'),
                   model_uri=MCP.mcpListResourceTemplatesResult__resource_templates, domain=None, range=Union[Union[dict, McpResourceTemplate], list[Union[dict, McpResourceTemplate]]])

slots.mcpListResourceTemplatesResult__result_type = Slot(uri=MCP.resultType, name="mcpListResourceTemplatesResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpListResourceTemplatesResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpListResourceTemplatesResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpListResourceTemplatesResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpListResourceTemplatesResult__ttl_ms, domain=None, range=int)

slots.mcpListResourceTemplatesResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpListResourceTemplatesResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListResourceTemplatesResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpListResourceTemplatesResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListResourceTemplatesResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListResourceTemplatesResultResponse__jsonrpc, domain=None, range=str)

slots.mcpListResourceTemplatesResultResponse__result = Slot(uri=MCP.result, name="mcpListResourceTemplatesResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpListResourceTemplatesResultResponse__result, domain=None, range=Union[dict, McpListResourceTemplatesResult])

slots.mcpListResourcesRequest__identifier = Slot(uri=MCP.identifier, name="mcpListResourcesRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListResourcesRequest__identifier, domain=None, range=Union[str, int])

slots.mcpListResourcesRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListResourcesRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListResourcesRequest__jsonrpc, domain=None, range=str)

slots.mcpListResourcesRequest__method = Slot(uri=MCP.method, name="mcpListResourcesRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpListResourcesRequest__method, domain=None, range=str)

slots.mcpListResourcesRequest__params = Slot(uri=MCP.params, name="mcpListResourcesRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpListResourcesRequest__params, domain=None, range=Union[dict, McpPaginatedRequestParams])

slots.mcpListResourcesResult__meta = Slot(uri=MCP._meta, name="mcpListResourcesResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpListResourcesResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpListResourcesResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpListResourcesResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpListResourcesResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpListResourcesResult__next_cursor = Slot(uri=MCP.nextCursor, name="mcpListResourcesResult__next_cursor", curie=MCP.curie('nextCursor'),
                   model_uri=MCP.mcpListResourcesResult__next_cursor, domain=None, range=Optional[Union[str, McpCursor]])

slots.mcpListResourcesResult__resources = Slot(uri=MCP.resources, name="mcpListResourcesResult__resources", curie=MCP.curie('resources'),
                   model_uri=MCP.mcpListResourcesResult__resources, domain=None, range=Union[Union[dict, McpResource], list[Union[dict, McpResource]]])

slots.mcpListResourcesResult__result_type = Slot(uri=MCP.resultType, name="mcpListResourcesResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpListResourcesResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpListResourcesResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpListResourcesResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpListResourcesResult__ttl_ms, domain=None, range=int)

slots.mcpListResourcesResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpListResourcesResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListResourcesResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpListResourcesResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListResourcesResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListResourcesResultResponse__jsonrpc, domain=None, range=str)

slots.mcpListResourcesResultResponse__result = Slot(uri=MCP.result, name="mcpListResourcesResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpListResourcesResultResponse__result, domain=None, range=Union[dict, McpListResourcesResult])

slots.mcpListRootsRequest__method = Slot(uri=MCP.method, name="mcpListRootsRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpListRootsRequest__method, domain=None, range=str)

slots.mcpListRootsRequest__params = Slot(uri=MCP.params, name="mcpListRootsRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpListRootsRequest__params, domain=None, range=Optional[Union[dict, McpListRootsRequestParams]])

slots.mcpListRootsRequestParams__meta = Slot(uri=MCP._meta, name="mcpListRootsRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpListRootsRequestParams__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpListRootsResult__roots = Slot(uri=MCP.roots, name="mcpListRootsResult__roots", curie=MCP.curie('roots'),
                   model_uri=MCP.mcpListRootsResult__roots, domain=None, range=Union[Union[dict, McpRoot], list[Union[dict, McpRoot]]])

slots.mcpListToolsRequest__identifier = Slot(uri=MCP.identifier, name="mcpListToolsRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListToolsRequest__identifier, domain=None, range=Union[str, int])

slots.mcpListToolsRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListToolsRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListToolsRequest__jsonrpc, domain=None, range=str)

slots.mcpListToolsRequest__method = Slot(uri=MCP.method, name="mcpListToolsRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpListToolsRequest__method, domain=None, range=str)

slots.mcpListToolsRequest__params = Slot(uri=MCP.params, name="mcpListToolsRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpListToolsRequest__params, domain=None, range=Union[dict, McpPaginatedRequestParams])

slots.mcpListToolsResult__meta = Slot(uri=MCP._meta, name="mcpListToolsResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpListToolsResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpListToolsResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpListToolsResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpListToolsResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpListToolsResult__next_cursor = Slot(uri=MCP.nextCursor, name="mcpListToolsResult__next_cursor", curie=MCP.curie('nextCursor'),
                   model_uri=MCP.mcpListToolsResult__next_cursor, domain=None, range=Optional[Union[str, McpCursor]])

slots.mcpListToolsResult__result_type = Slot(uri=MCP.resultType, name="mcpListToolsResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpListToolsResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpListToolsResult__tools = Slot(uri=MCP.tools, name="mcpListToolsResult__tools", curie=MCP.curie('tools'),
                   model_uri=MCP.mcpListToolsResult__tools, domain=None, range=Union[Union[dict, McpTool], list[Union[dict, McpTool]]])

slots.mcpListToolsResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpListToolsResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpListToolsResult__ttl_ms, domain=None, range=int)

slots.mcpListToolsResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpListToolsResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpListToolsResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpListToolsResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpListToolsResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpListToolsResultResponse__jsonrpc, domain=None, range=str)

slots.mcpListToolsResultResponse__result = Slot(uri=MCP.result, name="mcpListToolsResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpListToolsResultResponse__result, domain=None, range=Union[dict, McpListToolsResult])

slots.mcpLoggingMessageNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpLoggingMessageNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpLoggingMessageNotification__jsonrpc, domain=None, range=str)

slots.mcpLoggingMessageNotification__method = Slot(uri=MCP.method, name="mcpLoggingMessageNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpLoggingMessageNotification__method, domain=None, range=str)

slots.mcpLoggingMessageNotification__params = Slot(uri=MCP.params, name="mcpLoggingMessageNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpLoggingMessageNotification__params, domain=None, range=Union[dict, McpLoggingMessageNotificationParams])

slots.mcpLoggingMessageNotificationParams__meta = Slot(uri=MCP._meta, name="mcpLoggingMessageNotificationParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpLoggingMessageNotificationParams__meta, domain=None, range=Optional[Union[dict, McpNotificationMetaObject]])

slots.mcpLoggingMessageNotificationParams__data = Slot(uri=MCP.data, name="mcpLoggingMessageNotificationParams__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpLoggingMessageNotificationParams__data, domain=None, range=Union[dict, McpJSONValue])

slots.mcpLoggingMessageNotificationParams__level = Slot(uri=MCP.level, name="mcpLoggingMessageNotificationParams__level", curie=MCP.curie('level'),
                   model_uri=MCP.mcpLoggingMessageNotificationParams__level, domain=None, range=Union[str, "McpLoggingLevel"])

slots.mcpLoggingMessageNotificationParams__logger = Slot(uri=MCP.logger, name="mcpLoggingMessageNotificationParams__logger", curie=MCP.curie('logger'),
                   model_uri=MCP.mcpLoggingMessageNotificationParams__logger, domain=None, range=Optional[str])

slots.mcpMethodNotFoundError__code = Slot(uri=MCP.code, name="mcpMethodNotFoundError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpMethodNotFoundError__code, domain=None, range=int)

slots.mcpMethodNotFoundError__data = Slot(uri=MCP.data, name="mcpMethodNotFoundError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpMethodNotFoundError__data, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpMethodNotFoundError__message = Slot(uri=MCP.message, name="mcpMethodNotFoundError__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpMethodNotFoundError__message, domain=None, range=str)

slots.mcpMissingRequiredClientCapabilityError__error = Slot(uri=MCP.error, name="mcpMissingRequiredClientCapabilityError__error", curie=MCP.curie('error'),
                   model_uri=MCP.mcpMissingRequiredClientCapabilityError__error, domain=None, range=Union[dict, McpMissingRequiredClientCapabilityErrorError])

slots.mcpMissingRequiredClientCapabilityError__identifier = Slot(uri=MCP.identifier, name="mcpMissingRequiredClientCapabilityError__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpMissingRequiredClientCapabilityError__identifier, domain=None, range=Optional[Union[str, int]])

slots.mcpMissingRequiredClientCapabilityError__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpMissingRequiredClientCapabilityError__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpMissingRequiredClientCapabilityError__jsonrpc, domain=None, range=str)

slots.mcpMissingRequiredClientCapabilityErrorError__code = Slot(uri=MCP.code, name="mcpMissingRequiredClientCapabilityErrorError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpMissingRequiredClientCapabilityErrorError__code, domain=None, range=int)

slots.mcpMissingRequiredClientCapabilityErrorError__data = Slot(uri=MCP.data, name="mcpMissingRequiredClientCapabilityErrorError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpMissingRequiredClientCapabilityErrorError__data, domain=None, range=Union[dict, McpMissingRequiredClientCapabilityErrorErrorData])

slots.mcpMissingRequiredClientCapabilityErrorErrorData__required_capabilities = Slot(uri=MCP.requiredCapabilities, name="mcpMissingRequiredClientCapabilityErrorErrorData__required_capabilities", curie=MCP.curie('requiredCapabilities'),
                   model_uri=MCP.mcpMissingRequiredClientCapabilityErrorErrorData__required_capabilities, domain=None, range=Union[dict, McpClientCapabilities])

slots.mcpModelPreferences__cost_priority = Slot(uri=MCP.costPriority, name="mcpModelPreferences__cost_priority", curie=MCP.curie('costPriority'),
                   model_uri=MCP.mcpModelPreferences__cost_priority, domain=None, range=Optional[float])

slots.mcpModelPreferences__hints = Slot(uri=MCP.hints, name="mcpModelPreferences__hints", curie=MCP.curie('hints'),
                   model_uri=MCP.mcpModelPreferences__hints, domain=None, range=Optional[Union[Union[dict, McpModelHint], list[Union[dict, McpModelHint]]]])

slots.mcpModelPreferences__intelligence_priority = Slot(uri=MCP.intelligencePriority, name="mcpModelPreferences__intelligence_priority", curie=MCP.curie('intelligencePriority'),
                   model_uri=MCP.mcpModelPreferences__intelligence_priority, domain=None, range=Optional[float])

slots.mcpModelPreferences__speed_priority = Slot(uri=MCP.speedPriority, name="mcpModelPreferences__speed_priority", curie=MCP.curie('speedPriority'),
                   model_uri=MCP.mcpModelPreferences__speed_priority, domain=None, range=Optional[float])

slots.mcpNotification__method = Slot(uri=MCP.method, name="mcpNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpNotification__method, domain=None, range=str)

slots.mcpNotification__params = Slot(uri=MCP.params, name="mcpNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpNotification__params, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpNotificationMetaObject__mcp_subscription_id = Slot(uri=MCP.mcp_subscription_id, name="mcpNotificationMetaObject__mcp_subscription_id", curie=MCP.curie('mcp_subscription_id'),
                   model_uri=MCP.mcpNotificationMetaObject__mcp_subscription_id, domain=None, range=Optional[Union[str, int]])

slots.mcpNotificationParams__meta = Slot(uri=MCP._meta, name="mcpNotificationParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpNotificationParams__meta, domain=None, range=Optional[Union[dict, McpNotificationMetaObject]])

slots.mcpNumberSchema__default = Slot(uri=MCP.default, name="mcpNumberSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpNumberSchema__default, domain=None, range=Optional[float])

slots.mcpNumberSchema__maximum = Slot(uri=MCP.maximum, name="mcpNumberSchema__maximum", curie=MCP.curie('maximum'),
                   model_uri=MCP.mcpNumberSchema__maximum, domain=None, range=Optional[float])

slots.mcpNumberSchema__minimum = Slot(uri=MCP.minimum, name="mcpNumberSchema__minimum", curie=MCP.curie('minimum'),
                   model_uri=MCP.mcpNumberSchema__minimum, domain=None, range=Optional[float])

slots.mcpNumberSchema__kind = Slot(uri=MCP.kind, name="mcpNumberSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpNumberSchema__kind, domain=None, range=Union[str, "McpNumberSchemaType"])

slots.mcpPaginatedRequest__identifier = Slot(uri=MCP.identifier, name="mcpPaginatedRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpPaginatedRequest__identifier, domain=None, range=Union[str, int])

slots.mcpPaginatedRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpPaginatedRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpPaginatedRequest__jsonrpc, domain=None, range=str)

slots.mcpPaginatedRequest__method = Slot(uri=MCP.method, name="mcpPaginatedRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpPaginatedRequest__method, domain=None, range=str)

slots.mcpPaginatedRequest__params = Slot(uri=MCP.params, name="mcpPaginatedRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpPaginatedRequest__params, domain=None, range=Union[dict, McpPaginatedRequestParams])

slots.mcpPaginatedRequestParams__meta = Slot(uri=MCP._meta, name="mcpPaginatedRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpPaginatedRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpPaginatedRequestParams__cursor = Slot(uri=MCP.cursor, name="mcpPaginatedRequestParams__cursor", curie=MCP.curie('cursor'),
                   model_uri=MCP.mcpPaginatedRequestParams__cursor, domain=None, range=Optional[Union[str, McpCursor]])

slots.mcpPaginatedResult__meta = Slot(uri=MCP._meta, name="mcpPaginatedResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpPaginatedResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpPaginatedResult__next_cursor = Slot(uri=MCP.nextCursor, name="mcpPaginatedResult__next_cursor", curie=MCP.curie('nextCursor'),
                   model_uri=MCP.mcpPaginatedResult__next_cursor, domain=None, range=Optional[Union[str, McpCursor]])

slots.mcpPaginatedResult__result_type = Slot(uri=MCP.resultType, name="mcpPaginatedResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpPaginatedResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpParseError__code = Slot(uri=MCP.code, name="mcpParseError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpParseError__code, domain=None, range=int)

slots.mcpParseError__data = Slot(uri=MCP.data, name="mcpParseError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpParseError__data, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpParseError__message = Slot(uri=MCP.message, name="mcpParseError__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpParseError__message, domain=None, range=str)

slots.mcpProgressNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpProgressNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpProgressNotification__jsonrpc, domain=None, range=str)

slots.mcpProgressNotification__method = Slot(uri=MCP.method, name="mcpProgressNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpProgressNotification__method, domain=None, range=str)

slots.mcpProgressNotification__params = Slot(uri=MCP.params, name="mcpProgressNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpProgressNotification__params, domain=None, range=Union[dict, McpProgressNotificationParams])

slots.mcpProgressNotificationParams__meta = Slot(uri=MCP._meta, name="mcpProgressNotificationParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpProgressNotificationParams__meta, domain=None, range=Optional[Union[dict, McpNotificationMetaObject]])

slots.mcpProgressNotificationParams__message = Slot(uri=MCP.message, name="mcpProgressNotificationParams__message", curie=MCP.curie('message'),
                   model_uri=MCP.mcpProgressNotificationParams__message, domain=None, range=Optional[str])

slots.mcpProgressNotificationParams__progress = Slot(uri=MCP.progress, name="mcpProgressNotificationParams__progress", curie=MCP.curie('progress'),
                   model_uri=MCP.mcpProgressNotificationParams__progress, domain=None, range=float)

slots.mcpProgressNotificationParams__progress_token = Slot(uri=MCP.progressToken, name="mcpProgressNotificationParams__progress_token", curie=MCP.curie('progressToken'),
                   model_uri=MCP.mcpProgressNotificationParams__progress_token, domain=None, range=Union[str, int])

slots.mcpProgressNotificationParams__total = Slot(uri=MCP.total, name="mcpProgressNotificationParams__total", curie=MCP.curie('total'),
                   model_uri=MCP.mcpProgressNotificationParams__total, domain=None, range=Optional[float])

slots.mcpPrompt__meta = Slot(uri=MCP._meta, name="mcpPrompt__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpPrompt__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpPrompt__arguments = Slot(uri=MCP.arguments, name="mcpPrompt__arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.mcpPrompt__arguments, domain=None, range=Optional[Union[Union[dict, McpPromptArgument], list[Union[dict, McpPromptArgument]]]])

slots.mcpPrompt__icons = Slot(uri=MCP.icons, name="mcpPrompt__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpPrompt__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpPromptArgument__required = Slot(uri=SCHEMA.valueRequired, name="mcpPromptArgument__required", curie=SCHEMA.curie('valueRequired'),
                   model_uri=MCP.mcpPromptArgument__required, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpPromptListChangedNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpPromptListChangedNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpPromptListChangedNotification__jsonrpc, domain=None, range=str)

slots.mcpPromptListChangedNotification__method = Slot(uri=MCP.method, name="mcpPromptListChangedNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpPromptListChangedNotification__method, domain=None, range=str)

slots.mcpPromptListChangedNotification__params = Slot(uri=MCP.params, name="mcpPromptListChangedNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpPromptListChangedNotification__params, domain=None, range=Optional[Union[dict, McpNotificationParams]])

slots.mcpPromptMessage__content = Slot(uri=MCP.content, name="mcpPromptMessage__content", curie=MCP.curie('content'),
                   model_uri=MCP.mcpPromptMessage__content, domain=None, range=Union[dict, McpContentBlock])

slots.mcpPromptMessage__role = Slot(uri=MCP.role, name="mcpPromptMessage__role", curie=MCP.curie('role'),
                   model_uri=MCP.mcpPromptMessage__role, domain=None, range=Union[str, "McpRole"])

slots.mcpPromptReference__kind = Slot(uri=MCP.kind, name="mcpPromptReference__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpPromptReference__kind, domain=None, range=str)

slots.mcpReadResourceRequest__identifier = Slot(uri=MCP.identifier, name="mcpReadResourceRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpReadResourceRequest__identifier, domain=None, range=Union[str, int])

slots.mcpReadResourceRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpReadResourceRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpReadResourceRequest__jsonrpc, domain=None, range=str)

slots.mcpReadResourceRequest__method = Slot(uri=MCP.method, name="mcpReadResourceRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpReadResourceRequest__method, domain=None, range=str)

slots.mcpReadResourceRequest__params = Slot(uri=MCP.params, name="mcpReadResourceRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpReadResourceRequest__params, domain=None, range=Union[dict, McpReadResourceRequestParams])

slots.mcpReadResourceRequestParams__meta = Slot(uri=MCP._meta, name="mcpReadResourceRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpReadResourceRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpReadResourceRequestParams__input_responses = Slot(uri=MCP.inputResponses, name="mcpReadResourceRequestParams__input_responses", curie=MCP.curie('inputResponses'),
                   model_uri=MCP.mcpReadResourceRequestParams__input_responses, domain=None, range=Optional[Union[dict, McpInputResponses]])

slots.mcpReadResourceRequestParams__request_state = Slot(uri=MCP.requestState, name="mcpReadResourceRequestParams__request_state", curie=MCP.curie('requestState'),
                   model_uri=MCP.mcpReadResourceRequestParams__request_state, domain=None, range=Optional[str])

slots.mcpReadResourceRequestParams__uri = Slot(uri=MCP.uri, name="mcpReadResourceRequestParams__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpReadResourceRequestParams__uri, domain=None, range=Union[str, URI])

slots.mcpReadResourceResult__meta = Slot(uri=MCP._meta, name="mcpReadResourceResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpReadResourceResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpReadResourceResult__cache_scope = Slot(uri=MCP.cacheScope, name="mcpReadResourceResult__cache_scope", curie=MCP.curie('cacheScope'),
                   model_uri=MCP.mcpReadResourceResult__cache_scope, domain=None, range=Union[str, "McpCacheScope"])

slots.mcpReadResourceResult__contents = Slot(uri=MCP.contents, name="mcpReadResourceResult__contents", curie=MCP.curie('contents'),
                   model_uri=MCP.mcpReadResourceResult__contents, domain=None, range=Union[str, list[str]])

slots.mcpReadResourceResult__result_type = Slot(uri=MCP.resultType, name="mcpReadResourceResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpReadResourceResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpReadResourceResult__ttl_ms = Slot(uri=MCP.ttlMs, name="mcpReadResourceResult__ttl_ms", curie=MCP.curie('ttlMs'),
                   model_uri=MCP.mcpReadResourceResult__ttl_ms, domain=None, range=int)

slots.mcpReadResourceResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpReadResourceResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpReadResourceResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpReadResourceResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpReadResourceResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpReadResourceResultResponse__jsonrpc, domain=None, range=str)

slots.mcpReadResourceResultResponse__result = Slot(uri=MCP.result, name="mcpReadResourceResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpReadResourceResultResponse__result, domain=None, range=Union[dict, McpInputRequiredResult, McpReadResourceResult])

slots.mcpRequest__method = Slot(uri=MCP.method, name="mcpRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpRequest__method, domain=None, range=str)

slots.mcpRequest__params = Slot(uri=MCP.params, name="mcpRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpRequest__params, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpRequestMetaObject__mcp_client_capabilities = Slot(uri=MCP.mcp_client_capabilities, name="mcpRequestMetaObject__mcp_client_capabilities", curie=MCP.curie('mcp_client_capabilities'),
                   model_uri=MCP.mcpRequestMetaObject__mcp_client_capabilities, domain=None, range=Union[dict, McpClientCapabilities])

slots.mcpRequestMetaObject__mcp_client_info = Slot(uri=MCP.mcp_client_info, name="mcpRequestMetaObject__mcp_client_info", curie=MCP.curie('mcp_client_info'),
                   model_uri=MCP.mcpRequestMetaObject__mcp_client_info, domain=None, range=Optional[Union[dict, McpImplementation]])

slots.mcpRequestMetaObject__mcp_log_level = Slot(uri=MCP.mcp_log_level, name="mcpRequestMetaObject__mcp_log_level", curie=MCP.curie('mcp_log_level'),
                   model_uri=MCP.mcpRequestMetaObject__mcp_log_level, domain=None, range=Optional[Union[str, "McpLoggingLevel"]])

slots.mcpRequestMetaObject__mcp_protocol_version = Slot(uri=MCP.mcp_protocol_version, name="mcpRequestMetaObject__mcp_protocol_version", curie=MCP.curie('mcp_protocol_version'),
                   model_uri=MCP.mcpRequestMetaObject__mcp_protocol_version, domain=None, range=str)

slots.mcpRequestMetaObject__progress_token = Slot(uri=MCP.progressToken, name="mcpRequestMetaObject__progress_token", curie=MCP.curie('progressToken'),
                   model_uri=MCP.mcpRequestMetaObject__progress_token, domain=None, range=Optional[Union[str, int]])

slots.mcpRequestParams__meta = Slot(uri=MCP._meta, name="mcpRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpResource__meta = Slot(uri=MCP._meta, name="mcpResource__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResource__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpResource__annotations = Slot(uri=MCP.annotations, name="mcpResource__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpResource__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpResource__icons = Slot(uri=MCP.icons, name="mcpResource__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpResource__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpResource__mime_type = Slot(uri=MCP.mimeType, name="mcpResource__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpResource__mime_type, domain=None, range=Optional[str])

slots.mcpResource__size = Slot(uri=MCP.size, name="mcpResource__size", curie=MCP.curie('size'),
                   model_uri=MCP.mcpResource__size, domain=None, range=Optional[int])

slots.mcpResource__uri = Slot(uri=MCP.uri, name="mcpResource__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpResource__uri, domain=None, range=Union[str, URI])

slots.mcpResourceContents__meta = Slot(uri=MCP._meta, name="mcpResourceContents__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResourceContents__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpResourceContents__mime_type = Slot(uri=MCP.mimeType, name="mcpResourceContents__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpResourceContents__mime_type, domain=None, range=Optional[str])

slots.mcpResourceContents__uri = Slot(uri=MCP.uri, name="mcpResourceContents__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpResourceContents__uri, domain=None, range=Union[str, URI])

slots.mcpResourceLink__meta = Slot(uri=MCP._meta, name="mcpResourceLink__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResourceLink__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpResourceLink__annotations = Slot(uri=MCP.annotations, name="mcpResourceLink__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpResourceLink__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpResourceLink__icons = Slot(uri=MCP.icons, name="mcpResourceLink__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpResourceLink__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpResourceLink__mime_type = Slot(uri=MCP.mimeType, name="mcpResourceLink__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpResourceLink__mime_type, domain=None, range=Optional[str])

slots.mcpResourceLink__size = Slot(uri=MCP.size, name="mcpResourceLink__size", curie=MCP.curie('size'),
                   model_uri=MCP.mcpResourceLink__size, domain=None, range=Optional[int])

slots.mcpResourceLink__kind = Slot(uri=MCP.kind, name="mcpResourceLink__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpResourceLink__kind, domain=None, range=str)

slots.mcpResourceLink__uri = Slot(uri=MCP.uri, name="mcpResourceLink__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpResourceLink__uri, domain=None, range=Union[str, URI])

slots.mcpResourceListChangedNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpResourceListChangedNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpResourceListChangedNotification__jsonrpc, domain=None, range=str)

slots.mcpResourceListChangedNotification__method = Slot(uri=MCP.method, name="mcpResourceListChangedNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpResourceListChangedNotification__method, domain=None, range=str)

slots.mcpResourceListChangedNotification__params = Slot(uri=MCP.params, name="mcpResourceListChangedNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpResourceListChangedNotification__params, domain=None, range=Optional[Union[dict, McpNotificationParams]])

slots.mcpResourceRequestParams__meta = Slot(uri=MCP._meta, name="mcpResourceRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResourceRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpResourceRequestParams__uri = Slot(uri=MCP.uri, name="mcpResourceRequestParams__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpResourceRequestParams__uri, domain=None, range=Union[str, URI])

slots.mcpResourceTemplate__meta = Slot(uri=MCP._meta, name="mcpResourceTemplate__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResourceTemplate__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpResourceTemplate__annotations = Slot(uri=MCP.annotations, name="mcpResourceTemplate__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpResourceTemplate__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpResourceTemplate__icons = Slot(uri=MCP.icons, name="mcpResourceTemplate__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpResourceTemplate__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpResourceTemplate__mime_type = Slot(uri=MCP.mimeType, name="mcpResourceTemplate__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpResourceTemplate__mime_type, domain=None, range=Optional[str])

slots.mcpResourceTemplate__uri_template = Slot(uri=MCP.uriTemplate, name="mcpResourceTemplate__uri_template", curie=MCP.curie('uriTemplate'),
                   model_uri=MCP.mcpResourceTemplate__uri_template, domain=None, range=Union[str, McpUriTemplate])

slots.mcpResourceTemplateReference__kind = Slot(uri=MCP.kind, name="mcpResourceTemplateReference__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpResourceTemplateReference__kind, domain=None, range=str)

slots.mcpResourceTemplateReference__uri = Slot(uri=MCP.uri, name="mcpResourceTemplateReference__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpResourceTemplateReference__uri, domain=None, range=Union[str, McpUriTemplate])

slots.mcpResourceUpdatedNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpResourceUpdatedNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpResourceUpdatedNotification__jsonrpc, domain=None, range=str)

slots.mcpResourceUpdatedNotification__method = Slot(uri=MCP.method, name="mcpResourceUpdatedNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpResourceUpdatedNotification__method, domain=None, range=str)

slots.mcpResourceUpdatedNotification__params = Slot(uri=MCP.params, name="mcpResourceUpdatedNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpResourceUpdatedNotification__params, domain=None, range=Union[dict, McpResourceUpdatedNotificationParams])

slots.mcpResourceUpdatedNotificationParams__meta = Slot(uri=MCP._meta, name="mcpResourceUpdatedNotificationParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResourceUpdatedNotificationParams__meta, domain=None, range=Optional[Union[dict, McpNotificationMetaObject]])

slots.mcpResourceUpdatedNotificationParams__uri = Slot(uri=MCP.uri, name="mcpResourceUpdatedNotificationParams__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpResourceUpdatedNotificationParams__uri, domain=None, range=Union[str, URI])

slots.mcpResult__meta = Slot(uri=MCP._meta, name="mcpResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpResult__meta, domain=None, range=Optional[Union[dict, McpResultMetaObject]])

slots.mcpResult__result_type = Slot(uri=MCP.resultType, name="mcpResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpResultMetaObject__mcp_server_info = Slot(uri=MCP.mcp_server_info, name="mcpResultMetaObject__mcp_server_info", curie=MCP.curie('mcp_server_info'),
                   model_uri=MCP.mcpResultMetaObject__mcp_server_info, domain=None, range=Optional[Union[dict, McpImplementation]])

slots.mcpRoot__meta = Slot(uri=MCP._meta, name="mcpRoot__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpRoot__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpRoot__uri = Slot(uri=MCP.uri, name="mcpRoot__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpRoot__uri, domain=None, range=Union[str, URI])

slots.mcpSamplingMessage__meta = Slot(uri=MCP._meta, name="mcpSamplingMessage__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpSamplingMessage__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpSamplingMessage__content = Slot(uri=MCP.content, name="mcpSamplingMessage__content", curie=MCP.curie('content'),
                   model_uri=MCP.mcpSamplingMessage__content, domain=None, range=Union[dict, McpTextContent, McpImageContent, McpAudioContent, McpToolUseContent, McpToolResultContent, McpSamplingMessageContentBlock])

slots.mcpSamplingMessage__role = Slot(uri=MCP.role, name="mcpSamplingMessage__role", curie=MCP.curie('role'),
                   model_uri=MCP.mcpSamplingMessage__role, domain=None, range=Union[str, "McpRole"])

slots.mcpServerCapabilities__completions = Slot(uri=MCP.completions, name="mcpServerCapabilities__completions", curie=MCP.curie('completions'),
                   model_uri=MCP.mcpServerCapabilities__completions, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpServerCapabilities__experimental = Slot(uri=MCP.experimental, name="mcpServerCapabilities__experimental", curie=MCP.curie('experimental'),
                   model_uri=MCP.mcpServerCapabilities__experimental, domain=None, range=Optional[Union[dict, McpServerCapabilitiesExperimental]])

slots.mcpServerCapabilities__extensions = Slot(uri=MCP.extensions, name="mcpServerCapabilities__extensions", curie=MCP.curie('extensions'),
                   model_uri=MCP.mcpServerCapabilities__extensions, domain=None, range=Optional[Union[dict, McpServerCapabilitiesExtensions]])

slots.mcpServerCapabilities__logging = Slot(uri=MCP.logging, name="mcpServerCapabilities__logging", curie=MCP.curie('logging'),
                   model_uri=MCP.mcpServerCapabilities__logging, domain=None, range=Optional[Union[dict, McpJSONObject]])

slots.mcpServerCapabilities__prompts = Slot(uri=MCP.prompts, name="mcpServerCapabilities__prompts", curie=MCP.curie('prompts'),
                   model_uri=MCP.mcpServerCapabilities__prompts, domain=None, range=Optional[Union[dict, McpServerCapabilitiesPrompts]])

slots.mcpServerCapabilities__resources = Slot(uri=MCP.resources, name="mcpServerCapabilities__resources", curie=MCP.curie('resources'),
                   model_uri=MCP.mcpServerCapabilities__resources, domain=None, range=Optional[Union[dict, McpServerCapabilitiesResources]])

slots.mcpServerCapabilities__tools = Slot(uri=MCP.tools, name="mcpServerCapabilities__tools", curie=MCP.curie('tools'),
                   model_uri=MCP.mcpServerCapabilities__tools, domain=None, range=Optional[Union[dict, McpServerCapabilitiesTools]])

slots.mcpServerCapabilitiesPrompts__list_changed = Slot(uri=MCP.listChanged, name="mcpServerCapabilitiesPrompts__list_changed", curie=MCP.curie('listChanged'),
                   model_uri=MCP.mcpServerCapabilitiesPrompts__list_changed, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpServerCapabilitiesResources__list_changed = Slot(uri=MCP.listChanged, name="mcpServerCapabilitiesResources__list_changed", curie=MCP.curie('listChanged'),
                   model_uri=MCP.mcpServerCapabilitiesResources__list_changed, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpServerCapabilitiesResources__subscribe = Slot(uri=MCP.subscribe, name="mcpServerCapabilitiesResources__subscribe", curie=MCP.curie('subscribe'),
                   model_uri=MCP.mcpServerCapabilitiesResources__subscribe, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpServerCapabilitiesTools__list_changed = Slot(uri=MCP.listChanged, name="mcpServerCapabilitiesTools__list_changed", curie=MCP.curie('listChanged'),
                   model_uri=MCP.mcpServerCapabilitiesTools__list_changed, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpStringSchema__default = Slot(uri=MCP.default, name="mcpStringSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpStringSchema__default, domain=None, range=Optional[str])

slots.mcpStringSchema__format = Slot(uri=MCP.format, name="mcpStringSchema__format", curie=MCP.curie('format'),
                   model_uri=MCP.mcpStringSchema__format, domain=None, range=Optional[Union[str, "McpStringSchemaFormat"]])

slots.mcpStringSchema__max_length = Slot(uri=MCP.maxLength, name="mcpStringSchema__max_length", curie=MCP.curie('maxLength'),
                   model_uri=MCP.mcpStringSchema__max_length, domain=None, range=Optional[int])

slots.mcpStringSchema__min_length = Slot(uri=MCP.minLength, name="mcpStringSchema__min_length", curie=MCP.curie('minLength'),
                   model_uri=MCP.mcpStringSchema__min_length, domain=None, range=Optional[int])

slots.mcpStringSchema__kind = Slot(uri=MCP.kind, name="mcpStringSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpStringSchema__kind, domain=None, range=str)

slots.mcpSubscriptionFilter__prompts_list_changed = Slot(uri=MCP.promptsListChanged, name="mcpSubscriptionFilter__prompts_list_changed", curie=MCP.curie('promptsListChanged'),
                   model_uri=MCP.mcpSubscriptionFilter__prompts_list_changed, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpSubscriptionFilter__resource_subscriptions = Slot(uri=MCP.resourceSubscriptions, name="mcpSubscriptionFilter__resource_subscriptions", curie=MCP.curie('resourceSubscriptions'),
                   model_uri=MCP.mcpSubscriptionFilter__resource_subscriptions, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpSubscriptionFilter__resources_list_changed = Slot(uri=MCP.resourcesListChanged, name="mcpSubscriptionFilter__resources_list_changed", curie=MCP.curie('resourcesListChanged'),
                   model_uri=MCP.mcpSubscriptionFilter__resources_list_changed, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpSubscriptionFilter__tools_list_changed = Slot(uri=MCP.toolsListChanged, name="mcpSubscriptionFilter__tools_list_changed", curie=MCP.curie('toolsListChanged'),
                   model_uri=MCP.mcpSubscriptionFilter__tools_list_changed, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpSubscriptionsAcknowledgedNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpSubscriptionsAcknowledgedNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpSubscriptionsAcknowledgedNotification__jsonrpc, domain=None, range=str)

slots.mcpSubscriptionsAcknowledgedNotification__method = Slot(uri=MCP.method, name="mcpSubscriptionsAcknowledgedNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpSubscriptionsAcknowledgedNotification__method, domain=None, range=str)

slots.mcpSubscriptionsAcknowledgedNotification__params = Slot(uri=MCP.params, name="mcpSubscriptionsAcknowledgedNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpSubscriptionsAcknowledgedNotification__params, domain=None, range=Union[dict, McpSubscriptionsAcknowledgedNotificationParams])

slots.mcpSubscriptionsAcknowledgedNotificationParams__meta = Slot(uri=MCP._meta, name="mcpSubscriptionsAcknowledgedNotificationParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpSubscriptionsAcknowledgedNotificationParams__meta, domain=None, range=Optional[Union[dict, McpNotificationMetaObject]])

slots.mcpSubscriptionsAcknowledgedNotificationParams__notifications = Slot(uri=MCP.notifications, name="mcpSubscriptionsAcknowledgedNotificationParams__notifications", curie=MCP.curie('notifications'),
                   model_uri=MCP.mcpSubscriptionsAcknowledgedNotificationParams__notifications, domain=None, range=Union[dict, McpSubscriptionFilter])

slots.mcpSubscriptionsListenRequest__identifier = Slot(uri=MCP.identifier, name="mcpSubscriptionsListenRequest__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpSubscriptionsListenRequest__identifier, domain=None, range=Union[str, int])

slots.mcpSubscriptionsListenRequest__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpSubscriptionsListenRequest__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpSubscriptionsListenRequest__jsonrpc, domain=None, range=str)

slots.mcpSubscriptionsListenRequest__method = Slot(uri=MCP.method, name="mcpSubscriptionsListenRequest__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpSubscriptionsListenRequest__method, domain=None, range=str)

slots.mcpSubscriptionsListenRequest__params = Slot(uri=MCP.params, name="mcpSubscriptionsListenRequest__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpSubscriptionsListenRequest__params, domain=None, range=Union[dict, McpSubscriptionsListenRequestParams])

slots.mcpSubscriptionsListenRequestParams__meta = Slot(uri=MCP._meta, name="mcpSubscriptionsListenRequestParams__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpSubscriptionsListenRequestParams__meta, domain=None, range=Union[dict, McpRequestMetaObject])

slots.mcpSubscriptionsListenRequestParams__notifications = Slot(uri=MCP.notifications, name="mcpSubscriptionsListenRequestParams__notifications", curie=MCP.curie('notifications'),
                   model_uri=MCP.mcpSubscriptionsListenRequestParams__notifications, domain=None, range=Union[dict, McpSubscriptionFilter])

slots.mcpSubscriptionsListenResult__meta = Slot(uri=MCP._meta, name="mcpSubscriptionsListenResult__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpSubscriptionsListenResult__meta, domain=None, range=Union[dict, McpSubscriptionsListenResultMetaObject])

slots.mcpSubscriptionsListenResult__result_type = Slot(uri=MCP.resultType, name="mcpSubscriptionsListenResult__result_type", curie=MCP.curie('resultType'),
                   model_uri=MCP.mcpSubscriptionsListenResult__result_type, domain=None, range=Union[str, McpResultType])

slots.mcpSubscriptionsListenResultMetaObject__mcp_server_info = Slot(uri=MCP.mcp_server_info, name="mcpSubscriptionsListenResultMetaObject__mcp_server_info", curie=MCP.curie('mcp_server_info'),
                   model_uri=MCP.mcpSubscriptionsListenResultMetaObject__mcp_server_info, domain=None, range=Optional[Union[dict, McpImplementation]])

slots.mcpSubscriptionsListenResultMetaObject__mcp_subscription_id = Slot(uri=MCP.mcp_subscription_id, name="mcpSubscriptionsListenResultMetaObject__mcp_subscription_id", curie=MCP.curie('mcp_subscription_id'),
                   model_uri=MCP.mcpSubscriptionsListenResultMetaObject__mcp_subscription_id, domain=None, range=Union[str, int])

slots.mcpSubscriptionsListenResultResponse__identifier = Slot(uri=MCP.identifier, name="mcpSubscriptionsListenResultResponse__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpSubscriptionsListenResultResponse__identifier, domain=None, range=Union[str, int])

slots.mcpSubscriptionsListenResultResponse__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpSubscriptionsListenResultResponse__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpSubscriptionsListenResultResponse__jsonrpc, domain=None, range=str)

slots.mcpSubscriptionsListenResultResponse__result = Slot(uri=MCP.result, name="mcpSubscriptionsListenResultResponse__result", curie=MCP.curie('result'),
                   model_uri=MCP.mcpSubscriptionsListenResultResponse__result, domain=None, range=Union[dict, McpSubscriptionsListenResult])

slots.mcpTextContent__meta = Slot(uri=MCP._meta, name="mcpTextContent__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpTextContent__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpTextContent__annotations = Slot(uri=MCP.annotations, name="mcpTextContent__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpTextContent__annotations, domain=None, range=Optional[Union[dict, McpAnnotations]])

slots.mcpTextContent__text = Slot(uri=MCP.text, name="mcpTextContent__text", curie=MCP.curie('text'),
                   model_uri=MCP.mcpTextContent__text, domain=None, range=str)

slots.mcpTextContent__kind = Slot(uri=MCP.kind, name="mcpTextContent__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpTextContent__kind, domain=None, range=str)

slots.mcpTextResourceContents__meta = Slot(uri=MCP._meta, name="mcpTextResourceContents__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpTextResourceContents__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpTextResourceContents__mime_type = Slot(uri=MCP.mimeType, name="mcpTextResourceContents__mime_type", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mcpTextResourceContents__mime_type, domain=None, range=Optional[str])

slots.mcpTextResourceContents__text = Slot(uri=MCP.text, name="mcpTextResourceContents__text", curie=MCP.curie('text'),
                   model_uri=MCP.mcpTextResourceContents__text, domain=None, range=str)

slots.mcpTextResourceContents__uri = Slot(uri=MCP.uri, name="mcpTextResourceContents__uri", curie=MCP.curie('uri'),
                   model_uri=MCP.mcpTextResourceContents__uri, domain=None, range=Union[str, URI])

slots.mcpTitledMultiSelectEnumSchema__default = Slot(uri=MCP.default, name="mcpTitledMultiSelectEnumSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchema__default, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpTitledMultiSelectEnumSchema__items = Slot(uri=MCP.items, name="mcpTitledMultiSelectEnumSchema__items", curie=MCP.curie('items'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchema__items, domain=None, range=Union[dict, McpTitledMultiSelectEnumSchemaItems])

slots.mcpTitledMultiSelectEnumSchema__max_items = Slot(uri=MCP.maxItems, name="mcpTitledMultiSelectEnumSchema__max_items", curie=MCP.curie('maxItems'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchema__max_items, domain=None, range=Optional[int])

slots.mcpTitledMultiSelectEnumSchema__min_items = Slot(uri=MCP.minItems, name="mcpTitledMultiSelectEnumSchema__min_items", curie=MCP.curie('minItems'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchema__min_items, domain=None, range=Optional[int])

slots.mcpTitledMultiSelectEnumSchema__kind = Slot(uri=MCP.kind, name="mcpTitledMultiSelectEnumSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchema__kind, domain=None, range=str)

slots.mcpTitledMultiSelectEnumSchemaItems__any_of = Slot(uri=MCP.anyOf, name="mcpTitledMultiSelectEnumSchemaItems__any_of", curie=MCP.curie('anyOf'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchemaItems__any_of, domain=None, range=Union[Union[dict, McpTitledMultiSelectEnumSchemaItemsAnyOf], list[Union[dict, McpTitledMultiSelectEnumSchemaItemsAnyOf]]])

slots.mcpTitledMultiSelectEnumSchemaItemsAnyOf__const = Slot(uri=MCP.const, name="mcpTitledMultiSelectEnumSchemaItemsAnyOf__const", curie=MCP.curie('const'),
                   model_uri=MCP.mcpTitledMultiSelectEnumSchemaItemsAnyOf__const, domain=None, range=str)

slots.mcpTitledSingleSelectEnumSchema__default = Slot(uri=MCP.default, name="mcpTitledSingleSelectEnumSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpTitledSingleSelectEnumSchema__default, domain=None, range=Optional[str])

slots.mcpTitledSingleSelectEnumSchema__one_of = Slot(uri=MCP.oneOf, name="mcpTitledSingleSelectEnumSchema__one_of", curie=MCP.curie('oneOf'),
                   model_uri=MCP.mcpTitledSingleSelectEnumSchema__one_of, domain=None, range=Union[Union[dict, McpTitledSingleSelectEnumSchemaOneOf], list[Union[dict, McpTitledSingleSelectEnumSchemaOneOf]]])

slots.mcpTitledSingleSelectEnumSchema__kind = Slot(uri=MCP.kind, name="mcpTitledSingleSelectEnumSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpTitledSingleSelectEnumSchema__kind, domain=None, range=str)

slots.mcpTitledSingleSelectEnumSchemaOneOf__const = Slot(uri=MCP.const, name="mcpTitledSingleSelectEnumSchemaOneOf__const", curie=MCP.curie('const'),
                   model_uri=MCP.mcpTitledSingleSelectEnumSchemaOneOf__const, domain=None, range=str)

slots.mcpTool__meta = Slot(uri=MCP._meta, name="mcpTool__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpTool__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpTool__annotations = Slot(uri=MCP.annotations, name="mcpTool__annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.mcpTool__annotations, domain=None, range=Optional[Union[dict, McpToolAnnotations]])

slots.mcpTool__icons = Slot(uri=MCP.icons, name="mcpTool__icons", curie=MCP.curie('icons'),
                   model_uri=MCP.mcpTool__icons, domain=None, range=Optional[Union[Union[dict, McpIcon], list[Union[dict, McpIcon]]]])

slots.mcpTool__input_schema = Slot(uri=MCP.inputSchema, name="mcpTool__input_schema", curie=MCP.curie('inputSchema'),
                   model_uri=MCP.mcpTool__input_schema, domain=None, range=Union[dict, McpToolInputSchema])

slots.mcpTool__output_schema = Slot(uri=MCP.outputSchema, name="mcpTool__output_schema", curie=MCP.curie('outputSchema'),
                   model_uri=MCP.mcpTool__output_schema, domain=None, range=Optional[Union[dict, McpToolOutputSchema]])

slots.mcpToolAnnotations__destructive_hint = Slot(uri=MCP.destructiveHint, name="mcpToolAnnotations__destructive_hint", curie=MCP.curie('destructiveHint'),
                   model_uri=MCP.mcpToolAnnotations__destructive_hint, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpToolAnnotations__idempotent_hint = Slot(uri=MCP.idempotentHint, name="mcpToolAnnotations__idempotent_hint", curie=MCP.curie('idempotentHint'),
                   model_uri=MCP.mcpToolAnnotations__idempotent_hint, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpToolAnnotations__open_world_hint = Slot(uri=MCP.openWorldHint, name="mcpToolAnnotations__open_world_hint", curie=MCP.curie('openWorldHint'),
                   model_uri=MCP.mcpToolAnnotations__open_world_hint, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpToolAnnotations__read_only_hint = Slot(uri=MCP.readOnlyHint, name="mcpToolAnnotations__read_only_hint", curie=MCP.curie('readOnlyHint'),
                   model_uri=MCP.mcpToolAnnotations__read_only_hint, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpToolChoice__mode = Slot(uri=MCP.mode, name="mcpToolChoice__mode", curie=MCP.curie('mode'),
                   model_uri=MCP.mcpToolChoice__mode, domain=None, range=Optional[Union[str, "McpToolChoiceMode"]])

slots.mcpToolInputSchema__schema_dialect = Slot(uri=MCP.schema_dialect, name="mcpToolInputSchema__schema_dialect", curie=MCP.curie('schema_dialect'),
                   model_uri=MCP.mcpToolInputSchema__schema_dialect, domain=None, range=Optional[str])

slots.mcpToolInputSchema__kind = Slot(uri=MCP.kind, name="mcpToolInputSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpToolInputSchema__kind, domain=None, range=str)

slots.mcpToolListChangedNotification__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpToolListChangedNotification__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpToolListChangedNotification__jsonrpc, domain=None, range=str)

slots.mcpToolListChangedNotification__method = Slot(uri=MCP.method, name="mcpToolListChangedNotification__method", curie=MCP.curie('method'),
                   model_uri=MCP.mcpToolListChangedNotification__method, domain=None, range=str)

slots.mcpToolListChangedNotification__params = Slot(uri=MCP.params, name="mcpToolListChangedNotification__params", curie=MCP.curie('params'),
                   model_uri=MCP.mcpToolListChangedNotification__params, domain=None, range=Optional[Union[dict, McpNotificationParams]])

slots.mcpToolOutputSchema__schema_dialect = Slot(uri=MCP.schema_dialect, name="mcpToolOutputSchema__schema_dialect", curie=MCP.curie('schema_dialect'),
                   model_uri=MCP.mcpToolOutputSchema__schema_dialect, domain=None, range=Optional[str])

slots.mcpToolResultContent__meta = Slot(uri=MCP._meta, name="mcpToolResultContent__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpToolResultContent__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpToolResultContent__content = Slot(uri=MCP.content, name="mcpToolResultContent__content", curie=MCP.curie('content'),
                   model_uri=MCP.mcpToolResultContent__content, domain=None, range=Union[Union[dict, McpContentBlock], list[Union[dict, McpContentBlock]]])

slots.mcpToolResultContent__is_error = Slot(uri=MCP.isError, name="mcpToolResultContent__is_error", curie=MCP.curie('isError'),
                   model_uri=MCP.mcpToolResultContent__is_error, domain=None, range=Optional[Union[bool, Bool]])

slots.mcpToolResultContent__structured_content = Slot(uri=MCP.structuredContent, name="mcpToolResultContent__structured_content", curie=MCP.curie('structuredContent'),
                   model_uri=MCP.mcpToolResultContent__structured_content, domain=None, range=Optional[Union[dict, McpJSONValue]])

slots.mcpToolResultContent__tool_use_id = Slot(uri=MCP.toolUseId, name="mcpToolResultContent__tool_use_id", curie=MCP.curie('toolUseId'),
                   model_uri=MCP.mcpToolResultContent__tool_use_id, domain=None, range=str)

slots.mcpToolResultContent__kind = Slot(uri=MCP.kind, name="mcpToolResultContent__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpToolResultContent__kind, domain=None, range=str)

slots.mcpToolUseContent__meta = Slot(uri=MCP._meta, name="mcpToolUseContent__meta", curie=MCP.curie('_meta'),
                   model_uri=MCP.mcpToolUseContent__meta, domain=None, range=Optional[Union[dict, McpMetaObject]])

slots.mcpToolUseContent__identifier = Slot(uri=MCP.identifier, name="mcpToolUseContent__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpToolUseContent__identifier, domain=None, range=str)

slots.mcpToolUseContent__input = Slot(uri=MCP.input, name="mcpToolUseContent__input", curie=MCP.curie('input'),
                   model_uri=MCP.mcpToolUseContent__input, domain=None, range=Union[dict, McpJSONObject])

slots.mcpToolUseContent__kind = Slot(uri=MCP.kind, name="mcpToolUseContent__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpToolUseContent__kind, domain=None, range=str)

slots.mcpUnsupportedProtocolVersionError__error = Slot(uri=MCP.error, name="mcpUnsupportedProtocolVersionError__error", curie=MCP.curie('error'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionError__error, domain=None, range=Union[dict, McpUnsupportedProtocolVersionErrorError])

slots.mcpUnsupportedProtocolVersionError__identifier = Slot(uri=MCP.identifier, name="mcpUnsupportedProtocolVersionError__identifier", curie=MCP.curie('identifier'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionError__identifier, domain=None, range=Optional[Union[str, int]])

slots.mcpUnsupportedProtocolVersionError__jsonrpc = Slot(uri=MCP.jsonrpc, name="mcpUnsupportedProtocolVersionError__jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionError__jsonrpc, domain=None, range=str)

slots.mcpUnsupportedProtocolVersionErrorError__code = Slot(uri=MCP.code, name="mcpUnsupportedProtocolVersionErrorError__code", curie=MCP.curie('code'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionErrorError__code, domain=None, range=int)

slots.mcpUnsupportedProtocolVersionErrorError__data = Slot(uri=MCP.data, name="mcpUnsupportedProtocolVersionErrorError__data", curie=MCP.curie('data'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionErrorError__data, domain=None, range=Union[dict, McpUnsupportedProtocolVersionErrorErrorData])

slots.mcpUnsupportedProtocolVersionErrorErrorData__requested = Slot(uri=MCP.requested, name="mcpUnsupportedProtocolVersionErrorErrorData__requested", curie=MCP.curie('requested'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionErrorErrorData__requested, domain=None, range=str)

slots.mcpUnsupportedProtocolVersionErrorErrorData__supported = Slot(uri=MCP.supported, name="mcpUnsupportedProtocolVersionErrorErrorData__supported", curie=MCP.curie('supported'),
                   model_uri=MCP.mcpUnsupportedProtocolVersionErrorErrorData__supported, domain=None, range=Union[str, list[str]])

slots.mcpUntitledMultiSelectEnumSchema__default = Slot(uri=MCP.default, name="mcpUntitledMultiSelectEnumSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchema__default, domain=None, range=Optional[Union[str, list[str]]])

slots.mcpUntitledMultiSelectEnumSchema__items = Slot(uri=MCP.items, name="mcpUntitledMultiSelectEnumSchema__items", curie=MCP.curie('items'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchema__items, domain=None, range=Union[dict, McpUntitledMultiSelectEnumSchemaItems])

slots.mcpUntitledMultiSelectEnumSchema__max_items = Slot(uri=MCP.maxItems, name="mcpUntitledMultiSelectEnumSchema__max_items", curie=MCP.curie('maxItems'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchema__max_items, domain=None, range=Optional[int])

slots.mcpUntitledMultiSelectEnumSchema__min_items = Slot(uri=MCP.minItems, name="mcpUntitledMultiSelectEnumSchema__min_items", curie=MCP.curie('minItems'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchema__min_items, domain=None, range=Optional[int])

slots.mcpUntitledMultiSelectEnumSchema__kind = Slot(uri=MCP.kind, name="mcpUntitledMultiSelectEnumSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchema__kind, domain=None, range=str)

slots.mcpUntitledMultiSelectEnumSchemaItems__enum = Slot(uri=MCP.enum, name="mcpUntitledMultiSelectEnumSchemaItems__enum", curie=MCP.curie('enum'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchemaItems__enum, domain=None, range=Union[str, list[str]])

slots.mcpUntitledMultiSelectEnumSchemaItems__kind = Slot(uri=MCP.kind, name="mcpUntitledMultiSelectEnumSchemaItems__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpUntitledMultiSelectEnumSchemaItems__kind, domain=None, range=str)

slots.mcpUntitledSingleSelectEnumSchema__default = Slot(uri=MCP.default, name="mcpUntitledSingleSelectEnumSchema__default", curie=MCP.curie('default'),
                   model_uri=MCP.mcpUntitledSingleSelectEnumSchema__default, domain=None, range=Optional[str])

slots.mcpUntitledSingleSelectEnumSchema__enum = Slot(uri=MCP.enum, name="mcpUntitledSingleSelectEnumSchema__enum", curie=MCP.curie('enum'),
                   model_uri=MCP.mcpUntitledSingleSelectEnumSchema__enum, domain=None, range=Union[str, list[str]])

slots.mcpUntitledSingleSelectEnumSchema__kind = Slot(uri=MCP.kind, name="mcpUntitledSingleSelectEnumSchema__kind", curie=MCP.curie('kind'),
                   model_uri=MCP.mcpUntitledSingleSelectEnumSchema__kind, domain=None, range=str)

slots.McpBaseMetadata_name = Slot(uri=SCHEMA.name, name="McpBaseMetadata_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpBaseMetadata_name, domain=McpBaseMetadata, range=str)

slots.McpBaseMetadata_title = Slot(uri=SCHEMA.name, name="McpBaseMetadata_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpBaseMetadata_title, domain=McpBaseMetadata, range=Optional[str])

slots.McpBooleanSchema_description = Slot(uri=SCHEMA.description, name="McpBooleanSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpBooleanSchema_description, domain=McpBooleanSchema, range=Optional[str])

slots.McpBooleanSchema_title = Slot(uri=SCHEMA.name, name="McpBooleanSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpBooleanSchema_title, domain=McpBooleanSchema, range=Optional[str])

slots.McpCallToolRequestParams_name = Slot(uri=SCHEMA.name, name="McpCallToolRequestParams_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpCallToolRequestParams_name, domain=McpCallToolRequestParams, range=str)

slots.McpCompleteRequestParamsArgument_name = Slot(uri=SCHEMA.name, name="McpCompleteRequestParamsArgument_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpCompleteRequestParamsArgument_name, domain=McpCompleteRequestParamsArgument, range=str)

slots.McpElicitRequestURLParams_url = Slot(uri=SCHEMA.url, name="McpElicitRequestURLParams_url", curie=SCHEMA.curie('url'),
                   model_uri=MCP.McpElicitRequestURLParams_url, domain=McpElicitRequestURLParams, range=Union[str, URI])

slots.McpGetPromptRequestParams_name = Slot(uri=SCHEMA.name, name="McpGetPromptRequestParams_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpGetPromptRequestParams_name, domain=McpGetPromptRequestParams, range=str)

slots.McpGetPromptResult_description = Slot(uri=SCHEMA.description, name="McpGetPromptResult_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpGetPromptResult_description, domain=McpGetPromptResult, range=Optional[str])

slots.McpImplementation_description = Slot(uri=SCHEMA.description, name="McpImplementation_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpImplementation_description, domain=McpImplementation, range=Optional[str])

slots.McpImplementation_name = Slot(uri=SCHEMA.name, name="McpImplementation_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpImplementation_name, domain=McpImplementation, range=str)

slots.McpImplementation_title = Slot(uri=SCHEMA.name, name="McpImplementation_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpImplementation_title, domain=McpImplementation, range=Optional[str])

slots.McpImplementation_version = Slot(uri=SCHEMA.version, name="McpImplementation_version", curie=SCHEMA.curie('version'),
                   model_uri=MCP.McpImplementation_version, domain=McpImplementation, range=str)

slots.McpLegacyTitledEnumSchema_description = Slot(uri=SCHEMA.description, name="McpLegacyTitledEnumSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpLegacyTitledEnumSchema_description, domain=McpLegacyTitledEnumSchema, range=Optional[str])

slots.McpLegacyTitledEnumSchema_title = Slot(uri=SCHEMA.name, name="McpLegacyTitledEnumSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpLegacyTitledEnumSchema_title, domain=McpLegacyTitledEnumSchema, range=Optional[str])

slots.McpModelHint_name = Slot(uri=SCHEMA.name, name="McpModelHint_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpModelHint_name, domain=McpModelHint, range=Optional[str])

slots.McpNumberSchema_description = Slot(uri=SCHEMA.description, name="McpNumberSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpNumberSchema_description, domain=McpNumberSchema, range=Optional[str])

slots.McpNumberSchema_title = Slot(uri=SCHEMA.name, name="McpNumberSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpNumberSchema_title, domain=McpNumberSchema, range=Optional[str])

slots.McpPrompt_description = Slot(uri=SCHEMA.description, name="McpPrompt_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpPrompt_description, domain=McpPrompt, range=Optional[str])

slots.McpPrompt_name = Slot(uri=SCHEMA.name, name="McpPrompt_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpPrompt_name, domain=McpPrompt, range=str)

slots.McpPrompt_title = Slot(uri=SCHEMA.name, name="McpPrompt_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpPrompt_title, domain=McpPrompt, range=Optional[str])

slots.McpPromptArgument_description = Slot(uri=SCHEMA.description, name="McpPromptArgument_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpPromptArgument_description, domain=McpPromptArgument, range=Optional[str])

slots.McpPromptArgument_name = Slot(uri=SCHEMA.name, name="McpPromptArgument_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpPromptArgument_name, domain=McpPromptArgument, range=str)

slots.McpPromptArgument_title = Slot(uri=SCHEMA.name, name="McpPromptArgument_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpPromptArgument_title, domain=McpPromptArgument, range=Optional[str])

slots.McpPromptReference_name = Slot(uri=SCHEMA.name, name="McpPromptReference_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpPromptReference_name, domain=McpPromptReference, range=str)

slots.McpPromptReference_title = Slot(uri=SCHEMA.name, name="McpPromptReference_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpPromptReference_title, domain=McpPromptReference, range=Optional[str])

slots.McpResource_description = Slot(uri=SCHEMA.description, name="McpResource_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpResource_description, domain=McpResource, range=Optional[str])

slots.McpResource_name = Slot(uri=SCHEMA.name, name="McpResource_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpResource_name, domain=McpResource, range=str)

slots.McpResource_title = Slot(uri=SCHEMA.name, name="McpResource_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpResource_title, domain=McpResource, range=Optional[str])

slots.McpResourceLink_description = Slot(uri=SCHEMA.description, name="McpResourceLink_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpResourceLink_description, domain=McpResourceLink, range=Optional[str])

slots.McpResourceLink_name = Slot(uri=SCHEMA.name, name="McpResourceLink_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpResourceLink_name, domain=McpResourceLink, range=str)

slots.McpResourceLink_title = Slot(uri=SCHEMA.name, name="McpResourceLink_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpResourceLink_title, domain=McpResourceLink, range=Optional[str])

slots.McpResourceTemplate_description = Slot(uri=SCHEMA.description, name="McpResourceTemplate_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpResourceTemplate_description, domain=McpResourceTemplate, range=Optional[str])

slots.McpResourceTemplate_name = Slot(uri=SCHEMA.name, name="McpResourceTemplate_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpResourceTemplate_name, domain=McpResourceTemplate, range=str)

slots.McpResourceTemplate_title = Slot(uri=SCHEMA.name, name="McpResourceTemplate_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpResourceTemplate_title, domain=McpResourceTemplate, range=Optional[str])

slots.McpRoot_name = Slot(uri=SCHEMA.name, name="McpRoot_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpRoot_name, domain=McpRoot, range=Optional[str])

slots.McpStringSchema_description = Slot(uri=SCHEMA.description, name="McpStringSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpStringSchema_description, domain=McpStringSchema, range=Optional[str])

slots.McpStringSchema_title = Slot(uri=SCHEMA.name, name="McpStringSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpStringSchema_title, domain=McpStringSchema, range=Optional[str])

slots.McpTitledMultiSelectEnumSchema_description = Slot(uri=SCHEMA.description, name="McpTitledMultiSelectEnumSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpTitledMultiSelectEnumSchema_description, domain=McpTitledMultiSelectEnumSchema, range=Optional[str])

slots.McpTitledMultiSelectEnumSchema_title = Slot(uri=SCHEMA.name, name="McpTitledMultiSelectEnumSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpTitledMultiSelectEnumSchema_title, domain=McpTitledMultiSelectEnumSchema, range=Optional[str])

slots.McpTitledMultiSelectEnumSchemaItemsAnyOf_title = Slot(uri=SCHEMA.name, name="McpTitledMultiSelectEnumSchemaItemsAnyOf_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpTitledMultiSelectEnumSchemaItemsAnyOf_title, domain=McpTitledMultiSelectEnumSchemaItemsAnyOf, range=str)

slots.McpTitledSingleSelectEnumSchema_description = Slot(uri=SCHEMA.description, name="McpTitledSingleSelectEnumSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpTitledSingleSelectEnumSchema_description, domain=McpTitledSingleSelectEnumSchema, range=Optional[str])

slots.McpTitledSingleSelectEnumSchema_title = Slot(uri=SCHEMA.name, name="McpTitledSingleSelectEnumSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpTitledSingleSelectEnumSchema_title, domain=McpTitledSingleSelectEnumSchema, range=Optional[str])

slots.McpTitledSingleSelectEnumSchemaOneOf_title = Slot(uri=SCHEMA.name, name="McpTitledSingleSelectEnumSchemaOneOf_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpTitledSingleSelectEnumSchemaOneOf_title, domain=McpTitledSingleSelectEnumSchemaOneOf, range=str)

slots.McpTool_description = Slot(uri=SCHEMA.description, name="McpTool_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpTool_description, domain=McpTool, range=Optional[str])

slots.McpTool_name = Slot(uri=SCHEMA.name, name="McpTool_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpTool_name, domain=McpTool, range=str)

slots.McpTool_title = Slot(uri=SCHEMA.name, name="McpTool_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpTool_title, domain=McpTool, range=Optional[str])

slots.McpToolAnnotations_title = Slot(uri=SCHEMA.name, name="McpToolAnnotations_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpToolAnnotations_title, domain=McpToolAnnotations, range=Optional[str])

slots.McpToolUseContent_name = Slot(uri=SCHEMA.name, name="McpToolUseContent_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpToolUseContent_name, domain=McpToolUseContent, range=str)

slots.McpUntitledMultiSelectEnumSchema_description = Slot(uri=SCHEMA.description, name="McpUntitledMultiSelectEnumSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpUntitledMultiSelectEnumSchema_description, domain=McpUntitledMultiSelectEnumSchema, range=Optional[str])

slots.McpUntitledMultiSelectEnumSchema_title = Slot(uri=SCHEMA.name, name="McpUntitledMultiSelectEnumSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpUntitledMultiSelectEnumSchema_title, domain=McpUntitledMultiSelectEnumSchema, range=Optional[str])

slots.McpUntitledSingleSelectEnumSchema_description = Slot(uri=SCHEMA.description, name="McpUntitledSingleSelectEnumSchema_description", curie=SCHEMA.curie('description'),
                   model_uri=MCP.McpUntitledSingleSelectEnumSchema_description, domain=McpUntitledSingleSelectEnumSchema, range=Optional[str])

slots.McpUntitledSingleSelectEnumSchema_title = Slot(uri=SCHEMA.name, name="McpUntitledSingleSelectEnumSchema_title", curie=SCHEMA.curie('name'),
                   model_uri=MCP.McpUntitledSingleSelectEnumSchema_title, domain=McpUntitledSingleSelectEnumSchema, range=Optional[str])
