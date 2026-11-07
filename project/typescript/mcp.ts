/**
* The values MCP allows for `cacheScope`.
*/
export enum McpCacheScope {
    
    private = "private",
    public = "public",
};
/**
* The values MCP allows for `includeContext`.
*/
export enum McpCreateMessageRequestParamsIncludeContext {
    
    allServers = "allServers",
    none = "none",
    thisServer = "thisServer",
};
/**
* The values MCP allows for `action`.
*/
export enum McpElicitResultAction {
    
    accept = "accept",
    cancel = "cancel",
    decline = "decline",
};
/**
* The values MCP allows for `theme`.
*/
export enum McpIconTheme {
    
    dark = "dark",
    light = "light",
};
/**
* The severity of a log message.

These map to syslog message severities, as specified in RFC-5424:
https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1
*/
export enum McpLoggingLevel {
    
    alert = "alert",
    critical = "critical",
    debug = "debug",
    emergency = "emergency",
    error = "error",
    info = "info",
    notice = "notice",
    warning = "warning",
};
/**
* The values MCP allows for `type`.
*/
export enum McpNumberSchemaType {
    
    integer = "integer",
    number = "number",
};
/**
* The sender or recipient of messages and data in a conversation.
*/
export enum McpRole {
    
    assistant = "assistant",
    user = "user",
};
/**
* The values MCP allows for `format`.
*/
export enum McpStringSchemaFormat {
    
    date = "date",
    date_time = "date-time",
    email = "email",
    uri = "uri",
};
/**
* The values MCP allows for `mode`.
*/
export enum McpToolChoiceMode {
    
    auto = "auto",
    none = "none",
    required = "required",
};


/**
 * Optional annotations for the client. The client can use annotations to inform how objects are used or displayed
 */
export interface McpAnnotations {
    /** Describes who the intended audience of this object or data is.

It can include multiple entries to indicate content useful for multiple audiences (e.g., `["user", "assistant"]`). */
    audience?: string,
    /** The moment the resource was last modified, as an ISO 8601 formatted string.

Should be an ISO 8601 formatted string (e.g., "2025-01-12T15:00:58Z").

Examples: last activity timestamp in an open file, timestamp when the resource
was attached, etc. */
    lastModified?: string,
    /** Describes how important this data is for operating the server.

A value of 1 means "most important," and indicates that the data is
effectively required, while 0 means "least important," and indicates that
the data is entirely optional. */
    priority?: number,
}


/**
 * Audio provided to or from an LLM.
 */
export interface McpAudioContent {
    /** The kind of object, always `audio`. */
    type: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
    /** The base64-encoded audio data. */
    data: string,
    /** The MIME type of the audio. Different providers may support different audio types. */
    mimeType: string,
}


/**
 * Base interface for metadata with name (identifier) and title (display name) properties.
 */
export interface McpBaseMetadata {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
}


/**
 * A resource's contents as binary data, given as base64 text.
 */
export interface McpBlobResourceContents extends McpResourceContents {
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** A base64-encoded string representing the binary data of the item. */
    blob: string,
    /** The MIME type of this resource, if known. */
    mimeType?: string,
    /** The URI of this resource. */
    uri: string,
}


/**
 * A field of an elicitation form that takes true or false.
 */
export interface McpBooleanSchema {
    /** A description of the field for the user. */
    description?: string,
    /** A title for the field. */
    title?: string,
    /** The kind of object, always `boolean`. */
    type: string,
    /** The value the field takes when the user gives none. */
    default?: boolean,
}


/**
 * A result that supports a time-to-live (TTL) hint for client-side caching.
 */
export interface McpCacheableResult extends McpResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * Used by the client to invoke a tool provided by the server.
 */
export interface McpCallToolRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `tools/call`. */
    method: string,
    /** Parameters for a `tools/call` request. */
    params: McpCallToolRequestParams,
}


/**
 * Parameters for a `tools/call` request.
 */
export interface McpCallToolRequestParams extends McpInputResponseRequestParams {
    /** The name of the tool. */
    name: string,
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** Arguments to use for the tool call. */
    arguments?: McpJSONObject,
    /** A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request. */
    inputResponses?: McpInputResponses,
    /** State the server returned with an input-required result, sent back unchanged when the request is retried. */
    requestState?: string,
}


/**
 * The result returned by the server for a {@link CallToolRequesttools/call} request.
 */
export interface McpCallToolResult extends McpResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** A list of content objects that represent the unstructured result of the tool call. */
    content: McpContentBlock[],
    /** Whether the tool call ended in an error.

If not set, this is assumed to be false (the call was successful).

Any errors that originate from the tool SHOULD be reported inside the result
object, with `isError` set to true, _not_ as an MCP protocol-level error
response. Otherwise, the LLM would not be able to see that an error occurred
and self-correct.

However, any errors in _finding_ the tool, an error indicating that the
server does not support tool calls, or any other exceptional conditions,
should be reported as an MCP error response. */
    isError?: boolean,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** An optional JSON value that represents the structured result of the tool call.

This can be any JSON value (object, array, string, number, boolean, or null)
that conforms to the tool's outputSchema if one is defined. */
    structuredContent?: McpJSONValue,
}


/**
 * A successful response from the server for a {@link CallToolRequesttools/call} request.
 */
export interface McpCallToolResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** What the request returned. */
    result: string,
}


/**
 * This notification is sent by the client to indicate that it is cancelling a request it previously issued.

On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

This notification indicates that the result will be unused, so any associated processing SHOULD cease.
 */
export interface McpCancelledNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/cancelled`. */
    method: string,
    /** Parameters for a `notifications/cancelled` notification. */
    params: McpCancelledNotificationParams,
}


/**
 * Parameters for a `notifications/cancelled` notification.
 */
export interface McpCancelledNotificationParams extends McpNotificationParams {
    /** An optional string describing the reason for the cancellation. This MAY be logged or presented to the user. */
    reason?: string,
    /** Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpNotificationMetaObject,
    /** The ID of the request to cancel.

This MUST correspond to the ID of a request the client previously issued. */
    requestId: string,
}


/**
 * Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.
 */
export interface McpClientCapabilities {
    /** Present if the client supports elicitation from the server. */
    elicitation?: McpClientCapabilitiesElicitation,
    /** Experimental, non-standard capabilities that the client supports. */
    experimental?: McpClientCapabilitiesExperimental,
    /** Optional MCP extensions that the client supports. Keys are extension identifiers
(e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values are
per-extension settings objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix. */
    extensions?: McpClientCapabilitiesExtensions,
    /** Present if the client supports listing roots. */
    roots?: McpClientCapabilitiesRoots,
    /** Present if the client supports sampling from an LLM. */
    sampling?: McpClientCapabilitiesSampling,
}


/**
 * Present if the client supports elicitation from the server.
 */
export interface McpClientCapabilitiesElicitation {
    /** Settings for elicitation by form. */
    form?: McpJSONObject,
    /** Settings for elicitation by URL. */
    url_settings?: McpJSONObject,
}


/**
 * Experimental, non-standard capabilities that the client supports.
 */
export interface McpClientCapabilitiesExperimental {
}


/**
 * Optional MCP extensions that the client supports. Keys are extension identifiers
(e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values are
per-extension settings objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix.
 */
export interface McpClientCapabilitiesExtensions {
}


/**
 * Present if the client supports listing roots.
 */
export interface McpClientCapabilitiesRoots {
}


/**
 * Present if the client supports sampling from an LLM.
 */
export interface McpClientCapabilitiesSampling {
    /** Whether the client supports context inclusion via `includeContext` parameter.
If not declared, servers SHOULD only use `includeContext: "none"` (or omit it). */
    context?: McpJSONObject,
    /** Whether the client supports tool use via `tools` and `toolChoice` parameters. */
    tools?: McpJSONObject,
}


/**
 * This notification is sent by the client to indicate that it is cancelling a request it previously issued.

On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

This notification indicates that the result will be unused, so any associated processing SHOULD cease.
 */
export interface McpClientNotification extends McpCancelledNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/cancelled`. */
    method: string,
    /** Parameters for a `notifications/cancelled` notification. */
    params: McpCancelledNotificationParams,
}


