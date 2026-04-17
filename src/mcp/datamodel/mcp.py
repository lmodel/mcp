# Auto generated from mcp.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-18T00:39:45
# Schema: mcp
#
# id: https://w3id.org/lmodel/mcp
# description: Model Context Protocol LinkML Schema
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

metamodel_version = "1.7.0"
version = "draft"

# Namespaces
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
JSONRPC = CurieNamespace('jsonrpc', 'https://www.jsonrpc.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MCP = CurieNamespace('mcp', 'https://w3id.org/lmodel/mcp/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MCP


# Types
class Cursor(str):
    """ An opaque token used to represent a cursor for pagination. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Cursor"
    type_model_uri = MCP.Cursor


class ProgressToken(str):
    """ A progress token, used to associate progress notifications with the original request. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ProgressToken"
    type_model_uri = MCP.ProgressToken


class RequestId(str):
    """ A uniquely identifying ID for a request in JSON-RPC. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "RequestId"
    type_model_uri = MCP.RequestId


class JsonValue(object):
    """ Any JSON-serializable value. """
    type_class_uri = XSD["anyType"]
    type_class_curie = "xsd:anyType"
    type_name = "JsonValue"
    type_model_uri = MCP.JsonValue


# Class references



@dataclass(repr=False)
class HasMeta(YAMLRoot):
    """
    Mixin for types that carry a _meta field.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["HasMeta"]
    class_class_curie: ClassVar[str] = "mcp:HasMeta"
    class_name: ClassVar[str] = "HasMeta"
    class_model_uri: ClassVar[URIRef] = MCP.HasMeta

    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasAnnotations(YAMLRoot):
    """
    Mixin for types that carry annotations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["HasAnnotations"]
    class_class_curie: ClassVar[str] = "mcp:HasAnnotations"
    class_name: ClassVar[str] = "HasAnnotations"
    class_model_uri: ClassVar[URIRef] = MCP.HasAnnotations

    annotations: Optional[Union[dict, "Annotations"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasIcons(YAMLRoot):
    """
    Mixin for types that carry icons.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["HasIcons"]
    class_class_curie: ClassVar[str] = "mcp:HasIcons"
    class_name: ClassVar[str] = "HasIcons"
    class_model_uri: ClassVar[URIRef] = MCP.HasIcons

    icons: Optional[Union[Union[dict, "Icon"], list[Union[dict, "Icon"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasName(YAMLRoot):
    """
    Mixin for types that carry name and title.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["HasName"]
    class_class_curie: ClassVar[str] = "mcp:HasName"
    class_name: ClassVar[str] = "HasName"
    class_model_uri: ClassVar[URIRef] = MCP.HasName

    name: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Annotations(YAMLRoot):
    """
    Optional annotations for the client. The client can use annotations to inform how objects are used or displayed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Annotations"]
    class_class_curie: ClassVar[str] = "mcp:Annotations"
    class_name: ClassVar[str] = "Annotations"
    class_model_uri: ClassVar[URIRef] = MCP.Annotations

    audience: Optional[Union[Union[str, "Role"], list[Union[str, "Role"]]]] = empty_list()
    lastModified: Optional[str] = None
    priority: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.audience, list):
            self.audience = [self.audience] if self.audience is not None else []
        self.audience = [v if isinstance(v, Role) else Role(v) for v in self.audience]

        if self.lastModified is not None and not isinstance(self.lastModified, str):
            self.lastModified = str(self.lastModified)

        if self.priority is not None and not isinstance(self.priority, float):
            self.priority = float(self.priority)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Error(YAMLRoot):
    """
    A JSON-RPC error object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Error"]
    class_class_curie: ClassVar[str] = "mcp:Error"
    class_name: ClassVar[str] = "Error"
    class_model_uri: ClassVar[URIRef] = MCP.Error

    code: int = None
    message: str = None
    data: Optional[Union[dict, "ErrorData"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, int):
            self.code = int(self.code)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        if self.data is not None and not isinstance(self.data, ErrorData):
            self.data = ErrorData(**as_dict(self.data))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternalError(Error):
    """
    A JSON-RPC error indicating that an internal error occurred on the receiver (-32603).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InternalError"]
    class_class_curie: ClassVar[str] = "mcp:InternalError"
    class_name: ClassVar[str] = "InternalError"
    class_model_uri: ClassVar[URIRef] = MCP.InternalError

    code: int = None
    message: str = None

@dataclass(repr=False)
class InvalidParamsError(Error):
    """
    A JSON-RPC error indicating that the method parameters are invalid or malformed (-32602).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InvalidParamsError"]
    class_class_curie: ClassVar[str] = "mcp:InvalidParamsError"
    class_name: ClassVar[str] = "InvalidParamsError"
    class_model_uri: ClassVar[URIRef] = MCP.InvalidParamsError

    code: int = None
    message: str = None

@dataclass(repr=False)
class InvalidRequestError(Error):
    """
    A JSON-RPC error indicating that the request is not a valid request object (-32600).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InvalidRequestError"]
    class_class_curie: ClassVar[str] = "mcp:InvalidRequestError"
    class_name: ClassVar[str] = "InvalidRequestError"
    class_model_uri: ClassVar[URIRef] = MCP.InvalidRequestError

    code: int = None
    message: str = None

@dataclass(repr=False)
class MethodNotFoundError(Error):
    """
    A JSON-RPC error indicating that the requested method does not exist or is not available (-32601).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["MethodNotFoundError"]
    class_class_curie: ClassVar[str] = "mcp:MethodNotFoundError"
    class_name: ClassVar[str] = "MethodNotFoundError"
    class_model_uri: ClassVar[URIRef] = MCP.MethodNotFoundError

    code: int = None
    message: str = None

@dataclass(repr=False)
class ParseError(Error):
    """
    A JSON-RPC error indicating that invalid JSON was received by the server (-32700).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ParseError"]
    class_class_curie: ClassVar[str] = "mcp:ParseError"
    class_name: ClassVar[str] = "ParseError"
    class_model_uri: ClassVar[URIRef] = MCP.ParseError

    code: int = None
    message: str = None

@dataclass(repr=False)
class Icon(YAMLRoot):
    """
    An optionally-sized icon that can be displayed in a user interface.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Icon"]
    class_class_curie: ClassVar[str] = "mcp:Icon"
    class_name: ClassVar[str] = "Icon"
    class_model_uri: ClassVar[URIRef] = MCP.Icon

    src: Union[str, URI] = None
    mimeType: Optional[str] = None
    sizes: Optional[Union[str, list[str]]] = empty_list()
    theme: Optional[Union[str, "IconThemeEnum"]] = None

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

        if self.theme is not None and not isinstance(self.theme, IconThemeEnum):
            self.theme = IconThemeEnum(self.theme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Implementation(YAMLRoot):
    """
    Describes the MCP implementation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Implementation"]
    class_class_curie: ClassVar[str] = "mcp:Implementation"
    class_name: ClassVar[str] = "Implementation"
    class_model_uri: ClassVar[URIRef] = MCP.Implementation

    version: str = None
    name: str = None
    description: Optional[str] = None
    websiteUrl: Optional[Union[str, URI]] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.websiteUrl is not None and not isinstance(self.websiteUrl, URI):
            self.websiteUrl = URI(self.websiteUrl)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextContent(YAMLRoot):
    """
    Text provided to or from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TextContent"]
    class_class_curie: ClassVar[str] = "mcp:TextContent"
    class_name: ClassVar[str] = "TextContent"
    class_model_uri: ClassVar[URIRef] = MCP.TextContent

    text: str = None
    type: str = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageContent(YAMLRoot):
    """
    An image provided to or from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ImageContent"]
    class_class_curie: ClassVar[str] = "mcp:ImageContent"
    class_name: ClassVar[str] = "ImageContent"
    class_model_uri: ClassVar[URIRef] = MCP.ImageContent

    data: str = None
    mimeType: str = None
    type: str = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, str):
            self.data = str(self.data)

        if self._is_empty(self.mimeType):
            self.MissingRequiredField("mimeType")
        if not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AudioContent(YAMLRoot):
    """
    Audio provided to or from an LLM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["AudioContent"]
    class_class_curie: ClassVar[str] = "mcp:AudioContent"
    class_name: ClassVar[str] = "AudioContent"
    class_model_uri: ClassVar[URIRef] = MCP.AudioContent

    data: str = None
    mimeType: str = None
    type: str = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, str):
            self.data = str(self.data)

        if self._is_empty(self.mimeType):
            self.MissingRequiredField("mimeType")
        if not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContentBlock(YAMLRoot):
    """
    Structured text content block.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ContentBlock"]
    class_class_curie: ClassVar[str] = "mcp:ContentBlock"
    class_name: ClassVar[str] = "ContentBlock"
    class_model_uri: ClassVar[URIRef] = MCP.ContentBlock

    type: Optional[str] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmbeddedResource(YAMLRoot):
    """
    The contents of a resource, embedded into a prompt or tool call result.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["EmbeddedResource"]
    class_class_curie: ClassVar[str] = "mcp:EmbeddedResource"
    class_name: ClassVar[str] = "EmbeddedResource"
    class_model_uri: ClassVar[URIRef] = MCP.EmbeddedResource

    type: str = None
    resource: Union[dict, "ResourceContents"] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.resource):
            self.MissingRequiredField("resource")
        if not isinstance(self.resource, ResourceContents):
            self.resource = ResourceContents(**as_dict(self.resource))

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceLink(YAMLRoot):
    """
    A resource that the server is capable of reading, included in a prompt or tool call result.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceLink"]
    class_class_curie: ClassVar[str] = "mcp:ResourceLink"
    class_name: ClassVar[str] = "ResourceLink"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceLink

    uri: Union[str, URI] = None
    type: str = None
    name: str = None
    mimeType: Optional[str] = None
    description: Optional[str] = None
    size: Optional[int] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolUseContent(YAMLRoot):
    """
    A request from the assistant to call a tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolUseContent"]
    class_class_curie: ClassVar[str] = "mcp:ToolUseContent"
    class_name: ClassVar[str] = "ToolUseContent"
    class_model_uri: ClassVar[URIRef] = MCP.ToolUseContent

    id: str = None
    type: str = None
    name: str = None
    input: Union[dict, "ToolInput"] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, ToolInput):
            self.input = ToolInput(**as_dict(self.input))

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolResultContent(YAMLRoot):
    """
    The result of a tool use, provided by the user back to the assistant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolResultContent"]
    class_class_curie: ClassVar[str] = "mcp:ToolResultContent"
    class_name: ClassVar[str] = "ToolResultContent"
    class_model_uri: ClassVar[URIRef] = MCP.ToolResultContent

    content: Union[Union[dict, ContentBlock], list[Union[dict, ContentBlock]]] = None
    type: str = None
    toolUseId: str = None
    isError: Optional[Union[bool, Bool]] = None
    structuredContent: Optional[Union[dict, "StructuredContentData"]] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, ContentBlock) else ContentBlock(**as_dict(v)) for v in self.content]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.toolUseId):
            self.MissingRequiredField("toolUseId")
        if not isinstance(self.toolUseId, str):
            self.toolUseId = str(self.toolUseId)

        if self.isError is not None and not isinstance(self.isError, Bool):
            self.isError = Bool(self.isError)

        if self.structuredContent is not None and not isinstance(self.structuredContent, StructuredContentData):
            self.structuredContent = StructuredContentData(**as_dict(self.structuredContent))

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceContents(YAMLRoot):
    """
    Generic resource contents.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceContents"]
    class_class_curie: ClassVar[str] = "mcp:ResourceContents"
    class_name: ClassVar[str] = "ResourceContents"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceContents

    uri: Union[str, URI] = None
    mimeType: Optional[str] = None
    text: Optional[str] = None
    blob: Optional[str] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        if self.blob is not None and not isinstance(self.blob, str):
            self.blob = str(self.blob)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextResourceContents(YAMLRoot):
    """
    Text resource contents.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TextResourceContents"]
    class_class_curie: ClassVar[str] = "mcp:TextResourceContents"
    class_name: ClassVar[str] = "TextResourceContents"
    class_model_uri: ClassVar[URIRef] = MCP.TextResourceContents

    uri: Union[str, URI] = None
    text: str = None
    mimeType: Optional[str] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BlobResourceContents(YAMLRoot):
    """
    Blob resource contents.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["BlobResourceContents"]
    class_class_curie: ClassVar[str] = "mcp:BlobResourceContents"
    class_name: ClassVar[str] = "BlobResourceContents"
    class_model_uri: ClassVar[URIRef] = MCP.BlobResourceContents

    uri: Union[str, URI] = None
    blob: str = None
    mimeType: Optional[str] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._is_empty(self.blob):
            self.MissingRequiredField("blob")
        if not isinstance(self.blob, str):
            self.blob = str(self.blob)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(YAMLRoot):
    """
    A known resource that the server is capable of reading.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Resource"]
    class_class_curie: ClassVar[str] = "mcp:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = MCP.Resource

    uri: Union[str, URI] = None
    name: str = None
    mimeType: Optional[str] = None
    description: Optional[str] = None
    size: Optional[int] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceTemplate(YAMLRoot):
    """
    A template description for resources available on the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceTemplate"]
    class_class_curie: ClassVar[str] = "mcp:ResourceTemplate"
    class_name: ClassVar[str] = "ResourceTemplate"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceTemplate

    uriTemplate: str = None
    name: str = None
    mimeType: Optional[str] = None
    description: Optional[str] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    annotations: Optional[Union[dict, Annotations]] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uriTemplate):
            self.MissingRequiredField("uriTemplate")
        if not isinstance(self.uriTemplate, str):
            self.uriTemplate = str(self.uriTemplate)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.annotations is not None and not isinstance(self.annotations, Annotations):
            self.annotations = Annotations(**as_dict(self.annotations))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Root(YAMLRoot):
    """
    Represents a root directory or file that the server can operate on.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Root"]
    class_class_curie: ClassVar[str] = "mcp:Root"
    class_name: ClassVar[str] = "Root"
    class_model_uri: ClassVar[URIRef] = MCP.Root

    uri: Union[str, URI] = None
    name: Optional[str] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PromptArgument(YAMLRoot):
    """
    Describes an argument that a prompt can accept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PromptArgument"]
    class_class_curie: ClassVar[str] = "mcp:PromptArgument"
    class_name: ClassVar[str] = "PromptArgument"
    class_model_uri: ClassVar[URIRef] = MCP.PromptArgument

    name: str = None
    description: Optional[str] = None
    required: Optional[Union[bool, Bool]] = None
    required_field: Optional[Union[bool, Bool]] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.required is not None and not isinstance(self.required, Bool):
            self.required = Bool(self.required)

        if self.required_field is not None and not isinstance(self.required_field, Bool):
            self.required_field = Bool(self.required_field)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prompt(YAMLRoot):
    """
    A prompt or prompt template that the server offers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Prompt"]
    class_class_curie: ClassVar[str] = "mcp:Prompt"
    class_name: ClassVar[str] = "Prompt"
    class_model_uri: ClassVar[URIRef] = MCP.Prompt

    name: str = None
    arguments: Optional[Union[Union[dict, PromptArgument], list[Union[dict, PromptArgument]]]] = empty_list()
    description: Optional[str] = None
    _meta: Optional[Union[dict, "MetaObject"]] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="arguments", slot_type=PromptArgument, key_name="name", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PromptMessage(YAMLRoot):
    """
    Describes a message returned as part of a prompt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PromptMessage"]
    class_class_curie: ClassVar[str] = "mcp:PromptMessage"
    class_name: ClassVar[str] = "PromptMessage"
    class_model_uri: ClassVar[URIRef] = MCP.PromptMessage

    content: Union[dict, ContentBlock] = None
    role: Union[str, "Role"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, ContentBlock):
            self.content = ContentBlock(**as_dict(self.content))

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, Role):
            self.role = Role(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PromptReference(YAMLRoot):
    """
    Identifies a prompt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PromptReference"]
    class_class_curie: ClassVar[str] = "mcp:PromptReference"
    class_name: ClassVar[str] = "PromptReference"
    class_model_uri: ClassVar[URIRef] = MCP.PromptReference

    type: str = None
    name: str = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceTemplateReference(YAMLRoot):
    """
    A reference to a resource or resource template definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceTemplateReference"]
    class_class_curie: ClassVar[str] = "mcp:ResourceTemplateReference"
    class_name: ClassVar[str] = "ResourceTemplateReference"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceTemplateReference

    type: str = None
    uri: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolAnnotations(YAMLRoot):
    """
    Additional properties describing a Tool to clients. All properties are hints, not guarantees.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolAnnotations"]
    class_class_curie: ClassVar[str] = "mcp:ToolAnnotations"
    class_name: ClassVar[str] = "ToolAnnotations"
    class_model_uri: ClassVar[URIRef] = MCP.ToolAnnotations

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
class ToolChoice(YAMLRoot):
    """
    Controls tool selection behavior for sampling requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolChoice"]
    class_class_curie: ClassVar[str] = "mcp:ToolChoice"
    class_name: ClassVar[str] = "ToolChoice"
    class_model_uri: ClassVar[URIRef] = MCP.ToolChoice

    mode: Optional[Union[str, "ToolChoiceModeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mode is not None and not isinstance(self.mode, ToolChoiceModeEnum):
            self.mode = ToolChoiceModeEnum(self.mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolExecution(YAMLRoot):
    """
    Execution-related properties for a tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolExecution"]
    class_class_curie: ClassVar[str] = "mcp:ToolExecution"
    class_name: ClassVar[str] = "ToolExecution"
    class_model_uri: ClassVar[URIRef] = MCP.ToolExecution

    taskSupport: Optional[Union[str, "TaskSupportEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.taskSupport is not None and not isinstance(self.taskSupport, TaskSupportEnum):
            self.taskSupport = TaskSupportEnum(self.taskSupport)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetaObject(YAMLRoot):
    """
    Metadata object attached to protocol objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["MetaObject"]
    class_class_curie: ClassVar[str] = "mcp:MetaObject"
    class_name: ClassVar[str] = "MetaObject"
    class_model_uri: ClassVar[URIRef] = MCP.MetaObject

    progressToken: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.progressToken is not None and not isinstance(self.progressToken, str):
            self.progressToken = str(self.progressToken)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ArgumentMap(YAMLRoot):
    """
    Argument object used in prompt and tool calls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ArgumentMap"]
    class_class_curie: ClassVar[str] = "mcp:ArgumentMap"
    class_name: ClassVar[str] = "ArgumentMap"
    class_model_uri: ClassVar[URIRef] = MCP.ArgumentMap

    city: Optional[str] = None
    location: Optional[str] = None
    language: Optional[str] = None
    framework: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.framework is not None and not isinstance(self.framework, str):
            self.framework = str(self.framework)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompletionArgument(YAMLRoot):
    """
    Argument descriptor for completion requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompletionArgument"]
    class_class_curie: ClassVar[str] = "mcp:CompletionArgument"
    class_name: ClassVar[str] = "CompletionArgument"
    class_model_uri: ClassVar[URIRef] = MCP.CompletionArgument

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
class CompletionContext(YAMLRoot):
    """
    Additional context for completion requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompletionContext"]
    class_class_curie: ClassVar[str] = "mcp:CompletionContext"
    class_name: ClassVar[str] = "CompletionContext"
    class_model_uri: ClassVar[URIRef] = MCP.CompletionContext

    arguments: Optional[Union[dict, ArgumentMap]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.arguments is not None and not isinstance(self.arguments, ArgumentMap):
            self.arguments = ArgumentMap(**as_dict(self.arguments))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompletionData(YAMLRoot):
    """
    Completion result payload.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompletionData"]
    class_class_curie: ClassVar[str] = "mcp:CompletionData"
    class_name: ClassVar[str] = "CompletionData"
    class_model_uri: ClassVar[URIRef] = MCP.CompletionData

    values: Union[str, list[str]] = None
    total: Optional[float] = None
    hasMore: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.total is not None and not isinstance(self.total, float):
            self.total = float(self.total)

        if self.hasMore is not None and not isinstance(self.hasMore, Bool):
            self.hasMore = Bool(self.hasMore)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnumOption(YAMLRoot):
    """
    Single enumerated option with a machine value and display title.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["EnumOption"]
    class_class_curie: ClassVar[str] = "mcp:EnumOption"
    class_name: ClassVar[str] = "EnumOption"
    class_model_uri: ClassVar[URIRef] = MCP.EnumOption

    const: str = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.const):
            self.MissingRequiredField("const")
        if not isinstance(self.const, str):
            self.const = str(self.const)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SchemaItems(YAMLRoot):
    """
    JSON Schema items expression used by enum multi-select schemas.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SchemaItems"]
    class_class_curie: ClassVar[str] = "mcp:SchemaItems"
    class_name: ClassVar[str] = "SchemaItems"
    class_model_uri: ClassVar[URIRef] = MCP.SchemaItems

    type: Optional[str] = None
    enum: Optional[Union[str, list[str]]] = empty_list()
    anyOf: Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        self._normalize_inlined_as_list(slot_name="anyOf", slot_type=EnumOption, key_name="const", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JsonSchema(YAMLRoot):
    """
    Restricted JSON Schema object used in MCP payloads.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JsonSchema"]
    class_class_curie: ClassVar[str] = "mcp:JsonSchema"
    class_name: ClassVar[str] = "JsonSchema"
    class_model_uri: ClassVar[URIRef] = MCP.JsonSchema

    schemaUri: Optional[str] = None
    type: Optional[str] = None
    properties: Optional[Union[dict, "SchemaProperties"]] = None
    required_list: Optional[Union[str, list[str]]] = empty_list()
    additionalProperties: Optional[Union[bool, Bool]] = None
    minimum: Optional[int] = None
    maximum: Optional[int] = None
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
    format: Optional[Union[str, "StringFormatEnum"]] = None
    description: Optional[str] = None
    title: Optional[str] = None
    oneOf: Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]] = empty_list()
    anyOf: Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]] = empty_list()
    items: Optional[Union[dict, SchemaItems]] = None
    enum: Optional[Union[str, list[str]]] = empty_list()
    const: Optional[str] = None
    default: Optional[object] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.schemaUri is not None and not isinstance(self.schemaUri, str):
            self.schemaUri = str(self.schemaUri)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.properties is not None and not isinstance(self.properties, SchemaProperties):
            self.properties = SchemaProperties(**as_dict(self.properties))

        if not isinstance(self.required_list, list):
            self.required_list = [self.required_list] if self.required_list is not None else []
        self.required_list = [v if isinstance(v, str) else str(v) for v in self.required_list]

        if self.additionalProperties is not None and not isinstance(self.additionalProperties, Bool):
            self.additionalProperties = Bool(self.additionalProperties)

        if self.minimum is not None and not isinstance(self.minimum, int):
            self.minimum = int(self.minimum)

        if self.maximum is not None and not isinstance(self.maximum, int):
            self.maximum = int(self.maximum)

        if self.minLength is not None and not isinstance(self.minLength, int):
            self.minLength = int(self.minLength)

        if self.maxLength is not None and not isinstance(self.maxLength, int):
            self.maxLength = int(self.maxLength)

        if self.format is not None and not isinstance(self.format, StringFormatEnum):
            self.format = StringFormatEnum(self.format)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="oneOf", slot_type=EnumOption, key_name="const", keyed=False)

        self._normalize_inlined_as_list(slot_name="anyOf", slot_type=EnumOption, key_name="const", keyed=False)

        if self.items is not None and not isinstance(self.items, SchemaItems):
            self.items = SchemaItems(**as_dict(self.items))

        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        if self.const is not None and not isinstance(self.const, str):
            self.const = str(self.const)

        if self.default is not None and not isinstance(self.default, object):
            self.default = object(self.default)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SchemaProperties(YAMLRoot):
    """
    Named JSON Schema property map used by vendor fixtures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SchemaProperties"]
    class_class_curie: ClassVar[str] = "mcp:SchemaProperties"
    class_name: ClassVar[str] = "SchemaProperties"
    class_model_uri: ClassVar[URIRef] = MCP.SchemaProperties

    name: Optional[Union[dict, JsonSchema]] = None
    email: Optional[Union[dict, JsonSchema]] = None
    age: Optional[Union[dict, JsonSchema]] = None
    city: Optional[Union[dict, JsonSchema]] = None
    location: Optional[Union[dict, JsonSchema]] = None
    a: Optional[Union[dict, JsonSchema]] = None
    b: Optional[Union[dict, JsonSchema]] = None
    temperature: Optional[Union[dict, JsonSchema]] = None
    conditions: Optional[Union[dict, JsonSchema]] = None
    humidity: Optional[Union[dict, JsonSchema]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, JsonSchema):
            self.name = JsonSchema(**as_dict(self.name))

        if self.email is not None and not isinstance(self.email, JsonSchema):
            self.email = JsonSchema(**as_dict(self.email))

        if self.age is not None and not isinstance(self.age, JsonSchema):
            self.age = JsonSchema(**as_dict(self.age))

        if self.city is not None and not isinstance(self.city, JsonSchema):
            self.city = JsonSchema(**as_dict(self.city))

        if self.location is not None and not isinstance(self.location, JsonSchema):
            self.location = JsonSchema(**as_dict(self.location))

        if self.a is not None and not isinstance(self.a, JsonSchema):
            self.a = JsonSchema(**as_dict(self.a))

        if self.b is not None and not isinstance(self.b, JsonSchema):
            self.b = JsonSchema(**as_dict(self.b))

        if self.temperature is not None and not isinstance(self.temperature, JsonSchema):
            self.temperature = JsonSchema(**as_dict(self.temperature))

        if self.conditions is not None and not isinstance(self.conditions, JsonSchema):
            self.conditions = JsonSchema(**as_dict(self.conditions))

        if self.humidity is not None and not isinstance(self.humidity, JsonSchema):
            self.humidity = JsonSchema(**as_dict(self.humidity))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolInput(YAMLRoot):
    """
    Tool input payload.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolInput"]
    class_class_curie: ClassVar[str] = "mcp:ToolInput"
    class_name: ClassVar[str] = "ToolInput"
    class_model_uri: ClassVar[URIRef] = MCP.ToolInput

    city: Optional[str] = None
    location: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StructuredContentData(YAMLRoot):
    """
    Structured content object returned by tools.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["StructuredContentData"]
    class_class_curie: ClassVar[str] = "mcp:StructuredContentData"
    class_name: ClassVar[str] = "StructuredContentData"
    class_model_uri: ClassVar[URIRef] = MCP.StructuredContentData

    temperature: Optional[float] = None
    conditions: Optional[str] = None
    humidity: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.conditions is not None and not isinstance(self.conditions, str):
            self.conditions = str(self.conditions)

        if self.humidity is not None and not isinstance(self.humidity, float):
            self.humidity = float(self.humidity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogDetails(YAMLRoot):
    """
    Structured details attached to log data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["LogDetails"]
    class_class_curie: ClassVar[str] = "mcp:LogDetails"
    class_name: ClassVar[str] = "LogDetails"
    class_model_uri: ClassVar[URIRef] = MCP.LogDetails

    host: Optional[str] = None
    port: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.host is not None and not isinstance(self.host, str):
            self.host = str(self.host)

        if self.port is not None and not isinstance(self.port, int):
            self.port = int(self.port)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogData(YAMLRoot):
    """
    Structured log data payload.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["LogData"]
    class_class_curie: ClassVar[str] = "mcp:LogData"
    class_name: ClassVar[str] = "LogData"
    class_model_uri: ClassVar[URIRef] = MCP.LogData

    error: Optional[str] = None
    details: Optional[Union[dict, LogDetails]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.error is not None and not isinstance(self.error, str):
            self.error = str(self.error)

        if self.details is not None and not isinstance(self.details, LogDetails):
            self.details = LogDetails(**as_dict(self.details))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ErrorData(YAMLRoot):
    """
    Structured JSON-RPC error data payload.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ErrorData"]
    class_class_curie: ClassVar[str] = "mcp:ErrorData"
    class_name: ClassVar[str] = "ErrorData"
    class_model_uri: ClassVar[URIRef] = MCP.ErrorData

    reason: Optional[str] = None
    elicitations: Optional[Union[Union[dict, "URLElicitation"], list[Union[dict, "URLElicitation"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.reason is not None and not isinstance(self.reason, str):
            self.reason = str(self.reason)

        if not isinstance(self.elicitations, list):
            self.elicitations = [self.elicitations] if self.elicitations is not None else []
        self.elicitations = [v if isinstance(v, URLElicitation) else URLElicitation(**as_dict(v)) for v in self.elicitations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitationContent(YAMLRoot):
    """
    Form values returned by an elicitation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitationContent"]
    class_class_curie: ClassVar[str] = "mcp:ElicitationContent"
    class_name: ClassVar[str] = "ElicitationContent"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitationContent

    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class URLElicitation(YAMLRoot):
    """
    URL-based elicitation request payload carried in error data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["URLElicitation"]
    class_class_curie: ClassVar[str] = "mcp:URLElicitation"
    class_name: ClassVar[str] = "URLElicitation"
    class_model_uri: ClassVar[URIRef] = MCP.URLElicitation

    mode: Optional[str] = None
    elicitationId: Optional[str] = None
    message: Optional[str] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        if self.elicitationId is not None and not isinstance(self.elicitationId, str):
            self.elicitationId = str(self.elicitationId)

        if self.message is not None and not isinstance(self.message, str):
            self.message = str(self.message)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


class ElicitationCapability(YAMLRoot):
    """
    Client elicitation capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitationCapability"]
    class_class_curie: ClassVar[str] = "mcp:ElicitationCapability"
    class_name: ClassVar[str] = "ElicitationCapability"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitationCapability


class SamplingCapability(YAMLRoot):
    """
    Client sampling capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SamplingCapability"]
    class_class_curie: ClassVar[str] = "mcp:SamplingCapability"
    class_name: ClassVar[str] = "SamplingCapability"
    class_model_uri: ClassVar[URIRef] = MCP.SamplingCapability


@dataclass(repr=False)
class RootsCapability(YAMLRoot):
    """
    Client roots capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["RootsCapability"]
    class_class_curie: ClassVar[str] = "mcp:RootsCapability"
    class_name: ClassVar[str] = "RootsCapability"
    class_model_uri: ClassVar[URIRef] = MCP.RootsCapability

    listChanged: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PromptsCapability(YAMLRoot):
    """
    Server prompts capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PromptsCapability"]
    class_class_curie: ClassVar[str] = "mcp:PromptsCapability"
    class_name: ClassVar[str] = "PromptsCapability"
    class_model_uri: ClassVar[URIRef] = MCP.PromptsCapability

    listChanged: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourcesCapability(YAMLRoot):
    """
    Server resources capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourcesCapability"]
    class_class_curie: ClassVar[str] = "mcp:ResourcesCapability"
    class_name: ClassVar[str] = "ResourcesCapability"
    class_model_uri: ClassVar[URIRef] = MCP.ResourcesCapability

    listChanged: Optional[Union[bool, Bool]] = None
    subscribe: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        if self.subscribe is not None and not isinstance(self.subscribe, Bool):
            self.subscribe = Bool(self.subscribe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolsCapability(YAMLRoot):
    """
    Server tools capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolsCapability"]
    class_class_curie: ClassVar[str] = "mcp:ToolsCapability"
    class_name: ClassVar[str] = "ToolsCapability"
    class_model_uri: ClassVar[URIRef] = MCP.ToolsCapability

    listChanged: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listChanged is not None and not isinstance(self.listChanged, Bool):
            self.listChanged = Bool(self.listChanged)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskRequestCapabilities(YAMLRoot):
    """
    Task request capability map.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TaskRequestCapabilities"]
    class_class_curie: ClassVar[str] = "mcp:TaskRequestCapabilities"
    class_name: ClassVar[str] = "TaskRequestCapabilities"
    class_model_uri: ClassVar[URIRef] = MCP.TaskRequestCapabilities

    elicitation: Optional[Union[dict, ElicitationCapability]] = None
    sampling: Optional[Union[dict, SamplingCapability]] = None
    tools: Optional[Union[Union[dict, ToolsCapability], list[Union[dict, ToolsCapability]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elicitation is not None and not isinstance(self.elicitation, ElicitationCapability):
            self.elicitation = ElicitationCapability()

        if self.sampling is not None and not isinstance(self.sampling, SamplingCapability):
            self.sampling = SamplingCapability()

        if not isinstance(self.tools, list):
            self.tools = [self.tools] if self.tools is not None else []
        self.tools = [v if isinstance(v, ToolsCapability) else ToolsCapability(**as_dict(v)) for v in self.tools]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TasksCapability(YAMLRoot):
    """
    Task capability object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TasksCapability"]
    class_class_curie: ClassVar[str] = "mcp:TasksCapability"
    class_name: ClassVar[str] = "TasksCapability"
    class_model_uri: ClassVar[URIRef] = MCP.TasksCapability

    requests: Optional[Union[dict, TaskRequestCapabilities]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.requests is not None and not isinstance(self.requests, TaskRequestCapabilities):
            self.requests = TaskRequestCapabilities(**as_dict(self.requests))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtensionsCapability(YAMLRoot):
    """
    Server/client extension capability object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ExtensionsCapability"]
    class_class_curie: ClassVar[str] = "mcp:ExtensionsCapability"
    class_name: ClassVar[str] = "ExtensionsCapability"
    class_model_uri: ClassVar[URIRef] = MCP.ExtensionsCapability

    apps_extension: Optional[Union[dict, "ExtensionAppCapability"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.apps_extension is not None and not isinstance(self.apps_extension, ExtensionAppCapability):
            self.apps_extension = ExtensionAppCapability(**as_dict(self.apps_extension))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtensionAppCapability(YAMLRoot):
    """
    Extension payload for app mime type declarations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ExtensionAppCapability"]
    class_class_curie: ClassVar[str] = "mcp:ExtensionAppCapability"
    class_name: ClassVar[str] = "ExtensionAppCapability"
    class_model_uri: ClassVar[URIRef] = MCP.ExtensionAppCapability

    mimeTypes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.mimeTypes, list):
            self.mimeTypes = [self.mimeTypes] if self.mimeTypes is not None else []
        self.mimeTypes = [v if isinstance(v, str) else str(v) for v in self.mimeTypes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tool(YAMLRoot):
    """
    Definition for a tool the client can call.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Tool"]
    class_class_curie: ClassVar[str] = "mcp:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = MCP.Tool

    inputSchema: Union[dict, JsonSchema] = None
    name: str = None
    annotations: Optional[Union[dict, ToolAnnotations]] = None
    execution: Optional[Union[dict, ToolExecution]] = None
    description: Optional[str] = None
    outputSchema: Optional[Union[dict, JsonSchema]] = None
    _meta: Optional[Union[dict, MetaObject]] = None
    title: Optional[str] = None
    icons: Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.inputSchema):
            self.MissingRequiredField("inputSchema")
        if not isinstance(self.inputSchema, JsonSchema):
            self.inputSchema = JsonSchema(**as_dict(self.inputSchema))

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.annotations is not None and not isinstance(self.annotations, ToolAnnotations):
            self.annotations = ToolAnnotations(**as_dict(self.annotations))

        if self.execution is not None and not isinstance(self.execution, ToolExecution):
            self.execution = ToolExecution(**as_dict(self.execution))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.outputSchema is not None and not isinstance(self.outputSchema, JsonSchema):
            self.outputSchema = JsonSchema(**as_dict(self.outputSchema))

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="icons", slot_type=Icon, key_name="src", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelHint(YAMLRoot):
    """
    Hints to use for model selection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ModelHint"]
    class_class_curie: ClassVar[str] = "mcp:ModelHint"
    class_name: ClassVar[str] = "ModelHint"
    class_model_uri: ClassVar[URIRef] = MCP.ModelHint

    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelPreferences(YAMLRoot):
    """
    The server's preferences for model selection, requested of the client during sampling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ModelPreferences"]
    class_class_curie: ClassVar[str] = "mcp:ModelPreferences"
    class_name: ClassVar[str] = "ModelPreferences"
    class_model_uri: ClassVar[URIRef] = MCP.ModelPreferences

    costPriority: Optional[float] = None
    intelligencePriority: Optional[float] = None
    speedPriority: Optional[float] = None
    hints: Optional[Union[Union[dict, ModelHint], list[Union[dict, ModelHint]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.costPriority is not None and not isinstance(self.costPriority, float):
            self.costPriority = float(self.costPriority)

        if self.intelligencePriority is not None and not isinstance(self.intelligencePriority, float):
            self.intelligencePriority = float(self.intelligencePriority)

        if self.speedPriority is not None and not isinstance(self.speedPriority, float):
            self.speedPriority = float(self.speedPriority)

        if not isinstance(self.hints, list):
            self.hints = [self.hints] if self.hints is not None else []
        self.hints = [v if isinstance(v, ModelHint) else ModelHint(**as_dict(v)) for v in self.hints]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplingMessage(YAMLRoot):
    """
    Describes a message issued to or received from an LLM API.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SamplingMessage"]
    class_class_curie: ClassVar[str] = "mcp:SamplingMessage"
    class_name: ClassVar[str] = "SamplingMessage"
    class_model_uri: ClassVar[URIRef] = MCP.SamplingMessage

    content: Union[dict, ContentBlock] = None
    role: Union[str, "Role"] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, ContentBlock):
            self.content = ContentBlock(**as_dict(self.content))

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, Role):
            self.role = Role(self.role)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Task(YAMLRoot):
    """
    Data associated with a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Task"]
    class_class_curie: ClassVar[str] = "mcp:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = MCP.Task

    taskId: str = None
    status: Union[str, "TaskStatusEnum"] = None
    createdAt: str = None
    lastUpdatedAt: str = None
    ttl: int = None
    statusMessage: Optional[str] = None
    pollInterval: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taskId):
            self.MissingRequiredField("taskId")
        if not isinstance(self.taskId, str):
            self.taskId = str(self.taskId)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, TaskStatusEnum):
            self.status = TaskStatusEnum(self.status)

        if self._is_empty(self.createdAt):
            self.MissingRequiredField("createdAt")
        if not isinstance(self.createdAt, str):
            self.createdAt = str(self.createdAt)

        if self._is_empty(self.lastUpdatedAt):
            self.MissingRequiredField("lastUpdatedAt")
        if not isinstance(self.lastUpdatedAt, str):
            self.lastUpdatedAt = str(self.lastUpdatedAt)

        if self._is_empty(self.ttl):
            self.MissingRequiredField("ttl")
        if not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        if self.statusMessage is not None and not isinstance(self.statusMessage, str):
            self.statusMessage = str(self.statusMessage)

        if self.pollInterval is not None and not isinstance(self.pollInterval, int):
            self.pollInterval = int(self.pollInterval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskMetadata(YAMLRoot):
    """
    Metadata for augmenting a request with task execution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TaskMetadata"]
    class_class_curie: ClassVar[str] = "mcp:TaskMetadata"
    class_name: ClassVar[str] = "TaskMetadata"
    class_model_uri: ClassVar[URIRef] = MCP.TaskMetadata

    ttl: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ttl is not None and not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedTaskMetadata(YAMLRoot):
    """
    Metadata for associating messages with a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["RelatedTaskMetadata"]
    class_class_curie: ClassVar[str] = "mcp:RelatedTaskMetadata"
    class_name: ClassVar[str] = "RelatedTaskMetadata"
    class_model_uri: ClassVar[URIRef] = MCP.RelatedTaskMetadata

    taskId: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taskId):
            self.MissingRequiredField("taskId")
        if not isinstance(self.taskId, str):
            self.taskId = str(self.taskId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClientCapabilities(YAMLRoot):
    """
    Capabilities a client may support. Known capabilities are defined here, but this is not a closed set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ClientCapabilities"]
    class_class_curie: ClassVar[str] = "mcp:ClientCapabilities"
    class_name: ClassVar[str] = "ClientCapabilities"
    class_model_uri: ClassVar[URIRef] = MCP.ClientCapabilities

    elicitation: Optional[Union[dict, ElicitationCapability]] = None
    experimental: Optional[object] = None
    extensions: Optional[Union[dict, ExtensionsCapability]] = None
    roots: Optional[Union[Union[dict, RootsCapability], list[Union[dict, RootsCapability]]]] = empty_list()
    sampling: Optional[Union[dict, SamplingCapability]] = None
    tasks: Optional[Union[Union[dict, TasksCapability], list[Union[dict, TasksCapability]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.elicitation is not None and not isinstance(self.elicitation, ElicitationCapability):
            self.elicitation = ElicitationCapability()

        if self.experimental is not None and not isinstance(self.experimental, object):
            self.experimental = object(self.experimental)

        if self.extensions is not None and not isinstance(self.extensions, ExtensionsCapability):
            self.extensions = ExtensionsCapability(**as_dict(self.extensions))

        if not isinstance(self.roots, list):
            self.roots = [self.roots] if self.roots is not None else []
        self.roots = [v if isinstance(v, RootsCapability) else RootsCapability(**as_dict(v)) for v in self.roots]

        if self.sampling is not None and not isinstance(self.sampling, SamplingCapability):
            self.sampling = SamplingCapability()

        if not isinstance(self.tasks, list):
            self.tasks = [self.tasks] if self.tasks is not None else []
        self.tasks = [v if isinstance(v, TasksCapability) else TasksCapability(**as_dict(v)) for v in self.tasks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServerCapabilities(YAMLRoot):
    """
    Capabilities that a server may support. Known capabilities are defined here, but this is not a closed set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ServerCapabilities"]
    class_class_curie: ClassVar[str] = "mcp:ServerCapabilities"
    class_name: ClassVar[str] = "ServerCapabilities"
    class_model_uri: ClassVar[URIRef] = MCP.ServerCapabilities

    experimental: Optional[object] = None
    extensions: Optional[Union[dict, ExtensionsCapability]] = None
    prompts: Optional[Union[Union[dict, PromptsCapability], list[Union[dict, PromptsCapability]]]] = empty_list()
    resources: Optional[Union[Union[dict, ResourcesCapability], list[Union[dict, ResourcesCapability]]]] = empty_list()
    tools: Optional[Union[Union[dict, ToolsCapability], list[Union[dict, ToolsCapability]]]] = empty_list()
    tasks: Optional[Union[Union[dict, TasksCapability], list[Union[dict, TasksCapability]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.experimental is not None and not isinstance(self.experimental, object):
            self.experimental = object(self.experimental)

        if self.extensions is not None and not isinstance(self.extensions, ExtensionsCapability):
            self.extensions = ExtensionsCapability(**as_dict(self.extensions))

        if not isinstance(self.prompts, list):
            self.prompts = [self.prompts] if self.prompts is not None else []
        self.prompts = [v if isinstance(v, PromptsCapability) else PromptsCapability(**as_dict(v)) for v in self.prompts]

        if not isinstance(self.resources, list):
            self.resources = [self.resources] if self.resources is not None else []
        self.resources = [v if isinstance(v, ResourcesCapability) else ResourcesCapability(**as_dict(v)) for v in self.resources]

        if not isinstance(self.tools, list):
            self.tools = [self.tools] if self.tools is not None else []
        self.tools = [v if isinstance(v, ToolsCapability) else ToolsCapability(**as_dict(v)) for v in self.tools]

        if not isinstance(self.tasks, list):
            self.tasks = [self.tasks] if self.tasks is not None else []
        self.tasks = [v if isinstance(v, TasksCapability) else TasksCapability(**as_dict(v)) for v in self.tasks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StringSchema(YAMLRoot):
    """
    String schema definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["StringSchema"]
    class_class_curie: ClassVar[str] = "mcp:StringSchema"
    class_name: ClassVar[str] = "StringSchema"
    class_model_uri: ClassVar[URIRef] = MCP.StringSchema

    type: str = None
    default: Optional[object] = None
    default_value: Optional[str] = None
    description: Optional[str] = None
    format: Optional[Union[str, "StringFormatEnum"]] = None
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.default is not None and not isinstance(self.default, object):
            self.default = object(self.default)

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.format is not None and not isinstance(self.format, StringFormatEnum):
            self.format = StringFormatEnum(self.format)

        if self.minLength is not None and not isinstance(self.minLength, int):
            self.minLength = int(self.minLength)

        if self.maxLength is not None and not isinstance(self.maxLength, int):
            self.maxLength = int(self.maxLength)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NumberSchema(YAMLRoot):
    """
    Number schema definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["NumberSchema"]
    class_class_curie: ClassVar[str] = "mcp:NumberSchema"
    class_name: ClassVar[str] = "NumberSchema"
    class_model_uri: ClassVar[URIRef] = MCP.NumberSchema

    type: str = None
    default: Optional[int] = None
    default_value: Optional[str] = None
    description: Optional[str] = None
    minimum: Optional[int] = None
    maximum: Optional[int] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.default is not None and not isinstance(self.default, int):
            self.default = int(self.default)

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.minimum is not None and not isinstance(self.minimum, int):
            self.minimum = int(self.minimum)

        if self.maximum is not None and not isinstance(self.maximum, int):
            self.maximum = int(self.maximum)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BooleanSchema(YAMLRoot):
    """
    Boolean schema definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["BooleanSchema"]
    class_class_curie: ClassVar[str] = "mcp:BooleanSchema"
    class_name: ClassVar[str] = "BooleanSchema"
    class_model_uri: ClassVar[URIRef] = MCP.BooleanSchema

    type: str = None
    default: Optional[Union[bool, Bool]] = None
    default_value: Optional[Union[bool, Bool]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.default is not None and not isinstance(self.default, Bool):
            self.default = Bool(self.default)

        if self.default_value is not None and not isinstance(self.default_value, Bool):
            self.default_value = Bool(self.default_value)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UntitledSingleSelectEnumSchema(YAMLRoot):
    """
    Single-selection enum without display titles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["UntitledSingleSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:UntitledSingleSelectEnumSchema"
    class_name: ClassVar[str] = "UntitledSingleSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.UntitledSingleSelectEnumSchema

    type: str = None
    enum: Optional[Union[str, list[str]]] = empty_list()
    enum_values: Optional[Union[str, list[str]]] = empty_list()
    default: Optional[object] = None
    default_value: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        if not isinstance(self.enum_values, list):
            self.enum_values = [self.enum_values] if self.enum_values is not None else []
        self.enum_values = [v if isinstance(v, str) else str(v) for v in self.enum_values]

        if self.default is not None and not isinstance(self.default, object):
            self.default = object(self.default)

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TitledSingleSelectEnumSchema(YAMLRoot):
    """
    Single-selection enum with display titles for each option.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TitledSingleSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:TitledSingleSelectEnumSchema"
    class_name: ClassVar[str] = "TitledSingleSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.TitledSingleSelectEnumSchema

    type: str = None
    oneOf: Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]] = empty_list()
    default: Optional[object] = None
    default_value: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        self._normalize_inlined_as_list(slot_name="oneOf", slot_type=EnumOption, key_name="const", keyed=False)

        if self.default is not None and not isinstance(self.default, object):
            self.default = object(self.default)

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UntitledMultiSelectEnumSchema(YAMLRoot):
    """
    Multi-selection enum without display titles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["UntitledMultiSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:UntitledMultiSelectEnumSchema"
    class_name: ClassVar[str] = "UntitledMultiSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.UntitledMultiSelectEnumSchema

    type: str = None
    items: Optional[Union[dict, SchemaItems]] = None
    default: Optional[Union[str, list[str]]] = empty_list()
    default_value: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    minItems: Optional[int] = None
    maxItems: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.items is not None and not isinstance(self.items, SchemaItems):
            self.items = SchemaItems(**as_dict(self.items))

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, str) else str(v) for v in self.default]

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.minItems is not None and not isinstance(self.minItems, int):
            self.minItems = int(self.minItems)

        if self.maxItems is not None and not isinstance(self.maxItems, int):
            self.maxItems = int(self.maxItems)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TitledMultiSelectEnumSchema(YAMLRoot):
    """
    Multi-selection enum with display titles for each option.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TitledMultiSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:TitledMultiSelectEnumSchema"
    class_name: ClassVar[str] = "TitledMultiSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.TitledMultiSelectEnumSchema

    type: str = None
    items: Optional[Union[dict, SchemaItems]] = None
    default: Optional[Union[str, list[str]]] = empty_list()
    default_value: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    minItems: Optional[int] = None
    maxItems: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.items is not None and not isinstance(self.items, SchemaItems):
            self.items = SchemaItems(**as_dict(self.items))

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, str) else str(v) for v in self.default]

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.minItems is not None and not isinstance(self.minItems, int):
            self.minItems = int(self.minItems)

        if self.maxItems is not None and not isinstance(self.maxItems, int):
            self.maxItems = int(self.maxItems)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegacyTitledEnumSchema(YAMLRoot):
    """
    Legacy titled enum schema. Use TitledSingleSelectEnumSchema instead.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["LegacyTitledEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:LegacyTitledEnumSchema"
    class_name: ClassVar[str] = "LegacyTitledEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.LegacyTitledEnumSchema

    type: str = None
    enum: Optional[Union[str, list[str]]] = empty_list()
    enum_values: Optional[Union[str, list[str]]] = empty_list()
    enumNames: Optional[Union[str, list[str]]] = empty_list()
    default: Optional[object] = None
    default_value: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.enum, list):
            self.enum = [self.enum] if self.enum is not None else []
        self.enum = [v if isinstance(v, str) else str(v) for v in self.enum]

        if not isinstance(self.enum_values, list):
            self.enum_values = [self.enum_values] if self.enum_values is not None else []
        self.enum_values = [v if isinstance(v, str) else str(v) for v in self.enum_values]

        if not isinstance(self.enumNames, list):
            self.enumNames = [self.enumNames] if self.enumNames is not None else []
        self.enumNames = [v if isinstance(v, str) else str(v) for v in self.enumNames]

        if self.default is not None and not isinstance(self.default, object):
            self.default = object(self.default)

        if self.default_value is not None and not isinstance(self.default_value, str):
            self.default_value = str(self.default_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JSONRPCRequest(YAMLRoot):
    """
    A request that expects a response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JSONRPCRequest"]
    class_class_curie: ClassVar[str] = "mcp:JSONRPCRequest"
    class_name: ClassVar[str] = "JSONRPCRequest"
    class_model_uri: ClassVar[URIRef] = MCP.JSONRPCRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JSONRPCNotification(YAMLRoot):
    """
    A notification which does not expect a response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JSONRPCNotification"]
    class_class_curie: ClassVar[str] = "mcp:JSONRPCNotification"
    class_name: ClassVar[str] = "JSONRPCNotification"
    class_model_uri: ClassVar[URIRef] = MCP.JSONRPCNotification

    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JSONRPCResultResponse(YAMLRoot):
    """
    A successful (non-error) response to a request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JSONRPCResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:JSONRPCResultResponse"
    class_name: ClassVar[str] = "JSONRPCResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.JSONRPCResultResponse

    id: str = None
    jsonrpc: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JSONRPCErrorResponse(YAMLRoot):
    """
    A response to a request that indicates an error occurred.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JSONRPCErrorResponse"]
    class_class_curie: ClassVar[str] = "mcp:JSONRPCErrorResponse"
    class_name: ClassVar[str] = "JSONRPCErrorResponse"
    class_model_uri: ClassVar[URIRef] = MCP.JSONRPCErrorResponse

    jsonrpc: str = None
    error: Union[dict, Error] = None
    id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.jsonrpc):
            self.MissingRequiredField("jsonrpc")
        if not isinstance(self.jsonrpc, str):
            self.jsonrpc = str(self.jsonrpc)

        if self._is_empty(self.error):
            self.MissingRequiredField("error")
        if not isinstance(self.error, Error):
            self.error = Error(**as_dict(self.error))

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class URLElicitationRequiredError(JSONRPCErrorResponse):
    """
    A response indicating that additional information is required via URL elicitation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["URLElicitationRequiredError"]
    class_class_curie: ClassVar[str] = "mcp:URLElicitationRequiredError"
    class_name: ClassVar[str] = "URLElicitationRequiredError"
    class_model_uri: ClassVar[URIRef] = MCP.URLElicitationRequiredError

    jsonrpc: str = None
    error: Union[dict, Error] = None

@dataclass(repr=False)
class Result(YAMLRoot):
    """
    Common result fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["Result"]
    class_class_curie: ClassVar[str] = "mcp:Result"
    class_name: ClassVar[str] = "Result"
    class_model_uri: ClassVar[URIRef] = MCP.Result

    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CancelledNotificationParams(YAMLRoot):
    """
    Parameters for a notifications/cancelled notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CancelledNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:CancelledNotificationParams"
    class_name: ClassVar[str] = "CancelledNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.CancelledNotificationParams

    requestId: Optional[str] = None
    reason: Optional[str] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.requestId is not None and not isinstance(self.requestId, str):
            self.requestId = str(self.requestId)

        if self.reason is not None and not isinstance(self.reason, str):
            self.reason = str(self.reason)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProgressNotificationParams(YAMLRoot):
    """
    Parameters for a notifications/progress notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ProgressNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:ProgressNotificationParams"
    class_name: ClassVar[str] = "ProgressNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.ProgressNotificationParams

    progress: float = None
    progressToken: str = None
    total: Optional[float] = None
    message: Optional[str] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.progress):
            self.MissingRequiredField("progress")
        if not isinstance(self.progress, float):
            self.progress = float(self.progress)

        if self._is_empty(self.progressToken):
            self.MissingRequiredField("progressToken")
        if not isinstance(self.progressToken, str):
            self.progressToken = str(self.progressToken)

        if self.total is not None and not isinstance(self.total, float):
            self.total = float(self.total)

        if self.message is not None and not isinstance(self.message, str):
            self.message = str(self.message)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitationCompleteNotificationParams(YAMLRoot):
    """
    Parameters for a notifications/elicitation/complete notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitationCompleteNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:ElicitationCompleteNotificationParams"
    class_name: ClassVar[str] = "ElicitationCompleteNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitationCompleteNotificationParams

    elicitationId: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.elicitationId):
            self.MissingRequiredField("elicitationId")
        if not isinstance(self.elicitationId, str):
            self.elicitationId = str(self.elicitationId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LoggingMessageNotificationParams(YAMLRoot):
    """
    Parameters for a notifications/message notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["LoggingMessageNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:LoggingMessageNotificationParams"
    class_name: ClassVar[str] = "LoggingMessageNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.LoggingMessageNotificationParams

    data: Union[dict, LogData] = None
    level: Union[str, "LoggingLevel"] = None
    logger: Optional[str] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, LogData):
            self.data = LogData(**as_dict(self.data))

        if self._is_empty(self.level):
            self.MissingRequiredField("level")
        if not isinstance(self.level, LoggingLevel):
            self.level = LoggingLevel(self.level)

        if self.logger is not None and not isinstance(self.logger, str):
            self.logger = str(self.logger)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceUpdatedNotificationParams(YAMLRoot):
    """
    Parameters for a notifications/resources/updated notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceUpdatedNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:ResourceUpdatedNotificationParams"
    class_name: ClassVar[str] = "ResourceUpdatedNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceUpdatedNotificationParams

    uri: Union[str, URI] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskStatusNotificationParams(YAMLRoot):
    """
    Parameters for a notifications/tasks/status notification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TaskStatusNotificationParams"]
    class_class_curie: ClassVar[str] = "mcp:TaskStatusNotificationParams"
    class_name: ClassVar[str] = "TaskStatusNotificationParams"
    class_model_uri: ClassVar[URIRef] = MCP.TaskStatusNotificationParams

    taskId: str = None
    status: Union[str, "TaskStatusEnum"] = None
    createdAt: str = None
    lastUpdatedAt: str = None
    ttl: int = None
    statusMessage: Optional[str] = None
    pollInterval: Optional[int] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taskId):
            self.MissingRequiredField("taskId")
        if not isinstance(self.taskId, str):
            self.taskId = str(self.taskId)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, TaskStatusEnum):
            self.status = TaskStatusEnum(self.status)

        if self._is_empty(self.createdAt):
            self.MissingRequiredField("createdAt")
        if not isinstance(self.createdAt, str):
            self.createdAt = str(self.createdAt)

        if self._is_empty(self.lastUpdatedAt):
            self.MissingRequiredField("lastUpdatedAt")
        if not isinstance(self.lastUpdatedAt, str):
            self.lastUpdatedAt = str(self.lastUpdatedAt)

        if self._is_empty(self.ttl):
            self.MissingRequiredField("ttl")
        if not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        if self.statusMessage is not None and not isinstance(self.statusMessage, str):
            self.statusMessage = str(self.statusMessage)

        if self.pollInterval is not None and not isinstance(self.pollInterval, int):
            self.pollInterval = int(self.pollInterval)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CancelledNotification(JSONRPCNotification):
    """
    Notification to indicate that a previously-issued request is being cancelled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CancelledNotification"]
    class_class_curie: ClassVar[str] = "mcp:CancelledNotification"
    class_name: ClassVar[str] = "CancelledNotification"
    class_model_uri: ClassVar[URIRef] = MCP.CancelledNotification

    jsonrpc: str = None
    params: Union[dict, CancelledNotificationParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, CancelledNotificationParams):
            self.params = CancelledNotificationParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InitializedNotification(JSONRPCNotification):
    """
    Notification sent from the client to the server after initialization has finished.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InitializedNotification"]
    class_class_curie: ClassVar[str] = "mcp:InitializedNotification"
    class_name: ClassVar[str] = "InitializedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.InitializedNotification

    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProgressNotification(JSONRPCNotification):
    """
    Out-of-band notification to inform the receiver of a progress update.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ProgressNotification"]
    class_class_curie: ClassVar[str] = "mcp:ProgressNotification"
    class_name: ClassVar[str] = "ProgressNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ProgressNotification

    jsonrpc: str = None
    params: Union[dict, ProgressNotificationParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, ProgressNotificationParams):
            self.params = ProgressNotificationParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceListChangedNotification(JSONRPCNotification):
    """
    Notification that the list of resources the server can read from has changed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:ResourceListChangedNotification"
    class_name: ClassVar[str] = "ResourceListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceListChangedNotification

    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceUpdatedNotification(JSONRPCNotification):
    """
    Notification that a resource has changed and may need to be read again.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ResourceUpdatedNotification"]
    class_class_curie: ClassVar[str] = "mcp:ResourceUpdatedNotification"
    class_name: ClassVar[str] = "ResourceUpdatedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ResourceUpdatedNotification

    jsonrpc: str = None
    params: Union[dict, ResourceUpdatedNotificationParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, ResourceUpdatedNotificationParams):
            self.params = ResourceUpdatedNotificationParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PromptListChangedNotification(JSONRPCNotification):
    """
    Notification that the list of prompts the server offers has changed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PromptListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:PromptListChangedNotification"
    class_name: ClassVar[str] = "PromptListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.PromptListChangedNotification

    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolListChangedNotification(JSONRPCNotification):
    """
    Notification that the list of tools the server offers has changed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ToolListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:ToolListChangedNotification"
    class_name: ClassVar[str] = "ToolListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ToolListChangedNotification

    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RootsListChangedNotification(JSONRPCNotification):
    """
    Notification from the client that the list of roots has changed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["RootsListChangedNotification"]
    class_class_curie: ClassVar[str] = "mcp:RootsListChangedNotification"
    class_name: ClassVar[str] = "RootsListChangedNotification"
    class_model_uri: ClassVar[URIRef] = MCP.RootsListChangedNotification

    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LoggingMessageNotification(JSONRPCNotification):
    """
    Notification of a log message passed from server to client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["LoggingMessageNotification"]
    class_class_curie: ClassVar[str] = "mcp:LoggingMessageNotification"
    class_name: ClassVar[str] = "LoggingMessageNotification"
    class_model_uri: ClassVar[URIRef] = MCP.LoggingMessageNotification

    jsonrpc: str = None
    params: Union[dict, LoggingMessageNotificationParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, LoggingMessageNotificationParams):
            self.params = LoggingMessageNotificationParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitationCompleteNotification(JSONRPCNotification):
    """
    Notification from the server that an out-of-band elicitation request completed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitationCompleteNotification"]
    class_class_curie: ClassVar[str] = "mcp:ElicitationCompleteNotification"
    class_name: ClassVar[str] = "ElicitationCompleteNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitationCompleteNotification

    jsonrpc: str = None
    params: Union[dict, ElicitationCompleteNotificationParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, ElicitationCompleteNotificationParams):
            self.params = ElicitationCompleteNotificationParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskStatusNotification(JSONRPCNotification):
    """
    Notification that a task's status has changed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["TaskStatusNotification"]
    class_class_curie: ClassVar[str] = "mcp:TaskStatusNotification"
    class_name: ClassVar[str] = "TaskStatusNotification"
    class_model_uri: ClassVar[URIRef] = MCP.TaskStatusNotification

    jsonrpc: str = None
    params: Union[dict, TaskStatusNotificationParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, TaskStatusNotificationParams):
            self.params = TaskStatusNotificationParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CallToolRequestParams(YAMLRoot):
    """
    Parameters for a tools/call request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CallToolRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:CallToolRequestParams"
    class_name: ClassVar[str] = "CallToolRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.CallToolRequestParams

    name: str = None
    arguments: Optional[Union[dict, ArgumentMap]] = None
    task: Optional[Union[dict, TaskMetadata]] = None
    _meta: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.arguments is not None and not isinstance(self.arguments, ArgumentMap):
            self.arguments = ArgumentMap(**as_dict(self.arguments))

        if self.task is not None and not isinstance(self.task, TaskMetadata):
            self.task = TaskMetadata(**as_dict(self.task))

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetPromptRequestParams(YAMLRoot):
    """
    Parameters for a prompts/get request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetPromptRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:GetPromptRequestParams"
    class_name: ClassVar[str] = "GetPromptRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.GetPromptRequestParams

    name: str = None
    arguments: Optional[Union[dict, ArgumentMap]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.arguments is not None and not isinstance(self.arguments, ArgumentMap):
            self.arguments = ArgumentMap(**as_dict(self.arguments))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompleteRequestParams(YAMLRoot):
    """
    Parameters for a completion/complete request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompleteRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:CompleteRequestParams"
    class_name: ClassVar[str] = "CompleteRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.CompleteRequestParams

    argument: Union[dict, CompletionArgument] = None
    ref: Union[dict, PromptReference] = None
    context: Optional[Union[dict, CompletionContext]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.argument):
            self.MissingRequiredField("argument")
        if not isinstance(self.argument, CompletionArgument):
            self.argument = CompletionArgument(**as_dict(self.argument))

        if self._is_empty(self.ref):
            self.MissingRequiredField("ref")
        if not isinstance(self.ref, PromptReference):
            self.ref = PromptReference(**as_dict(self.ref))

        if self.context is not None and not isinstance(self.context, CompletionContext):
            self.context = CompletionContext(**as_dict(self.context))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReadResourceRequestParams(YAMLRoot):
    """
    Parameters for a resources/read request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ReadResourceRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:ReadResourceRequestParams"
    class_name: ClassVar[str] = "ReadResourceRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.ReadResourceRequestParams

    uri: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubscribeRequestParams(YAMLRoot):
    """
    Parameters for a resources/subscribe request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SubscribeRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:SubscribeRequestParams"
    class_name: ClassVar[str] = "SubscribeRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.SubscribeRequestParams

    uri: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnsubscribeRequestParams(YAMLRoot):
    """
    Parameters for a resources/unsubscribe request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["UnsubscribeRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:UnsubscribeRequestParams"
    class_name: ClassVar[str] = "UnsubscribeRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.UnsubscribeRequestParams

    uri: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SetLevelRequestParams(YAMLRoot):
    """
    Parameters for a logging/setLevel request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SetLevelRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:SetLevelRequestParams"
    class_name: ClassVar[str] = "SetLevelRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.SetLevelRequestParams

    level: Union[str, "LoggingLevel"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.level):
            self.MissingRequiredField("level")
        if not isinstance(self.level, LoggingLevel):
            self.level = LoggingLevel(self.level)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InitializeRequestParams(YAMLRoot):
    """
    Parameters for an initialize request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InitializeRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:InitializeRequestParams"
    class_name: ClassVar[str] = "InitializeRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.InitializeRequestParams

    capabilities: Union[dict, ClientCapabilities] = None
    clientInfo: Union[dict, Implementation] = None
    protocolVersion: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.capabilities):
            self.MissingRequiredField("capabilities")
        if not isinstance(self.capabilities, ClientCapabilities):
            self.capabilities = ClientCapabilities(**as_dict(self.capabilities))

        if self._is_empty(self.clientInfo):
            self.MissingRequiredField("clientInfo")
        if not isinstance(self.clientInfo, Implementation):
            self.clientInfo = Implementation(**as_dict(self.clientInfo))

        if self._is_empty(self.protocolVersion):
            self.MissingRequiredField("protocolVersion")
        if not isinstance(self.protocolVersion, str):
            self.protocolVersion = str(self.protocolVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreateMessageRequestParams(YAMLRoot):
    """
    Parameters for a sampling/createMessage request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CreateMessageRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:CreateMessageRequestParams"
    class_name: ClassVar[str] = "CreateMessageRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.CreateMessageRequestParams

    maxTokens: int = None
    messages: Union[Union[dict, SamplingMessage], list[Union[dict, SamplingMessage]]] = None
    modelPreferences: Optional[Union[dict, ModelPreferences]] = None
    systemPrompt: Optional[str] = None
    temperature: Optional[float] = None
    includeContext: Optional[Union[str, "IncludeContextEnum"]] = None
    stopSequences: Optional[Union[str, list[str]]] = empty_list()
    tools: Optional[Union[Union[dict, Tool], list[Union[dict, Tool]]]] = empty_list()
    toolChoice: Optional[Union[dict, ToolChoice]] = None
    task: Optional[Union[dict, TaskMetadata]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.maxTokens):
            self.MissingRequiredField("maxTokens")
        if not isinstance(self.maxTokens, int):
            self.maxTokens = int(self.maxTokens)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=SamplingMessage, key_name="role", keyed=False)

        if self.modelPreferences is not None and not isinstance(self.modelPreferences, ModelPreferences):
            self.modelPreferences = ModelPreferences(**as_dict(self.modelPreferences))

        if self.systemPrompt is not None and not isinstance(self.systemPrompt, str):
            self.systemPrompt = str(self.systemPrompt)

        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.includeContext is not None and not isinstance(self.includeContext, IncludeContextEnum):
            self.includeContext = IncludeContextEnum(self.includeContext)

        if not isinstance(self.stopSequences, list):
            self.stopSequences = [self.stopSequences] if self.stopSequences is not None else []
        self.stopSequences = [v if isinstance(v, str) else str(v) for v in self.stopSequences]

        self._normalize_inlined_as_list(slot_name="tools", slot_type=Tool, key_name="name", keyed=False)

        if self.toolChoice is not None and not isinstance(self.toolChoice, ToolChoice):
            self.toolChoice = ToolChoice(**as_dict(self.toolChoice))

        if self.task is not None and not isinstance(self.task, TaskMetadata):
            self.task = TaskMetadata(**as_dict(self.task))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitRequestFormParams(YAMLRoot):
    """
    Parameters for a form-mode elicitation request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitRequestFormParams"]
    class_class_curie: ClassVar[str] = "mcp:ElicitRequestFormParams"
    class_name: ClassVar[str] = "ElicitRequestFormParams"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitRequestFormParams

    message: str = None
    requestedSchema: Union[dict, JsonSchema] = None
    mode: Optional[str] = None
    task: Optional[Union[dict, TaskMetadata]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        if self._is_empty(self.requestedSchema):
            self.MissingRequiredField("requestedSchema")
        if not isinstance(self.requestedSchema, JsonSchema):
            self.requestedSchema = JsonSchema(**as_dict(self.requestedSchema))

        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        if self.task is not None and not isinstance(self.task, TaskMetadata):
            self.task = TaskMetadata(**as_dict(self.task))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitRequestURLParams(YAMLRoot):
    """
    Parameters for a URL-mode elicitation request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitRequestURLParams"]
    class_class_curie: ClassVar[str] = "mcp:ElicitRequestURLParams"
    class_name: ClassVar[str] = "ElicitRequestURLParams"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitRequestURLParams

    elicitationId: str = None
    message: str = None
    mode: str = None
    url: Union[str, URI] = None
    task: Optional[Union[dict, TaskMetadata]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.elicitationId):
            self.MissingRequiredField("elicitationId")
        if not isinstance(self.elicitationId, str):
            self.elicitationId = str(self.elicitationId)

        if self._is_empty(self.message):
            self.MissingRequiredField("message")
        if not isinstance(self.message, str):
            self.message = str(self.message)

        if self._is_empty(self.mode):
            self.MissingRequiredField("mode")
        if not isinstance(self.mode, str):
            self.mode = str(self.mode)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.task is not None and not isinstance(self.task, TaskMetadata):
            self.task = TaskMetadata(**as_dict(self.task))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PaginatedRequestParams(YAMLRoot):
    """
    Common params for paginated requests.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PaginatedRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:PaginatedRequestParams"
    class_name: ClassVar[str] = "PaginatedRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.PaginatedRequestParams

    cursor: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cursor is not None and not isinstance(self.cursor, str):
            self.cursor = str(self.cursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InitializeRequest(JSONRPCRequest):
    """
    Request sent from the client to the server when it first connects, asking it to begin initialization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InitializeRequest"]
    class_class_curie: ClassVar[str] = "mcp:InitializeRequest"
    class_name: ClassVar[str] = "InitializeRequest"
    class_model_uri: ClassVar[URIRef] = MCP.InitializeRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, InitializeRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, InitializeRequestParams):
            self.params = InitializeRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PingRequest(JSONRPCRequest):
    """
    A ping, issued by either the server or the client, to check that the other party is still alive.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PingRequest"]
    class_class_curie: ClassVar[str] = "mcp:PingRequest"
    class_name: ClassVar[str] = "PingRequest"
    class_model_uri: ClassVar[URIRef] = MCP.PingRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListResourcesRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of resources the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListResourcesRequest"]
    class_class_curie: ClassVar[str] = "mcp:ListResourcesRequest"
    class_name: ClassVar[str] = "ListResourcesRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ListResourcesRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListResourceTemplatesRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of resource templates the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListResourceTemplatesRequest"]
    class_class_curie: ClassVar[str] = "mcp:ListResourceTemplatesRequest"
    class_name: ClassVar[str] = "ListResourceTemplatesRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ListResourceTemplatesRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReadResourceRequest(JSONRPCRequest):
    """
    Sent from the client to the server, to read a specific resource URI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ReadResourceRequest"]
    class_class_curie: ClassVar[str] = "mcp:ReadResourceRequest"
    class_name: ClassVar[str] = "ReadResourceRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ReadResourceRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, ReadResourceRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, ReadResourceRequestParams):
            self.params = ReadResourceRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubscribeRequest(JSONRPCRequest):
    """
    Sent from the client to request resource update notifications.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SubscribeRequest"]
    class_class_curie: ClassVar[str] = "mcp:SubscribeRequest"
    class_name: ClassVar[str] = "SubscribeRequest"
    class_model_uri: ClassVar[URIRef] = MCP.SubscribeRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, SubscribeRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, SubscribeRequestParams):
            self.params = SubscribeRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnsubscribeRequest(JSONRPCRequest):
    """
    Sent from the client to cancel resource update notifications.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["UnsubscribeRequest"]
    class_class_curie: ClassVar[str] = "mcp:UnsubscribeRequest"
    class_name: ClassVar[str] = "UnsubscribeRequest"
    class_model_uri: ClassVar[URIRef] = MCP.UnsubscribeRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, UnsubscribeRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, UnsubscribeRequestParams):
            self.params = UnsubscribeRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListPromptsRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of prompts and prompt templates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListPromptsRequest"]
    class_class_curie: ClassVar[str] = "mcp:ListPromptsRequest"
    class_name: ClassVar[str] = "ListPromptsRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ListPromptsRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetPromptRequest(JSONRPCRequest):
    """
    Used by the client to get a prompt provided by the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetPromptRequest"]
    class_class_curie: ClassVar[str] = "mcp:GetPromptRequest"
    class_name: ClassVar[str] = "GetPromptRequest"
    class_model_uri: ClassVar[URIRef] = MCP.GetPromptRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, GetPromptRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, GetPromptRequestParams):
            self.params = GetPromptRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListToolsRequest(JSONRPCRequest):
    """
    Sent from the client to request a list of tools the server has.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListToolsRequest"]
    class_class_curie: ClassVar[str] = "mcp:ListToolsRequest"
    class_name: ClassVar[str] = "ListToolsRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ListToolsRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CallToolRequest(JSONRPCRequest):
    """
    Used by the client to invoke a tool provided by the server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CallToolRequest"]
    class_class_curie: ClassVar[str] = "mcp:CallToolRequest"
    class_name: ClassVar[str] = "CallToolRequest"
    class_model_uri: ClassVar[URIRef] = MCP.CallToolRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, CallToolRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, CallToolRequestParams):
            self.params = CallToolRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompleteRequest(JSONRPCRequest):
    """
    A request from the client to the server, to ask for completion options.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompleteRequest"]
    class_class_curie: ClassVar[str] = "mcp:CompleteRequest"
    class_name: ClassVar[str] = "CompleteRequest"
    class_model_uri: ClassVar[URIRef] = MCP.CompleteRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, CompleteRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, CompleteRequestParams):
            self.params = CompleteRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SetLevelRequest(JSONRPCRequest):
    """
    A request from the client to the server, to enable or adjust logging.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SetLevelRequest"]
    class_class_curie: ClassVar[str] = "mcp:SetLevelRequest"
    class_name: ClassVar[str] = "SetLevelRequest"
    class_model_uri: ClassVar[URIRef] = MCP.SetLevelRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, SetLevelRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, SetLevelRequestParams):
            self.params = SetLevelRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreateMessageRequest(JSONRPCRequest):
    """
    A request from the server to sample an LLM via the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CreateMessageRequest"]
    class_class_curie: ClassVar[str] = "mcp:CreateMessageRequest"
    class_name: ClassVar[str] = "CreateMessageRequest"
    class_model_uri: ClassVar[URIRef] = MCP.CreateMessageRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, CreateMessageRequestParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, CreateMessageRequestParams):
            self.params = CreateMessageRequestParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListRootsRequest(JSONRPCRequest):
    """
    Sent from the server to request a list of root URIs from the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListRootsRequest"]
    class_class_curie: ClassVar[str] = "mcp:ListRootsRequest"
    class_name: ClassVar[str] = "ListRootsRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ListRootsRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitRequest(JSONRPCRequest):
    """
    A request from the server to elicit additional information from the user via the client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitRequest"]
    class_class_curie: ClassVar[str] = "mcp:ElicitRequest"
    class_name: ClassVar[str] = "ElicitRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitRequest

    id: str = None
    jsonrpc: str = None
    params: Union[dict, ElicitRequestFormParams] = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, ElicitRequestFormParams):
            self.params = ElicitRequestFormParams(**as_dict(self.params))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListTasksRequest(JSONRPCRequest):
    """
    A request to retrieve a list of tasks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListTasksRequest"]
    class_class_curie: ClassVar[str] = "mcp:ListTasksRequest"
    class_name: ClassVar[str] = "ListTasksRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ListTasksRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetTaskRequest(JSONRPCRequest):
    """
    A request to retrieve the state of a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetTaskRequest"]
    class_class_curie: ClassVar[str] = "mcp:GetTaskRequest"
    class_name: ClassVar[str] = "GetTaskRequest"
    class_model_uri: ClassVar[URIRef] = MCP.GetTaskRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetTaskPayloadRequest(JSONRPCRequest):
    """
    A request to retrieve the result of a completed task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetTaskPayloadRequest"]
    class_class_curie: ClassVar[str] = "mcp:GetTaskPayloadRequest"
    class_name: ClassVar[str] = "GetTaskPayloadRequest"
    class_model_uri: ClassVar[URIRef] = MCP.GetTaskPayloadRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CancelTaskRequest(JSONRPCRequest):
    """
    A request to cancel a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CancelTaskRequest"]
    class_class_curie: ClassVar[str] = "mcp:CancelTaskRequest"
    class_name: ClassVar[str] = "CancelTaskRequest"
    class_model_uri: ClassVar[URIRef] = MCP.CancelTaskRequest

    id: str = None
    jsonrpc: str = None
    method: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InitializeResult(Result):
    """
    The result returned by the server for an initialize request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InitializeResult"]
    class_class_curie: ClassVar[str] = "mcp:InitializeResult"
    class_name: ClassVar[str] = "InitializeResult"
    class_model_uri: ClassVar[URIRef] = MCP.InitializeResult

    capabilities: Union[dict, ServerCapabilities] = None
    protocolVersion: str = None
    serverInfo: Union[dict, Implementation] = None
    instructions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.capabilities):
            self.MissingRequiredField("capabilities")
        if not isinstance(self.capabilities, ServerCapabilities):
            self.capabilities = ServerCapabilities(**as_dict(self.capabilities))

        if self._is_empty(self.protocolVersion):
            self.MissingRequiredField("protocolVersion")
        if not isinstance(self.protocolVersion, str):
            self.protocolVersion = str(self.protocolVersion)

        if self._is_empty(self.serverInfo):
            self.MissingRequiredField("serverInfo")
        if not isinstance(self.serverInfo, Implementation):
            self.serverInfo = Implementation(**as_dict(self.serverInfo))

        if self.instructions is not None and not isinstance(self.instructions, str):
            self.instructions = str(self.instructions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CallToolResult(Result):
    """
    The result returned by the server for a tools/call request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CallToolResult"]
    class_class_curie: ClassVar[str] = "mcp:CallToolResult"
    class_name: ClassVar[str] = "CallToolResult"
    class_model_uri: ClassVar[URIRef] = MCP.CallToolResult

    content: Union[Union[dict, ContentBlock], list[Union[dict, ContentBlock]]] = None
    isError: Optional[Union[bool, Bool]] = None
    structuredContent: Optional[Union[dict, StructuredContentData]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, ContentBlock) else ContentBlock(**as_dict(v)) for v in self.content]

        if self.isError is not None and not isinstance(self.isError, Bool):
            self.isError = Bool(self.isError)

        if self.structuredContent is not None and not isinstance(self.structuredContent, StructuredContentData):
            self.structuredContent = StructuredContentData(**as_dict(self.structuredContent))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompleteResult(Result):
    """
    The result returned by the server for a completion/complete request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompleteResult"]
    class_class_curie: ClassVar[str] = "mcp:CompleteResult"
    class_name: ClassVar[str] = "CompleteResult"
    class_model_uri: ClassVar[URIRef] = MCP.CompleteResult

    completion: Union[dict, CompletionData] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.completion):
            self.MissingRequiredField("completion")
        if not isinstance(self.completion, CompletionData):
            self.completion = CompletionData(**as_dict(self.completion))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetPromptResult(Result):
    """
    The result returned by the server for a prompts/get request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetPromptResult"]
    class_class_curie: ClassVar[str] = "mcp:GetPromptResult"
    class_name: ClassVar[str] = "GetPromptResult"
    class_model_uri: ClassVar[URIRef] = MCP.GetPromptResult

    messages: Union[Union[dict, PromptMessage], list[Union[dict, PromptMessage]]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=PromptMessage, key_name="role", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListPromptsResult(Result):
    """
    The result returned by the server for a prompts/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListPromptsResult"]
    class_class_curie: ClassVar[str] = "mcp:ListPromptsResult"
    class_name: ClassVar[str] = "ListPromptsResult"
    class_model_uri: ClassVar[URIRef] = MCP.ListPromptsResult

    prompts: Union[Union[dict, Prompt], list[Union[dict, Prompt]]] = None
    nextCursor: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prompts):
            self.MissingRequiredField("prompts")
        self._normalize_inlined_as_list(slot_name="prompts", slot_type=Prompt, key_name="name", keyed=False)

        if self.nextCursor is not None and not isinstance(self.nextCursor, str):
            self.nextCursor = str(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListResourcesResult(Result):
    """
    The result returned by the server for a resources/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListResourcesResult"]
    class_class_curie: ClassVar[str] = "mcp:ListResourcesResult"
    class_name: ClassVar[str] = "ListResourcesResult"
    class_model_uri: ClassVar[URIRef] = MCP.ListResourcesResult

    resources: Union[Union[dict, Resource], list[Union[dict, Resource]]] = None
    nextCursor: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resources):
            self.MissingRequiredField("resources")
        self._normalize_inlined_as_list(slot_name="resources", slot_type=Resource, key_name="uri", keyed=False)

        if self.nextCursor is not None and not isinstance(self.nextCursor, str):
            self.nextCursor = str(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListResourceTemplatesResult(Result):
    """
    The result returned by the server for a resources/templates/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListResourceTemplatesResult"]
    class_class_curie: ClassVar[str] = "mcp:ListResourceTemplatesResult"
    class_name: ClassVar[str] = "ListResourceTemplatesResult"
    class_model_uri: ClassVar[URIRef] = MCP.ListResourceTemplatesResult

    resourceTemplates: Union[Union[dict, ResourceTemplate], list[Union[dict, ResourceTemplate]]] = None
    nextCursor: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resourceTemplates):
            self.MissingRequiredField("resourceTemplates")
        self._normalize_inlined_as_list(slot_name="resourceTemplates", slot_type=ResourceTemplate, key_name="uriTemplate", keyed=False)

        if self.nextCursor is not None and not isinstance(self.nextCursor, str):
            self.nextCursor = str(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReadResourceResult(Result):
    """
    The result returned by the server for a resources/read request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ReadResourceResult"]
    class_class_curie: ClassVar[str] = "mcp:ReadResourceResult"
    class_name: ClassVar[str] = "ReadResourceResult"
    class_model_uri: ClassVar[URIRef] = MCP.ReadResourceResult

    contents: Union[Union[dict, ResourceContents], list[Union[dict, ResourceContents]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.contents):
            self.MissingRequiredField("contents")
        self._normalize_inlined_as_list(slot_name="contents", slot_type=ResourceContents, key_name="uri", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListToolsResult(Result):
    """
    The result returned by the server for a tools/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListToolsResult"]
    class_class_curie: ClassVar[str] = "mcp:ListToolsResult"
    class_name: ClassVar[str] = "ListToolsResult"
    class_model_uri: ClassVar[URIRef] = MCP.ListToolsResult

    tools: Union[Union[dict, Tool], list[Union[dict, Tool]]] = None
    nextCursor: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.tools):
            self.MissingRequiredField("tools")
        self._normalize_inlined_as_list(slot_name="tools", slot_type=Tool, key_name="name", keyed=False)

        if self.nextCursor is not None and not isinstance(self.nextCursor, str):
            self.nextCursor = str(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListRootsResult(Result):
    """
    The result returned by the client for a roots/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListRootsResult"]
    class_class_curie: ClassVar[str] = "mcp:ListRootsResult"
    class_name: ClassVar[str] = "ListRootsResult"
    class_model_uri: ClassVar[URIRef] = MCP.ListRootsResult

    roots: Union[Union[dict, Root], list[Union[dict, Root]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.roots):
            self.MissingRequiredField("roots")
        self._normalize_inlined_as_list(slot_name="roots", slot_type=Root, key_name="uri", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreateMessageResult(Result):
    """
    The result returned by the client for a sampling/createMessage request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CreateMessageResult"]
    class_class_curie: ClassVar[str] = "mcp:CreateMessageResult"
    class_name: ClassVar[str] = "CreateMessageResult"
    class_model_uri: ClassVar[URIRef] = MCP.CreateMessageResult

    content: Union[dict, ContentBlock] = None
    model: str = None
    role: Union[str, "Role"] = None
    stopReason: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, ContentBlock):
            self.content = ContentBlock(**as_dict(self.content))

        if self._is_empty(self.model):
            self.MissingRequiredField("model")
        if not isinstance(self.model, str):
            self.model = str(self.model)

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, Role):
            self.role = Role(self.role)

        if self.stopReason is not None and not isinstance(self.stopReason, str):
            self.stopReason = str(self.stopReason)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitResult(Result):
    """
    The result returned by the client for an elicitation/create request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitResult"]
    class_class_curie: ClassVar[str] = "mcp:ElicitResult"
    class_name: ClassVar[str] = "ElicitResult"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitResult

    action: Union[str, "ElicitActionEnum"] = None
    content: Optional[Union[dict, ElicitationContent]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, ElicitActionEnum):
            self.action = ElicitActionEnum(self.action)

        if self.content is not None and not isinstance(self.content, ElicitationContent):
            self.content = ElicitationContent(**as_dict(self.content))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreateTaskResult(Result):
    """
    The result returned for a task-augmented request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CreateTaskResult"]
    class_class_curie: ClassVar[str] = "mcp:CreateTaskResult"
    class_name: ClassVar[str] = "CreateTaskResult"
    class_model_uri: ClassVar[URIRef] = MCP.CreateTaskResult

    task: Union[dict, Task] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task):
            self.MissingRequiredField("task")
        if not isinstance(self.task, Task):
            self.task = Task(**as_dict(self.task))

        super().__post_init__(**kwargs)