/**
 * One of `DiscoverRequest`, `ListResourcesRequest`, `ListResourceTemplatesRequest`, `ReadResourceRequest`, `SubscriptionsListenRequest`, `ListPromptsRequest`, `GetPromptRequest`, `ListToolsRequest`, `CallToolRequest`, `CompleteRequest`.
 */
export interface McpClientRequest {
}


/**
 * Common result fields.
 */
export interface McpClientResult extends McpEmptyResult {
}


/**
 * A request from the client to the server, to ask for completion options.
 */
export interface McpCompleteRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `completion/complete`. */
    method: string,
    /** Parameters for a `completion/complete` request. */
    params: McpCompleteRequestParams,
}


/**
 * Parameters for a `completion/complete` request.
 */
export interface McpCompleteRequestParams extends McpRequestParams {
    /** Additional, optional context for completions */
    context?: McpCompleteRequestParamsContext,
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** The argument's information */
    argument: McpCompleteRequestParamsArgument,
    /** What the completion is for: a prompt or a resource template. */
    ref: string,
}


/**
 * The argument's information
 */
export interface McpCompleteRequestParamsArgument {
    /** The name of the argument */
    name: string,
    /** The value of the argument to use for completion matching. */
    value: string,
}


/**
 * Additional, optional context for completions
 */
export interface McpCompleteRequestParamsContext {
    /** Previously-resolved variables in a URI template or prompt. */
    arguments?: McpCompleteRequestParamsContextArguments,
}


/**
 * Previously-resolved variables in a URI template or prompt.
 */
export interface McpCompleteRequestParamsContextArguments {
}


/**
 * The result returned by the server for a {@link CompleteRequestcompletion/complete} request.
 */
export interface McpCompleteResult extends McpResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** The completion values and whether more are available. */
    completion: McpCompleteResultCompletion,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
}


/**
 * The object MCP's `CompleteResult` holds under `completion`.
 */
export interface McpCompleteResultCompletion {
    /** Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown. */
    hasMore?: boolean,
    /** The total number of completion options available. This can exceed the number of values actually sent in the response. */
    total?: number,
    /** An array of completion values. Must not exceed 100 items. */
    values: string[],
}


/**
 * A successful response from the server for a {@link CompleteRequestcompletion/complete} request.
 */
export interface McpCompleteResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The result returned by the server for a {@link CompleteRequestcompletion/complete} request. */
    result: McpCompleteResult,
}


/**
 * One of `TextContent`, `ImageContent`, `AudioContent`, `ResourceLink`, `EmbeddedResource`.
 */
export interface McpContentBlock {
}


/**
 * A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.
 */
export interface McpCreateMessageRequest {
    /** The method's name, always `sampling/createMessage`. */
    method: string,
    /** Parameters for a `sampling/createMessage` request. */
    params: McpCreateMessageRequestParams,
}


/**
 * Parameters for a `sampling/createMessage` request.
 */
export interface McpCreateMessageRequestParams {
    /** A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.
The client MAY ignore this request.

Default is `"none"`. The values `"thisServer"` and `"allServers"` are deprecated (SEP-2596): servers SHOULD
omit this field or use `"none"`, and SHOULD only use the deprecated values if the client declares
{@link ClientCapabilities.sampling.context}. */
    includeContext?: string,
    /** The requested maximum number of tokens to sample (to prevent runaway completions).

The client MAY choose to sample fewer tokens than the requested maximum. */
    maxTokens: number,
    /** Describes a message issued to or received from an LLM API. */
    messages: McpSamplingMessage[],
    /** Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific. */
    metadata?: McpJSONObject,
    /** The server's preferences for which model to select. The client MAY ignore these preferences. */
    modelPreferences?: McpModelPreferences,
    /** Sequences at which the model should stop generating. */
    stopSequences?: string[],
    /** An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt. */
    systemPrompt?: string,
    /** The sampling temperature the server asks the model to use. */
    temperature?: number,
    /** Controls how the model uses tools.
The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared.
Default is `{ mode: "auto" }`. */
    toolChoice?: McpToolChoice,
    /** Tools that the model may use during generation.
The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared. */
    tools?: McpTool[],
}


/**
 * The result returned by the client for a {@link CreateMessageRequestsampling/createMessage} request.
The client should inform the user before returning the sampled message, to allow them
to inspect the response (human in the loop) and decide whether to allow the server to see it.
 */
export interface McpCreateMessageResult extends McpSamplingMessage {
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** The content the message carries. */
    content: string,
    /** The name of the model that generated the message. */
    model: string,
    /** The sender or recipient of messages and data in a conversation. */
    role: string,
    /** The reason why sampling stopped, if known.

Standard values:
- `"endTurn"`: Natural end of the assistant's turn
- `"stopSequence"`: A stop sequence was encountered
- `"maxTokens"`: Maximum token limit was reached
- `"toolUse"`: The model wants to use one or more tools

This field is an open string to allow for provider-specific stop reasons. */
    stopReason?: string,
}


/**
 * A request from the client asking the server to advertise its supported
protocol versions, capabilities, and other metadata. Servers **MUST**
implement `server/discover`. Clients **MAY** call it but are not required
to — version negotiation can also happen inline via per-request `_meta`.
 */
export interface McpDiscoverRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `server/discover`. */
    method: string,
    /** Common params for any request. */
    params: McpRequestParams,
}


/**
 * The result returned by the server for a {@link DiscoverRequestserver/discover} request.
 */
export interface McpDiscoverResult extends McpCacheableResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** The capabilities of the server. */
    capabilities: McpServerCapabilities,
    /** Natural-language guidance describing the server and its features.

This can be used by clients to improve an LLM's understanding of
available tools (e.g., by including it in a system prompt). It should
focus on information that helps the model use the server effectively
and should not duplicate information already in tool descriptions. */
    instructions?: string,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** MCP Protocol Versions this server supports. The client should choose a
version from this list for use in subsequent requests. */
    supportedVersions: string[],
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * A successful response from the server for a {@link DiscoverRequestserver/discover} request.
 */
export interface McpDiscoverResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The result returned by the server for a {@link DiscoverRequestserver/discover} request. */
    result: McpDiscoverResult,
}


/**
 * A request from the server to elicit additional information from the user via the client.
 */
export interface McpElicitRequest {
    /** The method's name, always `elicitation/create`. */
    method: string,
    /** The parameters for a request to elicit additional information from the user via the client. */
    params: McpElicitRequestParams,
}


/**
 * The parameters for a request to elicit non-sensitive information from the user via a form in the client.
 */
export interface McpElicitRequestFormParams {
    /** The message to present to the user describing what information is being requested. */
    message: string,
    /** The elicitation mode. */
    mode?: string,
    /** A restricted subset of JSON Schema.
Only top-level properties are allowed, without nesting. */
    requestedSchema: McpElicitRequestFormParamsRequestedSchema,
}


/**
 * A restricted subset of JSON Schema.
Only top-level properties are allowed, without nesting.
 */
export interface McpElicitRequestFormParamsRequestedSchema {
    /** The kind of object, always `object`. */
    type: string,
    /** The JSON Schema dialect the schema is written in. */
    schema_dialect?: string,
    /** The fields of the form, by name. */
    properties: McpElicitRequestFormParamsRequestedSchemaProperties,
    /** The names of the fields the user must fill in. */
    required_names?: string[],
}


/**
 * The object MCP's `ElicitRequestFormParams` holds under `properties`.
 */
export interface McpElicitRequestFormParamsRequestedSchemaProperties {
}


/**
 * The parameters for a request to elicit additional information from the user via the client.
 */
export interface McpElicitRequestParams {
}


/**
 * The parameters for a request to elicit information from the user via a URL in the client.
 */
export interface McpElicitRequestURLParams {
    /** The URL that the user should navigate to. */
    url: string,
    /** The message to present to the user explaining why the interaction is needed. */
    message: string,
    /** The elicitation mode. */
    mode: string,
}


/**
 * The result returned by the client for an {@link ElicitRequestelicitation/create} request.
 */
export interface McpElicitResult {
    /** The user action in response to the elicitation.
- `"accept"`: User submitted the form/confirmed the action
- `"decline"`: User explicitly declined the action
- `"cancel"`: User dismissed without making an explicit choice */
    action: string,
    /** The submitted form data, only present when action is `"accept"` and mode was `"form"`.
Contains values matching the requested schema.
Omitted for out-of-band mode responses. */
    content?: McpElicitResultContent,
}


/**
 * The submitted form data, only present when action is `"accept"` and mode was `"form"`.
Contains values matching the requested schema.
Omitted for out-of-band mode responses.
 */
export interface McpElicitResultContent {
}


/**
 * The contents of a resource, embedded into a prompt or tool call result.

It is up to the client how best to render embedded resources for the benefit
of the LLM and/or the user.
 */
export interface McpEmbeddedResource {
    /** The resource's contents, as text or as binary data. */
    resource: string,
    /** The kind of object, always `resource`. */
    type: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
}


/**
 * Common result fields.
 */
export interface McpEmptyResult extends McpResult {
}


/**
 * One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`, `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`, `LegacyTitledEnumSchema`.
 */
export interface McpEnumSchema {
}


/**
 * The error a JSON-RPC error response carries: a code, a message and any data.
 */
export interface McpError {
    /** The error type that occurred. */
    code: number,
    /** Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). */
    data?: McpJSONValue,
    /** A short description of the error. The message SHOULD be limited to a concise single sentence. */
    message: string,
}


/**
 * Used by the client to get a prompt provided by the server.
 */
export interface McpGetPromptRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `prompts/get`. */
    method: string,
    /** Parameters for a `prompts/get` request. */
    params: McpGetPromptRequestParams,
}


/**
 * Parameters for a `prompts/get` request.
 */
export interface McpGetPromptRequestParams extends McpInputResponseRequestParams {
    /** The name of the prompt or prompt template. */
    name: string,
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** Arguments to use for templating the prompt. */
    arguments?: McpGetPromptRequestParamsArguments,
    /** A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request. */
    inputResponses?: McpInputResponses,
    /** State the server returned with an input-required result, sent back unchanged when the request is retried. */
    requestState?: string,
}


/**
 * Arguments to use for templating the prompt.
 */
export interface McpGetPromptRequestParamsArguments {
}


/**
 * The result returned by the server for a {@link GetPromptRequestprompts/get} request.
 */
export interface McpGetPromptResult extends McpResult {
    /** An optional description for the prompt. */
    description?: string,
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Describes a message returned as part of a prompt.

This is similar to {@link SamplingMessage}, but also supports the embedding of
resources from the MCP server. */
    messages: McpPromptMessage[],
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
}


/**
 * A successful response from the server for a {@link GetPromptRequestprompts/get} request.
 */
export interface McpGetPromptResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** What the request returned. */
    result: string,
}


/**
 * Returned when a server rejects a request because the values in the HTTP
headers do not match the corresponding values in the request body, or
because required headers are missing or malformed. For HTTP, the response
status code MUST be `400 Bad Request`.
 */
export interface McpHeaderMismatchError extends McpJSONRPCErrorResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id?: string,
    /** The error the request ended with. */
    error: McpHeaderMismatchErrorError,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
}


/**
 * MCP's `Error`, with the code this error carries.
 */
export interface McpHeaderMismatchErrorError extends McpError {
    /** The error code, always `-32020`. */
    code: number,
}


/**
 * An optionally-sized icon that can be displayed in a user interface.
 */
export interface McpIcon {
    /** Optional MIME type override if the source MIME type is missing or generic.
For example: `"image/png"`, `"image/jpeg"`, or `"image/svg+xml"`. */
    mimeType?: string,
    /** Optional array of strings that specify sizes at which the icon can be used.
Each string should be in WxH format (e.g., `"48x48"`, `"96x96"`) or `"any"` for scalable formats like SVG.

If not provided, the client should assume that the icon can be used at any size. */
    sizes?: string[],
    /** A standard URI pointing to an icon resource. May be an HTTP/HTTPS URL or a
`data:` URI with Base64-encoded image data.

Consumers SHOULD take steps to ensure URLs serving icons are from the
same domain as the client/server or a trusted domain.

Consumers SHOULD take appropriate precautions when consuming SVGs as they can contain
executable JavaScript. */
    src: string,
    /** Optional specifier for the theme this icon is designed for. `"light"` indicates
the icon is designed to be used with a light background, and `"dark"` indicates
the icon is designed to be used with a dark background.

If not provided, the client should assume the icon can be used with any theme. */
    theme?: string,
}


/**
 * Base interface to add `icons` property.
 */
export interface McpIcons {
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
}


/**
 * An image provided to or from an LLM.
 */
export interface McpImageContent {
    /** The kind of object, always `image`. */
    type: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
    /** The base64-encoded image data. */
    data: string,
    /** The MIME type of the image. Different providers may support different image types. */
    mimeType: string,
}


/**
 * Describes the MCP implementation.
 */
export interface McpImplementation extends McpBaseMetadata, McpIcons {
    /** An optional human-readable description of what this implementation does.

This can be used by clients or servers to provide context about their purpose
and capabilities. For example, a server might describe the types of resources
or tools it provides, while a client might describe its intended use case. */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** The version of this implementation. */
    version: string,
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
    /** An optional URL of the website for this implementation. */
    websiteUrl?: string,
}


/**
 * One of `CreateMessageRequest`, `ListRootsRequest`, `ElicitRequest`.
 */
export interface McpInputRequest {
}


/**
 * A map of server-initiated requests that the client must fulfill.
Keys are server-assigned identifiers; values are the request objects.
 */
export interface McpInputRequests {
}


/**
 * An InputRequiredResult sent by the server to indicate that additional input is needed
before the request can be completed.

At least one of `inputRequests` or `requestState` MUST be present.
 */
export interface McpInputRequiredResult extends McpResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** A map of server-initiated requests that the client must fulfill.
Keys are server-assigned identifiers; values are the request objects. */
    inputRequests?: McpInputRequests,
    /** State for the client to send back unchanged when it retries the request. */
    requestState?: string,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
}


/**
 * One of `CreateMessageResult`, `ListRootsResult`, `ElicitResult`.
 */
export interface McpInputResponse {
}


/**
 * Parameters a client request may carry: its responses to an input-required result's requests, and the state the server returned.
 */
export interface McpInputResponseRequestParams extends McpRequestParams {
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request. */
    inputResponses?: McpInputResponses,
    /** State the server returned with an input-required result, sent back unchanged when the request is retried. */
    requestState?: string,
}


/**
 * A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request.
 */
export interface McpInputResponses {
}


/**
 * A JSON-RPC error indicating that an internal error occurred on the receiver. This error is returned when the receiver encounters an unexpected condition that prevents it from fulfilling the request.
 */
export interface McpInternalError extends McpError {
    /** The error type that occurred. */
    code: number,
    /** Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). */
    data?: McpJSONValue,
    /** A short description of the error. The message SHOULD be limited to a concise single sentence. */
    message: string,
}


/**
 * A JSON-RPC error indicating that the method parameters are invalid or malformed.

In MCP, this error is returned in various contexts when request parameters fail validation:

- **Tools**: Unknown tool name or invalid tool arguments
- **Prompts**: Unknown prompt name or missing required arguments
- **Pagination**: Invalid or expired cursor values
- **Logging**: Invalid log level
- **Elicitation**: Server requests an elicitation mode not declared in client capabilities
- **Sampling**: Missing tool result or tool results mixed with other content
 */
export interface McpInvalidParamsError extends McpError {
    /** The error type that occurred. */
    code: number,
    /** Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). */
    data?: McpJSONValue,
    /** A short description of the error. The message SHOULD be limited to a concise single sentence. */
    message: string,
}


/**
 * A JSON-RPC error indicating that the request is not a valid request object. This error is returned when the message structure does not conform to the JSON-RPC 2.0 specification requirements for a request (e.g., missing required fields like `jsonrpc` or `method`, or using invalid types for these fields).
 */