class GetTaskPayloadResult(Result):
    """
    The result returned for a tasks/result request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetTaskPayloadResult"]
    class_class_curie: ClassVar[str] = "mcp:GetTaskPayloadResult"
    class_name: ClassVar[str] = "GetTaskPayloadResult"
    class_model_uri: ClassVar[URIRef] = MCP.GetTaskPayloadResult


@dataclass(repr=False)
class ListTasksResult(Result):
    """
    The result returned for a tasks/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListTasksResult"]
    class_class_curie: ClassVar[str] = "mcp:ListTasksResult"
    class_name: ClassVar[str] = "ListTasksResult"
    class_model_uri: ClassVar[URIRef] = MCP.ListTasksResult

    tasks: Union[Union[dict, Task], list[Union[dict, Task]]] = None
    nextCursor: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.tasks):
            self.MissingRequiredField("tasks")
        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="taskId", keyed=False)

        if self.nextCursor is not None and not isinstance(self.nextCursor, str):
            self.nextCursor = str(self.nextCursor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CancelTaskResult(Result):
    """
    The result returned for a tasks/cancel request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CancelTaskResult"]
    class_class_curie: ClassVar[str] = "mcp:CancelTaskResult"
    class_name: ClassVar[str] = "CancelTaskResult"
    class_model_uri: ClassVar[URIRef] = MCP.CancelTaskResult

    taskId: str = None
    status: Union[str, "TaskStatusEnum"] = None
    createdAt: str = None
    lastUpdatedAt: str = None
    ttl: int = None
    _meta: Optional[Union[dict, MetaObject]] = None
    statusMessage: Optional[str] = None
    pollInterval: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taskId):
            self.MissingRequiredField("taskId")
        if not isinstance(self.taskId, str):
            self.taskId = str(self.taskId)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, TaskStatusEnum):
            self.status = TaskStatusEnum(self.status)

        if self._is_empty(self.createdAt):
            self.MissingRequiredField("createdAt")
        if not isinstance(self.createdAt, str):
            self.createdAt = str(self.createdAt)

        if self._is_empty(self.lastUpdatedAt):
            self.MissingRequiredField("lastUpdatedAt")
        if not isinstance(self.lastUpdatedAt, str):
            self.lastUpdatedAt = str(self.lastUpdatedAt)

        if self._is_empty(self.ttl):
            self.MissingRequiredField("ttl")
        if not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.statusMessage is not None and not isinstance(self.statusMessage, str):
            self.statusMessage = str(self.statusMessage)

        if self.pollInterval is not None and not isinstance(self.pollInterval, int):
            self.pollInterval = int(self.pollInterval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetTaskResult(Result):
    """
    The result returned for a tasks/get request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetTaskResult"]
    class_class_curie: ClassVar[str] = "mcp:GetTaskResult"
    class_name: ClassVar[str] = "GetTaskResult"
    class_model_uri: ClassVar[URIRef] = MCP.GetTaskResult

    taskId: str = None
    status: Union[str, "TaskStatusEnum"] = None
    createdAt: str = None
    lastUpdatedAt: str = None
    ttl: int = None
    _meta: Optional[Union[dict, MetaObject]] = None
    statusMessage: Optional[str] = None
    pollInterval: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taskId):
            self.MissingRequiredField("taskId")
        if not isinstance(self.taskId, str):
            self.taskId = str(self.taskId)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, TaskStatusEnum):
            self.status = TaskStatusEnum(self.status)

        if self._is_empty(self.createdAt):
            self.MissingRequiredField("createdAt")
        if not isinstance(self.createdAt, str):
            self.createdAt = str(self.createdAt)

        if self._is_empty(self.lastUpdatedAt):
            self.MissingRequiredField("lastUpdatedAt")
        if not isinstance(self.lastUpdatedAt, str):
            self.lastUpdatedAt = str(self.lastUpdatedAt)

        if self._is_empty(self.ttl):
            self.MissingRequiredField("ttl")
        if not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        if self._meta is not None and not isinstance(self._meta, MetaObject):
            self._meta = MetaObject(**as_dict(self._meta))

        if self.statusMessage is not None and not isinstance(self.statusMessage, str):
            self.statusMessage = str(self.statusMessage)

        if self.pollInterval is not None and not isinstance(self.pollInterval, int):
            self.pollInterval = int(self.pollInterval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InitializeResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for an initialize request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["InitializeResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:InitializeResultResponse"
    class_name: ClassVar[str] = "InitializeResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.InitializeResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, InitializeResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, InitializeResult):
            self.result = InitializeResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CallToolResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a tools/call request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CallToolResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:CallToolResultResponse"
    class_name: ClassVar[str] = "CallToolResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.CallToolResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, CallToolResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, CallToolResult):
            self.result = CallToolResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompleteResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a completion/complete request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CompleteResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:CompleteResultResponse"
    class_name: ClassVar[str] = "CompleteResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.CompleteResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, CompleteResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, CompleteResult):
            self.result = CompleteResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetPromptResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a prompts/get request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetPromptResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:GetPromptResultResponse"
    class_name: ClassVar[str] = "GetPromptResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.GetPromptResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, GetPromptResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, GetPromptResult):
            self.result = GetPromptResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListPromptsResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a prompts/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListPromptsResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ListPromptsResultResponse"
    class_name: ClassVar[str] = "ListPromptsResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ListPromptsResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ListPromptsResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ListPromptsResult):
            self.result = ListPromptsResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListResourcesResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a resources/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListResourcesResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ListResourcesResultResponse"
    class_name: ClassVar[str] = "ListResourcesResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ListResourcesResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ListResourcesResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ListResourcesResult):
            self.result = ListResourcesResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListResourceTemplatesResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a resources/templates/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListResourceTemplatesResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ListResourceTemplatesResultResponse"
    class_name: ClassVar[str] = "ListResourceTemplatesResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ListResourceTemplatesResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ListResourceTemplatesResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ListResourceTemplatesResult):
            self.result = ListResourceTemplatesResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReadResourceResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a resources/read request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ReadResourceResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ReadResourceResultResponse"
    class_name: ClassVar[str] = "ReadResourceResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ReadResourceResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ReadResourceResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ReadResourceResult):
            self.result = ReadResourceResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListToolsResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a tools/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListToolsResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ListToolsResultResponse"
    class_name: ClassVar[str] = "ListToolsResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ListToolsResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ListToolsResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ListToolsResult):
            self.result = ListToolsResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListRootsResultResponse(JSONRPCResultResponse):
    """
    A successful response from the client for a roots/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListRootsResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ListRootsResultResponse"
    class_name: ClassVar[str] = "ListRootsResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ListRootsResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ListRootsResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ListRootsResult):
            self.result = ListRootsResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreateMessageResultResponse(JSONRPCResultResponse):
    """
    A successful response from the client for a sampling/createMessage request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CreateMessageResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:CreateMessageResultResponse"
    class_name: ClassVar[str] = "CreateMessageResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.CreateMessageResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, CreateMessageResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, CreateMessageResult):
            self.result = CreateMessageResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElicitResultResponse(JSONRPCResultResponse):
    """
    A successful response from the client for an elicitation/create request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ElicitResultResponse"
    class_name: ClassVar[str] = "ElicitResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ElicitResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ElicitResult):
            self.result = ElicitResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SetLevelResultResponse(JSONRPCResultResponse):
    """
    A successful response from the server for a logging/setLevel request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SetLevelResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:SetLevelResultResponse"
    class_name: ClassVar[str] = "SetLevelResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.SetLevelResultResponse

    id: str = None
    jsonrpc: str = None
    result: Optional[Union[dict, Result]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.result is not None and not isinstance(self.result, Result):
            self.result = Result(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PingResultResponse(JSONRPCResultResponse):
    """
    A successful response for a ping request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PingResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:PingResultResponse"
    class_name: ClassVar[str] = "PingResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.PingResultResponse

    id: str = None
    jsonrpc: str = None
    result: Optional[Union[dict, Result]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.result is not None and not isinstance(self.result, Result):
            self.result = Result(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubscribeResultResponse(JSONRPCResultResponse):
    """
    A successful response for a resources/subscribe request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SubscribeResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:SubscribeResultResponse"
    class_name: ClassVar[str] = "SubscribeResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.SubscribeResultResponse

    id: str = None
    jsonrpc: str = None
    result: Optional[Union[dict, Result]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.result is not None and not isinstance(self.result, Result):
            self.result = Result(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnsubscribeResultResponse(JSONRPCResultResponse):
    """
    A successful response for a resources/unsubscribe request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["UnsubscribeResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:UnsubscribeResultResponse"
    class_name: ClassVar[str] = "UnsubscribeResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.UnsubscribeResultResponse

    id: str = None
    jsonrpc: str = None
    result: Optional[Union[dict, Result]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.result is not None and not isinstance(self.result, Result):
            self.result = Result(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreateTaskResultResponse(JSONRPCResultResponse):
    """
    A successful response for a task-augmented request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CreateTaskResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:CreateTaskResultResponse"
    class_name: ClassVar[str] = "CreateTaskResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.CreateTaskResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, CreateTaskResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, CreateTaskResult):
            self.result = CreateTaskResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetTaskResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/get request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetTaskResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:GetTaskResultResponse"
    class_name: ClassVar[str] = "GetTaskResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.GetTaskResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, GetTaskResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, GetTaskResult):
            self.result = GetTaskResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GetTaskPayloadResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/result request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["GetTaskPayloadResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:GetTaskPayloadResultResponse"
    class_name: ClassVar[str] = "GetTaskPayloadResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.GetTaskPayloadResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, GetTaskPayloadResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, GetTaskPayloadResult):
            self.result = GetTaskPayloadResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CancelTaskResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/cancel request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["CancelTaskResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:CancelTaskResultResponse"
    class_name: ClassVar[str] = "CancelTaskResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.CancelTaskResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, CancelTaskResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, CancelTaskResult):
            self.result = CancelTaskResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListTasksResultResponse(JSONRPCResultResponse):
    """
    A successful response for a tasks/list request.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ListTasksResultResponse"]
    class_class_curie: ClassVar[str] = "mcp:ListTasksResultResponse"
    class_name: ClassVar[str] = "ListTasksResultResponse"
    class_model_uri: ClassVar[URIRef] = MCP.ListTasksResultResponse

    id: str = None
    jsonrpc: str = None
    result: Union[dict, ListTasksResult] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, ListTasksResult):
            self.result = ListTasksResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


class ClientNotification(YAMLRoot):
    """
    A union of all notifications that can be sent by a client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ClientNotification"]
    class_class_curie: ClassVar[str] = "mcp:ClientNotification"
    class_name: ClassVar[str] = "ClientNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ClientNotification


class ClientRequest(YAMLRoot):
    """
    A union of all requests that can be sent by a client.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ClientRequest"]
    class_class_curie: ClassVar[str] = "mcp:ClientRequest"
    class_name: ClassVar[str] = "ClientRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ClientRequest


class ClientResult(YAMLRoot):
    """
    A union of all result types that a client can return.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ClientResult"]
    class_class_curie: ClassVar[str] = "mcp:ClientResult"
    class_name: ClassVar[str] = "ClientResult"
    class_model_uri: ClassVar[URIRef] = MCP.ClientResult


class ServerNotification(YAMLRoot):
    """
    A union of all notifications that can be sent by a server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ServerNotification"]
    class_class_curie: ClassVar[str] = "mcp:ServerNotification"
    class_name: ClassVar[str] = "ServerNotification"
    class_model_uri: ClassVar[URIRef] = MCP.ServerNotification


class ServerRequest(YAMLRoot):
    """
    A union of all requests that can be sent by a server.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ServerRequest"]
    class_class_curie: ClassVar[str] = "mcp:ServerRequest"
    class_name: ClassVar[str] = "ServerRequest"
    class_model_uri: ClassVar[URIRef] = MCP.ServerRequest


class ServerResult(YAMLRoot):
    """
    A union of all result types that a server can return.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ServerResult"]
    class_class_curie: ClassVar[str] = "mcp:ServerResult"
    class_name: ClassVar[str] = "ServerResult"
    class_model_uri: ClassVar[URIRef] = MCP.ServerResult


class JSONRPCMessage(YAMLRoot):
    """
    A union of all JSON-RPC message types (requests, notifications, and responses).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JSONRPCMessage"]
    class_class_curie: ClassVar[str] = "mcp:JSONRPCMessage"
    class_name: ClassVar[str] = "JSONRPCMessage"
    class_model_uri: ClassVar[URIRef] = MCP.JSONRPCMessage


class JSONRPCResponse(YAMLRoot):
    """
    A union of all JSON-RPC response types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["JSONRPCResponse"]
    class_class_curie: ClassVar[str] = "mcp:JSONRPCResponse"
    class_name: ClassVar[str] = "JSONRPCResponse"
    class_model_uri: ClassVar[URIRef] = MCP.JSONRPCResponse


class ElicitRequestParams(YAMLRoot):
    """
    A union of all elicitation request parameter types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ElicitRequestParams"]
    class_class_curie: ClassVar[str] = "mcp:ElicitRequestParams"
    class_name: ClassVar[str] = "ElicitRequestParams"
    class_model_uri: ClassVar[URIRef] = MCP.ElicitRequestParams


class EnumSchema(YAMLRoot):
    """
    A union of all enum schema types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["EnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:EnumSchema"
    class_name: ClassVar[str] = "EnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.EnumSchema


class SingleSelectEnumSchema(YAMLRoot):
    """
    A union of single-select enum schema types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SingleSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:SingleSelectEnumSchema"
    class_name: ClassVar[str] = "SingleSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.SingleSelectEnumSchema


class MultiSelectEnumSchema(YAMLRoot):
    """
    A union of multi-select enum schema types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["MultiSelectEnumSchema"]
    class_class_curie: ClassVar[str] = "mcp:MultiSelectEnumSchema"
    class_name: ClassVar[str] = "MultiSelectEnumSchema"
    class_model_uri: ClassVar[URIRef] = MCP.MultiSelectEnumSchema


class PrimitiveSchemaDefinition(YAMLRoot):
    """
    A union of all primitive schema definition types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["PrimitiveSchemaDefinition"]
    class_class_curie: ClassVar[str] = "mcp:PrimitiveSchemaDefinition"
    class_name: ClassVar[str] = "PrimitiveSchemaDefinition"
    class_model_uri: ClassVar[URIRef] = MCP.PrimitiveSchemaDefinition


class ContentBlockVariants(YAMLRoot):
    """
    A union of all content block types. Maps to the vendor schema ContentBlock anyOf definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["ContentBlockVariants"]
    class_class_curie: ClassVar[str] = "mcp:ContentBlockVariants"
    class_name: ClassVar[str] = "ContentBlockVariants"
    class_model_uri: ClassVar[URIRef] = MCP.ContentBlockVariants


class SamplingMessageContentBlock(YAMLRoot):
    """
    A union of content types valid in sampling messages.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MCP["SamplingMessageContentBlock"]
    class_class_curie: ClassVar[str] = "mcp:SamplingMessageContentBlock"
    class_name: ClassVar[str] = "SamplingMessageContentBlock"
    class_model_uri: ClassVar[URIRef] = MCP.SamplingMessageContentBlock


# Enumerations
class Role(EnumDefinitionImpl):
    """
    The sender or recipient of messages and data in a conversation.
    """
    assistant = PermissibleValue(
        text="assistant",
        description="The assistant role.")
    user = PermissibleValue(
        text="user",
        description="The user role.")

    _defn = EnumDefinition(
        name="Role",
        description="The sender or recipient of messages and data in a conversation.",
    )

class LoggingLevel(EnumDefinitionImpl):
    """
    The severity of a log message. Maps to syslog message severities (RFC-5424).
    """
    alert = PermissibleValue(
        text="alert",
        description="Alert severity.")
    critical = PermissibleValue(
        text="critical",
        description="Critical severity.")
    debug = PermissibleValue(
        text="debug",
        description="Debug severity.")
    emergency = PermissibleValue(
        text="emergency",
        description="Emergency severity.")
    error = PermissibleValue(
        text="error",
        description="Error severity.")
    info = PermissibleValue(
        text="info",
        description="Informational severity.")
    notice = PermissibleValue(
        text="notice",
        description="Notice severity.")
    warning = PermissibleValue(
        text="warning",
        description="Warning severity.")

    _defn = EnumDefinition(
        name="LoggingLevel",
        description="The severity of a log message. Maps to syslog message severities (RFC-5424).",
    )

class TaskStatusEnum(EnumDefinitionImpl):
    """
    The status of a task.
    """
    cancelled = PermissibleValue(
        text="cancelled",
        description="Task was cancelled.")
    completed = PermissibleValue(
        text="completed",
        description="Task completed successfully.")
    failed = PermissibleValue(
        text="failed",
        description="Task failed.")
    input_required = PermissibleValue(
        text="input_required",
        description="Task requires additional input.")
    working = PermissibleValue(
        text="working",
        description="Task is currently in progress.")

    _defn = EnumDefinition(
        name="TaskStatusEnum",
        description="The status of a task.",
    )

class IncludeContextEnum(EnumDefinitionImpl):
    """
    Context inclusion mode for sampling requests.
    """
    allServers = PermissibleValue(
        text="allServers",
        description="Include context from all servers.")
    none = PermissibleValue(
        text="none",
        description="Include no context.")
    thisServer = PermissibleValue(
        text="thisServer",
        description="Include context from calling server only.")

    _defn = EnumDefinition(
        name="IncludeContextEnum",
        description="Context inclusion mode for sampling requests.",
    )

class ElicitActionEnum(EnumDefinitionImpl):
    """
    User action in response to an elicitation.
    """
    accept = PermissibleValue(
        text="accept",
        description="User submitted the form/confirmed the action.")
    cancel = PermissibleValue(
        text="cancel",
        description="User dismissed without making an explicit choice.")
    decline = PermissibleValue(
        text="decline",
        description="User explicitly declined the action.")

    _defn = EnumDefinition(
        name="ElicitActionEnum",
        description="User action in response to an elicitation.",
    )

class ToolChoiceModeEnum(EnumDefinitionImpl):
    """
    Controls tool selection behavior for sampling requests.
    """
    auto = PermissibleValue(
        text="auto",
        description="Model decides whether to use tools (default).")
    none = PermissibleValue(
        text="none",
        description="Model MUST NOT use any tools.")
    required = PermissibleValue(
        text="required",
        description="Model MUST use at least one tool before completing.")

    _defn = EnumDefinition(
        name="ToolChoiceModeEnum",
        description="Controls tool selection behavior for sampling requests.",
    )

class TaskSupportEnum(EnumDefinitionImpl):
    """
    Indicates whether a tool supports task-augmented execution.
    """
    forbidden = PermissibleValue(
        text="forbidden",
        description="Tool does not support task-augmented execution (default).")
    optional = PermissibleValue(
        text="optional",
        description="Tool may support task-augmented execution.")
    required = PermissibleValue(
        text="required",
        description="Tool requires task-augmented execution.")

    _defn = EnumDefinition(
        name="TaskSupportEnum",
        description="Indicates whether a tool supports task-augmented execution.",
    )

class IconThemeEnum(EnumDefinitionImpl):
    """
    Theme specifier for an icon.
    """
    dark = PermissibleValue(
        text="dark",
        description="Icon designed for a dark background.")
    light = PermissibleValue(
        text="light",
        description="Icon designed for a light background.")

    _defn = EnumDefinition(
        name="IconThemeEnum",
        description="Theme specifier for an icon.",
    )

class NumberTypeEnum(EnumDefinitionImpl):
    """
    Number type discriminator.
    """
    integer = PermissibleValue(
        text="integer",
        description="Integer type.")
    number = PermissibleValue(
        text="number",
        description="Number type.")

    _defn = EnumDefinition(
        name="NumberTypeEnum",
        description="Number type discriminator.",
    )

class StringFormatEnum(EnumDefinitionImpl):
    """
    String format constraints.
    """
    date = PermissibleValue(
        text="date",
        description="Date format.")
    email = PermissibleValue(
        text="email",
        description="Email format.")
    uri = PermissibleValue(
        text="uri",
        description="URI format.")

    _defn = EnumDefinition(
        name="StringFormatEnum",
        description="String format constraints.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "date-time",
            PermissibleValue(
                text="date-time",
                description="Date-time format."))

# Slots
class slots:
    pass

slots.jsonrpc = Slot(uri=MCP.jsonrpc, name="jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.jsonrpc, domain=None, range=str)

slots.id = Slot(uri=MCP.id, name="id", curie=MCP.curie('id'),
                   model_uri=MCP.id, domain=None, range=Optional[str])

slots.method = Slot(uri=MCP.method, name="method", curie=MCP.curie('method'),
                   model_uri=MCP.method, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.name, domain=None, range=Optional[str])

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=MCP.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=MCP.description, domain=None, range=Optional[str])

slots.uri = Slot(uri=MCP.uri, name="uri", curie=MCP.curie('uri'),
                   model_uri=MCP.uri, domain=None, range=Optional[Union[str, URI]])

slots.mimeType = Slot(uri=MCP.mimeType, name="mimeType", curie=MCP.curie('mimeType'),
                   model_uri=MCP.mimeType, domain=None, range=Optional[str])

slots.type = Slot(uri=MCP.type, name="type", curie=MCP.curie('type'),
                   model_uri=MCP.type, domain=None, range=Optional[str])

slots.text = Slot(uri=MCP.text, name="text", curie=MCP.curie('text'),
                   model_uri=MCP.text, domain=None, range=Optional[str])

slots.data = Slot(uri=MCP.data, name="data", curie=MCP.curie('data'),
                   model_uri=MCP.data, domain=None, range=Optional[str])

slots.default = Slot(uri=MCP.default, name="default", curie=MCP.curie('default'),
                   model_uri=MCP.default, domain=None, range=Optional[object])

slots.enum = Slot(uri=MCP.enum, name="enum", curie=MCP.curie('enum'),
                   model_uri=MCP.enum, domain=None, range=Optional[Union[str, list[str]]])

slots.oneOf = Slot(uri=MCP.oneOf, name="oneOf", curie=MCP.curie('oneOf'),
                   model_uri=MCP.oneOf, domain=None, range=Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]])

slots.items = Slot(uri=MCP.items, name="items", curie=MCP.curie('items'),
                   model_uri=MCP.items, domain=None, range=Optional[Union[dict, SchemaItems]])

slots.blob = Slot(uri=MCP.blob, name="blob", curie=MCP.curie('blob'),
                   model_uri=MCP.blob, domain=None, range=Optional[str])

slots.audience = Slot(uri=MCP.audience, name="audience", curie=MCP.curie('audience'),
                   model_uri=MCP.audience, domain=None, range=Optional[Union[Union[str, "Role"], list[Union[str, "Role"]]]])

slots.priority = Slot(uri=MCP.priority, name="priority", curie=MCP.curie('priority'),
                   model_uri=MCP.priority, domain=None, range=Optional[float])

slots.lastModified = Slot(uri=MCP.lastModified, name="lastModified", curie=MCP.curie('lastModified'),
                   model_uri=MCP.lastModified, domain=None, range=Optional[str])

slots.annotations = Slot(uri=MCP.annotations, name="annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.annotations, domain=None, range=Optional[Union[dict, Annotations]])

slots.content = Slot(uri=MCP.content, name="content", curie=MCP.curie('content'),
                   model_uri=MCP.content, domain=None, range=Optional[Union[dict, ContentBlock]])

slots.isError = Slot(uri=MCP.isError, name="isError", curie=MCP.curie('isError'),
                   model_uri=MCP.isError, domain=None, range=Optional[Union[bool, Bool]])

slots.model = Slot(uri=MCP.model, name="model", curie=MCP.curie('model'),
                   model_uri=MCP.model, domain=None, range=Optional[str])

slots.role = Slot(uri=MCP.role, name="role", curie=MCP.curie('role'),
                   model_uri=MCP.role, domain=None, range=Optional[Union[str, "Role"]])

slots.stopReason = Slot(uri=MCP.stopReason, name="stopReason", curie=MCP.curie('stopReason'),
                   model_uri=MCP.stopReason, domain=None, range=Optional[str])

slots.cursor = Slot(uri=MCP.cursor, name="cursor", curie=MCP.curie('cursor'),
                   model_uri=MCP.cursor, domain=None, range=Optional[str])

slots.nextCursor = Slot(uri=MCP.nextCursor, name="nextCursor", curie=MCP.curie('nextCursor'),
                   model_uri=MCP.nextCursor, domain=None, range=Optional[str])

slots.progress = Slot(uri=MCP.progress, name="progress", curie=MCP.curie('progress'),
                   model_uri=MCP.progress, domain=None, range=Optional[float])

slots.progressToken = Slot(uri=MCP.progressToken, name="progressToken", curie=MCP.curie('progressToken'),
                   model_uri=MCP.progressToken, domain=None, range=Optional[str])

slots.total = Slot(uri=MCP.total, name="total", curie=MCP.curie('total'),
                   model_uri=MCP.total, domain=None, range=Optional[float])

slots.message = Slot(uri=MCP.message, name="message", curie=MCP.curie('message'),
                   model_uri=MCP.message, domain=None, range=Optional[str])

slots.code = Slot(uri=MCP.code, name="code", curie=MCP.curie('code'),
                   model_uri=MCP.code, domain=None, range=Optional[int])

slots.error = Slot(uri=MCP.error, name="error", curie=MCP.curie('error'),
                   model_uri=MCP.error, domain=None, range=Optional[Union[dict, Error]])

slots.taskId = Slot(uri=MCP.taskId, name="taskId", curie=MCP.curie('taskId'),
                   model_uri=MCP.taskId, domain=None, range=Optional[str])

slots.status = Slot(uri=MCP.status, name="status", curie=MCP.curie('status'),
                   model_uri=MCP.status, domain=None, range=Optional[Union[str, "TaskStatusEnum"]])

slots.createdAt = Slot(uri=MCP.createdAt, name="createdAt", curie=MCP.curie('createdAt'),
                   model_uri=MCP.createdAt, domain=None, range=Optional[str])

slots.lastUpdatedAt = Slot(uri=MCP.lastUpdatedAt, name="lastUpdatedAt", curie=MCP.curie('lastUpdatedAt'),
                   model_uri=MCP.lastUpdatedAt, domain=None, range=Optional[str])

slots.ttl = Slot(uri=MCP.ttl, name="ttl", curie=MCP.curie('ttl'),
                   model_uri=MCP.ttl, domain=None, range=Optional[int])

slots.statusMessage = Slot(uri=MCP.statusMessage, name="statusMessage", curie=MCP.curie('statusMessage'),
                   model_uri=MCP.statusMessage, domain=None, range=Optional[str])

slots.pollInterval = Slot(uri=MCP.pollInterval, name="pollInterval", curie=MCP.curie('pollInterval'),
                   model_uri=MCP.pollInterval, domain=None, range=Optional[int])

slots.protocolVersion = Slot(uri=MCP.protocolVersion, name="protocolVersion", curie=MCP.curie('protocolVersion'),
                   model_uri=MCP.protocolVersion, domain=None, range=Optional[str])

slots.capabilities = Slot(uri=MCP.capabilities, name="capabilities", curie=MCP.curie('capabilities'),
                   model_uri=MCP.capabilities, domain=None, range=Optional[str])

slots.instructions = Slot(uri=MCP.instructions, name="instructions", curie=MCP.curie('instructions'),
                   model_uri=MCP.instructions, domain=None, range=Optional[str])

slots.experimental = Slot(uri=MCP.experimental, name="experimental", curie=MCP.curie('experimental'),
                   model_uri=MCP.experimental, domain=None, range=Optional[object])

slots.extensions = Slot(uri=MCP.extensions, name="extensions", curie=MCP.curie('extensions'),
                   model_uri=MCP.extensions, domain=None, range=Optional[object])

slots.elicitation = Slot(uri=MCP.elicitation, name="elicitation", curie=MCP.curie('elicitation'),
                   model_uri=MCP.elicitation, domain=None, range=Optional[object])

slots.sampling = Slot(uri=MCP.sampling, name="sampling", curie=MCP.curie('sampling'),
                   model_uri=MCP.sampling, domain=None, range=Optional[object])

slots.inputSchema = Slot(uri=MCP.inputSchema, name="inputSchema", curie=MCP.curie('inputSchema'),
                   model_uri=MCP.inputSchema, domain=None, range=Optional[Union[dict, JsonSchema]])

slots.outputSchema = Slot(uri=MCP.outputSchema, name="outputSchema", curie=MCP.curie('outputSchema'),
                   model_uri=MCP.outputSchema, domain=None, range=Optional[Union[dict, JsonSchema]])

slots.uriTemplate = Slot(uri=MCP.uriTemplate, name="uriTemplate", curie=MCP.curie('uriTemplate'),
                   model_uri=MCP.uriTemplate, domain=None, range=Optional[str])

slots.size = Slot(uri=MCP.size, name="size", curie=MCP.curie('size'),
                   model_uri=MCP.size, domain=None, range=Optional[int])

slots.level = Slot(uri=MCP.level, name="level", curie=MCP.curie('level'),
                   model_uri=MCP.level, domain=None, range=Optional[Union[str, "LoggingLevel"]])

slots.logger = Slot(uri=MCP.logger, name="logger", curie=MCP.curie('logger'),
                   model_uri=MCP.logger, domain=None, range=Optional[str])

slots.src = Slot(uri=MCP.src, name="src", curie=MCP.curie('src'),
                   model_uri=MCP.src, domain=None, range=Optional[Union[str, URI]])

slots.sizes = Slot(uri=MCP.sizes, name="sizes", curie=MCP.curie('sizes'),
                   model_uri=MCP.sizes, domain=None, range=Optional[Union[str, list[str]]])

slots.theme = Slot(uri=MCP.theme, name="theme", curie=MCP.curie('theme'),
                   model_uri=MCP.theme, domain=None, range=Optional[Union[str, "IconThemeEnum"]])

slots.arguments = Slot(uri=MCP.arguments, name="arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.arguments, domain=None, range=Optional[Union[dict, ArgumentMap]])

slots.required_field = Slot(uri=MCP.required_field, name="required_field", curie=MCP.curie('required_field'),
                   model_uri=MCP.required_field, domain=None, range=Optional[Union[bool, Bool]])

slots.required = Slot(uri=MCP.required, name="required", curie=MCP.curie('required'),
                   model_uri=MCP.required, domain=None, range=Optional[Union[bool, Bool]])

slots.maxTokens = Slot(uri=MCP.maxTokens, name="maxTokens", curie=MCP.curie('maxTokens'),
                   model_uri=MCP.maxTokens, domain=None, range=Optional[int])

slots.systemPrompt = Slot(uri=MCP.systemPrompt, name="systemPrompt", curie=MCP.curie('systemPrompt'),
                   model_uri=MCP.systemPrompt, domain=None, range=Optional[str])

slots.temperature = Slot(uri=MCP.temperature, name="temperature", curie=MCP.curie('temperature'),
                   model_uri=MCP.temperature, domain=None, range=Optional[float])

slots.includeContext = Slot(uri=MCP.includeContext, name="includeContext", curie=MCP.curie('includeContext'),
                   model_uri=MCP.includeContext, domain=None, range=Optional[Union[str, "IncludeContextEnum"]])

slots.modelPreferences = Slot(uri=MCP.modelPreferences, name="modelPreferences", curie=MCP.curie('modelPreferences'),
                   model_uri=MCP.modelPreferences, domain=None, range=Optional[Union[dict, ModelPreferences]])

slots.toolChoice = Slot(uri=MCP.toolChoice, name="toolChoice", curie=MCP.curie('toolChoice'),
                   model_uri=MCP.toolChoice, domain=None, range=Optional[Union[dict, ToolChoice]])

slots.action = Slot(uri=MCP.action, name="action", curie=MCP.curie('action'),
                   model_uri=MCP.action, domain=None, range=Optional[Union[str, "ElicitActionEnum"]])

slots.requestedSchema = Slot(uri=MCP.requestedSchema, name="requestedSchema", curie=MCP.curie('requestedSchema'),
                   model_uri=MCP.requestedSchema, domain=None, range=Optional[Union[dict, JsonSchema]])

slots.elicitationId = Slot(uri=MCP.elicitationId, name="elicitationId", curie=MCP.curie('elicitationId'),
                   model_uri=MCP.elicitationId, domain=None, range=Optional[str])

slots.url = Slot(uri=MCP.url, name="url", curie=MCP.curie('url'),
                   model_uri=MCP.url, domain=None, range=Optional[Union[str, URI]])

slots.mode = Slot(uri=MCP.mode, name="mode", curie=MCP.curie('mode'),
                   model_uri=MCP.mode, domain=None, range=Optional[str])

slots.version = Slot(uri=MCP.version, name="version", curie=MCP.curie('version'),
                   model_uri=MCP.version, domain=None, range=Optional[str])

slots.websiteUrl = Slot(uri=MCP.websiteUrl, name="websiteUrl", curie=MCP.curie('websiteUrl'),
                   model_uri=MCP.websiteUrl, domain=None, range=Optional[Union[str, URI]])

slots.default_value = Slot(uri=MCP.default_value, name="default_value", curie=MCP.curie('default_value'),
                   model_uri=MCP.default_value, domain=None, range=Optional[str])

slots.schemaUri = Slot(uri=MCP.schemaUri, name="schemaUri", curie=MCP.curie('schemaUri'),
                   model_uri=MCP.schemaUri, domain=None, range=Optional[str])

slots.properties = Slot(uri=MCP.properties, name="properties", curie=MCP.curie('properties'),
                   model_uri=MCP.properties, domain=None, range=Optional[Union[dict, SchemaProperties]])

slots.required_list = Slot(uri=MCP.required_list, name="required_list", curie=MCP.curie('required_list'),
                   model_uri=MCP.required_list, domain=None, range=Optional[Union[str, list[str]]])

slots.additionalProperties = Slot(uri=MCP.additionalProperties, name="additionalProperties", curie=MCP.curie('additionalProperties'),
                   model_uri=MCP.additionalProperties, domain=None, range=Optional[Union[bool, Bool]])

slots.anyOf = Slot(uri=MCP.anyOf, name="anyOf", curie=MCP.curie('anyOf'),
                   model_uri=MCP.anyOf, domain=None, range=Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]])

slots.const = Slot(uri=MCP.const, name="const", curie=MCP.curie('const'),
                   model_uri=MCP.const, domain=None, range=Optional[str])

slots.city = Slot(uri=MCP.city, name="city", curie=MCP.curie('city'),
                   model_uri=MCP.city, domain=None, range=Optional[str])

slots.location = Slot(uri=MCP.location, name="location", curie=MCP.curie('location'),
                   model_uri=MCP.location, domain=None, range=Optional[str])

slots.language = Slot(uri=MCP.language, name="language", curie=MCP.curie('language'),
                   model_uri=MCP.language, domain=None, range=Optional[str])

slots.framework = Slot(uri=MCP.framework, name="framework", curie=MCP.curie('framework'),
                   model_uri=MCP.framework, domain=None, range=Optional[str])

slots.email = Slot(uri=MCP.email, name="email", curie=MCP.curie('email'),
                   model_uri=MCP.email, domain=None, range=Optional[str])

slots.age = Slot(uri=MCP.age, name="age", curie=MCP.curie('age'),
                   model_uri=MCP.age, domain=None, range=Optional[int])

slots.a = Slot(uri=MCP.a, name="a", curie=MCP.curie('a'),
                   model_uri=MCP.a, domain=None, range=Optional[Union[dict, JsonSchema]])

slots.b = Slot(uri=MCP.b, name="b", curie=MCP.curie('b'),
                   model_uri=MCP.b, domain=None, range=Optional[Union[dict, JsonSchema]])

slots.conditions = Slot(uri=MCP.conditions, name="conditions", curie=MCP.curie('conditions'),
                   model_uri=MCP.conditions, domain=None, range=Optional[str])

slots.humidity = Slot(uri=MCP.humidity, name="humidity", curie=MCP.curie('humidity'),
                   model_uri=MCP.humidity, domain=None, range=Optional[float])

slots.host = Slot(uri=MCP.host, name="host", curie=MCP.curie('host'),
                   model_uri=MCP.host, domain=None, range=Optional[str])

slots.port = Slot(uri=MCP.port, name="port", curie=MCP.curie('port'),
                   model_uri=MCP.port, domain=None, range=Optional[int])

slots.details = Slot(uri=MCP.details, name="details", curie=MCP.curie('details'),
                   model_uri=MCP.details, domain=None, range=Optional[Union[dict, LogDetails]])

slots.requests = Slot(uri=MCP.requests, name="requests", curie=MCP.curie('requests'),
                   model_uri=MCP.requests, domain=None, range=Optional[Union[dict, TaskRequestCapabilities]])

slots.apps_extension = Slot(uri=MCP.apps_extension, name="apps_extension", curie=MCP.curie('apps_extension'),
                   model_uri=MCP.apps_extension, domain=None, range=Optional[Union[dict, ExtensionAppCapability]])

slots.mimeTypes = Slot(uri=MCP.mimeTypes, name="mimeTypes", curie=MCP.curie('mimeTypes'),
                   model_uri=MCP.mimeTypes, domain=None, range=Optional[Union[str, list[str]]])

slots.elicitations = Slot(uri=MCP.elicitations, name="elicitations", curie=MCP.curie('elicitations'),
                   model_uri=MCP.elicitations, domain=None, range=Optional[Union[Union[dict, URLElicitation], list[Union[dict, URLElicitation]]]])

slots.format = Slot(uri=MCP.format, name="format", curie=MCP.curie('format'),
                   model_uri=MCP.format, domain=None, range=Optional[Union[str, "StringFormatEnum"]])

slots.minimum = Slot(uri=MCP.minimum, name="minimum", curie=MCP.curie('minimum'),
                   model_uri=MCP.minimum, domain=None, range=Optional[int])

slots.maximum = Slot(uri=MCP.maximum, name="maximum", curie=MCP.curie('maximum'),
                   model_uri=MCP.maximum, domain=None, range=Optional[int])

slots.minLength = Slot(uri=MCP.minLength, name="minLength", curie=MCP.curie('minLength'),
                   model_uri=MCP.minLength, domain=None, range=Optional[int])

slots.maxLength = Slot(uri=MCP.maxLength, name="maxLength", curie=MCP.curie('maxLength'),
                   model_uri=MCP.maxLength, domain=None, range=Optional[int])

slots.enum_values = Slot(uri=MCP.enum_values, name="enum_values", curie=MCP.curie('enum_values'),
                   model_uri=MCP.enum_values, domain=None, range=Optional[Union[str, list[str]]])

slots.enumNames = Slot(uri=MCP.enumNames, name="enumNames", curie=MCP.curie('enumNames'),
                   model_uri=MCP.enumNames, domain=None, range=Optional[Union[str, list[str]]])

slots.minItems = Slot(uri=MCP.minItems, name="minItems", curie=MCP.curie('minItems'),
                   model_uri=MCP.minItems, domain=None, range=Optional[int])

slots.maxItems = Slot(uri=MCP.maxItems, name="maxItems", curie=MCP.curie('maxItems'),
                   model_uri=MCP.maxItems, domain=None, range=Optional[int])

slots.destructiveHint = Slot(uri=MCP.destructiveHint, name="destructiveHint", curie=MCP.curie('destructiveHint'),
                   model_uri=MCP.destructiveHint, domain=None, range=Optional[Union[bool, Bool]])

slots.idempotentHint = Slot(uri=MCP.idempotentHint, name="idempotentHint", curie=MCP.curie('idempotentHint'),
                   model_uri=MCP.idempotentHint, domain=None, range=Optional[Union[bool, Bool]])

slots.openWorldHint = Slot(uri=MCP.openWorldHint, name="openWorldHint", curie=MCP.curie('openWorldHint'),
                   model_uri=MCP.openWorldHint, domain=None, range=Optional[Union[bool, Bool]])

slots.readOnlyHint = Slot(uri=MCP.readOnlyHint, name="readOnlyHint", curie=MCP.curie('readOnlyHint'),
                   model_uri=MCP.readOnlyHint, domain=None, range=Optional[Union[bool, Bool]])

slots.toolUseId = Slot(uri=MCP.toolUseId, name="toolUseId", curie=MCP.curie('toolUseId'),
                   model_uri=MCP.toolUseId, domain=None, range=Optional[str])

slots.input = Slot(uri=MCP.input, name="input", curie=MCP.curie('input'),
                   model_uri=MCP.input, domain=None, range=Optional[Union[dict, ToolInput]])

slots.structuredContent = Slot(uri=MCP.structuredContent, name="structuredContent", curie=MCP.curie('structuredContent'),
                   model_uri=MCP.structuredContent, domain=None, range=Optional[Union[dict, StructuredContentData]])

slots.reason = Slot(uri=MCP.reason, name="reason", curie=MCP.curie('reason'),
                   model_uri=MCP.reason, domain=None, range=Optional[str])

slots.requestId = Slot(uri=MCP.requestId, name="requestId", curie=MCP.curie('requestId'),
                   model_uri=MCP.requestId, domain=None, range=Optional[str])

slots.hasMore = Slot(uri=MCP.hasMore, name="hasMore", curie=MCP.curie('hasMore'),
                   model_uri=MCP.hasMore, domain=None, range=Optional[Union[bool, Bool]])

slots.values = Slot(uri=MCP.values, name="values", curie=MCP.curie('values'),
                   model_uri=MCP.values, domain=None, range=Optional[Union[str, list[str]]])

slots.value = Slot(uri=MCP.value, name="value", curie=MCP.curie('value'),
                   model_uri=MCP.value, domain=None, range=Optional[str])

slots.listChanged = Slot(uri=MCP.listChanged, name="listChanged", curie=MCP.curie('listChanged'),
                   model_uri=MCP.listChanged, domain=None, range=Optional[Union[bool, Bool]])

slots.subscribe = Slot(uri=MCP.subscribe, name="subscribe", curie=MCP.curie('subscribe'),
                   model_uri=MCP.subscribe, domain=None, range=Optional[Union[bool, Bool]])

slots.icons = Slot(uri=MCP.icons, name="icons", curie=MCP.curie('icons'),
                   model_uri=MCP.icons, domain=None, range=Optional[Union[Union[dict, Icon], list[Union[dict, Icon]]]])

slots.costPriority = Slot(uri=MCP.costPriority, name="costPriority", curie=MCP.curie('costPriority'),
                   model_uri=MCP.costPriority, domain=None, range=Optional[float])

slots.intelligencePriority = Slot(uri=MCP.intelligencePriority, name="intelligencePriority", curie=MCP.curie('intelligencePriority'),
                   model_uri=MCP.intelligencePriority, domain=None, range=Optional[float])

slots.speedPriority = Slot(uri=MCP.speedPriority, name="speedPriority", curie=MCP.curie('speedPriority'),
                   model_uri=MCP.speedPriority, domain=None, range=Optional[float])

slots.stopSequences = Slot(uri=MCP.stopSequences, name="stopSequences", curie=MCP.curie('stopSequences'),
                   model_uri=MCP.stopSequences, domain=None, range=Optional[Union[str, list[str]]])

slots.task = Slot(uri=MCP.task, name="task", curie=MCP.curie('task'),
                   model_uri=MCP.task, domain=None, range=Optional[Union[dict, Task]])

slots.taskSupport = Slot(uri=MCP.taskSupport, name="taskSupport", curie=MCP.curie('taskSupport'),
                   model_uri=MCP.taskSupport, domain=None, range=Optional[Union[str, "TaskSupportEnum"]])

slots._meta = Slot(uri=MCP._meta, name="_meta", curie=MCP.curie('_meta'),
                   model_uri=MCP._meta, domain=None, range=Optional[Union[dict, MetaObject]])

slots.resource = Slot(uri=MCP.resource, name="resource", curie=MCP.curie('resource'),
                   model_uri=MCP.resource, domain=None, range=Optional[Union[dict, ResourceContents]])

slots.params = Slot(uri=MCP.params, name="params", curie=MCP.curie('params'),
                   model_uri=MCP.params, domain=None, range=Optional[str])

slots.result = Slot(uri=MCP.result, name="result", curie=MCP.curie('result'),
                   model_uri=MCP.result, domain=None, range=Optional[Union[dict, Result]])

slots.execution = Slot(uri=MCP.execution, name="execution", curie=MCP.curie('execution'),
                   model_uri=MCP.execution, domain=None, range=Optional[Union[dict, ToolExecution]])

slots.hints = Slot(uri=MCP.hints, name="hints", curie=MCP.curie('hints'),
                   model_uri=MCP.hints, domain=None, range=Optional[Union[Union[dict, ModelHint], list[Union[dict, ModelHint]]]])

slots.messages = Slot(uri=MCP.messages, name="messages", curie=MCP.curie('messages'),
                   model_uri=MCP.messages, domain=None, range=Optional[Union[Union[dict, SamplingMessage], list[Union[dict, SamplingMessage]]]])

slots.prompts = Slot(uri=MCP.prompts, name="prompts", curie=MCP.curie('prompts'),
                   model_uri=MCP.prompts, domain=None, range=Optional[Union[Union[dict, Prompt], list[Union[dict, Prompt]]]])

slots.resources = Slot(uri=MCP.resources, name="resources", curie=MCP.curie('resources'),
                   model_uri=MCP.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.resourceTemplates = Slot(uri=MCP.resourceTemplates, name="resourceTemplates", curie=MCP.curie('resourceTemplates'),
                   model_uri=MCP.resourceTemplates, domain=None, range=Optional[Union[Union[dict, ResourceTemplate], list[Union[dict, ResourceTemplate]]]])

slots.contents = Slot(uri=MCP.contents, name="contents", curie=MCP.curie('contents'),
                   model_uri=MCP.contents, domain=None, range=Optional[Union[Union[dict, ResourceContents], list[Union[dict, ResourceContents]]]])

slots.tools = Slot(uri=MCP.tools, name="tools", curie=MCP.curie('tools'),
                   model_uri=MCP.tools, domain=None, range=Optional[Union[Union[dict, Tool], list[Union[dict, Tool]]]])

slots.roots = Slot(uri=MCP.roots, name="roots", curie=MCP.curie('roots'),
                   model_uri=MCP.roots, domain=None, range=Optional[Union[Union[dict, Root], list[Union[dict, Root]]]])

slots.tasks = Slot(uri=MCP.tasks, name="tasks", curie=MCP.curie('tasks'),
                   model_uri=MCP.tasks, domain=None, range=Optional[Union[Union[dict, Task], list[Union[dict, Task]]]])

slots.completion = Slot(uri=MCP.completion, name="completion", curie=MCP.curie('completion'),
                   model_uri=MCP.completion, domain=None, range=Optional[Union[dict, CompletionData]])

slots.clientInfo = Slot(uri=MCP.clientInfo, name="clientInfo", curie=MCP.curie('clientInfo'),
                   model_uri=MCP.clientInfo, domain=None, range=Optional[Union[dict, Implementation]])

slots.serverInfo = Slot(uri=MCP.serverInfo, name="serverInfo", curie=MCP.curie('serverInfo'),
                   model_uri=MCP.serverInfo, domain=None, range=Optional[Union[dict, Implementation]])

slots.argument = Slot(uri=MCP.argument, name="argument", curie=MCP.curie('argument'),
                   model_uri=MCP.argument, domain=None, range=Optional[Union[dict, CompletionArgument]])

slots.ref = Slot(uri=MCP.ref, name="ref", curie=MCP.curie('ref'),
                   model_uri=MCP.ref, domain=None, range=Optional[Union[dict, PromptReference]])

slots.context = Slot(uri=MCP.context, name="context", curie=MCP.curie('context'),
                   model_uri=MCP.context, domain=None, range=Optional[Union[dict, CompletionContext]])

slots.Error_code = Slot(uri=MCP.code, name="Error_code", curie=MCP.curie('code'),
                   model_uri=MCP.Error_code, domain=Error, range=int)

slots.Error_data = Slot(uri=MCP.data, name="Error_data", curie=MCP.curie('data'),
                   model_uri=MCP.Error_data, domain=Error, range=Optional[Union[dict, "ErrorData"]])

slots.Error_message = Slot(uri=MCP.message, name="Error_message", curie=MCP.curie('message'),
                   model_uri=MCP.Error_message, domain=Error, range=str)

slots.Icon_src = Slot(uri=MCP.src, name="Icon_src", curie=MCP.curie('src'),
                   model_uri=MCP.Icon_src, domain=Icon, range=Union[str, URI])

slots.Implementation_name = Slot(uri=SCHEMA.name, name="Implementation_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.Implementation_name, domain=Implementation, range=str)

slots.Implementation_version = Slot(uri=MCP.version, name="Implementation_version", curie=MCP.curie('version'),
                   model_uri=MCP.Implementation_version, domain=Implementation, range=str)

slots.TextContent_text = Slot(uri=MCP.text, name="TextContent_text", curie=MCP.curie('text'),
                   model_uri=MCP.TextContent_text, domain=TextContent, range=str)

slots.TextContent_type = Slot(uri=MCP.type, name="TextContent_type", curie=MCP.curie('type'),
                   model_uri=MCP.TextContent_type, domain=TextContent, range=str)

slots.ImageContent_data = Slot(uri=MCP.data, name="ImageContent_data", curie=MCP.curie('data'),
                   model_uri=MCP.ImageContent_data, domain=ImageContent, range=str)

slots.ImageContent_mimeType = Slot(uri=MCP.mimeType, name="ImageContent_mimeType", curie=MCP.curie('mimeType'),
                   model_uri=MCP.ImageContent_mimeType, domain=ImageContent, range=str)

slots.ImageContent_type = Slot(uri=MCP.type, name="ImageContent_type", curie=MCP.curie('type'),
                   model_uri=MCP.ImageContent_type, domain=ImageContent, range=str)

slots.AudioContent_data = Slot(uri=MCP.data, name="AudioContent_data", curie=MCP.curie('data'),
                   model_uri=MCP.AudioContent_data, domain=AudioContent, range=str)

slots.AudioContent_mimeType = Slot(uri=MCP.mimeType, name="AudioContent_mimeType", curie=MCP.curie('mimeType'),
                   model_uri=MCP.AudioContent_mimeType, domain=AudioContent, range=str)

slots.AudioContent_type = Slot(uri=MCP.type, name="AudioContent_type", curie=MCP.curie('type'),
                   model_uri=MCP.AudioContent_type, domain=AudioContent, range=str)

slots.EmbeddedResource_resource = Slot(uri=MCP.resource, name="EmbeddedResource_resource", curie=MCP.curie('resource'),
                   model_uri=MCP.EmbeddedResource_resource, domain=EmbeddedResource, range=Union[dict, "ResourceContents"])

slots.EmbeddedResource_type = Slot(uri=MCP.type, name="EmbeddedResource_type", curie=MCP.curie('type'),
                   model_uri=MCP.EmbeddedResource_type, domain=EmbeddedResource, range=str)

slots.ResourceLink_name = Slot(uri=SCHEMA.name, name="ResourceLink_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.ResourceLink_name, domain=ResourceLink, range=str)

slots.ResourceLink_uri = Slot(uri=MCP.uri, name="ResourceLink_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.ResourceLink_uri, domain=ResourceLink, range=Union[str, URI])

slots.ResourceLink_type = Slot(uri=MCP.type, name="ResourceLink_type", curie=MCP.curie('type'),
                   model_uri=MCP.ResourceLink_type, domain=ResourceLink, range=str)

slots.ToolUseContent_id = Slot(uri=MCP.id, name="ToolUseContent_id", curie=MCP.curie('id'),
                   model_uri=MCP.ToolUseContent_id, domain=ToolUseContent, range=str)

slots.ToolUseContent_type = Slot(uri=MCP.type, name="ToolUseContent_type", curie=MCP.curie('type'),
                   model_uri=MCP.ToolUseContent_type, domain=ToolUseContent, range=str)

slots.ToolUseContent_name = Slot(uri=SCHEMA.name, name="ToolUseContent_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.ToolUseContent_name, domain=ToolUseContent, range=str)

slots.ToolUseContent_input = Slot(uri=MCP.input, name="ToolUseContent_input", curie=MCP.curie('input'),
                   model_uri=MCP.ToolUseContent_input, domain=ToolUseContent, range=Union[dict, "ToolInput"])

slots.ToolResultContent_content = Slot(uri=MCP.content, name="ToolResultContent_content", curie=MCP.curie('content'),
                   model_uri=MCP.ToolResultContent_content, domain=ToolResultContent, range=Union[Union[dict, ContentBlock], list[Union[dict, ContentBlock]]])

slots.ToolResultContent_type = Slot(uri=MCP.type, name="ToolResultContent_type", curie=MCP.curie('type'),
                   model_uri=MCP.ToolResultContent_type, domain=ToolResultContent, range=str)

slots.ToolResultContent_toolUseId = Slot(uri=MCP.toolUseId, name="ToolResultContent_toolUseId", curie=MCP.curie('toolUseId'),
                   model_uri=MCP.ToolResultContent_toolUseId, domain=ToolResultContent, range=str)

slots.ResourceContents_uri = Slot(uri=MCP.uri, name="ResourceContents_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.ResourceContents_uri, domain=ResourceContents, range=Union[str, URI])

slots.TextResourceContents_uri = Slot(uri=MCP.uri, name="TextResourceContents_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.TextResourceContents_uri, domain=TextResourceContents, range=Union[str, URI])

slots.TextResourceContents_text = Slot(uri=MCP.text, name="TextResourceContents_text", curie=MCP.curie('text'),
                   model_uri=MCP.TextResourceContents_text, domain=TextResourceContents, range=str)

slots.BlobResourceContents_uri = Slot(uri=MCP.uri, name="BlobResourceContents_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.BlobResourceContents_uri, domain=BlobResourceContents, range=Union[str, URI])

slots.BlobResourceContents_blob = Slot(uri=MCP.blob, name="BlobResourceContents_blob", curie=MCP.curie('blob'),
                   model_uri=MCP.BlobResourceContents_blob, domain=BlobResourceContents, range=str)

slots.Resource_name = Slot(uri=SCHEMA.name, name="Resource_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.Resource_name, domain=Resource, range=str)

slots.Resource_uri = Slot(uri=MCP.uri, name="Resource_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.Resource_uri, domain=Resource, range=Union[str, URI])

slots.ResourceTemplate_name = Slot(uri=SCHEMA.name, name="ResourceTemplate_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.ResourceTemplate_name, domain=ResourceTemplate, range=str)

slots.ResourceTemplate_uriTemplate = Slot(uri=MCP.uriTemplate, name="ResourceTemplate_uriTemplate", curie=MCP.curie('uriTemplate'),
                   model_uri=MCP.ResourceTemplate_uriTemplate, domain=ResourceTemplate, range=str)

slots.Root_uri = Slot(uri=MCP.uri, name="Root_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.Root_uri, domain=Root, range=Union[str, URI])

slots.PromptArgument_name = Slot(uri=SCHEMA.name, name="PromptArgument_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.PromptArgument_name, domain=PromptArgument, range=str)

slots.Prompt_arguments = Slot(uri=MCP.arguments, name="Prompt_arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.Prompt_arguments, domain=Prompt, range=Optional[Union[Union[dict, PromptArgument], list[Union[dict, PromptArgument]]]])

slots.Prompt_name = Slot(uri=SCHEMA.name, name="Prompt_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.Prompt_name, domain=Prompt, range=str)

slots.PromptMessage_content = Slot(uri=MCP.content, name="PromptMessage_content", curie=MCP.curie('content'),
                   model_uri=MCP.PromptMessage_content, domain=PromptMessage, range=Union[dict, ContentBlock])

slots.PromptMessage_role = Slot(uri=MCP.role, name="PromptMessage_role", curie=MCP.curie('role'),
                   model_uri=MCP.PromptMessage_role, domain=PromptMessage, range=Union[str, "Role"])

slots.PromptReference_name = Slot(uri=SCHEMA.name, name="PromptReference_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.PromptReference_name, domain=PromptReference, range=str)

slots.PromptReference_type = Slot(uri=MCP.type, name="PromptReference_type", curie=MCP.curie('type'),
                   model_uri=MCP.PromptReference_type, domain=PromptReference, range=str)

slots.ResourceTemplateReference_type = Slot(uri=MCP.type, name="ResourceTemplateReference_type", curie=MCP.curie('type'),
                   model_uri=MCP.ResourceTemplateReference_type, domain=ResourceTemplateReference, range=str)

slots.ResourceTemplateReference_uri = Slot(uri=MCP.uri, name="ResourceTemplateReference_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.ResourceTemplateReference_uri, domain=ResourceTemplateReference, range=Union[str, URI])

slots.ToolChoice_mode = Slot(uri=MCP.mode, name="ToolChoice_mode", curie=MCP.curie('mode'),
                   model_uri=MCP.ToolChoice_mode, domain=ToolChoice, range=Optional[Union[str, "ToolChoiceModeEnum"]])

slots.CompletionArgument_name = Slot(uri=SCHEMA.name, name="CompletionArgument_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.CompletionArgument_name, domain=CompletionArgument, range=str)

slots.CompletionArgument_value = Slot(uri=MCP.value, name="CompletionArgument_value", curie=MCP.curie('value'),
                   model_uri=MCP.CompletionArgument_value, domain=CompletionArgument, range=str)

slots.CompletionData_values = Slot(uri=MCP.values, name="CompletionData_values", curie=MCP.curie('values'),
                   model_uri=MCP.CompletionData_values, domain=CompletionData, range=Union[str, list[str]])

slots.EnumOption_const = Slot(uri=MCP.const, name="EnumOption_const", curie=MCP.curie('const'),
                   model_uri=MCP.EnumOption_const, domain=EnumOption, range=str)

slots.SchemaProperties_name = Slot(uri=SCHEMA.name, name="SchemaProperties_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.SchemaProperties_name, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_email = Slot(uri=MCP.email, name="SchemaProperties_email", curie=MCP.curie('email'),
                   model_uri=MCP.SchemaProperties_email, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_age = Slot(uri=MCP.age, name="SchemaProperties_age", curie=MCP.curie('age'),
                   model_uri=MCP.SchemaProperties_age, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_city = Slot(uri=MCP.city, name="SchemaProperties_city", curie=MCP.curie('city'),
                   model_uri=MCP.SchemaProperties_city, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_location = Slot(uri=MCP.location, name="SchemaProperties_location", curie=MCP.curie('location'),
                   model_uri=MCP.SchemaProperties_location, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_a = Slot(uri=MCP.a, name="SchemaProperties_a", curie=MCP.curie('a'),
                   model_uri=MCP.SchemaProperties_a, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_b = Slot(uri=MCP.b, name="SchemaProperties_b", curie=MCP.curie('b'),
                   model_uri=MCP.SchemaProperties_b, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_temperature = Slot(uri=MCP.temperature, name="SchemaProperties_temperature", curie=MCP.curie('temperature'),
                   model_uri=MCP.SchemaProperties_temperature, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_conditions = Slot(uri=MCP.conditions, name="SchemaProperties_conditions", curie=MCP.curie('conditions'),
                   model_uri=MCP.SchemaProperties_conditions, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.SchemaProperties_humidity = Slot(uri=MCP.humidity, name="SchemaProperties_humidity", curie=MCP.curie('humidity'),
                   model_uri=MCP.SchemaProperties_humidity, domain=SchemaProperties, range=Optional[Union[dict, JsonSchema]])

slots.LogData_error = Slot(uri=MCP.error, name="LogData_error", curie=MCP.curie('error'),
                   model_uri=MCP.LogData_error, domain=LogData, range=Optional[str])

slots.LogData_details = Slot(uri=MCP.details, name="LogData_details", curie=MCP.curie('details'),
                   model_uri=MCP.LogData_details, domain=LogData, range=Optional[Union[dict, LogDetails]])

slots.ErrorData_elicitations = Slot(uri=MCP.elicitations, name="ErrorData_elicitations", curie=MCP.curie('elicitations'),
                   model_uri=MCP.ErrorData_elicitations, domain=ErrorData, range=Optional[Union[Union[dict, "URLElicitation"], list[Union[dict, "URLElicitation"]]]])

slots.TaskRequestCapabilities_elicitation = Slot(uri=MCP.elicitation, name="TaskRequestCapabilities_elicitation", curie=MCP.curie('elicitation'),
                   model_uri=MCP.TaskRequestCapabilities_elicitation, domain=TaskRequestCapabilities, range=Optional[Union[dict, ElicitationCapability]])

slots.TaskRequestCapabilities_sampling = Slot(uri=MCP.sampling, name="TaskRequestCapabilities_sampling", curie=MCP.curie('sampling'),
                   model_uri=MCP.TaskRequestCapabilities_sampling, domain=TaskRequestCapabilities, range=Optional[Union[dict, SamplingCapability]])

slots.TaskRequestCapabilities_tools = Slot(uri=MCP.tools, name="TaskRequestCapabilities_tools", curie=MCP.curie('tools'),
                   model_uri=MCP.TaskRequestCapabilities_tools, domain=TaskRequestCapabilities, range=Optional[Union[Union[dict, ToolsCapability], list[Union[dict, ToolsCapability]]]])

slots.TasksCapability_requests = Slot(uri=MCP.requests, name="TasksCapability_requests", curie=MCP.curie('requests'),
                   model_uri=MCP.TasksCapability_requests, domain=TasksCapability, range=Optional[Union[dict, TaskRequestCapabilities]])

slots.ExtensionsCapability_apps_extension = Slot(uri=MCP.apps_extension, name="ExtensionsCapability_apps_extension", curie=MCP.curie('apps_extension'),
                   model_uri=MCP.ExtensionsCapability_apps_extension, domain=ExtensionsCapability, range=Optional[Union[dict, "ExtensionAppCapability"]])

slots.ExtensionAppCapability_mimeTypes = Slot(uri=MCP.mimeTypes, name="ExtensionAppCapability_mimeTypes", curie=MCP.curie('mimeTypes'),
                   model_uri=MCP.ExtensionAppCapability_mimeTypes, domain=ExtensionAppCapability, range=Optional[Union[str, list[str]]])

slots.Tool_annotations = Slot(uri=MCP.annotations, name="Tool_annotations", curie=MCP.curie('annotations'),
                   model_uri=MCP.Tool_annotations, domain=Tool, range=Optional[Union[dict, ToolAnnotations]])

slots.Tool_execution = Slot(uri=MCP.execution, name="Tool_execution", curie=MCP.curie('execution'),
                   model_uri=MCP.Tool_execution, domain=Tool, range=Optional[Union[dict, ToolExecution]])

slots.Tool_name = Slot(uri=SCHEMA.name, name="Tool_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.Tool_name, domain=Tool, range=str)

slots.Tool_inputSchema = Slot(uri=MCP.inputSchema, name="Tool_inputSchema", curie=MCP.curie('inputSchema'),
                   model_uri=MCP.Tool_inputSchema, domain=Tool, range=Union[dict, JsonSchema])

slots.SamplingMessage_content = Slot(uri=MCP.content, name="SamplingMessage_content", curie=MCP.curie('content'),
                   model_uri=MCP.SamplingMessage_content, domain=SamplingMessage, range=Union[dict, ContentBlock])

slots.SamplingMessage_role = Slot(uri=MCP.role, name="SamplingMessage_role", curie=MCP.curie('role'),
                   model_uri=MCP.SamplingMessage_role, domain=SamplingMessage, range=Union[str, "Role"])

slots.Task_taskId = Slot(uri=MCP.taskId, name="Task_taskId", curie=MCP.curie('taskId'),
                   model_uri=MCP.Task_taskId, domain=Task, range=str)

slots.Task_status = Slot(uri=MCP.status, name="Task_status", curie=MCP.curie('status'),
                   model_uri=MCP.Task_status, domain=Task, range=Union[str, "TaskStatusEnum"])

slots.Task_createdAt = Slot(uri=MCP.createdAt, name="Task_createdAt", curie=MCP.curie('createdAt'),
                   model_uri=MCP.Task_createdAt, domain=Task, range=str)

slots.Task_lastUpdatedAt = Slot(uri=MCP.lastUpdatedAt, name="Task_lastUpdatedAt", curie=MCP.curie('lastUpdatedAt'),
                   model_uri=MCP.Task_lastUpdatedAt, domain=Task, range=str)

slots.Task_ttl = Slot(uri=MCP.ttl, name="Task_ttl", curie=MCP.curie('ttl'),
                   model_uri=MCP.Task_ttl, domain=Task, range=int)

slots.RelatedTaskMetadata_taskId = Slot(uri=MCP.taskId, name="RelatedTaskMetadata_taskId", curie=MCP.curie('taskId'),
                   model_uri=MCP.RelatedTaskMetadata_taskId, domain=RelatedTaskMetadata, range=str)

slots.ClientCapabilities_elicitation = Slot(uri=MCP.elicitation, name="ClientCapabilities_elicitation", curie=MCP.curie('elicitation'),
                   model_uri=MCP.ClientCapabilities_elicitation, domain=ClientCapabilities, range=Optional[Union[dict, ElicitationCapability]])

slots.ClientCapabilities_extensions = Slot(uri=MCP.extensions, name="ClientCapabilities_extensions", curie=MCP.curie('extensions'),
                   model_uri=MCP.ClientCapabilities_extensions, domain=ClientCapabilities, range=Optional[Union[dict, ExtensionsCapability]])

slots.ClientCapabilities_sampling = Slot(uri=MCP.sampling, name="ClientCapabilities_sampling", curie=MCP.curie('sampling'),
                   model_uri=MCP.ClientCapabilities_sampling, domain=ClientCapabilities, range=Optional[Union[dict, SamplingCapability]])

slots.ClientCapabilities_roots = Slot(uri=MCP.roots, name="ClientCapabilities_roots", curie=MCP.curie('roots'),
                   model_uri=MCP.ClientCapabilities_roots, domain=ClientCapabilities, range=Optional[Union[Union[dict, RootsCapability], list[Union[dict, RootsCapability]]]])

slots.ClientCapabilities_tasks = Slot(uri=MCP.tasks, name="ClientCapabilities_tasks", curie=MCP.curie('tasks'),
                   model_uri=MCP.ClientCapabilities_tasks, domain=ClientCapabilities, range=Optional[Union[Union[dict, TasksCapability], list[Union[dict, TasksCapability]]]])

slots.ServerCapabilities_extensions = Slot(uri=MCP.extensions, name="ServerCapabilities_extensions", curie=MCP.curie('extensions'),
                   model_uri=MCP.ServerCapabilities_extensions, domain=ServerCapabilities, range=Optional[Union[dict, ExtensionsCapability]])

slots.ServerCapabilities_prompts = Slot(uri=MCP.prompts, name="ServerCapabilities_prompts", curie=MCP.curie('prompts'),
                   model_uri=MCP.ServerCapabilities_prompts, domain=ServerCapabilities, range=Optional[Union[Union[dict, PromptsCapability], list[Union[dict, PromptsCapability]]]])

slots.ServerCapabilities_resources = Slot(uri=MCP.resources, name="ServerCapabilities_resources", curie=MCP.curie('resources'),
                   model_uri=MCP.ServerCapabilities_resources, domain=ServerCapabilities, range=Optional[Union[Union[dict, ResourcesCapability], list[Union[dict, ResourcesCapability]]]])

slots.ServerCapabilities_tools = Slot(uri=MCP.tools, name="ServerCapabilities_tools", curie=MCP.curie('tools'),
                   model_uri=MCP.ServerCapabilities_tools, domain=ServerCapabilities, range=Optional[Union[Union[dict, ToolsCapability], list[Union[dict, ToolsCapability]]]])

slots.ServerCapabilities_tasks = Slot(uri=MCP.tasks, name="ServerCapabilities_tasks", curie=MCP.curie('tasks'),
                   model_uri=MCP.ServerCapabilities_tasks, domain=ServerCapabilities, range=Optional[Union[Union[dict, TasksCapability], list[Union[dict, TasksCapability]]]])

slots.StringSchema_type = Slot(uri=MCP.type, name="StringSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.StringSchema_type, domain=StringSchema, range=str)

slots.NumberSchema_default = Slot(uri=MCP.default, name="NumberSchema_default", curie=MCP.curie('default'),
                   model_uri=MCP.NumberSchema_default, domain=NumberSchema, range=Optional[int])

slots.NumberSchema_type = Slot(uri=MCP.type, name="NumberSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.NumberSchema_type, domain=NumberSchema, range=str)

slots.BooleanSchema_default = Slot(uri=MCP.default, name="BooleanSchema_default", curie=MCP.curie('default'),
                   model_uri=MCP.BooleanSchema_default, domain=BooleanSchema, range=Optional[Union[bool, Bool]])

slots.BooleanSchema_default_value = Slot(uri=MCP.default_value, name="BooleanSchema_default_value", curie=MCP.curie('default_value'),
                   model_uri=MCP.BooleanSchema_default_value, domain=BooleanSchema, range=Optional[Union[bool, Bool]])

slots.BooleanSchema_type = Slot(uri=MCP.type, name="BooleanSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.BooleanSchema_type, domain=BooleanSchema, range=str)

slots.UntitledSingleSelectEnumSchema_type = Slot(uri=MCP.type, name="UntitledSingleSelectEnumSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.UntitledSingleSelectEnumSchema_type, domain=UntitledSingleSelectEnumSchema, range=str)

slots.TitledSingleSelectEnumSchema_oneOf = Slot(uri=MCP.oneOf, name="TitledSingleSelectEnumSchema_oneOf", curie=MCP.curie('oneOf'),
                   model_uri=MCP.TitledSingleSelectEnumSchema_oneOf, domain=TitledSingleSelectEnumSchema, range=Optional[Union[Union[dict, EnumOption], list[Union[dict, EnumOption]]]])

slots.TitledSingleSelectEnumSchema_type = Slot(uri=MCP.type, name="TitledSingleSelectEnumSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.TitledSingleSelectEnumSchema_type, domain=TitledSingleSelectEnumSchema, range=str)

slots.UntitledMultiSelectEnumSchema_items = Slot(uri=MCP.items, name="UntitledMultiSelectEnumSchema_items", curie=MCP.curie('items'),
                   model_uri=MCP.UntitledMultiSelectEnumSchema_items, domain=UntitledMultiSelectEnumSchema, range=Optional[Union[dict, SchemaItems]])

slots.UntitledMultiSelectEnumSchema_default = Slot(uri=MCP.default, name="UntitledMultiSelectEnumSchema_default", curie=MCP.curie('default'),
                   model_uri=MCP.UntitledMultiSelectEnumSchema_default, domain=UntitledMultiSelectEnumSchema, range=Optional[Union[str, list[str]]])

slots.UntitledMultiSelectEnumSchema_type = Slot(uri=MCP.type, name="UntitledMultiSelectEnumSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.UntitledMultiSelectEnumSchema_type, domain=UntitledMultiSelectEnumSchema, range=str)

slots.TitledMultiSelectEnumSchema_items = Slot(uri=MCP.items, name="TitledMultiSelectEnumSchema_items", curie=MCP.curie('items'),
                   model_uri=MCP.TitledMultiSelectEnumSchema_items, domain=TitledMultiSelectEnumSchema, range=Optional[Union[dict, SchemaItems]])

slots.TitledMultiSelectEnumSchema_default = Slot(uri=MCP.default, name="TitledMultiSelectEnumSchema_default", curie=MCP.curie('default'),
                   model_uri=MCP.TitledMultiSelectEnumSchema_default, domain=TitledMultiSelectEnumSchema, range=Optional[Union[str, list[str]]])

slots.TitledMultiSelectEnumSchema_type = Slot(uri=MCP.type, name="TitledMultiSelectEnumSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.TitledMultiSelectEnumSchema_type, domain=TitledMultiSelectEnumSchema, range=str)

slots.LegacyTitledEnumSchema_type = Slot(uri=MCP.type, name="LegacyTitledEnumSchema_type", curie=MCP.curie('type'),
                   model_uri=MCP.LegacyTitledEnumSchema_type, domain=LegacyTitledEnumSchema, range=str)

slots.JSONRPCRequest_id = Slot(uri=MCP.id, name="JSONRPCRequest_id", curie=MCP.curie('id'),
                   model_uri=MCP.JSONRPCRequest_id, domain=JSONRPCRequest, range=str)

slots.JSONRPCRequest_jsonrpc = Slot(uri=MCP.jsonrpc, name="JSONRPCRequest_jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.JSONRPCRequest_jsonrpc, domain=JSONRPCRequest, range=str)

slots.JSONRPCRequest_method = Slot(uri=MCP.method, name="JSONRPCRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.JSONRPCRequest_method, domain=JSONRPCRequest, range=str)

slots.JSONRPCNotification_jsonrpc = Slot(uri=MCP.jsonrpc, name="JSONRPCNotification_jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.JSONRPCNotification_jsonrpc, domain=JSONRPCNotification, range=str)

slots.JSONRPCNotification_method = Slot(uri=MCP.method, name="JSONRPCNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.JSONRPCNotification_method, domain=JSONRPCNotification, range=str)

slots.JSONRPCResultResponse_id = Slot(uri=MCP.id, name="JSONRPCResultResponse_id", curie=MCP.curie('id'),
                   model_uri=MCP.JSONRPCResultResponse_id, domain=JSONRPCResultResponse, range=str)

slots.JSONRPCResultResponse_jsonrpc = Slot(uri=MCP.jsonrpc, name="JSONRPCResultResponse_jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.JSONRPCResultResponse_jsonrpc, domain=JSONRPCResultResponse, range=str)

slots.JSONRPCErrorResponse_jsonrpc = Slot(uri=MCP.jsonrpc, name="JSONRPCErrorResponse_jsonrpc", curie=MCP.curie('jsonrpc'),
                   model_uri=MCP.JSONRPCErrorResponse_jsonrpc, domain=JSONRPCErrorResponse, range=str)

slots.JSONRPCErrorResponse_error = Slot(uri=MCP.error, name="JSONRPCErrorResponse_error", curie=MCP.curie('error'),
                   model_uri=MCP.JSONRPCErrorResponse_error, domain=JSONRPCErrorResponse, range=Union[dict, Error])

slots.JSONRPCErrorResponse_id = Slot(uri=MCP.id, name="JSONRPCErrorResponse_id", curie=MCP.curie('id'),
                   model_uri=MCP.JSONRPCErrorResponse_id, domain=JSONRPCErrorResponse, range=Optional[str])

slots.ProgressNotificationParams_progress = Slot(uri=MCP.progress, name="ProgressNotificationParams_progress", curie=MCP.curie('progress'),
                   model_uri=MCP.ProgressNotificationParams_progress, domain=ProgressNotificationParams, range=float)

slots.ProgressNotificationParams_progressToken = Slot(uri=MCP.progressToken, name="ProgressNotificationParams_progressToken", curie=MCP.curie('progressToken'),
                   model_uri=MCP.ProgressNotificationParams_progressToken, domain=ProgressNotificationParams, range=str)

slots.ElicitationCompleteNotificationParams_elicitationId = Slot(uri=MCP.elicitationId, name="ElicitationCompleteNotificationParams_elicitationId", curie=MCP.curie('elicitationId'),
                   model_uri=MCP.ElicitationCompleteNotificationParams_elicitationId, domain=ElicitationCompleteNotificationParams, range=str)

slots.LoggingMessageNotificationParams_data = Slot(uri=MCP.data, name="LoggingMessageNotificationParams_data", curie=MCP.curie('data'),
                   model_uri=MCP.LoggingMessageNotificationParams_data, domain=LoggingMessageNotificationParams, range=Union[dict, LogData])

slots.LoggingMessageNotificationParams_level = Slot(uri=MCP.level, name="LoggingMessageNotificationParams_level", curie=MCP.curie('level'),
                   model_uri=MCP.LoggingMessageNotificationParams_level, domain=LoggingMessageNotificationParams, range=Union[str, "LoggingLevel"])

slots.ResourceUpdatedNotificationParams_uri = Slot(uri=MCP.uri, name="ResourceUpdatedNotificationParams_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.ResourceUpdatedNotificationParams_uri, domain=ResourceUpdatedNotificationParams, range=Union[str, URI])

slots.TaskStatusNotificationParams_taskId = Slot(uri=MCP.taskId, name="TaskStatusNotificationParams_taskId", curie=MCP.curie('taskId'),
                   model_uri=MCP.TaskStatusNotificationParams_taskId, domain=TaskStatusNotificationParams, range=str)

slots.TaskStatusNotificationParams_status = Slot(uri=MCP.status, name="TaskStatusNotificationParams_status", curie=MCP.curie('status'),
                   model_uri=MCP.TaskStatusNotificationParams_status, domain=TaskStatusNotificationParams, range=Union[str, "TaskStatusEnum"])

slots.TaskStatusNotificationParams_createdAt = Slot(uri=MCP.createdAt, name="TaskStatusNotificationParams_createdAt", curie=MCP.curie('createdAt'),
                   model_uri=MCP.TaskStatusNotificationParams_createdAt, domain=TaskStatusNotificationParams, range=str)

slots.TaskStatusNotificationParams_lastUpdatedAt = Slot(uri=MCP.lastUpdatedAt, name="TaskStatusNotificationParams_lastUpdatedAt", curie=MCP.curie('lastUpdatedAt'),
                   model_uri=MCP.TaskStatusNotificationParams_lastUpdatedAt, domain=TaskStatusNotificationParams, range=str)

slots.TaskStatusNotificationParams_ttl = Slot(uri=MCP.ttl, name="TaskStatusNotificationParams_ttl", curie=MCP.curie('ttl'),
                   model_uri=MCP.TaskStatusNotificationParams_ttl, domain=TaskStatusNotificationParams, range=int)

slots.CancelledNotification_params = Slot(uri=MCP.params, name="CancelledNotification_params", curie=MCP.curie('params'),
                   model_uri=MCP.CancelledNotification_params, domain=CancelledNotification, range=Union[dict, CancelledNotificationParams])

slots.CancelledNotification_method = Slot(uri=MCP.method, name="CancelledNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.CancelledNotification_method, domain=CancelledNotification, range=str)

slots.InitializedNotification_method = Slot(uri=MCP.method, name="InitializedNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.InitializedNotification_method, domain=InitializedNotification, range=str)

slots.ProgressNotification_params = Slot(uri=MCP.params, name="ProgressNotification_params", curie=MCP.curie('params'),
                   model_uri=MCP.ProgressNotification_params, domain=ProgressNotification, range=Union[dict, ProgressNotificationParams])

slots.ProgressNotification_method = Slot(uri=MCP.method, name="ProgressNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.ProgressNotification_method, domain=ProgressNotification, range=str)

slots.ResourceListChangedNotification_method = Slot(uri=MCP.method, name="ResourceListChangedNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.ResourceListChangedNotification_method, domain=ResourceListChangedNotification, range=str)

slots.ResourceUpdatedNotification_params = Slot(uri=MCP.params, name="ResourceUpdatedNotification_params", curie=MCP.curie('params'),
                   model_uri=MCP.ResourceUpdatedNotification_params, domain=ResourceUpdatedNotification, range=Union[dict, ResourceUpdatedNotificationParams])

slots.ResourceUpdatedNotification_method = Slot(uri=MCP.method, name="ResourceUpdatedNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.ResourceUpdatedNotification_method, domain=ResourceUpdatedNotification, range=str)

slots.PromptListChangedNotification_method = Slot(uri=MCP.method, name="PromptListChangedNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.PromptListChangedNotification_method, domain=PromptListChangedNotification, range=str)

slots.ToolListChangedNotification_method = Slot(uri=MCP.method, name="ToolListChangedNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.ToolListChangedNotification_method, domain=ToolListChangedNotification, range=str)

slots.RootsListChangedNotification_method = Slot(uri=MCP.method, name="RootsListChangedNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.RootsListChangedNotification_method, domain=RootsListChangedNotification, range=str)

slots.LoggingMessageNotification_params = Slot(uri=MCP.params, name="LoggingMessageNotification_params", curie=MCP.curie('params'),
                   model_uri=MCP.LoggingMessageNotification_params, domain=LoggingMessageNotification, range=Union[dict, LoggingMessageNotificationParams])

slots.LoggingMessageNotification_method = Slot(uri=MCP.method, name="LoggingMessageNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.LoggingMessageNotification_method, domain=LoggingMessageNotification, range=str)

slots.ElicitationCompleteNotification_params = Slot(uri=MCP.params, name="ElicitationCompleteNotification_params", curie=MCP.curie('params'),
                   model_uri=MCP.ElicitationCompleteNotification_params, domain=ElicitationCompleteNotification, range=Union[dict, ElicitationCompleteNotificationParams])

slots.ElicitationCompleteNotification_method = Slot(uri=MCP.method, name="ElicitationCompleteNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.ElicitationCompleteNotification_method, domain=ElicitationCompleteNotification, range=str)

slots.TaskStatusNotification_params = Slot(uri=MCP.params, name="TaskStatusNotification_params", curie=MCP.curie('params'),
                   model_uri=MCP.TaskStatusNotification_params, domain=TaskStatusNotification, range=Union[dict, TaskStatusNotificationParams])

slots.TaskStatusNotification_method = Slot(uri=MCP.method, name="TaskStatusNotification_method", curie=MCP.curie('method'),
                   model_uri=MCP.TaskStatusNotification_method, domain=TaskStatusNotification, range=str)

slots.CallToolRequestParams_arguments = Slot(uri=MCP.arguments, name="CallToolRequestParams_arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.CallToolRequestParams_arguments, domain=CallToolRequestParams, range=Optional[Union[dict, ArgumentMap]])

slots.CallToolRequestParams_task = Slot(uri=MCP.task, name="CallToolRequestParams_task", curie=MCP.curie('task'),
                   model_uri=MCP.CallToolRequestParams_task, domain=CallToolRequestParams, range=Optional[Union[dict, TaskMetadata]])

slots.CallToolRequestParams_name = Slot(uri=SCHEMA.name, name="CallToolRequestParams_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.CallToolRequestParams_name, domain=CallToolRequestParams, range=str)

slots.GetPromptRequestParams_arguments = Slot(uri=MCP.arguments, name="GetPromptRequestParams_arguments", curie=MCP.curie('arguments'),
                   model_uri=MCP.GetPromptRequestParams_arguments, domain=GetPromptRequestParams, range=Optional[Union[dict, ArgumentMap]])

slots.GetPromptRequestParams_name = Slot(uri=SCHEMA.name, name="GetPromptRequestParams_name", curie=SCHEMA.curie('name'),
                   model_uri=MCP.GetPromptRequestParams_name, domain=GetPromptRequestParams, range=str)

slots.CompleteRequestParams_argument = Slot(uri=MCP.argument, name="CompleteRequestParams_argument", curie=MCP.curie('argument'),
                   model_uri=MCP.CompleteRequestParams_argument, domain=CompleteRequestParams, range=Union[dict, CompletionArgument])

slots.CompleteRequestParams_context = Slot(uri=MCP.context, name="CompleteRequestParams_context", curie=MCP.curie('context'),
                   model_uri=MCP.CompleteRequestParams_context, domain=CompleteRequestParams, range=Optional[Union[dict, CompletionContext]])

slots.CompleteRequestParams_ref = Slot(uri=MCP.ref, name="CompleteRequestParams_ref", curie=MCP.curie('ref'),
                   model_uri=MCP.CompleteRequestParams_ref, domain=CompleteRequestParams, range=Union[dict, PromptReference])

slots.ReadResourceRequestParams_uri = Slot(uri=MCP.uri, name="ReadResourceRequestParams_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.ReadResourceRequestParams_uri, domain=ReadResourceRequestParams, range=Union[str, URI])

slots.SubscribeRequestParams_uri = Slot(uri=MCP.uri, name="SubscribeRequestParams_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.SubscribeRequestParams_uri, domain=SubscribeRequestParams, range=Union[str, URI])

slots.UnsubscribeRequestParams_uri = Slot(uri=MCP.uri, name="UnsubscribeRequestParams_uri", curie=MCP.curie('uri'),
                   model_uri=MCP.UnsubscribeRequestParams_uri, domain=UnsubscribeRequestParams, range=Union[str, URI])

slots.SetLevelRequestParams_level = Slot(uri=MCP.level, name="SetLevelRequestParams_level", curie=MCP.curie('level'),
                   model_uri=MCP.SetLevelRequestParams_level, domain=SetLevelRequestParams, range=Union[str, "LoggingLevel"])

slots.InitializeRequestParams_capabilities = Slot(uri=MCP.capabilities, name="InitializeRequestParams_capabilities", curie=MCP.curie('capabilities'),
                   model_uri=MCP.InitializeRequestParams_capabilities, domain=InitializeRequestParams, range=Union[dict, ClientCapabilities])

slots.InitializeRequestParams_clientInfo = Slot(uri=MCP.clientInfo, name="InitializeRequestParams_clientInfo", curie=MCP.curie('clientInfo'),
                   model_uri=MCP.InitializeRequestParams_clientInfo, domain=InitializeRequestParams, range=Union[dict, Implementation])

slots.InitializeRequestParams_protocolVersion = Slot(uri=MCP.protocolVersion, name="InitializeRequestParams_protocolVersion", curie=MCP.curie('protocolVersion'),
                   model_uri=MCP.InitializeRequestParams_protocolVersion, domain=InitializeRequestParams, range=str)

slots.CreateMessageRequestParams_maxTokens = Slot(uri=MCP.maxTokens, name="CreateMessageRequestParams_maxTokens", curie=MCP.curie('maxTokens'),
                   model_uri=MCP.CreateMessageRequestParams_maxTokens, domain=CreateMessageRequestParams, range=int)

slots.CreateMessageRequestParams_messages = Slot(uri=MCP.messages, name="CreateMessageRequestParams_messages", curie=MCP.curie('messages'),
                   model_uri=MCP.CreateMessageRequestParams_messages, domain=CreateMessageRequestParams, range=Union[Union[dict, SamplingMessage], list[Union[dict, SamplingMessage]]])

slots.CreateMessageRequestParams_modelPreferences = Slot(uri=MCP.modelPreferences, name="CreateMessageRequestParams_modelPreferences", curie=MCP.curie('modelPreferences'),
                   model_uri=MCP.CreateMessageRequestParams_modelPreferences, domain=CreateMessageRequestParams, range=Optional[Union[dict, ModelPreferences]])

slots.CreateMessageRequestParams_tools = Slot(uri=MCP.tools, name="CreateMessageRequestParams_tools", curie=MCP.curie('tools'),
                   model_uri=MCP.CreateMessageRequestParams_tools, domain=CreateMessageRequestParams, range=Optional[Union[Union[dict, Tool], list[Union[dict, Tool]]]])

slots.CreateMessageRequestParams_toolChoice = Slot(uri=MCP.toolChoice, name="CreateMessageRequestParams_toolChoice", curie=MCP.curie('toolChoice'),
                   model_uri=MCP.CreateMessageRequestParams_toolChoice, domain=CreateMessageRequestParams, range=Optional[Union[dict, ToolChoice]])

slots.CreateMessageRequestParams_task = Slot(uri=MCP.task, name="CreateMessageRequestParams_task", curie=MCP.curie('task'),
                   model_uri=MCP.CreateMessageRequestParams_task, domain=CreateMessageRequestParams, range=Optional[Union[dict, TaskMetadata]])

slots.ElicitRequestFormParams_message = Slot(uri=MCP.message, name="ElicitRequestFormParams_message", curie=MCP.curie('message'),
                   model_uri=MCP.ElicitRequestFormParams_message, domain=ElicitRequestFormParams, range=str)

slots.ElicitRequestFormParams_requestedSchema = Slot(uri=MCP.requestedSchema, name="ElicitRequestFormParams_requestedSchema", curie=MCP.curie('requestedSchema'),
                   model_uri=MCP.ElicitRequestFormParams_requestedSchema, domain=ElicitRequestFormParams, range=Union[dict, JsonSchema])

slots.ElicitRequestFormParams_task = Slot(uri=MCP.task, name="ElicitRequestFormParams_task", curie=MCP.curie('task'),
                   model_uri=MCP.ElicitRequestFormParams_task, domain=ElicitRequestFormParams, range=Optional[Union[dict, TaskMetadata]])

slots.ElicitRequestURLParams_elicitationId = Slot(uri=MCP.elicitationId, name="ElicitRequestURLParams_elicitationId", curie=MCP.curie('elicitationId'),
                   model_uri=MCP.ElicitRequestURLParams_elicitationId, domain=ElicitRequestURLParams, range=str)

slots.ElicitRequestURLParams_message = Slot(uri=MCP.message, name="ElicitRequestURLParams_message", curie=MCP.curie('message'),
                   model_uri=MCP.ElicitRequestURLParams_message, domain=ElicitRequestURLParams, range=str)

slots.ElicitRequestURLParams_mode = Slot(uri=MCP.mode, name="ElicitRequestURLParams_mode", curie=MCP.curie('mode'),
                   model_uri=MCP.ElicitRequestURLParams_mode, domain=ElicitRequestURLParams, range=str)

slots.ElicitRequestURLParams_url = Slot(uri=MCP.url, name="ElicitRequestURLParams_url", curie=MCP.curie('url'),
                   model_uri=MCP.ElicitRequestURLParams_url, domain=ElicitRequestURLParams, range=Union[str, URI])

slots.ElicitRequestURLParams_task = Slot(uri=MCP.task, name="ElicitRequestURLParams_task", curie=MCP.curie('task'),
                   model_uri=MCP.ElicitRequestURLParams_task, domain=ElicitRequestURLParams, range=Optional[Union[dict, TaskMetadata]])

slots.InitializeRequest_params = Slot(uri=MCP.params, name="InitializeRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.InitializeRequest_params, domain=InitializeRequest, range=Union[dict, InitializeRequestParams])

slots.InitializeRequest_method = Slot(uri=MCP.method, name="InitializeRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.InitializeRequest_method, domain=InitializeRequest, range=str)

slots.PingRequest_method = Slot(uri=MCP.method, name="PingRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.PingRequest_method, domain=PingRequest, range=str)

slots.ListResourcesRequest_method = Slot(uri=MCP.method, name="ListResourcesRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ListResourcesRequest_method, domain=ListResourcesRequest, range=str)

slots.ListResourceTemplatesRequest_method = Slot(uri=MCP.method, name="ListResourceTemplatesRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ListResourceTemplatesRequest_method, domain=ListResourceTemplatesRequest, range=str)

slots.ReadResourceRequest_params = Slot(uri=MCP.params, name="ReadResourceRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.ReadResourceRequest_params, domain=ReadResourceRequest, range=Union[dict, ReadResourceRequestParams])

slots.ReadResourceRequest_method = Slot(uri=MCP.method, name="ReadResourceRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ReadResourceRequest_method, domain=ReadResourceRequest, range=str)

slots.SubscribeRequest_params = Slot(uri=MCP.params, name="SubscribeRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.SubscribeRequest_params, domain=SubscribeRequest, range=Union[dict, SubscribeRequestParams])

slots.SubscribeRequest_method = Slot(uri=MCP.method, name="SubscribeRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.SubscribeRequest_method, domain=SubscribeRequest, range=str)

slots.UnsubscribeRequest_params = Slot(uri=MCP.params, name="UnsubscribeRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.UnsubscribeRequest_params, domain=UnsubscribeRequest, range=Union[dict, UnsubscribeRequestParams])

slots.UnsubscribeRequest_method = Slot(uri=MCP.method, name="UnsubscribeRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.UnsubscribeRequest_method, domain=UnsubscribeRequest, range=str)

slots.ListPromptsRequest_method = Slot(uri=MCP.method, name="ListPromptsRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ListPromptsRequest_method, domain=ListPromptsRequest, range=str)

slots.GetPromptRequest_params = Slot(uri=MCP.params, name="GetPromptRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.GetPromptRequest_params, domain=GetPromptRequest, range=Union[dict, GetPromptRequestParams])

slots.GetPromptRequest_method = Slot(uri=MCP.method, name="GetPromptRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.GetPromptRequest_method, domain=GetPromptRequest, range=str)

slots.ListToolsRequest_method = Slot(uri=MCP.method, name="ListToolsRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ListToolsRequest_method, domain=ListToolsRequest, range=str)

slots.CallToolRequest_params = Slot(uri=MCP.params, name="CallToolRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.CallToolRequest_params, domain=CallToolRequest, range=Union[dict, CallToolRequestParams])

slots.CallToolRequest_method = Slot(uri=MCP.method, name="CallToolRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.CallToolRequest_method, domain=CallToolRequest, range=str)

slots.CompleteRequest_params = Slot(uri=MCP.params, name="CompleteRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.CompleteRequest_params, domain=CompleteRequest, range=Union[dict, CompleteRequestParams])

slots.CompleteRequest_method = Slot(uri=MCP.method, name="CompleteRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.CompleteRequest_method, domain=CompleteRequest, range=str)

slots.SetLevelRequest_params = Slot(uri=MCP.params, name="SetLevelRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.SetLevelRequest_params, domain=SetLevelRequest, range=Union[dict, SetLevelRequestParams])

slots.SetLevelRequest_method = Slot(uri=MCP.method, name="SetLevelRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.SetLevelRequest_method, domain=SetLevelRequest, range=str)

slots.CreateMessageRequest_params = Slot(uri=MCP.params, name="CreateMessageRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.CreateMessageRequest_params, domain=CreateMessageRequest, range=Union[dict, CreateMessageRequestParams])

slots.CreateMessageRequest_method = Slot(uri=MCP.method, name="CreateMessageRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.CreateMessageRequest_method, domain=CreateMessageRequest, range=str)

slots.ListRootsRequest_method = Slot(uri=MCP.method, name="ListRootsRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ListRootsRequest_method, domain=ListRootsRequest, range=str)

slots.ElicitRequest_params = Slot(uri=MCP.params, name="ElicitRequest_params", curie=MCP.curie('params'),
                   model_uri=MCP.ElicitRequest_params, domain=ElicitRequest, range=Union[dict, ElicitRequestFormParams])

slots.ElicitRequest_method = Slot(uri=MCP.method, name="ElicitRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ElicitRequest_method, domain=ElicitRequest, range=str)

slots.ListTasksRequest_method = Slot(uri=MCP.method, name="ListTasksRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.ListTasksRequest_method, domain=ListTasksRequest, range=str)

slots.GetTaskRequest_method = Slot(uri=MCP.method, name="GetTaskRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.GetTaskRequest_method, domain=GetTaskRequest, range=str)

slots.GetTaskPayloadRequest_method = Slot(uri=MCP.method, name="GetTaskPayloadRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.GetTaskPayloadRequest_method, domain=GetTaskPayloadRequest, range=str)

slots.CancelTaskRequest_method = Slot(uri=MCP.method, name="CancelTaskRequest_method", curie=MCP.curie('method'),
                   model_uri=MCP.CancelTaskRequest_method, domain=CancelTaskRequest, range=str)

slots.InitializeResult_capabilities = Slot(uri=MCP.capabilities, name="InitializeResult_capabilities", curie=MCP.curie('capabilities'),
                   model_uri=MCP.InitializeResult_capabilities, domain=InitializeResult, range=Union[dict, ServerCapabilities])

slots.InitializeResult_protocolVersion = Slot(uri=MCP.protocolVersion, name="InitializeResult_protocolVersion", curie=MCP.curie('protocolVersion'),
                   model_uri=MCP.InitializeResult_protocolVersion, domain=InitializeResult, range=str)

slots.InitializeResult_serverInfo = Slot(uri=MCP.serverInfo, name="InitializeResult_serverInfo", curie=MCP.curie('serverInfo'),
                   model_uri=MCP.InitializeResult_serverInfo, domain=InitializeResult, range=Union[dict, Implementation])

slots.CallToolResult_content = Slot(uri=MCP.content, name="CallToolResult_content", curie=MCP.curie('content'),
                   model_uri=MCP.CallToolResult_content, domain=CallToolResult, range=Union[Union[dict, ContentBlock], list[Union[dict, ContentBlock]]])

slots.CallToolResult_structuredContent = Slot(uri=MCP.structuredContent, name="CallToolResult_structuredContent", curie=MCP.curie('structuredContent'),
                   model_uri=MCP.CallToolResult_structuredContent, domain=CallToolResult, range=Optional[Union[dict, StructuredContentData]])

slots.CompleteResult_completion = Slot(uri=MCP.completion, name="CompleteResult_completion", curie=MCP.curie('completion'),
                   model_uri=MCP.CompleteResult_completion, domain=CompleteResult, range=Union[dict, CompletionData])

slots.GetPromptResult_messages = Slot(uri=MCP.messages, name="GetPromptResult_messages", curie=MCP.curie('messages'),
                   model_uri=MCP.GetPromptResult_messages, domain=GetPromptResult, range=Union[Union[dict, PromptMessage], list[Union[dict, PromptMessage]]])

slots.ListPromptsResult_prompts = Slot(uri=MCP.prompts, name="ListPromptsResult_prompts", curie=MCP.curie('prompts'),
                   model_uri=MCP.ListPromptsResult_prompts, domain=ListPromptsResult, range=Union[Union[dict, Prompt], list[Union[dict, Prompt]]])

slots.ListResourcesResult_resources = Slot(uri=MCP.resources, name="ListResourcesResult_resources", curie=MCP.curie('resources'),
                   model_uri=MCP.ListResourcesResult_resources, domain=ListResourcesResult, range=Union[Union[dict, Resource], list[Union[dict, Resource]]])

slots.ListResourceTemplatesResult_resourceTemplates = Slot(uri=MCP.resourceTemplates, name="ListResourceTemplatesResult_resourceTemplates", curie=MCP.curie('resourceTemplates'),
                   model_uri=MCP.ListResourceTemplatesResult_resourceTemplates, domain=ListResourceTemplatesResult, range=Union[Union[dict, ResourceTemplate], list[Union[dict, ResourceTemplate]]])

slots.ReadResourceResult_contents = Slot(uri=MCP.contents, name="ReadResourceResult_contents", curie=MCP.curie('contents'),
                   model_uri=MCP.ReadResourceResult_contents, domain=ReadResourceResult, range=Union[Union[dict, ResourceContents], list[Union[dict, ResourceContents]]])

slots.ListToolsResult_tools = Slot(uri=MCP.tools, name="ListToolsResult_tools", curie=MCP.curie('tools'),
                   model_uri=MCP.ListToolsResult_tools, domain=ListToolsResult, range=Union[Union[dict, Tool], list[Union[dict, Tool]]])

slots.ListRootsResult_roots = Slot(uri=MCP.roots, name="ListRootsResult_roots", curie=MCP.curie('roots'),
                   model_uri=MCP.ListRootsResult_roots, domain=ListRootsResult, range=Union[Union[dict, Root], list[Union[dict, Root]]])

slots.CreateMessageResult_content = Slot(uri=MCP.content, name="CreateMessageResult_content", curie=MCP.curie('content'),
                   model_uri=MCP.CreateMessageResult_content, domain=CreateMessageResult, range=Union[dict, ContentBlock])

slots.CreateMessageResult_model = Slot(uri=MCP.model, name="CreateMessageResult_model", curie=MCP.curie('model'),
                   model_uri=MCP.CreateMessageResult_model, domain=CreateMessageResult, range=str)

slots.CreateMessageResult_role = Slot(uri=MCP.role, name="CreateMessageResult_role", curie=MCP.curie('role'),
                   model_uri=MCP.CreateMessageResult_role, domain=CreateMessageResult, range=Union[str, "Role"])

slots.ElicitResult_action = Slot(uri=MCP.action, name="ElicitResult_action", curie=MCP.curie('action'),
                   model_uri=MCP.ElicitResult_action, domain=ElicitResult, range=Union[str, "ElicitActionEnum"])

slots.ElicitResult_content = Slot(uri=MCP.content, name="ElicitResult_content", curie=MCP.curie('content'),
                   model_uri=MCP.ElicitResult_content, domain=ElicitResult, range=Optional[Union[dict, ElicitationContent]])

slots.CreateTaskResult_task = Slot(uri=MCP.task, name="CreateTaskResult_task", curie=MCP.curie('task'),
                   model_uri=MCP.CreateTaskResult_task, domain=CreateTaskResult, range=Union[dict, Task])

slots.ListTasksResult_tasks = Slot(uri=MCP.tasks, name="ListTasksResult_tasks", curie=MCP.curie('tasks'),
                   model_uri=MCP.ListTasksResult_tasks, domain=ListTasksResult, range=Union[Union[dict, Task], list[Union[dict, Task]]])

slots.CancelTaskResult_taskId = Slot(uri=MCP.taskId, name="CancelTaskResult_taskId", curie=MCP.curie('taskId'),
                   model_uri=MCP.CancelTaskResult_taskId, domain=CancelTaskResult, range=str)

slots.CancelTaskResult_status = Slot(uri=MCP.status, name="CancelTaskResult_status", curie=MCP.curie('status'),
                   model_uri=MCP.CancelTaskResult_status, domain=CancelTaskResult, range=Union[str, "TaskStatusEnum"])

slots.CancelTaskResult_createdAt = Slot(uri=MCP.createdAt, name="CancelTaskResult_createdAt", curie=MCP.curie('createdAt'),
                   model_uri=MCP.CancelTaskResult_createdAt, domain=CancelTaskResult, range=str)

slots.CancelTaskResult_lastUpdatedAt = Slot(uri=MCP.lastUpdatedAt, name="CancelTaskResult_lastUpdatedAt", curie=MCP.curie('lastUpdatedAt'),
                   model_uri=MCP.CancelTaskResult_lastUpdatedAt, domain=CancelTaskResult, range=str)

slots.CancelTaskResult_ttl = Slot(uri=MCP.ttl, name="CancelTaskResult_ttl", curie=MCP.curie('ttl'),
                   model_uri=MCP.CancelTaskResult_ttl, domain=CancelTaskResult, range=int)

slots.GetTaskResult_taskId = Slot(uri=MCP.taskId, name="GetTaskResult_taskId", curie=MCP.curie('taskId'),
                   model_uri=MCP.GetTaskResult_taskId, domain=GetTaskResult, range=str)

slots.GetTaskResult_status = Slot(uri=MCP.status, name="GetTaskResult_status", curie=MCP.curie('status'),
                   model_uri=MCP.GetTaskResult_status, domain=GetTaskResult, range=Union[str, "TaskStatusEnum"])

slots.GetTaskResult_createdAt = Slot(uri=MCP.createdAt, name="GetTaskResult_createdAt", curie=MCP.curie('createdAt'),
                   model_uri=MCP.GetTaskResult_createdAt, domain=GetTaskResult, range=str)

slots.GetTaskResult_lastUpdatedAt = Slot(uri=MCP.lastUpdatedAt, name="GetTaskResult_lastUpdatedAt", curie=MCP.curie('lastUpdatedAt'),
                   model_uri=MCP.GetTaskResult_lastUpdatedAt, domain=GetTaskResult, range=str)

slots.GetTaskResult_ttl = Slot(uri=MCP.ttl, name="GetTaskResult_ttl", curie=MCP.curie('ttl'),
                   model_uri=MCP.GetTaskResult_ttl, domain=GetTaskResult, range=int)

slots.InitializeResultResponse_result = Slot(uri=MCP.result, name="InitializeResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.InitializeResultResponse_result, domain=InitializeResultResponse, range=Union[dict, InitializeResult])

slots.CallToolResultResponse_result = Slot(uri=MCP.result, name="CallToolResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.CallToolResultResponse_result, domain=CallToolResultResponse, range=Union[dict, CallToolResult])

slots.CompleteResultResponse_result = Slot(uri=MCP.result, name="CompleteResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.CompleteResultResponse_result, domain=CompleteResultResponse, range=Union[dict, CompleteResult])

slots.GetPromptResultResponse_result = Slot(uri=MCP.result, name="GetPromptResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.GetPromptResultResponse_result, domain=GetPromptResultResponse, range=Union[dict, GetPromptResult])

slots.ListPromptsResultResponse_result = Slot(uri=MCP.result, name="ListPromptsResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ListPromptsResultResponse_result, domain=ListPromptsResultResponse, range=Union[dict, ListPromptsResult])

slots.ListResourcesResultResponse_result = Slot(uri=MCP.result, name="ListResourcesResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ListResourcesResultResponse_result, domain=ListResourcesResultResponse, range=Union[dict, ListResourcesResult])

slots.ListResourceTemplatesResultResponse_result = Slot(uri=MCP.result, name="ListResourceTemplatesResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ListResourceTemplatesResultResponse_result, domain=ListResourceTemplatesResultResponse, range=Union[dict, ListResourceTemplatesResult])

slots.ReadResourceResultResponse_result = Slot(uri=MCP.result, name="ReadResourceResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ReadResourceResultResponse_result, domain=ReadResourceResultResponse, range=Union[dict, ReadResourceResult])

slots.ListToolsResultResponse_result = Slot(uri=MCP.result, name="ListToolsResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ListToolsResultResponse_result, domain=ListToolsResultResponse, range=Union[dict, ListToolsResult])

slots.ListRootsResultResponse_result = Slot(uri=MCP.result, name="ListRootsResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ListRootsResultResponse_result, domain=ListRootsResultResponse, range=Union[dict, ListRootsResult])

slots.CreateMessageResultResponse_result = Slot(uri=MCP.result, name="CreateMessageResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.CreateMessageResultResponse_result, domain=CreateMessageResultResponse, range=Union[dict, CreateMessageResult])

slots.ElicitResultResponse_result = Slot(uri=MCP.result, name="ElicitResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ElicitResultResponse_result, domain=ElicitResultResponse, range=Union[dict, ElicitResult])

slots.CreateTaskResultResponse_result = Slot(uri=MCP.result, name="CreateTaskResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.CreateTaskResultResponse_result, domain=CreateTaskResultResponse, range=Union[dict, CreateTaskResult])

slots.GetTaskResultResponse_result = Slot(uri=MCP.result, name="GetTaskResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.GetTaskResultResponse_result, domain=GetTaskResultResponse, range=Union[dict, GetTaskResult])

slots.GetTaskPayloadResultResponse_result = Slot(uri=MCP.result, name="GetTaskPayloadResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.GetTaskPayloadResultResponse_result, domain=GetTaskPayloadResultResponse, range=Union[dict, GetTaskPayloadResult])

slots.CancelTaskResultResponse_result = Slot(uri=MCP.result, name="CancelTaskResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.CancelTaskResultResponse_result, domain=CancelTaskResultResponse, range=Union[dict, CancelTaskResult])

slots.ListTasksResultResponse_result = Slot(uri=MCP.result, name="ListTasksResultResponse_result", curie=MCP.curie('result'),
                   model_uri=MCP.ListTasksResultResponse_result, domain=ListTasksResultResponse, range=Union[dict, ListTasksResult])