export interface McpInvalidRequestError extends McpError {
    /** The error type that occurred. */
    code: number,
    /** Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). */
    data?: McpJSONValue,
    /** A short description of the error. The message SHOULD be limited to a concise single sentence. */
    message: string,
}


/**
 * A JSON object, whose values are JSON values.
 */
export interface McpJSONObject {
}


/**
 * A response to a request that indicates an error occurred.
 */
export interface McpJSONRPCErrorResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id?: string,
    /** The error the request ended with. */
    error: McpError,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
}


/**
 * Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.
 */
export interface McpJSONRPCMessage {
}


/**
 * A notification which does not expect a response.
 */
export interface McpJSONRPCNotification extends McpNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The name of the method. */
    method: string,
    /** The parameters the message carries. */
    params?: McpJSONObject,
}


/**
 * A request that expects a response.
 */
export interface McpJSONRPCRequest extends McpRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The name of the method. */
    method: string,
    /** The parameters the message carries. */
    params?: McpJSONObject,
}


/**
 * A response to a request, containing either the result or error.
 */
export interface McpJSONRPCResponse {
}


/**
 * A successful (non-error) response to a request.
 */
export interface McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** Common result fields. */
    result: McpResult,
}


/**
 * Any JSON value: a string, a number, a boolean, null, an object or an array.
 */
export interface McpJSONValue {
}


/**
 * Use {@link TitledSingleSelectEnumSchema} instead.
This interface will be removed in a future version.
 */
export interface McpLegacyTitledEnumSchema {
    /** A description of the field for the user. */
    description?: string,
    /** A title for the field. */
    title?: string,
    /** The kind of object, always `string`. */
    type: string,
    /** The value the field takes when the user gives none. */
    default?: string,
    /** The values the field offers. */
    enum: string[],
    /** (Legacy) Display names for enum values.
Non-standard according to JSON schema 2020-12. */
    enumNames?: string[],
}


/**
 * Sent from the client to request a list of prompts and prompt templates the server has.
 */
export interface McpListPromptsRequest extends McpPaginatedRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `prompts/list`. */
    method: string,
    /** Common params for paginated requests. */
    params: McpPaginatedRequestParams,
}


/**
 * The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
 */
export interface McpListPromptsResult extends McpPaginatedResult, McpCacheableResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** An opaque token representing the pagination position after the last returned result.
If present, there may be more results available. */
    nextCursor?: string,
    /** A prompt or prompt template that the server offers. */
    prompts: McpPrompt[],
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * A successful response from the server for a {@link ListPromptsRequestprompts/list} request.
 */
export interface McpListPromptsResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The result returned by the server for a {@link ListPromptsRequestprompts/list} request. */
    result: McpListPromptsResult,
}


/**
 * Sent from the client to request a list of resource templates the server has.
 */
export interface McpListResourceTemplatesRequest extends McpPaginatedRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `resources/templates/list`. */
    method: string,
    /** Common params for paginated requests. */
    params: McpPaginatedRequestParams,
}


/**
 * The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
 */
export interface McpListResourceTemplatesResult extends McpPaginatedResult, McpCacheableResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** An opaque token representing the pagination position after the last returned result.
If present, there may be more results available. */
    nextCursor?: string,
    /** A template description for resources available on the server. */
    resourceTemplates: McpResourceTemplate[],
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * A successful response from the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
 */
export interface McpListResourceTemplatesResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request. */
    result: McpListResourceTemplatesResult,
}


/**
 * Sent from the client to request a list of resources the server has.
 */
export interface McpListResourcesRequest extends McpPaginatedRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `resources/list`. */
    method: string,
    /** Common params for paginated requests. */
    params: McpPaginatedRequestParams,
}


/**
 * The result returned by the server for a {@link ListResourcesRequestresources/list} request.
 */
export interface McpListResourcesResult extends McpPaginatedResult, McpCacheableResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** An opaque token representing the pagination position after the last returned result.
If present, there may be more results available. */
    nextCursor?: string,
    /** A known resource that the server is capable of reading. */
    resources: McpResource[],
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * A successful response from the server for a {@link ListResourcesRequestresources/list} request.
 */
export interface McpListResourcesResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The result returned by the server for a {@link ListResourcesRequestresources/list} request. */
    result: McpListResourcesResult,
}


/**
 * Sent from the server to request a list of root URIs from the client. Roots allow
servers to ask for specific directories or files to operate on. A common example
for roots is providing a set of repositories or directories a server should operate
on.

This request is typically used when the server needs to understand the file system
structure or access specific locations that the client has permission to read from.
 */
export interface McpListRootsRequest {
    /** The method's name, always `roots/list`. */
    method: string,
    /** The parameters the message carries. */
    params?: McpListRootsRequestParams,
}


/**
 * The object MCP's `ListRootsRequest` holds under `params`.
 */
export interface McpListRootsRequestParams {
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
}


/**
 * The result returned by the client for a {@link ListRootsRequestroots/list} request.
This result contains an array of {@link Root} objects, each representing a root directory
or file that the server can operate on.
 */
export interface McpListRootsResult {
    /** Represents a root directory or file that the server can operate on. */
    roots: McpRoot[],
}


/**
 * Sent from the client to request a list of tools the server has.
 */
export interface McpListToolsRequest extends McpPaginatedRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `tools/list`. */
    method: string,
    /** Common params for paginated requests. */
    params: McpPaginatedRequestParams,
}


/**
 * The result returned by the server for a {@link ListToolsRequesttools/list} request.
 */
export interface McpListToolsResult extends McpPaginatedResult, McpCacheableResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** An opaque token representing the pagination position after the last returned result.
If present, there may be more results available. */
    nextCursor?: string,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** Definition for a tool the client can call. */
    tools: McpTool[],
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * A successful response from the server for a {@link ListToolsRequesttools/list} request.
 */
export interface McpListToolsResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The result returned by the server for a {@link ListToolsRequesttools/list} request. */
    result: McpListToolsResult,
}


/**
 * JSONRPCNotification of a log message passed from server to client. The client opts in by setting `"io.modelcontextprotocol/logLevel"` in a request's `_meta`.
 */
export interface McpLoggingMessageNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/message`. */
    method: string,
    /** Parameters for a `notifications/message` notification. */
    params: McpLoggingMessageNotificationParams,
}


/**
 * Parameters for a `notifications/message` notification.
 */
export interface McpLoggingMessageNotificationParams extends McpNotificationParams {
    /** Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpNotificationMetaObject,
    /** The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here. */
    data: McpJSONValue,
    /** The severity of this log message. */
    level: string,
    /** An optional name of the logger issuing this message. */
    logger?: string,
}


/**
 * Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

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
 */
export interface McpMetaObject {
}


/**
 * A JSON-RPC error indicating that the requested method does not exist or is not available.

In MCP, a server returns this error when a client invokes a method the server does not implement — either a genuinely unknown method, or one gated behind a server capability the server did not advertise (e.g., calling `prompts/list` when the `prompts` capability was not advertised).

A request that requires a client capability the client did not declare is signalled instead by {@link MissingRequiredClientCapabilityError} (`-32021`).
 */
export interface McpMethodNotFoundError extends McpError {
    /** The error type that occurred. */
    code: number,
    /** Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). */
    data?: McpJSONValue,
    /** A short description of the error. The message SHOULD be limited to a concise single sentence. */
    message: string,
}


/**
 * Returned when processing a request requires a capability the client did not
declare in `clientCapabilities`. For HTTP, the response status code MUST be
`400 Bad Request`.
 */
export interface McpMissingRequiredClientCapabilityError extends McpJSONRPCErrorResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id?: string,
    /** The error the request ended with. */
    error: McpMissingRequiredClientCapabilityErrorError,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
}


/**
 * MCP's `Error`, with the code and data this error carries.
 */
export interface McpMissingRequiredClientCapabilityErrorError extends McpError {
    /** The error code, always `-32021`. */
    code: number,
    /** Details of the error. */
    data: McpMissingRequiredClientCapabilityErrorErrorData,
}


/**
 * The object MCP's `MissingRequiredClientCapabilityError` holds under `data`.
 */
export interface McpMissingRequiredClientCapabilityErrorErrorData {
    /** The capabilities the server requires from the client to process this request. */
    requiredCapabilities: McpClientCapabilities,
}


/**
 * Hints to use for model selection.

Keys not declared here are currently left unspecified by the spec and are up
to the client to interpret.
 */
export interface McpModelHint {
    /** A hint for a model name.

The client SHOULD treat this as a substring of a model name; for example:
 - `claude-3-5-sonnet` should match `claude-3-5-sonnet-20241022`
 - `sonnet` should match `claude-3-5-sonnet-20241022`, `claude-3-sonnet-20240229`, etc.
 - `claude` should match any Claude model

The client MAY also map the string to a different provider's model name or a different model family, as long as it fills a similar niche; for example:
 - `gemini-1.5-flash` could match `claude-3-haiku-20240307` */
    name?: string,
}


/**
 * The server's preferences for model selection, requested of the client during sampling.

Because LLMs can vary along multiple dimensions, choosing the "best" model is
rarely straightforward.  Different models excel in different areas—some are
faster but less capable, others are more capable but more expensive, and so
on. This interface allows servers to express their priorities across multiple
dimensions to help clients make an appropriate selection for their use case.

These preferences are always advisory. The client MAY ignore them. It is also
up to the client to decide how to interpret these preferences and how to
balance them against other considerations.
 */
export interface McpModelPreferences {
    /** How much to prioritize cost when selecting a model. A value of 0 means cost
is not important, while a value of 1 means cost is the most important
factor. */
    costPriority?: number,
    /** Optional hints to use for model selection.

If multiple hints are specified, the client MUST evaluate them in order
(such that the first match is taken).

The client SHOULD prioritize these hints over the numeric priorities, but
MAY still use the priorities to select from ambiguous matches. */
    hints?: McpModelHint[],
    /** How much to prioritize intelligence and capabilities when selecting a
model. A value of 0 means intelligence is not important, while a value of 1
means intelligence is the most important factor. */
    intelligencePriority?: number,
    /** How much to prioritize sampling speed (latency) when selecting a model. A
value of 0 means speed is not important, while a value of 1 means speed is
the most important factor. */
    speedPriority?: number,
}


/**
 * One of `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`.
 */
export interface McpMultiSelectEnumSchema {
}


/**
 * The method and the parameters a notification carries.
 */
export interface McpNotification {
    /** The name of the method. */
    method: string,
    /** The parameters the message carries. */
    params?: McpJSONObject,
}


/**
 * Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
 */
export interface McpNotificationMetaObject extends McpMetaObject {
    /** Identifies the subscription stream a notification was delivered on. The
server MUST include this key on every notification delivered via a
{@link SubscriptionsListenRequestsubscriptions/listen} stream, so the
client can correlate the notification with the originating subscription.
The key is absent on notifications not delivered via a subscription
stream (e.g. progress notifications for an in-flight request), which is
why it is optional here.

The value is the JSON-RPC ID of the `subscriptions/listen` request that
opened the stream. */
    mcp_subscription_id?: string,
}


/**
 * Common params for any notification.
 */
export interface McpNotificationParams {
    /** Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpNotificationMetaObject,
}


/**
 * A field of an elicitation form that takes a number or an integer.
 */
export interface McpNumberSchema {
    /** A description of the field for the user. */
    description?: string,
    /** A title for the field. */
    title?: string,
    /** The kind of value the field takes. */
    type: string,
    /** The value the field takes when the user gives none. */
    default?: number,
    /** The largest value the field accepts. */
    maximum?: number,
    /** The smallest value the field accepts. */
    minimum?: number,
}


/**
 * A request for a list that the server returns a page at a time.
 */
export interface McpPaginatedRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The name of the method. */
    method: string,
    /** Common params for paginated requests. */
    params: McpPaginatedRequestParams,
}


/**
 * Common params for paginated requests.
 */
export interface McpPaginatedRequestParams extends McpRequestParams {
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** An opaque token representing the current pagination position.
If provided, the server should return results starting after this cursor. */
    cursor?: string,
}


/**
 * A result that holds a page of a list, and the cursor of the next page.
 */
export interface McpPaginatedResult extends McpResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** An opaque token representing the pagination position after the last returned result.
If present, there may be more results available. */
    nextCursor?: string,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
}


/**
 * A JSON-RPC error indicating that invalid JSON was received by the server. This error is returned when the server cannot parse the JSON text of a message.
 */
export interface McpParseError extends McpError {
    /** The error type that occurred. */
    code: number,
    /** Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). */
    data?: McpJSONValue,
    /** A short description of the error. The message SHOULD be limited to a concise single sentence. */
    message: string,
}


/**
 * Restricted schema definitions that only allow primitive types
without nested objects or arrays.
 */
export interface McpPrimitiveSchemaDefinition {
}


/**
 * An out-of-band notification used to inform the receiver of a progress update for a long-running request.
 */
export interface McpProgressNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/progress`. */
    method: string,
    /** Parameters for a {@link ProgressNotificationnotifications/progress} notification. */
    params: McpProgressNotificationParams,
}


/**
 * Parameters for a {@link ProgressNotificationnotifications/progress} notification.
 */
export interface McpProgressNotificationParams extends McpNotificationParams {
    /** Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpNotificationMetaObject,
    /** An optional message describing the current progress. */
    message?: string,
    /** The progress thus far. This should increase every time progress is made, even if the total is unknown. */
    progress: number,
    /** The progress token which was given in the initial request, used to associate this notification with the request that is proceeding. */
    progressToken: string,
    /** Total number of items to process (or total progress required), if known. */
    total?: number,
}


/**
 * A prompt or prompt template that the server offers.
 */
export interface McpPrompt extends McpBaseMetadata, McpIcons {
    /** An optional description of what this prompt provides */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** A list of arguments to use for templating the prompt. */
    arguments?: McpPromptArgument[],
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
}


/**
 * Describes an argument that a prompt can accept.
 */
export interface McpPromptArgument extends McpBaseMetadata {
    /** A human-readable description of the argument. */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** Whether this argument must be provided. */
    required?: boolean,
}


/**
 * An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `promptsListChanged` filter field.
 */
export interface McpPromptListChangedNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/prompts/list_changed`. */
    method: string,
    /** Common params for any notification. */
    params?: McpNotificationParams,
}


/**
 * Describes a message returned as part of a prompt.

This is similar to {@link SamplingMessage}, but also supports the embedding of
resources from the MCP server.
 */
export interface McpPromptMessage {
    /** The content the message carries. */
    content: McpContentBlock,
    /** The sender or recipient of messages and data in a conversation. */
    role: string,
}


/**
 * Identifies a prompt.
 */
export interface McpPromptReference extends McpBaseMetadata {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** The kind of object, always `ref/prompt`. */
    type: string,
}


/**
 * Sent from the client to the server, to read a specific resource URI.
 */
export interface McpReadResourceRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `resources/read`. */
    method: string,
    /** Parameters for a `resources/read` request. */
    params: McpReadResourceRequestParams,
}


/**
 * Parameters for a `resources/read` request.
 */
export interface McpReadResourceRequestParams extends McpResourceRequestParams, McpInputResponseRequestParams {
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** A map of client responses to server-initiated requests.
Keys correspond to the keys in the {@link InputRequests} map;
values are the client's result for each request. */
    inputResponses?: McpInputResponses,
    /** State the server returned with an input-required result, sent back unchanged when the request is retried. */
    requestState?: string,
    /** The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it. */
    uri: string,
}


/**
 * The result returned by the server for a {@link ReadResourceRequestresources/read} request.
 */
export interface McpReadResourceResult extends McpCacheableResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the intended scope of the cached response, analogous to HTTP
`Cache-Control: public` vs `Cache-Control: private`.

- `"public"`: The response does not contain user-specific data. Any
  client or intermediary (e.g., shared gateway, caching proxy) MAY cache
  the response and serve it across authorization contexts.
- `"private"`: The response MAY be cached and reused only within the
  same authorization context. Caches MUST NOT be shared across
  authorization contexts (e.g., a different access token requires a
  different cache). */
    cacheScope: string,
    /** The contents of the resource that was read. */
    contents: string[],
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
    /** A hint from the server indicating how long (in milliseconds) the
client MAY cache this response before re-fetching. Semantics are
analogous to HTTP Cache-Control max-age.

- If 0, The response SHOULD be considered immediately stale,
  The client MAY re-fetch every time the result is needed.
- If positive, the client SHOULD consider the result fresh for this many
  milliseconds after receiving the response. */
    ttlMs: number,
}


/**
 * A successful response from the server for a {@link ReadResourceRequestresources/read} request.
 */
export interface McpReadResourceResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** What the request returned. */
    result: string,
}


/**
 * The method and the parameters a request carries.
 */
export interface McpRequest {
    /** The name of the method. */
    method: string,
    /** The parameters the message carries. */
    params?: McpJSONObject,
}


/**
 * Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
 */
export interface McpRequestMetaObject extends McpMetaObject {
    /** The client's capabilities for this specific request. Required.

Capabilities are declared per-request rather than once at initialization;
an empty object means the client supports no optional capabilities.
Servers MUST NOT infer capabilities from prior requests. */
    mcp_client_capabilities: McpClientCapabilities,
    /** Identifies the client software making the request. Clients SHOULD
include this field on every request unless specifically configured not
to do so.

The {@link Implementation} schema requires `name` and `version`; other
fields are optional.

The value is self-reported by the client and is not verified by the
protocol. It is intended for display, logging, and debugging. Servers
SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
security decisions. */
    mcp_client_info?: McpImplementation,
    /** The desired log level for this request. Optional.

If absent, the server MUST NOT send any {@link LoggingMessageNotificationnotifications/message}
notifications for this request. The client opts in to log messages by
explicitly setting a level. Replaces the former `logging/setLevel` RPC. */
    mcp_log_level?: string,
    /** The MCP Protocol Version being used for this request. Required.

For the HTTP transport, this value MUST match the `MCP-Protocol-Version`
header; otherwise the server MUST return a `400 Bad Request`. If the
server does not support the requested version, it MUST return an
{@link UnsupportedProtocolVersionError}. */
    mcp_protocol_version: string,
    /** If specified, the caller is requesting out-of-band progress notifications for this request (as represented by {@link ProgressNotificationnotifications/progress}). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. */
    progressToken?: string,
}


/**
 * Common params for any request.
 */
export interface McpRequestParams {
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
}


/**
 * A known resource that the server is capable of reading.
 */
export interface McpResource extends McpBaseMetadata, McpIcons {
    /** A description of what this resource represents.

This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model. */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
    /** The MIME type of this resource, if known. */
    mimeType?: string,
    /** The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

This can be used by Hosts to display file sizes and estimate context window usage. */
    size?: number,
    /** The URI of this resource. */
    uri: string,
}


/**
 * The contents of a specific resource or sub-resource.
 */
export interface McpResourceContents {
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** The MIME type of this resource, if known. */
    mimeType?: string,
    /** The URI of this resource. */
    uri: string,
}


/**
 * A resource that the server is capable of reading, included in a prompt or tool call result.

Note: resource links returned by tools are not guaranteed to appear in the results of {@link ListResourcesRequestresources/list} requests.
 */
export interface McpResourceLink extends McpResource {
    /** A description of what this resource represents.

This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model. */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** The kind of object, always `resource_link`. */
    type: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
    /** The MIME type of this resource, if known. */
    mimeType?: string,
    /** The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

This can be used by Hosts to display file sizes and estimate context window usage. */
    size?: number,
    /** The URI of this resource. */
    uri: string,
}


/**
 * An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `resourcesListChanged` filter field.
 */
export interface McpResourceListChangedNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/resources/list_changed`. */
    method: string,
    /** Common params for any notification. */
    params?: McpNotificationParams,
}


/**
 * Common params for resource-related requests.
 */
export interface McpResourceRequestParams extends McpRequestParams {
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it. */
    uri: string,
}


/**
 * A template description for resources available on the server.
 */
export interface McpResourceTemplate extends McpBaseMetadata, McpIcons {
    /** A description of what this template is for.

This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model. */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
    /** The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type. */
    mimeType?: string,
    /** A URI template (according to RFC 6570) that can be used to construct resource URIs. */
    uriTemplate: string,
}


/**
 * A reference to a resource or resource template definition.
 */
export interface McpResourceTemplateReference {
    /** The kind of object, always `ref/resource`. */
    type: string,
    /** The URI or URI template of the resource. */
    uri: string,
}


/**
 * A notification from the server to the client, informing it that a resource has changed and may need to be read again. This is only sent for resources the client opted in to via the `resourceSubscriptions` field of a {@link SubscriptionsListenRequestsubscriptions/listen} request.
 */
export interface McpResourceUpdatedNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/resources/updated`. */
    method: string,
    /** Parameters for a `notifications/resources/updated` notification. */
    params: McpResourceUpdatedNotificationParams,
}


/**
 * Parameters for a `notifications/resources/updated` notification.
 */
export interface McpResourceUpdatedNotificationParams extends McpNotificationParams {
    /** Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpNotificationMetaObject,
    /** The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to. */
    uri: string,
}


/**
 * Common result fields.
 */
export interface McpResult {
    /** Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpResultMetaObject,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
}


/**
 * Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
 */
export interface McpResultMetaObject extends McpMetaObject {
    /** Identifies the server software producing the response. Servers SHOULD
include this field on every response unless specifically configured not
to do so.

The {@link Implementation} schema requires `name` and `version`; other
fields are optional.

The value is self-reported by the server and is not verified by the
protocol. It is intended for display, logging, and debugging. Clients
SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
security decisions. */
    mcp_server_info?: McpImplementation,
}


/**
 * Represents a root directory or file that the server can operate on.
 */
export interface McpRoot {
    /** An optional name for the root. This can be used to provide a human-readable
identifier for the root, which may be useful for display purposes or for
referencing the root in other parts of the application. */
    name?: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** The URI identifying the root. This *must* start with `file://` for now.
This restriction may be relaxed in future versions of the protocol to allow
other URI schemes. */
    uri: string,
}


/**
 * Describes a message issued to or received from an LLM API.
 */
export interface McpSamplingMessage {
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** The content the message carries. */
    content: string,
    /** The sender or recipient of messages and data in a conversation. */
    role: string,
}


/**
 * One of `TextContent`, `ImageContent`, `AudioContent`, `ToolUseContent`, `ToolResultContent`.
 */
export interface McpSamplingMessageContentBlock {
}


/**
 * Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.
 */
export interface McpServerCapabilities {
    /** Present if the server supports argument autocompletion suggestions. */
    completions?: McpJSONObject,
    /** Experimental, non-standard capabilities that the server supports. */
    experimental?: McpServerCapabilitiesExperimental,
    /** Optional MCP extensions that the server supports. Keys are extension identifiers
(e.g., "io.modelcontextprotocol/tasks"), and values are per-extension settings
objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix. */
    extensions?: McpServerCapabilitiesExtensions,
    /** Present if the server supports sending log messages to the client. */
    logging?: McpJSONObject,
    /** Present if the server offers any prompt templates. */
    prompts?: McpServerCapabilitiesPrompts,
    /** Present if the server offers any resources to read. */
    resources?: McpServerCapabilitiesResources,
    /** Present if the server offers any tools to call. */
    tools?: McpServerCapabilitiesTools,
}


/**
 * Experimental, non-standard capabilities that the server supports.
 */
export interface McpServerCapabilitiesExperimental {
}


/**
 * Optional MCP extensions that the server supports. Keys are extension identifiers
(e.g., "io.modelcontextprotocol/tasks"), and values are per-extension settings
objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix.
 */
export interface McpServerCapabilitiesExtensions {
}


/**
 * Present if the server offers any prompt templates.
 */
export interface McpServerCapabilitiesPrompts {
    /** Whether this server supports notifications for changes to the prompt list. */
    listChanged?: boolean,
}


/**
 * Present if the server offers any resources to read.
 */
export interface McpServerCapabilitiesResources {
    /** Whether this server supports notifications for changes to the resource list. */
    listChanged?: boolean,
    /** Whether this server supports subscribing to resource updates. */
    subscribe?: boolean,
}


/**
 * Present if the server offers any tools to call.
 */
export interface McpServerCapabilitiesTools {
    /** Whether this server supports notifications for changes to the tool list. */
    listChanged?: boolean,
}


/**
 * One of `CancelledNotification`, `ProgressNotification`, `ResourceListChangedNotification`, `SubscriptionsAcknowledgedNotification`, `ResourceUpdatedNotification`, `PromptListChangedNotification`, `ToolListChangedNotification`, `LoggingMessageNotification`.
 */
export interface McpServerNotification {
}


/**
 * One of `Result`, `InputRequiredResult`, `DiscoverResult`, `ListResourcesResult`, `ListResourceTemplatesResult`, `ReadResourceResult`, `SubscriptionsListenResult`, `ListPromptsResult`, `GetPromptResult`, `ListToolsResult`, `CallToolResult`, `CompleteResult`.
 */
export interface McpServerResult {
}


/**
 * One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`.
 */
export interface McpSingleSelectEnumSchema {
}


/**
 * A field of an elicitation form that takes text.
 */
export interface McpStringSchema {
    /** A description of the field for the user. */
    description?: string,
    /** A title for the field. */
    title?: string,
    /** The kind of object, always `string`. */
    type: string,
    /** The value the field takes when the user gives none. */
    default?: string,
    /** The format the string must have. */
    format?: string,
    /** The most characters the field accepts. */
    maxLength?: number,
    /** The fewest characters the field accepts. */
    minLength?: number,
}


/**
 * The set of notification types a client may opt in to on a
{@link SubscriptionsListenRequestsubscriptions/listen} request.

Each notification type is **opt-in**; the server **MUST NOT** send
notification types the client has not explicitly requested here.
 */
export interface McpSubscriptionFilter {
    /** If true, receive {@link PromptListChangedNotificationnotifications/prompts/list_changed}. */
    promptsListChanged?: boolean,
    /** Subscribe to {@link ResourceUpdatedNotificationnotifications/resources/updated} for these resource URIs.
Replaces the former `resources/subscribe` RPC. */
    resourceSubscriptions?: string[],
    /** If true, receive {@link ResourceListChangedNotificationnotifications/resources/list_changed}. */
    resourcesListChanged?: boolean,
    /** If true, receive {@link ToolListChangedNotificationnotifications/tools/list_changed}. */
    toolsListChanged?: boolean,
}


/**
 * Sent by the server to acknowledge that a
{@link SubscriptionsListenRequestsubscriptions/listen} subscription has been
established and to report which notification types it agreed to honor.

This notification MUST be the first message the server sends carrying the
subscription's ID in `io.modelcontextprotocol/subscriptionId`. The server MUST
NOT send any notification on the subscription before acknowledging it. On
stdio, where every subscription shares one channel, this ordering is defined
per subscription ID and not per channel: messages belonging to other
subscriptions MAY be interleaved before it.
 */
export interface McpSubscriptionsAcknowledgedNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/subscriptions/acknowledged`. */
    method: string,
    /** Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification. */
    params: McpSubscriptionsAcknowledgedNotificationParams,
}


/**
 * Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.
 */
export interface McpSubscriptionsAcknowledgedNotificationParams extends McpNotificationParams {
    /** Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply. */
    _meta?: McpNotificationMetaObject,
    /** The subset of requested notification types the server agreed to honor.
Only includes notification types the server actually supports; if the
client requested an unsupported type (e.g., `promptsListChanged` when
the server has no prompts), it is omitted from this set. */
    notifications: McpSubscriptionFilter,
}


/**
 * Sent from the client to open a long-lived channel for receiving notifications
outside the context of a specific request. Replaces the previous HTTP GET
endpoint and ensures consistent behavior between HTTP and STDIO.
 */
export interface McpSubscriptionsListenRequest extends McpJSONRPCRequest {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `subscriptions/listen`. */
    method: string,
    /** Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request. */
    params: McpSubscriptionsListenRequestParams,
}


/**
 * Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.
 */
export interface McpSubscriptionsListenRequestParams extends McpRequestParams {
    /** Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply. */
    _meta: McpRequestMetaObject,
    /** The notifications the client opts in to on this stream. The server
**MUST NOT** send notification types the client has not explicitly
requested. */
    notifications: McpSubscriptionFilter,
}


/**
 * The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
request, signalling that the subscription has ended gracefully (for example,
during server shutdown). Because the listen stream is long-lived, this result
is sent only when the server tears the subscription down; an abrupt transport
close carries no response. The result body is otherwise empty.
 */
export interface McpSubscriptionsListenResult extends McpResult {
    /** Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
{@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply. */
    _meta: McpSubscriptionsListenResultMetaObject,
    /** Indicates the type of the result, which allows the client to determine
how to parse the result object.

Servers implementing this protocol version MUST include this field.
For backward compatibility, when a client receives a result from a
server implementing an earlier protocol version (which does not include
`resultType`), the client MUST treat the absent field as `"complete"`. */
    resultType: string,
}


/**
 * Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
{@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
 */
export interface McpSubscriptionsListenResultMetaObject extends McpResultMetaObject {
    /** Identifies the server software producing the response. Servers SHOULD
include this field on every response unless specifically configured not
to do so.

The {@link Implementation} schema requires `name` and `version`; other
fields are optional.

The value is self-reported by the server and is not verified by the
protocol. It is intended for display, logging, and debugging. Clients
SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
security decisions. */
    mcp_server_info?: McpImplementation,
    /** Identifies the subscription stream this response closes, so the client can
correlate it with the originating subscription — mirroring the same key on
the stream's notifications. The value is the JSON-RPC ID of the
`subscriptions/listen` request that opened the stream (and equals this
response's `id`). */
    mcp_subscription_id: string,
}


/**
 * A successful response from the server for a {@link SubscriptionsListenRequestsubscriptions/listen}
request, sent when the server tears the subscription down gracefully.
 */
export interface McpSubscriptionsListenResultResponse extends McpJSONRPCResultResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id: string,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
request, signalling that the subscription has ended gracefully (for example,
during server shutdown). Because the listen stream is long-lived, this result
is sent only when the server tears the subscription down; an abrupt transport
close carries no response. The result body is otherwise empty. */
    result: McpSubscriptionsListenResult,
}


/**
 * Text provided to or from an LLM.
 */
export interface McpTextContent {
    /** The kind of object, always `text`. */
    type: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional annotations for the client. */
    annotations?: McpAnnotations,
    /** The text content of the message. */
    text: string,
}


/**
 * A resource's contents as text.
 */
export interface McpTextResourceContents extends McpResourceContents {
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** The MIME type of this resource, if known. */
    mimeType?: string,
    /** The text of the item. This must only be set if the item can actually be represented as text (not binary data). */
    text: string,
    /** The URI of this resource. */
    uri: string,
}


/**
 * Schema for multiple-selection enumeration with display titles for each option.
 */
export interface McpTitledMultiSelectEnumSchema {
    /** Optional description for the enum field. */
    description?: string,
    /** Optional title for the enum field. */
    title?: string,
    /** The kind of object, always `array`. */
    type: string,
    /** Optional default value. */
    default?: string[],
    /** Schema for array items with enum options and display labels. */
    items: McpTitledMultiSelectEnumSchemaItems,
    /** Maximum number of items to select. */
    maxItems?: number,
    /** Minimum number of items to select. */
    minItems?: number,
}


/**
 * Schema for array items with enum options and display labels.
 */
export interface McpTitledMultiSelectEnumSchemaItems {
    /** Array of enum options with values and display labels. */
    anyOf: McpTitledMultiSelectEnumSchemaItemsAnyOf[],
}


/**
 * The object MCP's `TitledMultiSelectEnumSchema` holds under `anyOf`.
 */
export interface McpTitledMultiSelectEnumSchemaItemsAnyOf {
    /** Display title for this option. */
    title: string,
    /** The constant enum value. */
    const: string,
}


/**
 * Schema for single-selection enumeration with display titles for each option.
 */
export interface McpTitledSingleSelectEnumSchema {
    /** Optional description for the enum field. */
    description?: string,
    /** Optional title for the enum field. */
    title?: string,
    /** The kind of object, always `string`. */
    type: string,
    /** Optional default value. */
    default?: string,
    /** Array of enum options with values and display labels. */
    oneOf: McpTitledSingleSelectEnumSchemaOneOf[],
}


/**
 * The object MCP's `TitledSingleSelectEnumSchema` holds under `oneOf`.
 */
export interface McpTitledSingleSelectEnumSchemaOneOf {
    /** Display label for this option. */
    title: string,
    /** The enum value. */
    const: string,
}


/**
 * Definition for a tool the client can call.
 */
export interface McpTool extends McpBaseMetadata, McpIcons {
    /** A human-readable description of the tool.

This can be used by clients to improve the LLM's understanding of available tools. It can be thought of like a "hint" to the model. */
    description?: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present). */
    name: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for {@link Tool},
where `annotations.title` should be given precedence over using `name`,
if present). */
    title?: string,
    /** Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`). */
    _meta?: McpMetaObject,
    /** Optional additional tool information.

Display name precedence order is: `title`, `annotations.title`, then `name`. */
    annotations?: McpToolAnnotations,
    /** Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:
- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:
- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format) */
    icons?: McpIcon[],
    /** A JSON Schema object defining the expected parameters for the tool.

Tool arguments are always JSON objects, so `type: "object"` is required at the root.
Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — including
composition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords
(`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any other
standard validation or annotation keywords.

Property schemas may carry an `x-mcp-header` annotation to mirror the
argument value into an HTTP header on the Streamable HTTP transport. See
the Streamable HTTP transport specification for the validity and
extraction rules.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided. */
    inputSchema: McpToolInputSchema,
    /** An optional JSON Schema object defining the structure of the tool's output returned in
the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided. */
    outputSchema?: McpToolOutputSchema,
}


/**
 * Additional properties describing a {@link Tool} to clients.

NOTE: all properties in `ToolAnnotations` are **hints**.
They are not guaranteed to provide a faithful description of
tool behavior (including descriptive properties like `title`).

Clients should never make tool use decisions based on `ToolAnnotations`
received from untrusted servers.
 */
export interface McpToolAnnotations {
    /** A human-readable title for the tool. */
    title?: string,
    /** If true, the tool may perform destructive updates to its environment.
If false, the tool performs only additive updates.

(This property is meaningful only when `readOnlyHint == false`)

Default: true */
    destructiveHint?: boolean,
    /** If true, calling the tool repeatedly with the same arguments
will have no additional effect on its environment.

(This property is meaningful only when `readOnlyHint == false`)

Default: false */
    idempotentHint?: boolean,
    /** If true, this tool may interact with an "open world" of external
entities. If false, the tool's domain of interaction is closed.
For example, the world of a web search tool is open, whereas that
of a memory tool is not.

Default: true */
    openWorldHint?: boolean,
    /** If true, the tool does not modify its environment.

Default: false */
    readOnlyHint?: boolean,
}


/**
 * Controls tool selection behavior for sampling requests.
 */
export interface McpToolChoice {
    /** Controls the tool use ability of the model:
- `"auto"`: Model decides whether to use tools (default)
- `"required"`: Model MUST use at least one tool before completing
- `"none"`: Model MUST NOT use any tools */
    mode?: string,
}


/**
 * A JSON Schema object defining the expected parameters for the tool.

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
 */
export interface McpToolInputSchema {
    /** The kind of object, always `object`. */
    type: string,
    /** The JSON Schema dialect the schema is written in. */
    schema_dialect?: string,
}


/**
 * An optional notification from the server to the client, informing it that the list of tools it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `toolsListChanged` filter field.
 */
export interface McpToolListChangedNotification extends McpJSONRPCNotification {
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
    /** The method's name, always `notifications/tools/list_changed`. */
    method: string,
    /** Common params for any notification. */
    params?: McpNotificationParams,
}


/**
 * An optional JSON Schema object defining the structure of the tool's output returned in
the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
 */
export interface McpToolOutputSchema {
    /** The JSON Schema dialect the schema is written in. */
    schema_dialect?: string,
}


/**
 * The result of a tool use, provided by the user back to the assistant.
 */
export interface McpToolResultContent {
    /** The kind of object, always `tool_result`. */
    type: string,
    /** Optional metadata about the tool result. Clients SHOULD preserve this field when
including tool results in subsequent sampling requests to enable caching optimizations. */
    _meta?: McpMetaObject,
    /** The unstructured result content of the tool use.

This has the same format as {@link CallToolResult.content} and can include text, images,
audio, resource links, and embedded resources. */
    content: McpContentBlock[],
    /** Whether the tool use resulted in an error.

If true, the content typically describes the error that occurred.
Default: false */
    isError?: boolean,
    /** An optional structured result value.

This can be any JSON value (object, array, string, number, boolean, or null).
If the tool defined an {@link Tool.outputSchema}, this SHOULD conform to that schema. */
    structuredContent?: McpJSONValue,
    /** The ID of the tool use this result corresponds to.

This MUST match the ID from a previous {@link ToolUseContent}. */
    toolUseId: string,
}


/**
 * A request from the assistant to call a tool.
 */
export interface McpToolUseContent {
    /** A unique identifier for this tool use.

This ID is used to match tool results to their corresponding tool uses. */
    id: string,
    /** The name of the tool to call. */
    name: string,
    /** The kind of object, always `tool_use`. */
    type: string,
    /** Optional metadata about the tool use. Clients SHOULD preserve this field when
including tool uses in subsequent sampling requests to enable caching optimizations. */
    _meta?: McpMetaObject,
    /** The arguments to pass to the tool, conforming to the tool's input schema. */
    input: McpJSONObject,
}


/**
 * Returned when the request's protocol version is unknown to the server or
unsupported (e.g., a known experimental or draft version the server has
chosen not to implement). For HTTP, the response status code MUST be
`400 Bad Request`.
 */
export interface McpUnsupportedProtocolVersionError extends McpJSONRPCErrorResponse {
    /** A uniquely identifying ID for a request in JSON-RPC. */
    id?: string,
    /** The error the request ended with. */
    error: McpUnsupportedProtocolVersionErrorError,
    /** The JSON-RPC version, always `2.0`. */
    jsonrpc: string,
}


/**
 * MCP's `Error`, with the code and data this error carries.
 */
export interface McpUnsupportedProtocolVersionErrorError extends McpError {
    /** The error code, always `-32022`. */
    code: number,
    /** Details of the error. */
    data: McpUnsupportedProtocolVersionErrorErrorData,
}


/**
 * The object MCP's `UnsupportedProtocolVersionError` holds under `data`.
 */
export interface McpUnsupportedProtocolVersionErrorErrorData {
    /** The protocol version that was requested by the client. */
    requested: string,
    /** Protocol versions the server supports. The client should choose a
mutually supported version from this list and retry. */
    supported: string[],
}


/**
 * Schema for multiple-selection enumeration without display titles for options.
 */
export interface McpUntitledMultiSelectEnumSchema {
    /** Optional description for the enum field. */
    description?: string,
    /** Optional title for the enum field. */
    title?: string,
    /** The kind of object, always `array`. */
    type: string,
    /** Optional default value. */
    default?: string[],
    /** Schema for the array items. */
    items: McpUntitledMultiSelectEnumSchemaItems,
    /** Maximum number of items to select. */
    maxItems?: number,
    /** Minimum number of items to select. */
    minItems?: number,
}


/**
 * Schema for the array items.
 */
export interface McpUntitledMultiSelectEnumSchemaItems {
    /** The kind of object, always `string`. */
    type: string,
    /** Array of enum values to choose from. */
    enum: string[],
}


/**
 * Schema for single-selection enumeration without display titles for options.
 */
export interface McpUntitledSingleSelectEnumSchema {
    /** Optional description for the enum field. */
    description?: string,
    /** Optional title for the enum field. */
    title?: string,
    /** The kind of object, always `string`. */
    type: string,
    /** Optional default value. */
    default?: string,
    /** Array of enum values to choose from. */
    enum: string[],
}



