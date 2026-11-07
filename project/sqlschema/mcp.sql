-- # Class: McpAnnotations Description: Optional annotations for the client. The client can use annotations to inform how objects are used or displayed
--     * Slot: id
--     * Slot: lastModified Description: The moment the resource was last modified, as an ISO 8601 formatted string.Should be an ISO 8601 formatted string (e.g., "2025-01-12T15:00:58Z").Examples: last activity timestamp in an open file, timestamp when the resourcewas attached, etc.
--     * Slot: priority Description: Describes how important this data is for operating the server.A value of 1 means "most important," and indicates that the data iseffectively required, while 0 means "least important," and indicates thatthe data is entirely optional.
-- # Class: McpAudioContent Description: Audio provided to or from an LLM.
--     * Slot: id
--     * Slot: data Description: The base64-encoded audio data.
--     * Slot: mimeType Description: The MIME type of the audio. Different providers may support different audio types.
--     * Slot: type Description: The kind of object, always `audio`.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpBaseMetadata Description: Base interface for metadata with name (identifier) and title (display name) properties.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
-- # Class: McpBlobResourceContents Description: MCP's `BlobResourceContents`.
--     * Slot: id
--     * Slot: blob Description: A base64-encoded string representing the binary data of the item.
--     * Slot: mimeType Description: The MIME type of this resource, if known.
--     * Slot: uri Description: The URI of this resource.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpBooleanSchema Description: MCP's `BooleanSchema`.
--     * Slot: id
--     * Slot: default Description: The value the field takes when the user gives none.
--     * Slot: description Description: A description of the field for the user.
--     * Slot: title Description: A title for the field.
--     * Slot: type Description: The kind of object, always `boolean`.
-- # Class: McpCacheableResult Description: A result that supports a time-to-live (TTL) hint for client-side caching.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpCallToolRequest Description: Used by the client to invoke a tool provided by the server.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `tools/call`.
--     * Slot: params_id Description: Parameters for a `tools/call` request.
-- # Class: McpCallToolRequestParams Description: Parameters for a `tools/call` request.
--     * Slot: id
--     * Slot: name Description: The name of the tool.
--     * Slot: requestState Description: State the server handed out with an input-required result, sent back unchanged when the request is retried.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: arguments_id Description: Arguments to use for the tool call.
--     * Slot: inputResponses_id Description: A map of client responses to server-initiated requests.Keys correspond to the keys in the {@link InputRequests} map;values are the client's result for each request.
-- # Class: McpCallToolResult Description: The result returned by the server for a {@link CallToolRequesttools/call} request.
--     * Slot: id
--     * Slot: isError Description: Whether the tool call ended in an error.If not set, this is assumed to be false (the call was successful).Any errors that originate from the tool SHOULD be reported inside the resultobject, with `isError` set to true, _not_ as an MCP protocol-level errorresponse. Otherwise, the LLM would not be able to see that an error occurredand self-correct.However, any errors in _finding_ the tool, an error indicating that theserver does not support tool calls, or any other exceptional conditions,should be reported as an MCP error response.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: structuredContent_id Description: An optional JSON value that represents the structured result of the tool call.This can be any JSON value (object, array, string, number, boolean, or null)that conforms to the tool's outputSchema if one is defined.
-- # Class: McpCallToolResultResponse Description: A successful response from the server for a {@link CallToolRequesttools/call} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result Description: What the request returned.
-- # Class: McpCancelledNotification Description: This notification is sent by the client to indicate that it is cancelling a request it previously issued.On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.This notification indicates that the result will be unused, so any associated processing SHOULD cease.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/cancelled`.
--     * Slot: params_id Description: Parameters for a `notifications/cancelled` notification.
-- # Class: McpCancelledNotificationParams Description: Parameters for a `notifications/cancelled` notification.
--     * Slot: id
--     * Slot: reason Description: An optional string describing the reason for the cancellation. This MAY be logged or presented to the user.
--     * Slot: requestId Description: The ID of the request to cancel.This MUST correspond to the ID of a request the client previously issued.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpClientCapabilities Description: Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.
--     * Slot: id
--     * Slot: elicitation_id Description: Present if the client supports elicitation from the server.
--     * Slot: experimental_id Description: Experimental, non-standard capabilities that the client supports.
--     * Slot: extensions_id Description: Optional MCP extensions that the client supports. Keys are extension identifiers(e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values areper-extension settings objects. An empty object indicates support with no settings.Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with amandatory prefix.
--     * Slot: roots_id Description: Present if the client supports listing roots.
--     * Slot: sampling_id Description: Present if the client supports sampling from an LLM.
-- # Class: McpClientCapabilitiesElicitation Description: Present if the client supports elicitation from the server.
--     * Slot: id
--     * Slot: form_id Description: Settings for elicitation by form.
--     * Slot: url_id Description: Settings for elicitation by URL.
-- # Class: McpClientCapabilitiesExperimental Description: Experimental, non-standard capabilities that the client supports.
--     * Slot: id
-- # Class: McpClientCapabilitiesExtensions Description: Optional MCP extensions that the client supports. Keys are extension identifiers(e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values areper-extension settings objects. An empty object indicates support with no settings.Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with amandatory prefix.
--     * Slot: id
-- # Class: McpClientCapabilitiesRoots Description: Present if the client supports listing roots.
--     * Slot: id
-- # Class: McpClientCapabilitiesSampling Description: Present if the client supports sampling from an LLM.
--     * Slot: id
--     * Slot: context_id Description: Whether the client supports context inclusion via `includeContext` parameter.If not declared, servers SHOULD only use `includeContext: "none"` (or omit it).
--     * Slot: tools_id Description: Whether the client supports tool use via `tools` and `toolChoice` parameters.
-- # Class: McpClientNotification Description: This notification is sent by the client to indicate that it is cancelling a request it previously issued.On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.This notification indicates that the result will be unused, so any associated processing SHOULD cease.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/cancelled`.
--     * Slot: params_id Description: Parameters for a `notifications/cancelled` notification.
-- # Class: McpClientRequest Description: One of `DiscoverRequest`, `ListResourcesRequest`, `ListResourceTemplatesRequest`, `ReadResourceRequest`, `SubscriptionsListenRequest`, `ListPromptsRequest`, `GetPromptRequest`, `ListToolsRequest`, `CallToolRequest`, `CompleteRequest`.
--     * Slot: id
-- # Class: McpClientResult Description: Common result fields.
--     * Slot: id
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpCompleteRequest Description: A request from the client to the server, to ask for completion options.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `completion/complete`.
--     * Slot: params_id Description: Parameters for a `completion/complete` request.
-- # Class: McpCompleteRequestParams Description: Parameters for a `completion/complete` request.
--     * Slot: id
--     * Slot: ref Description: What the completion is for: a prompt or a resource template.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: argument_id Description: The argument's information
--     * Slot: context_id Description: Additional, optional context for completions
-- # Class: McpCompleteRequestParamsArgument Description: The argument's information
--     * Slot: id
--     * Slot: name Description: The name of the argument
--     * Slot: value Description: The value of the argument to use for completion matching.
-- # Class: McpCompleteRequestParamsContext Description: Additional, optional context for completions
--     * Slot: id
--     * Slot: arguments_id Description: Previously-resolved variables in a URI template or prompt.
-- # Class: McpCompleteRequestParamsContextArguments Description: Previously-resolved variables in a URI template or prompt.
--     * Slot: id
-- # Class: McpCompleteResult Description: The result returned by the server for a {@link CompleteRequestcompletion/complete} request.
--     * Slot: id
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: completion_id Description: The completion values and whether more are available.
-- # Class: McpCompleteResultCompletion Description: The object MCP's `CompleteResult` holds under `completion`.
--     * Slot: id
--     * Slot: hasMore Description: Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown.
--     * Slot: total Description: The total number of completion options available. This can exceed the number of values actually sent in the response.
-- # Class: McpCompleteResultResponse Description: A successful response from the server for a {@link CompleteRequestcompletion/complete} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The result returned by the server for a {@link CompleteRequestcompletion/complete} request.
-- # Class: McpContentBlock Description: One of `TextContent`, `ImageContent`, `AudioContent`, `ResourceLink`, `EmbeddedResource`.
--     * Slot: id
--     * Slot: McpCallToolResult_id Description: Autocreated FK slot
--     * Slot: McpToolResultContent_id Description: Autocreated FK slot
-- # Class: McpCreateMessageRequest Description: A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.
--     * Slot: id
--     * Slot: method Description: The method's name, always `sampling/createMessage`.
--     * Slot: params_id Description: Parameters for a `sampling/createMessage` request.
-- # Class: McpCreateMessageRequestParams Description: Parameters for a `sampling/createMessage` request.
--     * Slot: id
--     * Slot: includeContext Description: A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.The client MAY ignore this request.Default is `"none"`. The values `"thisServer"` and `"allServers"` are deprecated (SEP-2596): servers SHOULDomit this field or use `"none"`, and SHOULD only use the deprecated values if the client declares{@link ClientCapabilities.sampling.context}.
--     * Slot: maxTokens Description: The requested maximum number of tokens to sample (to prevent runaway completions).The client MAY choose to sample fewer tokens than the requested maximum.
--     * Slot: systemPrompt Description: An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt.
--     * Slot: temperature Description: The sampling temperature the server asks the model to use.
--     * Slot: metadata_id Description: Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific.
--     * Slot: modelPreferences_id Description: The server's preferences for which model to select. The client MAY ignore these preferences.
--     * Slot: toolChoice_id Description: Controls how the model uses tools.The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared.Default is `{ mode: "auto" }`.
-- # Class: McpCreateMessageResult Description: The result returned by the client for a {@link CreateMessageRequestsampling/createMessage} request.The client should inform the user before returning the sampled message, to allow themto inspect the response (human in the loop) and decide whether to allow the server to see it.
--     * Slot: id
--     * Slot: content Description: The content the message carries.
--     * Slot: model Description: The name of the model that generated the message.
--     * Slot: role Description: The sender or recipient of messages and data in a conversation.
--     * Slot: stopReason Description: The reason why sampling stopped, if known.Standard values:- `"endTurn"`: Natural end of the assistant's turn- `"stopSequence"`: A stop sequence was encountered- `"maxTokens"`: Maximum token limit was reached- `"toolUse"`: The model wants to use one or more toolsThis field is an open string to allow for provider-specific stop reasons.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpDiscoverRequest Description: A request from the client asking the server to advertise its supportedprotocol versions, capabilities, and other metadata. Servers **MUST**implement `server/discover`. Clients **MAY** call it but are not requiredto — version negotiation can also happen inline via per-request `_meta`.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `server/discover`.
--     * Slot: params_id Description: Common params for any request.
-- # Class: McpDiscoverResult Description: The result returned by the server for a {@link DiscoverRequestserver/discover} request.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: instructions Description: Natural-language guidance describing the server and its features.This can be used by clients to improve an LLM's understanding ofavailable tools (e.g., by including it in a system prompt). It shouldfocus on information that helps the model use the server effectivelyand should not duplicate information already in tool descriptions.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: capabilities_id Description: The capabilities of the server.
-- # Class: McpDiscoverResultResponse Description: A successful response from the server for a {@link DiscoverRequestserver/discover} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The result returned by the server for a {@link DiscoverRequestserver/discover} request.
-- # Class: McpElicitRequest Description: A request from the server to elicit additional information from the user via the client.
--     * Slot: id
--     * Slot: method Description: The method's name, always `elicitation/create`.
--     * Slot: params_id Description: The parameters for a request to elicit additional information from the user via the client.
-- # Class: McpElicitRequestFormParams Description: The parameters for a request to elicit non-sensitive information from the user via a form in the client.
--     * Slot: id
--     * Slot: message Description: The message to present to the user describing what information is being requested.
--     * Slot: mode Description: The elicitation mode.
--     * Slot: requestedSchema_id Description: A restricted subset of JSON Schema.Only top-level properties are allowed, without nesting.
-- # Class: McpElicitRequestFormParamsRequestedSchema Description: A restricted subset of JSON Schema.Only top-level properties are allowed, without nesting.
--     * Slot: id
--     * Slot: schema_dialect Description: The JSON Schema dialect the schema is written in.
--     * Slot: type Description: The kind of object, always `object`.
--     * Slot: properties_id Description: The fields of the form, by name.
-- # Class: McpElicitRequestFormParamsRequestedSchemaProperties Description: The object MCP's `ElicitRequestFormParams` holds under `properties`.
--     * Slot: id
-- # Class: McpElicitRequestParams Description: The parameters for a request to elicit additional information from the user via the client.
--     * Slot: id
-- # Class: McpElicitRequestURLParams Description: The parameters for a request to elicit information from the user via a URL in the client.
--     * Slot: id
--     * Slot: message Description: The message to present to the user explaining why the interaction is needed.
--     * Slot: mode Description: The elicitation mode.
--     * Slot: url Description: The URL that the user should navigate to.
-- # Class: McpElicitResult Description: The result returned by the client for an {@link ElicitRequestelicitation/create} request.
--     * Slot: id
--     * Slot: action Description: The user action in response to the elicitation.- `"accept"`: User submitted the form/confirmed the action- `"decline"`: User explicitly declined the action- `"cancel"`: User dismissed without making an explicit choice
--     * Slot: content_id Description: The submitted form data, only present when action is `"accept"` and mode was `"form"`.Contains values matching the requested schema.Omitted for out-of-band mode responses.
-- # Class: McpElicitResultContent Description: The submitted form data, only present when action is `"accept"` and mode was `"form"`.Contains values matching the requested schema.Omitted for out-of-band mode responses.
--     * Slot: id
-- # Class: McpEmbeddedResource Description: The contents of a resource, embedded into a prompt or tool call result.It is up to the client how best to render embedded resources for the benefitof the LLM and/or the user.
--     * Slot: id
--     * Slot: resource Description: The resource's contents, as text or as binary data.
--     * Slot: type Description: The kind of object, always `resource`.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpEmptyResult Description: Common result fields.
--     * Slot: id
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpEnumSchema Description: One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`, `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`, `LegacyTitledEnumSchema`.
--     * Slot: id
-- # Class: McpError Description: MCP's `Error`.
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpGetPromptRequest Description: Used by the client to get a prompt provided by the server.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `prompts/get`.
--     * Slot: params_id Description: Parameters for a `prompts/get` request.
-- # Class: McpGetPromptRequestParams Description: Parameters for a `prompts/get` request.
--     * Slot: id
--     * Slot: name Description: The name of the prompt or prompt template.
--     * Slot: requestState Description: State the server handed out with an input-required result, sent back unchanged when the request is retried.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: arguments_id Description: Arguments to use for templating the prompt.
--     * Slot: inputResponses_id Description: A map of client responses to server-initiated requests.Keys correspond to the keys in the {@link InputRequests} map;values are the client's result for each request.
-- # Class: McpGetPromptRequestParamsArguments Description: Arguments to use for templating the prompt.
--     * Slot: id
-- # Class: McpGetPromptResult Description: The result returned by the server for a {@link GetPromptRequestprompts/get} request.
--     * Slot: id
--     * Slot: description Description: An optional description for the prompt.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpGetPromptResultResponse Description: A successful response from the server for a {@link GetPromptRequestprompts/get} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result Description: What the request returned.
-- # Class: McpHeaderMismatchError Description: Returned when a server rejects a request because the values in the HTTPheaders do not match the corresponding values in the request body, orbecause required headers are missing or malformed. For HTTP, the responsestatus code MUST be `400 Bad Request`.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: error_id Description: The error the request ended with.
-- # Class: McpHeaderMismatchErrorError Description: MCP's `Error`, with the code and data this error carries.
--     * Slot: id
--     * Slot: code Description: The error code, always `-32020`.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpIcon Description: An optionally-sized icon that can be displayed in a user interface.
--     * Slot: id
--     * Slot: mimeType Description: Optional MIME type override if the source MIME type is missing or generic.For example: `"image/png"`, `"image/jpeg"`, or `"image/svg+xml"`.
--     * Slot: src Description: A standard URI pointing to an icon resource. May be an HTTP/HTTPS URL or a`data:` URI with Base64-encoded image data.Consumers SHOULD take steps to ensure URLs serving icons are from thesame domain as the client/server or a trusted domain.Consumers SHOULD take appropriate precautions when consuming SVGs as they can containexecutable JavaScript.
--     * Slot: theme Description: Optional specifier for the theme this icon is designed for. `"light"` indicatesthe icon is designed to be used with a light background, and `"dark"` indicatesthe icon is designed to be used with a dark background.If not provided, the client should assume the icon can be used with any theme.
--     * Slot: McpIcons_id Description: Autocreated FK slot
--     * Slot: McpImplementation_id Description: Autocreated FK slot
--     * Slot: McpPrompt_id Description: Autocreated FK slot
--     * Slot: McpResource_id Description: Autocreated FK slot
--     * Slot: McpResourceLink_id Description: Autocreated FK slot
--     * Slot: McpResourceTemplate_id Description: Autocreated FK slot
--     * Slot: McpTool_id Description: Autocreated FK slot
-- # Class: McpIcons Description: Base interface to add `icons` property.
--     * Slot: id
-- # Class: McpImageContent Description: An image provided to or from an LLM.
--     * Slot: id
--     * Slot: data Description: The base64-encoded image data.
--     * Slot: mimeType Description: The MIME type of the image. Different providers may support different image types.
--     * Slot: type Description: The kind of object, always `image`.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpImplementation Description: Describes the MCP implementation.
--     * Slot: id
--     * Slot: description Description: An optional human-readable description of what this implementation does.This can be used by clients or servers to provide context about their purposeand capabilities. For example, a server might describe the types of resourcesor tools it provides, while a client might describe its intended use case.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: version Description: The version of this implementation.
--     * Slot: websiteUrl Description: An optional URL of the website for this implementation.
-- # Class: McpInputRequest Description: One of `CreateMessageRequest`, `ListRootsRequest`, `ElicitRequest`.
--     * Slot: id
-- # Class: McpInputRequests Description: A map of server-initiated requests that the client must fulfill.Keys are server-assigned identifiers; values are the request objects.
--     * Slot: id
-- # Class: McpInputRequiredResult Description: An InputRequiredResult sent by the server to indicate that additional input is neededbefore the request can be completed.At least one of `inputRequests` or `requestState` MUST be present.
--     * Slot: id
--     * Slot: requestState Description: State for the client to send back unchanged when it retries the request.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: inputRequests_id Description: A map of server-initiated requests that the client must fulfill.Keys are server-assigned identifiers; values are the request objects.
-- # Class: McpInputResponse Description: One of `CreateMessageResult`, `ListRootsResult`, `ElicitResult`.
--     * Slot: id
-- # Class: McpInputResponseRequestParams Description: MCP's `InputResponseRequestParams`.
--     * Slot: id
--     * Slot: requestState Description: State the server handed out with an input-required result, sent back unchanged when the request is retried.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: inputResponses_id Description: A map of client responses to server-initiated requests.Keys correspond to the keys in the {@link InputRequests} map;values are the client's result for each request.
-- # Class: McpInputResponses Description: A map of client responses to server-initiated requests.Keys correspond to the keys in the {@link InputRequests} map;values are the client's result for each request.
--     * Slot: id
-- # Class: McpInternalError Description: A JSON-RPC error indicating that an internal error occurred on the receiver. This error is returned when the receiver encounters an unexpected condition that prevents it from fulfilling the request.
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpInvalidParamsError Description: A JSON-RPC error indicating that the method parameters are invalid or malformed.In MCP, this error is returned in various contexts when request parameters fail validation:- **Tools**: Unknown tool name or invalid tool arguments- **Prompts**: Unknown prompt name or missing required arguments- **Pagination**: Invalid or expired cursor values- **Logging**: Invalid log level- **Elicitation**: Server requests an elicitation mode not declared in client capabilities- **Sampling**: Missing tool result or tool results mixed with other content
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpInvalidRequestError Description: A JSON-RPC error indicating that the request is not a valid request object. This error is returned when the message structure does not conform to the JSON-RPC 2.0 specification requirements for a request (e.g., missing required fields like `jsonrpc` or `method`, or using invalid types for these fields).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpJSONObject Description: A JSON object, whose values are JSON values.
--     * Slot: id
-- # Class: McpJSONRPCErrorResponse Description: A response to a request that indicates an error occurred.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: error_id Description: The error the request ended with.
-- # Class: McpJSONRPCMessage Description: Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.
--     * Slot: id
-- # Class: McpJSONRPCNotification Description: A notification which does not expect a response.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The name of the method.
--     * Slot: params_id Description: The parameters the message carries.
-- # Class: McpJSONRPCRequest Description: A request that expects a response.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The name of the method.
--     * Slot: params_id Description: The parameters the message carries.
-- # Class: McpJSONRPCResponse Description: A response to a request, containing either the result or error.
--     * Slot: id
-- # Class: McpJSONRPCResultResponse Description: A successful (non-error) response to a request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: Common result fields.
-- # Class: McpJSONValue Description: One of `JSONObject`.
--     * Slot: id
-- # Class: McpLegacyTitledEnumSchema Description: Use {@link TitledSingleSelectEnumSchema} instead.This interface will be removed in a future version.
--     * Slot: id
--     * Slot: default Description: The value the field takes when the user gives none.
--     * Slot: description Description: A description of the field for the user.
--     * Slot: title Description: A title for the field.
--     * Slot: type Description: The kind of object, always `string`.
-- # Class: McpListPromptsRequest Description: Sent from the client to request a list of prompts and prompt templates the server has.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `prompts/list`.
--     * Slot: params_id Description: Common params for paginated requests.
-- # Class: McpListPromptsResult Description: The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result.If present, there may be more results available.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpListPromptsResultResponse Description: A successful response from the server for a {@link ListPromptsRequestprompts/list} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
-- # Class: McpListResourceTemplatesRequest Description: Sent from the client to request a list of resource templates the server has.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `resources/templates/list`.
--     * Slot: params_id Description: Common params for paginated requests.
-- # Class: McpListResourceTemplatesResult Description: The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result.If present, there may be more results available.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpListResourceTemplatesResultResponse Description: A successful response from the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
-- # Class: McpListResourcesRequest Description: Sent from the client to request a list of resources the server has.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `resources/list`.
--     * Slot: params_id Description: Common params for paginated requests.
-- # Class: McpListResourcesResult Description: The result returned by the server for a {@link ListResourcesRequestresources/list} request.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result.If present, there may be more results available.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpListResourcesResultResponse Description: A successful response from the server for a {@link ListResourcesRequestresources/list} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The result returned by the server for a {@link ListResourcesRequestresources/list} request.
-- # Class: McpListRootsRequest Description: Sent from the server to request a list of root URIs from the client. Roots allowservers to ask for specific directories or files to operate on. A common examplefor roots is providing a set of repositories or directories a server should operateon.This request is typically used when the server needs to understand the file systemstructure or access specific locations that the client has permission to read from.
--     * Slot: id
--     * Slot: method Description: The method's name, always `roots/list`.
--     * Slot: params_id Description: The parameters the message carries.
-- # Class: McpListRootsRequestParams Description: The object MCP's `ListRootsRequest` holds under `params`.
--     * Slot: id
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpListRootsResult Description: The result returned by the client for a {@link ListRootsRequestroots/list} request.This result contains an array of {@link Root} objects, each representing a root directoryor file that the server can operate on.
--     * Slot: id
-- # Class: McpListToolsRequest Description: Sent from the client to request a list of tools the server has.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `tools/list`.
--     * Slot: params_id Description: Common params for paginated requests.
-- # Class: McpListToolsResult Description: The result returned by the server for a {@link ListToolsRequesttools/list} request.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result.If present, there may be more results available.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpListToolsResultResponse Description: A successful response from the server for a {@link ListToolsRequesttools/list} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The result returned by the server for a {@link ListToolsRequesttools/list} request.
-- # Class: McpLoggingMessageNotification Description: JSONRPCNotification of a log message passed from server to client. The client opts in by setting `"io.modelcontextprotocol/logLevel"` in a request's `_meta`.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/message`.
--     * Slot: params_id Description: Parameters for a `notifications/message` notification.
-- # Class: McpLoggingMessageNotificationParams Description: Parameters for a `notifications/message` notification.
--     * Slot: id
--     * Slot: level Description: The severity of this log message.
--     * Slot: logger Description: An optional name of the logger issuing this message.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: data_id Description: The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here.
-- # Class: McpMetaObject Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: id
-- # Class: McpMethodNotFoundError Description: A JSON-RPC error indicating that the requested method does not exist or is not available.In MCP, a server returns this error when a client invokes a method the server does not implement — either a genuinely unknown method, or one gated behind a server capability the server did not advertise (e.g., calling `prompts/list` when the `prompts` capability was not advertised).A request that requires a client capability the client did not declare is signalled instead by {@link MissingRequiredClientCapabilityError} (`-32021`).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpMissingRequiredClientCapabilityError Description: Returned when processing a request requires a capability the client did notdeclare in `clientCapabilities`. For HTTP, the response status code MUST be`400 Bad Request`.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: error_id Description: The error the request ended with.
-- # Class: McpMissingRequiredClientCapabilityErrorError Description: MCP's `Error`, with the code and data this error carries.
--     * Slot: id
--     * Slot: code Description: The error code, always `-32021`.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Details of the error.
-- # Class: McpMissingRequiredClientCapabilityErrorErrorData Description: The object MCP's `MissingRequiredClientCapabilityError` holds under `data`.
--     * Slot: id
--     * Slot: requiredCapabilities_id Description: The capabilities the server requires from the client to process this request.
-- # Class: McpModelHint Description: Hints to use for model selection.Keys not declared here are currently left unspecified by the spec and are upto the client to interpret.
--     * Slot: id
--     * Slot: name Description: A hint for a model name.The client SHOULD treat this as a substring of a model name; for example: - `claude-3-5-sonnet` should match `claude-3-5-sonnet-20241022` - `sonnet` should match `claude-3-5-sonnet-20241022`, `claude-3-sonnet-20240229`, etc. - `claude` should match any Claude modelThe client MAY also map the string to a different provider's model name or a different model family, as long as it fills a similar niche; for example: - `gemini-1.5-flash` could match `claude-3-haiku-20240307`
--     * Slot: McpModelPreferences_id Description: Autocreated FK slot
-- # Class: McpModelPreferences Description: The server's preferences for model selection, requested of the client during sampling.Because LLMs can vary along multiple dimensions, choosing the "best" model israrely straightforward.  Different models excel in different areas—some arefaster but less capable, others are more capable but more expensive, and soon. This interface allows servers to express their priorities across multipledimensions to help clients make an appropriate selection for their use case.These preferences are always advisory. The client MAY ignore them. It is alsoup to the client to decide how to interpret these preferences and how tobalance them against other considerations.
--     * Slot: id
--     * Slot: costPriority Description: How much to prioritize cost when selecting a model. A value of 0 means costis not important, while a value of 1 means cost is the most importantfactor.
--     * Slot: intelligencePriority Description: How much to prioritize intelligence and capabilities when selecting amodel. A value of 0 means intelligence is not important, while a value of 1means intelligence is the most important factor.
--     * Slot: speedPriority Description: How much to prioritize sampling speed (latency) when selecting a model. Avalue of 0 means speed is not important, while a value of 1 means speed isthe most important factor.
-- # Class: McpMultiSelectEnumSchema Description: One of `UntitledMultiSelectEnumSchema`, `TitledMultiSelectEnumSchema`.
--     * Slot: id
-- # Class: McpNotification Description: MCP's `Notification`.
--     * Slot: id
--     * Slot: method Description: The name of the method.
--     * Slot: params_id Description: The parameters the message carries.
-- # Class: McpNotificationMetaObject Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: id
--     * Slot: mcp_subscription_id Description: Identifies the subscription stream a notification was delivered on. Theserver MUST include this key on every notification delivered via a{@link SubscriptionsListenRequestsubscriptions/listen} stream, so theclient can correlate the notification with the originating subscription.The key is absent on notifications not delivered via a subscriptionstream (e.g. progress notifications for an in-flight request), which iswhy it is optional here.The value is the JSON-RPC ID of the `subscriptions/listen` request thatopened the stream.
-- # Class: McpNotificationParams Description: Common params for any notification.
--     * Slot: id
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpNumberSchema Description: MCP's `NumberSchema`.
--     * Slot: id
--     * Slot: default Description: The value the field takes when the user gives none.
--     * Slot: description Description: A description of the field for the user.
--     * Slot: maximum Description: The largest value the field accepts.
--     * Slot: minimum Description: The smallest value the field accepts.
--     * Slot: title Description: A title for the field.
--     * Slot: type Description: The kind of value the field takes.
-- # Class: McpPaginatedRequest Description: MCP's `PaginatedRequest`.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The name of the method.
--     * Slot: params_id Description: Common params for paginated requests.
-- # Class: McpPaginatedRequestParams Description: Common params for paginated requests.
--     * Slot: id
--     * Slot: cursor Description: An opaque token representing the current pagination position.If provided, the server should return results starting after this cursor.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpPaginatedResult Description: MCP's `PaginatedResult`.
--     * Slot: id
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result.If present, there may be more results available.
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpParseError Description: A JSON-RPC error indicating that invalid JSON was received by the server. This error is returned when the server cannot parse the JSON text of a message.
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
-- # Class: McpPrimitiveSchemaDefinition Description: Restricted schema definitions that only allow primitive typeswithout nested objects or arrays.
--     * Slot: id
-- # Class: McpProgressNotification Description: An out-of-band notification used to inform the receiver of a progress update for a long-running request.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/progress`.
--     * Slot: params_id Description: Parameters for a {@link ProgressNotificationnotifications/progress} notification.
-- # Class: McpProgressNotificationParams Description: Parameters for a {@link ProgressNotificationnotifications/progress} notification.
--     * Slot: id
--     * Slot: message Description: An optional message describing the current progress.
--     * Slot: progress Description: The progress thus far. This should increase every time progress is made, even if the total is unknown.
--     * Slot: progressToken Description: The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.
--     * Slot: total Description: Total number of items to process (or total progress required), if known.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpPrompt Description: A prompt or prompt template that the server offers.
--     * Slot: id
--     * Slot: description Description: An optional description of what this prompt provides
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: McpListPromptsResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpPromptArgument Description: Describes an argument that a prompt can accept.
--     * Slot: id
--     * Slot: description Description: A human-readable description of the argument.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: required Description: Whether this argument must be provided.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: McpPrompt_id Description: Autocreated FK slot
-- # Class: McpPromptListChangedNotification Description: An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `promptsListChanged` filter field.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/prompts/list_changed`.
--     * Slot: params_id Description: Common params for any notification.
-- # Class: McpPromptMessage Description: Describes a message returned as part of a prompt.This is similar to {@link SamplingMessage}, but also supports the embedding ofresources from the MCP server.
--     * Slot: id
--     * Slot: role Description: The sender or recipient of messages and data in a conversation.
--     * Slot: McpGetPromptResult_id Description: Autocreated FK slot
--     * Slot: content_id Description: The content the message carries.
-- # Class: McpPromptReference Description: Identifies a prompt.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: type Description: The kind of object, always `ref/prompt`.
-- # Class: McpReadResourceRequest Description: Sent from the client to the server, to read a specific resource URI.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `resources/read`.
--     * Slot: params_id Description: Parameters for a `resources/read` request.
-- # Class: McpReadResourceRequestParams Description: Parameters for a `resources/read` request.
--     * Slot: id
--     * Slot: requestState Description: State the server handed out with an input-required result, sent back unchanged when the request is retried.
--     * Slot: uri Description: The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: inputResponses_id Description: A map of client responses to server-initiated requests.Keys correspond to the keys in the {@link InputRequests} map;values are the client's result for each request.
-- # Class: McpReadResourceResult Description: The result returned by the server for a {@link ReadResourceRequestresources/read} request.
--     * Slot: id
--     * Slot: cacheScope Description: Indicates the intended scope of the cached response, analogous to HTTP`Cache-Control: public` vs `Cache-Control: private`.- `"public"`: The response does not contain user-specific data. Any  client or intermediary (e.g., shared gateway, caching proxy) MAY cache  the response and serve it across authorization contexts.- `"private"`: The response MAY be cached and reused only within the  same authorization context. Caches MUST NOT be shared across  authorization contexts (e.g., a different access token requires a  different cache).
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: ttlMs Description: A hint from the server indicating how long (in milliseconds) theclient MAY cache this response before re-fetching. Semantics areanalogous to HTTP Cache-Control max-age.- If 0, The response SHOULD be considered immediately stale,  The client MAY re-fetch every time the result is needed.- If positive, the client SHOULD consider the result fresh for this many  milliseconds after receiving the response.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpReadResourceResultResponse Description: A successful response from the server for a {@link ReadResourceRequestresources/read} request.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result Description: What the request returned.
-- # Class: McpRequest Description: MCP's `Request`.
--     * Slot: id
--     * Slot: method Description: The name of the method.
--     * Slot: params_id Description: The parameters the message carries.
-- # Class: McpRequestMetaObject Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: id
--     * Slot: mcp_log_level Description: The desired log level for this request. Optional.If absent, the server MUST NOT send any {@link LoggingMessageNotificationnotifications/message}notifications for this request. The client opts in to log messages byexplicitly setting a level. Replaces the former `logging/setLevel` RPC.
--     * Slot: mcp_protocol_version Description: The MCP Protocol Version being used for this request. Required.For the HTTP transport, this value MUST match the `MCP-Protocol-Version`header; otherwise the server MUST return a `400 Bad Request`. If theserver does not support the requested version, it MUST return an{@link UnsupportedProtocolVersionError}.
--     * Slot: progressToken Description: If specified, the caller is requesting out-of-band progress notifications for this request (as represented by {@link ProgressNotificationnotifications/progress}). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.
--     * Slot: mcp_client_capabilities_id Description: The client's capabilities for this specific request. Required.Capabilities are declared per-request rather than once at initialization;an empty object means the client supports no optional capabilities.Servers MUST NOT infer capabilities from prior requests.
--     * Slot: mcp_client_info_id Description: Identifies the client software making the request. Clients SHOULDinclude this field on every request unless specifically configured notto do so.The {@link Implementation} schema requires `name` and `version`; otherfields are optional.The value is self-reported by the client and is not verified by theprotocol. It is intended for display, logging, and debugging. ServersSHOULD NOT use it to change their behavior, and SHOULD NOT rely on it forsecurity decisions.
-- # Class: McpRequestParams Description: Common params for any request.
--     * Slot: id
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpResource Description: A known resource that the server is capable of reading.
--     * Slot: id
--     * Slot: description Description: A description of what this resource represents.This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.
--     * Slot: mimeType Description: The MIME type of this resource, if known.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: size Description: The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.This can be used by Hosts to display file sizes and estimate context window usage.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: uri Description: The URI of this resource.
--     * Slot: McpListResourcesResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpResourceContents Description: The contents of a specific resource or sub-resource.
--     * Slot: id
--     * Slot: mimeType Description: The MIME type of this resource, if known.
--     * Slot: uri Description: The URI of this resource.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpResourceLink Description: A resource that the server is capable of reading, included in a prompt or tool call result.Note: resource links returned by tools are not guaranteed to appear in the results of {@link ListResourcesRequestresources/list} requests.
--     * Slot: id
--     * Slot: description Description: A description of what this resource represents.This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.
--     * Slot: mimeType Description: The MIME type of this resource, if known.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: size Description: The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.This can be used by Hosts to display file sizes and estimate context window usage.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: type Description: The kind of object, always `resource_link`.
--     * Slot: uri Description: The URI of this resource.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpResourceListChangedNotification Description: An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `resourcesListChanged` filter field.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/resources/list_changed`.
--     * Slot: params_id Description: Common params for any notification.
-- # Class: McpResourceRequestParams Description: Common params for resource-related requests.
--     * Slot: id
--     * Slot: uri Description: The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpResourceTemplate Description: A template description for resources available on the server.
--     * Slot: id
--     * Slot: description Description: A description of what this template is for.This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.
--     * Slot: mimeType Description: The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: uriTemplate Description: A URI template (according to RFC 6570) that can be used to construct resource URIs.
--     * Slot: McpListResourceTemplatesResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpResourceTemplateReference Description: A reference to a resource or resource template definition.
--     * Slot: id
--     * Slot: type Description: The kind of object, always `ref/resource`.
--     * Slot: uri Description: The URI or URI template of the resource.
-- # Class: McpResourceUpdatedNotification Description: A notification from the server to the client, informing it that a resource has changed and may need to be read again. This is only sent for resources the client opted in to via the `resourceSubscriptions` field of a {@link SubscriptionsListenRequestsubscriptions/listen} request.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/resources/updated`.
--     * Slot: params_id Description: Parameters for a `notifications/resources/updated` notification.
-- # Class: McpResourceUpdatedNotificationParams Description: Parameters for a `notifications/resources/updated` notification.
--     * Slot: id
--     * Slot: uri Description: The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpResult Description: Common result fields.
--     * Slot: id
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
-- # Class: McpResultMetaObject Description: Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: id
--     * Slot: mcp_server_info_id Description: Identifies the server software producing the response. Servers SHOULDinclude this field on every response unless specifically configured notto do so.The {@link Implementation} schema requires `name` and `version`; otherfields are optional.The value is self-reported by the server and is not verified by theprotocol. It is intended for display, logging, and debugging. ClientsSHOULD NOT use it to change their behavior, and SHOULD NOT rely on it forsecurity decisions.
-- # Class: McpRoot Description: Represents a root directory or file that the server can operate on.
--     * Slot: id
--     * Slot: name Description: An optional name for the root. This can be used to provide a human-readableidentifier for the root, which may be useful for display purposes or forreferencing the root in other parts of the application.
--     * Slot: uri Description: The URI identifying the root. This *must* start with `file://` for now.This restriction may be relaxed in future versions of the protocol to allowother URI schemes.
--     * Slot: McpListRootsResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpSamplingMessage Description: Describes a message issued to or received from an LLM API.
--     * Slot: id
--     * Slot: content Description: The content the message carries.
--     * Slot: role Description: The sender or recipient of messages and data in a conversation.
--     * Slot: McpCreateMessageRequestParams_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpSamplingMessageContentBlock Description: One of `TextContent`, `ImageContent`, `AudioContent`, `ToolUseContent`, `ToolResultContent`.
--     * Slot: id
-- # Class: McpServerCapabilities Description: Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.
--     * Slot: id
--     * Slot: completions_id Description: Present if the server supports argument autocompletion suggestions.
--     * Slot: experimental_id Description: Experimental, non-standard capabilities that the server supports.
--     * Slot: extensions_id Description: Optional MCP extensions that the server supports. Keys are extension identifiers(e.g., "io.modelcontextprotocol/tasks"), and values are per-extension settingsobjects. An empty object indicates support with no settings.Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with amandatory prefix.
--     * Slot: logging_id Description: Present if the server supports sending log messages to the client.
--     * Slot: prompts_id Description: Present if the server offers any prompt templates.
--     * Slot: resources_id Description: Present if the server offers any resources to read.
--     * Slot: tools_id Description: Present if the server offers any tools to call.
-- # Class: McpServerCapabilitiesExperimental Description: Experimental, non-standard capabilities that the server supports.
--     * Slot: id
-- # Class: McpServerCapabilitiesExtensions Description: Optional MCP extensions that the server supports. Keys are extension identifiers(e.g., "io.modelcontextprotocol/tasks"), and values are per-extension settingsobjects. An empty object indicates support with no settings.Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with amandatory prefix.
--     * Slot: id
-- # Class: McpServerCapabilitiesPrompts Description: Present if the server offers any prompt templates.
--     * Slot: id
--     * Slot: listChanged Description: Whether this server supports notifications for changes to the prompt list.
-- # Class: McpServerCapabilitiesResources Description: Present if the server offers any resources to read.
--     * Slot: id
--     * Slot: listChanged Description: Whether this server supports notifications for changes to the resource list.
--     * Slot: subscribe Description: Whether this server supports subscribing to resource updates.
-- # Class: McpServerCapabilitiesTools Description: Present if the server offers any tools to call.
--     * Slot: id
--     * Slot: listChanged Description: Whether this server supports notifications for changes to the tool list.
-- # Class: McpServerNotification Description: One of `CancelledNotification`, `ProgressNotification`, `ResourceListChangedNotification`, `SubscriptionsAcknowledgedNotification`, `ResourceUpdatedNotification`, `PromptListChangedNotification`, `ToolListChangedNotification`, `LoggingMessageNotification`.
--     * Slot: id
-- # Class: McpServerResult Description: One of `Result`, `InputRequiredResult`, `DiscoverResult`, `ListResourcesResult`, `ListResourceTemplatesResult`, `ReadResourceResult`, `SubscriptionsListenResult`, `ListPromptsResult`, `GetPromptResult`, `ListToolsResult`, `CallToolResult`, `CompleteResult`.
--     * Slot: id
-- # Class: McpSingleSelectEnumSchema Description: One of `UntitledSingleSelectEnumSchema`, `TitledSingleSelectEnumSchema`.
--     * Slot: id
-- # Class: McpStringSchema Description: MCP's `StringSchema`.
--     * Slot: id
--     * Slot: default Description: The value the field takes when the user gives none.
--     * Slot: description Description: A description of the field for the user.
--     * Slot: format Description: The format the string must have.
--     * Slot: maxLength Description: The most characters the field accepts.
--     * Slot: minLength Description: The fewest characters the field accepts.
--     * Slot: title Description: A title for the field.
--     * Slot: type Description: The kind of object, always `string`.
-- # Class: McpSubscriptionFilter Description: The set of notification types a client may opt in to on a{@link SubscriptionsListenRequestsubscriptions/listen} request.Each notification type is **opt-in**; the server **MUST NOT** sendnotification types the client has not explicitly requested here.
--     * Slot: id
--     * Slot: promptsListChanged Description: If true, receive {@link PromptListChangedNotificationnotifications/prompts/list_changed}.
--     * Slot: resourcesListChanged Description: If true, receive {@link ResourceListChangedNotificationnotifications/resources/list_changed}.
--     * Slot: toolsListChanged Description: If true, receive {@link ToolListChangedNotificationnotifications/tools/list_changed}.
-- # Class: McpSubscriptionsAcknowledgedNotification Description: Sent by the server to acknowledge that a{@link SubscriptionsListenRequestsubscriptions/listen} subscription has beenestablished and to report which notification types it agreed to honor.This notification MUST be the first message the server sends carrying thesubscription's ID in `io.modelcontextprotocol/subscriptionId`. The server MUSTNOT send any notification on the subscription before acknowledging it. Onstdio, where every subscription shares one channel, this ordering is definedper subscription ID and not per channel: messages belonging to othersubscriptions MAY be interleaved before it.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/subscriptions/acknowledged`.
--     * Slot: params_id Description: Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.
-- # Class: McpSubscriptionsAcknowledgedNotificationParams Description: Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.
--     * Slot: id
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: notifications_id Description: The subset of requested notification types the server agreed to honor.Only includes notification types the server actually supports; if theclient requested an unsupported type (e.g., `promptsListChanged` whenthe server has no prompts), it is omitted from this set.
-- # Class: McpSubscriptionsListenRequest Description: Sent from the client to open a long-lived channel for receiving notificationsoutside the context of a specific request. Replaces the previous HTTP GETendpoint and ensures consistent behavior between HTTP and STDIO.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `subscriptions/listen`.
--     * Slot: params_id Description: Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.
-- # Class: McpSubscriptionsListenRequestParams Description: Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.
--     * Slot: id
--     * Slot: _meta_id Description: Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
--     * Slot: notifications_id Description: The notifications the client opts in to on this stream. The server**MUST NOT** send notification types the client has not explicitlyrequested.
-- # Class: McpSubscriptionsListenResult Description: The response to a {@link SubscriptionsListenRequestsubscriptions/listen}request, signalling that the subscription has ended gracefully (for example,during server shutdown). Because the listen stream is long-lived, this resultis sent only when the server tears the subscription down; an abrupt transportclose carries no response. The result body is otherwise empty.
--     * Slot: id
--     * Slot: resultType Description: Indicates the type of the result, which allows the client to determinehow to parse the result object.Servers implementing this protocol version MUST include this field.For backward compatibility, when a client receives a result from aserver implementing an earlier protocol version (which does not include`resultType`), the client MUST treat the absent field as `"complete"`.
--     * Slot: _meta_id Description: Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a{@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
-- # Class: McpSubscriptionsListenResultMetaObject Description: Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a{@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
--     * Slot: id
--     * Slot: mcp_subscription_id Description: Identifies the subscription stream this response closes, so the client cancorrelate it with the originating subscription — mirroring the same key onthe stream's notifications. The value is the JSON-RPC ID of the`subscriptions/listen` request that opened the stream (and equals thisresponse's `id`).
--     * Slot: mcp_server_info_id Description: Identifies the server software producing the response. Servers SHOULDinclude this field on every response unless specifically configured notto do so.The {@link Implementation} schema requires `name` and `version`; otherfields are optional.The value is self-reported by the server and is not verified by theprotocol. It is intended for display, logging, and debugging. ClientsSHOULD NOT use it to change their behavior, and SHOULD NOT rely on it forsecurity decisions.
-- # Class: McpSubscriptionsListenResultResponse Description: A successful response from the server for a {@link SubscriptionsListenRequestsubscriptions/listen}request, sent when the server tears the subscription down gracefully.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: result_id Description: The response to a {@link SubscriptionsListenRequestsubscriptions/listen}request, signalling that the subscription has ended gracefully (for example,during server shutdown). Because the listen stream is long-lived, this resultis sent only when the server tears the subscription down; an abrupt transportclose carries no response. The result body is otherwise empty.
-- # Class: McpTextContent Description: Text provided to or from an LLM.
--     * Slot: id
--     * Slot: text Description: The text content of the message.
--     * Slot: type Description: The kind of object, always `text`.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: McpTextResourceContents Description: MCP's `TextResourceContents`.
--     * Slot: id
--     * Slot: mimeType Description: The MIME type of this resource, if known.
--     * Slot: text Description: The text of the item. This must only be set if the item can actually be represented as text (not binary data).
--     * Slot: uri Description: The URI of this resource.
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
-- # Class: McpTitledMultiSelectEnumSchema Description: Schema for multiple-selection enumeration with display titles for each option.
--     * Slot: id
--     * Slot: description Description: Optional description for the enum field.
--     * Slot: maxItems Description: Maximum number of items to select.
--     * Slot: minItems Description: Minimum number of items to select.
--     * Slot: title Description: Optional title for the enum field.
--     * Slot: type Description: The kind of object, always `array`.
--     * Slot: items_id Description: Schema for array items with enum options and display labels.
-- # Class: McpTitledMultiSelectEnumSchemaItems Description: Schema for array items with enum options and display labels.
--     * Slot: id
-- # Class: McpTitledMultiSelectEnumSchemaItemsAnyOf Description: The object MCP's `TitledMultiSelectEnumSchema` holds under `anyOf`.
--     * Slot: id
--     * Slot: const Description: The constant enum value.
--     * Slot: title Description: Display title for this option.
--     * Slot: McpTitledMultiSelectEnumSchemaItems_id Description: Autocreated FK slot
-- # Class: McpTitledSingleSelectEnumSchema Description: Schema for single-selection enumeration with display titles for each option.
--     * Slot: id
--     * Slot: default Description: Optional default value.
--     * Slot: description Description: Optional description for the enum field.
--     * Slot: title Description: Optional title for the enum field.
--     * Slot: type Description: The kind of object, always `string`.
-- # Class: McpTitledSingleSelectEnumSchemaOneOf Description: The object MCP's `TitledSingleSelectEnumSchema` holds under `oneOf`.
--     * Slot: id
--     * Slot: const Description: The enum value.
--     * Slot: title Description: Display label for this option.
--     * Slot: McpTitledSingleSelectEnumSchema_id Description: Autocreated FK slot
-- # Class: McpTool Description: Definition for a tool the client can call.
--     * Slot: id
--     * Slot: description Description: A human-readable description of the tool.This can be used by clients to improve the LLM's understanding of available tools. It can be thought of like a "hint" to the model.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood,even by those unfamiliar with domain-specific terminology.If not provided, the name should be used for display (except for {@link Tool},where `annotations.title` should be given precedence over using `name`,if present).
--     * Slot: McpCreateMessageRequestParams_id Description: Autocreated FK slot
--     * Slot: McpListToolsResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.Valid keys have two segments:**Prefix:**- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.**Name:**- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
--     * Slot: annotations_id Description: Optional additional tool information.Display name precedence order is: `title`, `annotations.title`, then `name`.
--     * Slot: inputSchema_id Description: A JSON Schema object defining the expected parameters for the tool.Tool arguments are always JSON objects, so `type: "object"` is required at the root.Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — includingcomposition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords(`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any otherstandard validation or annotation keywords.Property schemas may carry an `x-mcp-header` annotation to mirror theargument value into an HTTP header on the Streamable HTTP transport. Seethe Streamable HTTP transport specification for the validity andextraction rules.Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
--     * Slot: outputSchema_id Description: An optional JSON Schema object defining the structure of the tool's output returned inthe structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
-- # Class: McpToolAnnotations Description: Additional properties describing a {@link Tool} to clients.NOTE: all properties in `ToolAnnotations` are **hints**.They are not guaranteed to provide a faithful description oftool behavior (including descriptive properties like `title`).Clients should never make tool use decisions based on `ToolAnnotations`received from untrusted servers.
--     * Slot: id
--     * Slot: destructiveHint Description: If true, the tool may perform destructive updates to its environment.If false, the tool performs only additive updates.(This property is meaningful only when `readOnlyHint == false`)Default: true
--     * Slot: idempotentHint Description: If true, calling the tool repeatedly with the same argumentswill have no additional effect on its environment.(This property is meaningful only when `readOnlyHint == false`)Default: false
--     * Slot: openWorldHint Description: If true, this tool may interact with an "open world" of externalentities. If false, the tool's domain of interaction is closed.For example, the world of a web search tool is open, whereas thatof a memory tool is not.Default: true
--     * Slot: readOnlyHint Description: If true, the tool does not modify its environment.Default: false
--     * Slot: title Description: A human-readable title for the tool.
-- # Class: McpToolChoice Description: Controls tool selection behavior for sampling requests.
--     * Slot: id
--     * Slot: mode Description: Controls the tool use ability of the model:- `"auto"`: Model decides whether to use tools (default)- `"required"`: Model MUST use at least one tool before completing- `"none"`: Model MUST NOT use any tools
-- # Class: McpToolInputSchema Description: A JSON Schema object defining the expected parameters for the tool.Tool arguments are always JSON objects, so `type: "object"` is required at the root.Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — includingcomposition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords(`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any otherstandard validation or annotation keywords.Property schemas may carry an `x-mcp-header` annotation to mirror theargument value into an HTTP header on the Streamable HTTP transport. Seethe Streamable HTTP transport specification for the validity andextraction rules.Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
--     * Slot: id
--     * Slot: schema_dialect Description: The JSON Schema dialect the schema is written in.
--     * Slot: type Description: The kind of object, always `object`.
-- # Class: McpToolListChangedNotification Description: An optional notification from the server to the client, informing it that the list of tools it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `toolsListChanged` filter field.
--     * Slot: id
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: method Description: The method's name, always `notifications/tools/list_changed`.
--     * Slot: params_id Description: Common params for any notification.
-- # Class: McpToolOutputSchema Description: An optional JSON Schema object defining the structure of the tool's output returned inthe structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
--     * Slot: id
--     * Slot: schema_dialect Description: The JSON Schema dialect the schema is written in.
-- # Class: McpToolResultContent Description: The result of a tool use, provided by the user back to the assistant.
--     * Slot: id
--     * Slot: isError Description: Whether the tool use resulted in an error.If true, the content typically describes the error that occurred.Default: false
--     * Slot: toolUseId Description: The ID of the tool use this result corresponds to.This MUST match the ID from a previous {@link ToolUseContent}.
--     * Slot: type Description: The kind of object, always `tool_result`.
--     * Slot: _meta_id Description: Optional metadata about the tool result. Clients SHOULD preserve this field whenincluding tool results in subsequent sampling requests to enable caching optimizations.
--     * Slot: structuredContent_id Description: An optional structured result value.This can be any JSON value (object, array, string, number, boolean, or null).If the tool defined an {@link Tool.outputSchema}, this SHOULD conform to that schema.
-- # Class: McpToolUseContent Description: A request from the assistant to call a tool.
--     * Slot: uid
--     * Slot: id Description: A unique identifier for this tool use.This ID is used to match tool results to their corresponding tool uses.
--     * Slot: name Description: The name of the tool to call.
--     * Slot: type Description: The kind of object, always `tool_use`.
--     * Slot: _meta_id Description: Optional metadata about the tool use. Clients SHOULD preserve this field whenincluding tool uses in subsequent sampling requests to enable caching optimizations.
--     * Slot: input_id Description: The arguments to pass to the tool, conforming to the tool's input schema.
-- # Class: McpUnsupportedProtocolVersionError Description: Returned when the request's protocol version is unknown to the server orunsupported (e.g., a known experimental or draft version the server haschosen not to implement). For HTTP, the response status code MUST be`400 Bad Request`.
--     * Slot: uid
--     * Slot: id Description: A uniquely identifying ID for a request in JSON-RPC.
--     * Slot: jsonrpc Description: The JSON-RPC version, always `2.0`.
--     * Slot: error_id Description: The error the request ended with.
-- # Class: McpUnsupportedProtocolVersionErrorError Description: MCP's `Error`, with the code and data this error carries.
--     * Slot: id
--     * Slot: code Description: The error code, always `-32022`.
--     * Slot: message Description: A short description of the error. The message SHOULD be limited to a concise single sentence.
--     * Slot: data_id Description: Details of the error.
-- # Class: McpUnsupportedProtocolVersionErrorErrorData Description: The object MCP's `UnsupportedProtocolVersionError` holds under `data`.
--     * Slot: id
--     * Slot: requested Description: The protocol version that was requested by the client.
-- # Class: McpUntitledMultiSelectEnumSchema Description: Schema for multiple-selection enumeration without display titles for options.
--     * Slot: id
--     * Slot: description Description: Optional description for the enum field.
--     * Slot: maxItems Description: Maximum number of items to select.
--     * Slot: minItems Description: Minimum number of items to select.
--     * Slot: title Description: Optional title for the enum field.
--     * Slot: type Description: The kind of object, always `array`.
--     * Slot: items_id Description: Schema for the array items.
-- # Class: McpUntitledMultiSelectEnumSchemaItems Description: Schema for the array items.
--     * Slot: id
--     * Slot: type Description: The kind of object, always `string`.
-- # Class: McpUntitledSingleSelectEnumSchema Description: Schema for single-selection enumeration without display titles for options.
--     * Slot: id
--     * Slot: default Description: Optional default value.
--     * Slot: description Description: Optional description for the enum field.
--     * Slot: title Description: Optional title for the enum field.
--     * Slot: type Description: The kind of object, always `string`.
-- # Class: McpAnnotations_audience
--     * Slot: McpAnnotations_id Description: Autocreated FK slot
--     * Slot: audience Description: Describes who the intended audience of this object or data is.It can include multiple entries to indicate content useful for multiple audiences (e.g., `["user", "assistant"]`).
-- # Class: McpCompleteResultCompletion_values
--     * Slot: McpCompleteResultCompletion_id Description: Autocreated FK slot
--     * Slot: values Description: An array of completion values. Must not exceed 100 items.
-- # Class: McpCreateMessageRequestParams_stopSequences
--     * Slot: McpCreateMessageRequestParams_id Description: Autocreated FK slot
--     * Slot: stopSequences Description: Sequences at which the model should stop generating.
-- # Class: McpDiscoverResult_supportedVersions
--     * Slot: McpDiscoverResult_id Description: Autocreated FK slot
--     * Slot: supportedVersions Description: MCP Protocol Versions this server supports. The client should choose aversion from this list for use in subsequent requests.
-- # Class: McpElicitRequestFormParamsRequestedSchema_required
--     * Slot: McpElicitRequestFormParamsRequestedSchema_id Description: Autocreated FK slot
--     * Slot: required Description: The names of the fields the user must fill in.
-- # Class: McpIcon_sizes
--     * Slot: McpIcon_id Description: Autocreated FK slot
--     * Slot: sizes Description: Optional array of strings that specify sizes at which the icon can be used.Each string should be in WxH format (e.g., `"48x48"`, `"96x96"`) or `"any"` for scalable formats like SVG.If not provided, the client should assume that the icon can be used at any size.
-- # Class: McpLegacyTitledEnumSchema_enum
--     * Slot: McpLegacyTitledEnumSchema_id Description: Autocreated FK slot
--     * Slot: enum Description: The values the field offers.
-- # Class: McpLegacyTitledEnumSchema_enumNames
--     * Slot: McpLegacyTitledEnumSchema_id Description: Autocreated FK slot
--     * Slot: enumNames Description: (Legacy) Display names for enum values.Non-standard according to JSON schema 2020-12.
-- # Class: McpReadResourceResult_contents
--     * Slot: McpReadResourceResult_id Description: Autocreated FK slot
--     * Slot: contents Description: The contents of the resource that was read.
-- # Class: McpSubscriptionFilter_resourceSubscriptions
--     * Slot: McpSubscriptionFilter_id Description: Autocreated FK slot
--     * Slot: resourceSubscriptions Description: Subscribe to {@link ResourceUpdatedNotificationnotifications/resources/updated} for these resource URIs.Replaces the former `resources/subscribe` RPC.
-- # Class: McpTitledMultiSelectEnumSchema_default
--     * Slot: McpTitledMultiSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: default Description: Optional default value.
-- # Class: McpUnsupportedProtocolVersionErrorErrorData_supported
--     * Slot: McpUnsupportedProtocolVersionErrorErrorData_id Description: Autocreated FK slot
--     * Slot: supported Description: Protocol versions the server supports. The client should choose amutually supported version from this list and retry.
-- # Class: McpUntitledMultiSelectEnumSchema_default
--     * Slot: McpUntitledMultiSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: default Description: Optional default value.
-- # Class: McpUntitledMultiSelectEnumSchemaItems_enum
--     * Slot: McpUntitledMultiSelectEnumSchemaItems_id Description: Autocreated FK slot
--     * Slot: enum Description: Array of enum values to choose from.
-- # Class: McpUntitledSingleSelectEnumSchema_enum
--     * Slot: McpUntitledSingleSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: enum Description: Array of enum values to choose from.

CREATE TABLE "McpAnnotations" (
	id INTEGER NOT NULL,
	"lastModified" TEXT,
	priority FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpAnnotations_id" ON "McpAnnotations" (id);

CREATE TABLE "McpBaseMetadata" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpBaseMetadata_id" ON "McpBaseMetadata" (id);

CREATE TABLE "McpBooleanSchema" (
	id INTEGER NOT NULL,
	"default" BOOLEAN,
	description TEXT,
	title TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpBooleanSchema_id" ON "McpBooleanSchema" (id);

CREATE TABLE "McpCallToolResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_McpCallToolResultResponse_uid" ON "McpCallToolResultResponse" (uid);

CREATE TABLE "McpClientCapabilitiesExperimental" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpClientCapabilitiesExperimental_id" ON "McpClientCapabilitiesExperimental" (id);

CREATE TABLE "McpClientCapabilitiesExtensions" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpClientCapabilitiesExtensions_id" ON "McpClientCapabilitiesExtensions" (id);

CREATE TABLE "McpClientCapabilitiesRoots" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpClientCapabilitiesRoots_id" ON "McpClientCapabilitiesRoots" (id);

CREATE TABLE "McpClientRequest" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpClientRequest_id" ON "McpClientRequest" (id);

CREATE TABLE "McpCompleteRequestParamsArgument" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpCompleteRequestParamsArgument_id" ON "McpCompleteRequestParamsArgument" (id);

CREATE TABLE "McpCompleteRequestParamsContextArguments" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpCompleteRequestParamsContextArguments_id" ON "McpCompleteRequestParamsContextArguments" (id);

CREATE TABLE "McpCompleteResultCompletion" (
	id INTEGER NOT NULL,
	"hasMore" BOOLEAN,
	total INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpCompleteResultCompletion_id" ON "McpCompleteResultCompletion" (id);

CREATE TABLE "McpElicitRequestFormParamsRequestedSchemaProperties" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpElicitRequestFormParamsRequestedSchemaProperties_id" ON "McpElicitRequestFormParamsRequestedSchemaProperties" (id);

CREATE TABLE "McpElicitRequestParams" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpElicitRequestParams_id" ON "McpElicitRequestParams" (id);

CREATE TABLE "McpElicitRequestURLParams" (
	id INTEGER NOT NULL,
	message TEXT NOT NULL,
	mode TEXT NOT NULL,
	url TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpElicitRequestURLParams_id" ON "McpElicitRequestURLParams" (id);

CREATE TABLE "McpElicitResultContent" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpElicitResultContent_id" ON "McpElicitResultContent" (id);

CREATE TABLE "McpEnumSchema" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpEnumSchema_id" ON "McpEnumSchema" (id);

CREATE TABLE "McpGetPromptRequestParamsArguments" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpGetPromptRequestParamsArguments_id" ON "McpGetPromptRequestParamsArguments" (id);

CREATE TABLE "McpGetPromptResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_McpGetPromptResultResponse_uid" ON "McpGetPromptResultResponse" (uid);

CREATE TABLE "McpIcons" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpIcons_id" ON "McpIcons" (id);

CREATE TABLE "McpImplementation" (
	id INTEGER NOT NULL,
	description TEXT,
	name TEXT NOT NULL,
	title TEXT,
	version TEXT NOT NULL,
	"websiteUrl" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpImplementation_id" ON "McpImplementation" (id);

CREATE TABLE "McpInputRequest" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpInputRequest_id" ON "McpInputRequest" (id);

CREATE TABLE "McpInputRequests" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpInputRequests_id" ON "McpInputRequests" (id);

CREATE TABLE "McpInputResponse" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpInputResponse_id" ON "McpInputResponse" (id);

CREATE TABLE "McpInputResponses" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpInputResponses_id" ON "McpInputResponses" (id);

CREATE TABLE "McpJSONObject" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpJSONObject_id" ON "McpJSONObject" (id);

CREATE TABLE "McpJSONRPCMessage" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpJSONRPCMessage_id" ON "McpJSONRPCMessage" (id);

CREATE TABLE "McpJSONRPCResponse" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpJSONRPCResponse_id" ON "McpJSONRPCResponse" (id);

CREATE TABLE "McpJSONValue" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpJSONValue_id" ON "McpJSONValue" (id);

CREATE TABLE "McpLegacyTitledEnumSchema" (
	id INTEGER NOT NULL,
	"default" TEXT,
	description TEXT,
	title TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpLegacyTitledEnumSchema_id" ON "McpLegacyTitledEnumSchema" (id);

CREATE TABLE "McpListRootsResult" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpListRootsResult_id" ON "McpListRootsResult" (id);

CREATE TABLE "McpMetaObject" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpMetaObject_id" ON "McpMetaObject" (id);

CREATE TABLE "McpModelPreferences" (
	id INTEGER NOT NULL,
	"costPriority" FLOAT,
	"intelligencePriority" FLOAT,
	"speedPriority" FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpModelPreferences_id" ON "McpModelPreferences" (id);

CREATE TABLE "McpMultiSelectEnumSchema" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpMultiSelectEnumSchema_id" ON "McpMultiSelectEnumSchema" (id);

CREATE TABLE "McpNotificationMetaObject" (
	id INTEGER NOT NULL,
	mcp_subscription_id TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpNotificationMetaObject_id" ON "McpNotificationMetaObject" (id);

CREATE TABLE "McpNumberSchema" (
	id INTEGER NOT NULL,
	"default" FLOAT,
	description TEXT,
	maximum FLOAT,
	minimum FLOAT,
	title TEXT,
	type VARCHAR(7) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpNumberSchema_id" ON "McpNumberSchema" (id);

CREATE TABLE "McpPrimitiveSchemaDefinition" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpPrimitiveSchemaDefinition_id" ON "McpPrimitiveSchemaDefinition" (id);

CREATE TABLE "McpPromptReference" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	title TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpPromptReference_id" ON "McpPromptReference" (id);

CREATE TABLE "McpReadResourceResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_McpReadResourceResultResponse_uid" ON "McpReadResourceResultResponse" (uid);

CREATE TABLE "McpResourceTemplateReference" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	uri TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpResourceTemplateReference_id" ON "McpResourceTemplateReference" (id);

CREATE TABLE "McpSamplingMessageContentBlock" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpSamplingMessageContentBlock_id" ON "McpSamplingMessageContentBlock" (id);

CREATE TABLE "McpServerCapabilitiesExperimental" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerCapabilitiesExperimental_id" ON "McpServerCapabilitiesExperimental" (id);

CREATE TABLE "McpServerCapabilitiesExtensions" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerCapabilitiesExtensions_id" ON "McpServerCapabilitiesExtensions" (id);

CREATE TABLE "McpServerCapabilitiesPrompts" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerCapabilitiesPrompts_id" ON "McpServerCapabilitiesPrompts" (id);

CREATE TABLE "McpServerCapabilitiesResources" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	subscribe BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerCapabilitiesResources_id" ON "McpServerCapabilitiesResources" (id);

CREATE TABLE "McpServerCapabilitiesTools" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerCapabilitiesTools_id" ON "McpServerCapabilitiesTools" (id);

CREATE TABLE "McpServerNotification" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerNotification_id" ON "McpServerNotification" (id);

CREATE TABLE "McpServerResult" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpServerResult_id" ON "McpServerResult" (id);

CREATE TABLE "McpSingleSelectEnumSchema" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpSingleSelectEnumSchema_id" ON "McpSingleSelectEnumSchema" (id);

CREATE TABLE "McpStringSchema" (
	id INTEGER NOT NULL,
	"default" TEXT,
	description TEXT,
	format VARCHAR(9),
	"maxLength" INTEGER,
	"minLength" INTEGER,
	title TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpStringSchema_id" ON "McpStringSchema" (id);

CREATE TABLE "McpSubscriptionFilter" (
	id INTEGER NOT NULL,
	"promptsListChanged" BOOLEAN,
	"resourcesListChanged" BOOLEAN,
	"toolsListChanged" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpSubscriptionFilter_id" ON "McpSubscriptionFilter" (id);

CREATE TABLE "McpTitledMultiSelectEnumSchemaItems" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpTitledMultiSelectEnumSchemaItems_id" ON "McpTitledMultiSelectEnumSchemaItems" (id);

CREATE TABLE "McpTitledSingleSelectEnumSchema" (
	id INTEGER NOT NULL,
	"default" TEXT,
	description TEXT,
	title TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpTitledSingleSelectEnumSchema_id" ON "McpTitledSingleSelectEnumSchema" (id);

CREATE TABLE "McpToolAnnotations" (
	id INTEGER NOT NULL,
	"destructiveHint" BOOLEAN,
	"idempotentHint" BOOLEAN,
	"openWorldHint" BOOLEAN,
	"readOnlyHint" BOOLEAN,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpToolAnnotations_id" ON "McpToolAnnotations" (id);

CREATE TABLE "McpToolChoice" (
	id INTEGER NOT NULL,
	mode VARCHAR(8),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpToolChoice_id" ON "McpToolChoice" (id);

CREATE TABLE "McpToolInputSchema" (
	id INTEGER NOT NULL,
	schema_dialect TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpToolInputSchema_id" ON "McpToolInputSchema" (id);

CREATE TABLE "McpToolOutputSchema" (
	id INTEGER NOT NULL,
	schema_dialect TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpToolOutputSchema_id" ON "McpToolOutputSchema" (id);

CREATE TABLE "McpUnsupportedProtocolVersionErrorErrorData" (
	id INTEGER NOT NULL,
	requested TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpUnsupportedProtocolVersionErrorErrorData_id" ON "McpUnsupportedProtocolVersionErrorErrorData" (id);

CREATE TABLE "McpUntitledMultiSelectEnumSchemaItems" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpUntitledMultiSelectEnumSchemaItems_id" ON "McpUntitledMultiSelectEnumSchemaItems" (id);

CREATE TABLE "McpUntitledSingleSelectEnumSchema" (
	id INTEGER NOT NULL,
	"default" TEXT,
	description TEXT,
	title TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_McpUntitledSingleSelectEnumSchema_id" ON "McpUntitledSingleSelectEnumSchema" (id);

CREATE TABLE "McpAudioContent" (
	id INTEGER NOT NULL,
	data TEXT NOT NULL,
	"mimeType" TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpAudioContent_id" ON "McpAudioContent" (id);

CREATE TABLE "McpBlobResourceContents" (
	id INTEGER NOT NULL,
	blob TEXT NOT NULL,
	"mimeType" TEXT,
	uri TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpBlobResourceContents_id" ON "McpBlobResourceContents" (id);

CREATE TABLE "McpCancelledNotificationParams" (
	id INTEGER NOT NULL,
	reason TEXT,
	"requestId" TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpNotificationMetaObject" (id)
);
CREATE INDEX "ix_McpCancelledNotificationParams_id" ON "McpCancelledNotificationParams" (id);

CREATE TABLE "McpClientCapabilitiesElicitation" (
	id INTEGER NOT NULL,
	form_id INTEGER,
	url_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(form_id) REFERENCES "McpJSONObject" (id),
	FOREIGN KEY(url_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpClientCapabilitiesElicitation_id" ON "McpClientCapabilitiesElicitation" (id);

CREATE TABLE "McpClientCapabilitiesSampling" (
	id INTEGER NOT NULL,
	context_id INTEGER,
	tools_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(context_id) REFERENCES "McpJSONObject" (id),
	FOREIGN KEY(tools_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpClientCapabilitiesSampling_id" ON "McpClientCapabilitiesSampling" (id);

CREATE TABLE "McpCompleteRequestParamsContext" (
	id INTEGER NOT NULL,
	arguments_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(arguments_id) REFERENCES "McpCompleteRequestParamsContextArguments" (id)
);
CREATE INDEX "ix_McpCompleteRequestParamsContext_id" ON "McpCompleteRequestParamsContext" (id);

CREATE TABLE "McpCreateMessageRequestParams" (
	id INTEGER NOT NULL,
	"includeContext" VARCHAR(10),
	"maxTokens" INTEGER NOT NULL,
	"systemPrompt" TEXT,
	temperature FLOAT,
	metadata_id INTEGER,
	"modelPreferences_id" INTEGER,
	"toolChoice_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "McpJSONObject" (id),
	FOREIGN KEY("modelPreferences_id") REFERENCES "McpModelPreferences" (id),
	FOREIGN KEY("toolChoice_id") REFERENCES "McpToolChoice" (id)
);
CREATE INDEX "ix_McpCreateMessageRequestParams_id" ON "McpCreateMessageRequestParams" (id);

CREATE TABLE "McpCreateMessageResult" (
	id INTEGER NOT NULL,
	content TEXT NOT NULL,
	model TEXT NOT NULL,
	role VARCHAR(9) NOT NULL,
	"stopReason" TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpCreateMessageResult_id" ON "McpCreateMessageResult" (id);

CREATE TABLE "McpElicitRequest" (
	id INTEGER NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpElicitRequestParams" (id)
);
CREATE INDEX "ix_McpElicitRequest_id" ON "McpElicitRequest" (id);

CREATE TABLE "McpElicitRequestFormParamsRequestedSchema" (
	id INTEGER NOT NULL,
	schema_dialect TEXT,
	type TEXT NOT NULL,
	properties_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(properties_id) REFERENCES "McpElicitRequestFormParamsRequestedSchemaProperties" (id)
);
CREATE INDEX "ix_McpElicitRequestFormParamsRequestedSchema_id" ON "McpElicitRequestFormParamsRequestedSchema" (id);

CREATE TABLE "McpElicitResult" (
	id INTEGER NOT NULL,
	action VARCHAR(7) NOT NULL,
	content_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(content_id) REFERENCES "McpElicitResultContent" (id)
);
CREATE INDEX "ix_McpElicitResult_id" ON "McpElicitResult" (id);

CREATE TABLE "McpEmbeddedResource" (
	id INTEGER NOT NULL,
	resource TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpEmbeddedResource_id" ON "McpEmbeddedResource" (id);

CREATE TABLE "McpError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpError_id" ON "McpError" (id);

CREATE TABLE "McpHeaderMismatchErrorError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpHeaderMismatchErrorError_id" ON "McpHeaderMismatchErrorError" (id);

CREATE TABLE "McpImageContent" (
	id INTEGER NOT NULL,
	data TEXT NOT NULL,
	"mimeType" TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpImageContent_id" ON "McpImageContent" (id);

CREATE TABLE "McpInternalError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpInternalError_id" ON "McpInternalError" (id);

CREATE TABLE "McpInvalidParamsError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpInvalidParamsError_id" ON "McpInvalidParamsError" (id);

CREATE TABLE "McpInvalidRequestError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpInvalidRequestError_id" ON "McpInvalidRequestError" (id);

CREATE TABLE "McpJSONRPCNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpJSONRPCNotification_id" ON "McpJSONRPCNotification" (id);

CREATE TABLE "McpJSONRPCRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpJSONRPCRequest_uid" ON "McpJSONRPCRequest" (uid);

CREATE TABLE "McpListRootsRequestParams" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpListRootsRequestParams_id" ON "McpListRootsRequestParams" (id);

CREATE TABLE "McpLoggingMessageNotificationParams" (
	id INTEGER NOT NULL,
	level VARCHAR(9) NOT NULL,
	logger TEXT,
	_meta_id INTEGER,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpNotificationMetaObject" (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpLoggingMessageNotificationParams_id" ON "McpLoggingMessageNotificationParams" (id);

CREATE TABLE "McpMethodNotFoundError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpMethodNotFoundError_id" ON "McpMethodNotFoundError" (id);

CREATE TABLE "McpModelHint" (
	id INTEGER NOT NULL,
	name TEXT,
	"McpModelPreferences_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpModelPreferences_id") REFERENCES "McpModelPreferences" (id)
);
CREATE INDEX "ix_McpModelHint_id" ON "McpModelHint" (id);

CREATE TABLE "McpNotification" (
	id INTEGER NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpNotification_id" ON "McpNotification" (id);

CREATE TABLE "McpNotificationParams" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpNotificationMetaObject" (id)
);
CREATE INDEX "ix_McpNotificationParams_id" ON "McpNotificationParams" (id);

CREATE TABLE "McpParseError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpParseError_id" ON "McpParseError" (id);

CREATE TABLE "McpProgressNotificationParams" (
	id INTEGER NOT NULL,
	message TEXT,
	progress FLOAT NOT NULL,
	"progressToken" TEXT NOT NULL,
	total FLOAT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpNotificationMetaObject" (id)
);
CREATE INDEX "ix_McpProgressNotificationParams_id" ON "McpProgressNotificationParams" (id);

CREATE TABLE "McpRequest" (
	id INTEGER NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpRequest_id" ON "McpRequest" (id);

CREATE TABLE "McpResourceContents" (
	id INTEGER NOT NULL,
	"mimeType" TEXT,
	uri TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpResourceContents_id" ON "McpResourceContents" (id);

CREATE TABLE "McpResourceLink" (
	id INTEGER NOT NULL,
	description TEXT,
	"mimeType" TEXT,
	name TEXT NOT NULL,
	size INTEGER,
	title TEXT,
	type TEXT NOT NULL,
	uri TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpResourceLink_id" ON "McpResourceLink" (id);

CREATE TABLE "McpResourceUpdatedNotificationParams" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpNotificationMetaObject" (id)
);
CREATE INDEX "ix_McpResourceUpdatedNotificationParams_id" ON "McpResourceUpdatedNotificationParams" (id);

CREATE TABLE "McpResultMetaObject" (
	id INTEGER NOT NULL,
	mcp_server_info_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(mcp_server_info_id) REFERENCES "McpImplementation" (id)
);
CREATE INDEX "ix_McpResultMetaObject_id" ON "McpResultMetaObject" (id);

CREATE TABLE "McpRoot" (
	id INTEGER NOT NULL,
	name TEXT,
	uri TEXT NOT NULL,
	"McpListRootsResult_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpListRootsResult_id") REFERENCES "McpListRootsResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpRoot_id" ON "McpRoot" (id);

CREATE TABLE "McpServerCapabilities" (
	id INTEGER NOT NULL,
	completions_id INTEGER,
	experimental_id INTEGER,
	extensions_id INTEGER,
	logging_id INTEGER,
	prompts_id INTEGER,
	resources_id INTEGER,
	tools_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(completions_id) REFERENCES "McpJSONObject" (id),
	FOREIGN KEY(experimental_id) REFERENCES "McpServerCapabilitiesExperimental" (id),
	FOREIGN KEY(extensions_id) REFERENCES "McpServerCapabilitiesExtensions" (id),
	FOREIGN KEY(logging_id) REFERENCES "McpJSONObject" (id),
	FOREIGN KEY(prompts_id) REFERENCES "McpServerCapabilitiesPrompts" (id),
	FOREIGN KEY(resources_id) REFERENCES "McpServerCapabilitiesResources" (id),
	FOREIGN KEY(tools_id) REFERENCES "McpServerCapabilitiesTools" (id)
);
CREATE INDEX "ix_McpServerCapabilities_id" ON "McpServerCapabilities" (id);

CREATE TABLE "McpSubscriptionsAcknowledgedNotificationParams" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	notifications_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpNotificationMetaObject" (id),
	FOREIGN KEY(notifications_id) REFERENCES "McpSubscriptionFilter" (id)
);
CREATE INDEX "ix_McpSubscriptionsAcknowledgedNotificationParams_id" ON "McpSubscriptionsAcknowledgedNotificationParams" (id);

CREATE TABLE "McpSubscriptionsListenResultMetaObject" (
	id INTEGER NOT NULL,
	mcp_subscription_id TEXT NOT NULL,
	mcp_server_info_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(mcp_server_info_id) REFERENCES "McpImplementation" (id)
);
CREATE INDEX "ix_McpSubscriptionsListenResultMetaObject_id" ON "McpSubscriptionsListenResultMetaObject" (id);

CREATE TABLE "McpTextContent" (
	id INTEGER NOT NULL,
	text TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpTextContent_id" ON "McpTextContent" (id);

CREATE TABLE "McpTextResourceContents" (
	id INTEGER NOT NULL,
	"mimeType" TEXT,
	text TEXT NOT NULL,
	uri TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpTextResourceContents_id" ON "McpTextResourceContents" (id);

CREATE TABLE "McpTitledMultiSelectEnumSchema" (
	id INTEGER NOT NULL,
	description TEXT,
	"maxItems" INTEGER,
	"minItems" INTEGER,
	title TEXT,
	type TEXT NOT NULL,
	items_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(items_id) REFERENCES "McpTitledMultiSelectEnumSchemaItems" (id)
);
CREATE INDEX "ix_McpTitledMultiSelectEnumSchema_id" ON "McpTitledMultiSelectEnumSchema" (id);

CREATE TABLE "McpTitledMultiSelectEnumSchemaItemsAnyOf" (
	id INTEGER NOT NULL,
	const TEXT NOT NULL,
	title TEXT NOT NULL,
	"McpTitledMultiSelectEnumSchemaItems_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpTitledMultiSelectEnumSchemaItems_id") REFERENCES "McpTitledMultiSelectEnumSchemaItems" (id)
);
CREATE INDEX "ix_McpTitledMultiSelectEnumSchemaItemsAnyOf_id" ON "McpTitledMultiSelectEnumSchemaItemsAnyOf" (id);

CREATE TABLE "McpTitledSingleSelectEnumSchemaOneOf" (
	id INTEGER NOT NULL,
	const TEXT NOT NULL,
	title TEXT NOT NULL,
	"McpTitledSingleSelectEnumSchema_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpTitledSingleSelectEnumSchema_id") REFERENCES "McpTitledSingleSelectEnumSchema" (id)
);
CREATE INDEX "ix_McpTitledSingleSelectEnumSchemaOneOf_id" ON "McpTitledSingleSelectEnumSchemaOneOf" (id);

CREATE TABLE "McpToolResultContent" (
	id INTEGER NOT NULL,
	"isError" BOOLEAN,
	"toolUseId" TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	"structuredContent_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY("structuredContent_id") REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpToolResultContent_id" ON "McpToolResultContent" (id);

CREATE TABLE "McpToolUseContent" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	input_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(input_id) REFERENCES "McpJSONObject" (id)
);
CREATE INDEX "ix_McpToolUseContent_uid" ON "McpToolUseContent" (uid);

CREATE TABLE "McpUnsupportedProtocolVersionErrorError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpUnsupportedProtocolVersionErrorErrorData" (id)
);
CREATE INDEX "ix_McpUnsupportedProtocolVersionErrorError_id" ON "McpUnsupportedProtocolVersionErrorError" (id);

CREATE TABLE "McpUntitledMultiSelectEnumSchema" (
	id INTEGER NOT NULL,
	description TEXT,
	"maxItems" INTEGER,
	"minItems" INTEGER,
	title TEXT,
	type TEXT NOT NULL,
	items_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(items_id) REFERENCES "McpUntitledMultiSelectEnumSchemaItems" (id)
);
CREATE INDEX "ix_McpUntitledMultiSelectEnumSchema_id" ON "McpUntitledMultiSelectEnumSchema" (id);

CREATE TABLE "McpAnnotations_audience" (
	"McpAnnotations_id" INTEGER,
	audience VARCHAR(9),
	PRIMARY KEY ("McpAnnotations_id", audience),
	FOREIGN KEY("McpAnnotations_id") REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpAnnotations_audience_audience" ON "McpAnnotations_audience" (audience);
CREATE INDEX "ix_McpAnnotations_audience_McpAnnotations_id" ON "McpAnnotations_audience" ("McpAnnotations_id");

CREATE TABLE "McpCompleteResultCompletion_values" (
	"McpCompleteResultCompletion_id" INTEGER,
	"values" TEXT NOT NULL,
	PRIMARY KEY ("McpCompleteResultCompletion_id", "values"),
	FOREIGN KEY("McpCompleteResultCompletion_id") REFERENCES "McpCompleteResultCompletion" (id)
);
CREATE INDEX "ix_McpCompleteResultCompletion_values_values" ON "McpCompleteResultCompletion_values" ("values");
CREATE INDEX "ix_McpCompleteResultCompletion_values_McpCompleteResultCompletion_id" ON "McpCompleteResultCompletion_values" ("McpCompleteResultCompletion_id");

CREATE TABLE "McpLegacyTitledEnumSchema_enum" (
	"McpLegacyTitledEnumSchema_id" INTEGER,
	enum TEXT NOT NULL,
	PRIMARY KEY ("McpLegacyTitledEnumSchema_id", enum),
	FOREIGN KEY("McpLegacyTitledEnumSchema_id") REFERENCES "McpLegacyTitledEnumSchema" (id)
);
CREATE INDEX "ix_McpLegacyTitledEnumSchema_enum_McpLegacyTitledEnumSchema_id" ON "McpLegacyTitledEnumSchema_enum" ("McpLegacyTitledEnumSchema_id");
CREATE INDEX "ix_McpLegacyTitledEnumSchema_enum_enum" ON "McpLegacyTitledEnumSchema_enum" (enum);

CREATE TABLE "McpLegacyTitledEnumSchema_enumNames" (
	"McpLegacyTitledEnumSchema_id" INTEGER,
	"enumNames" TEXT,
	PRIMARY KEY ("McpLegacyTitledEnumSchema_id", "enumNames"),
	FOREIGN KEY("McpLegacyTitledEnumSchema_id") REFERENCES "McpLegacyTitledEnumSchema" (id)
);
CREATE INDEX "ix_McpLegacyTitledEnumSchema_enumNames_enumNames" ON "McpLegacyTitledEnumSchema_enumNames" ("enumNames");
CREATE INDEX "ix_McpLegacyTitledEnumSchema_enumNames_McpLegacyTitledEnumSchema_id" ON "McpLegacyTitledEnumSchema_enumNames" ("McpLegacyTitledEnumSchema_id");

CREATE TABLE "McpSubscriptionFilter_resourceSubscriptions" (
	"McpSubscriptionFilter_id" INTEGER,
	"resourceSubscriptions" TEXT,
	PRIMARY KEY ("McpSubscriptionFilter_id", "resourceSubscriptions"),
	FOREIGN KEY("McpSubscriptionFilter_id") REFERENCES "McpSubscriptionFilter" (id)
);
CREATE INDEX "ix_McpSubscriptionFilter_resourceSubscriptions_resourceSubscriptions" ON "McpSubscriptionFilter_resourceSubscriptions" ("resourceSubscriptions");
CREATE INDEX "ix_McpSubscriptionFilter_resourceSubscriptions_McpSubscriptionFilter_id" ON "McpSubscriptionFilter_resourceSubscriptions" ("McpSubscriptionFilter_id");

CREATE TABLE "McpUnsupportedProtocolVersionErrorErrorData_supported" (
	"McpUnsupportedProtocolVersionErrorErrorData_id" INTEGER,
	supported TEXT NOT NULL,
	PRIMARY KEY ("McpUnsupportedProtocolVersionErrorErrorData_id", supported),
	FOREIGN KEY("McpUnsupportedProtocolVersionErrorErrorData_id") REFERENCES "McpUnsupportedProtocolVersionErrorErrorData" (id)
);
CREATE INDEX "ix_McpUnsupportedProtocolVersionErrorErrorData_supported_McpUnsupportedProtocolVersionErrorErrorData_id" ON "McpUnsupportedProtocolVersionErrorErrorData_supported" ("McpUnsupportedProtocolVersionErrorErrorData_id");
CREATE INDEX "ix_McpUnsupportedProtocolVersionErrorErrorData_supported_supported" ON "McpUnsupportedProtocolVersionErrorErrorData_supported" (supported);

CREATE TABLE "McpUntitledMultiSelectEnumSchemaItems_enum" (
	"McpUntitledMultiSelectEnumSchemaItems_id" INTEGER,
	enum TEXT NOT NULL,
	PRIMARY KEY ("McpUntitledMultiSelectEnumSchemaItems_id", enum),
	FOREIGN KEY("McpUntitledMultiSelectEnumSchemaItems_id") REFERENCES "McpUntitledMultiSelectEnumSchemaItems" (id)
);
CREATE INDEX "ix_McpUntitledMultiSelectEnumSchemaItems_enum_enum" ON "McpUntitledMultiSelectEnumSchemaItems_enum" (enum);
CREATE INDEX "ix_McpUntitledMultiSelectEnumSchemaItems_enum_McpUntitledMultiSelectEnumSchemaItems_id" ON "McpUntitledMultiSelectEnumSchemaItems_enum" ("McpUntitledMultiSelectEnumSchemaItems_id");

CREATE TABLE "McpUntitledSingleSelectEnumSchema_enum" (
	"McpUntitledSingleSelectEnumSchema_id" INTEGER,
	enum TEXT NOT NULL,
	PRIMARY KEY ("McpUntitledSingleSelectEnumSchema_id", enum),
	FOREIGN KEY("McpUntitledSingleSelectEnumSchema_id") REFERENCES "McpUntitledSingleSelectEnumSchema" (id)
);
CREATE INDEX "ix_McpUntitledSingleSelectEnumSchema_enum_McpUntitledSingleSelectEnumSchema_id" ON "McpUntitledSingleSelectEnumSchema_enum" ("McpUntitledSingleSelectEnumSchema_id");
CREATE INDEX "ix_McpUntitledSingleSelectEnumSchema_enum_enum" ON "McpUntitledSingleSelectEnumSchema_enum" (enum);

CREATE TABLE "McpCacheableResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpCacheableResult_id" ON "McpCacheableResult" (id);

CREATE TABLE "McpCallToolResult" (
	id INTEGER NOT NULL,
	"isError" BOOLEAN,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	"structuredContent_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id),
	FOREIGN KEY("structuredContent_id") REFERENCES "McpJSONValue" (id)
);
CREATE INDEX "ix_McpCallToolResult_id" ON "McpCallToolResult" (id);

CREATE TABLE "McpCancelledNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpCancelledNotificationParams" (id)
);
CREATE INDEX "ix_McpCancelledNotification_id" ON "McpCancelledNotification" (id);

CREATE TABLE "McpClientCapabilities" (
	id INTEGER NOT NULL,
	elicitation_id INTEGER,
	experimental_id INTEGER,
	extensions_id INTEGER,
	roots_id INTEGER,
	sampling_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(elicitation_id) REFERENCES "McpClientCapabilitiesElicitation" (id),
	FOREIGN KEY(experimental_id) REFERENCES "McpClientCapabilitiesExperimental" (id),
	FOREIGN KEY(extensions_id) REFERENCES "McpClientCapabilitiesExtensions" (id),
	FOREIGN KEY(roots_id) REFERENCES "McpClientCapabilitiesRoots" (id),
	FOREIGN KEY(sampling_id) REFERENCES "McpClientCapabilitiesSampling" (id)
);
CREATE INDEX "ix_McpClientCapabilities_id" ON "McpClientCapabilities" (id);

CREATE TABLE "McpClientNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpCancelledNotificationParams" (id)
);
CREATE INDEX "ix_McpClientNotification_id" ON "McpClientNotification" (id);

CREATE TABLE "McpClientResult" (
	id INTEGER NOT NULL,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpClientResult_id" ON "McpClientResult" (id);

CREATE TABLE "McpCompleteResult" (
	id INTEGER NOT NULL,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	completion_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id),
	FOREIGN KEY(completion_id) REFERENCES "McpCompleteResultCompletion" (id)
);
CREATE INDEX "ix_McpCompleteResult_id" ON "McpCompleteResult" (id);

CREATE TABLE "McpCreateMessageRequest" (
	id INTEGER NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpCreateMessageRequestParams" (id)
);
CREATE INDEX "ix_McpCreateMessageRequest_id" ON "McpCreateMessageRequest" (id);

CREATE TABLE "McpDiscoverResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	instructions TEXT,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	capabilities_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id),
	FOREIGN KEY(capabilities_id) REFERENCES "McpServerCapabilities" (id)
);
CREATE INDEX "ix_McpDiscoverResult_id" ON "McpDiscoverResult" (id);

CREATE TABLE "McpElicitRequestFormParams" (
	id INTEGER NOT NULL,
	message TEXT NOT NULL,
	mode TEXT,
	"requestedSchema_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("requestedSchema_id") REFERENCES "McpElicitRequestFormParamsRequestedSchema" (id)
);
CREATE INDEX "ix_McpElicitRequestFormParams_id" ON "McpElicitRequestFormParams" (id);

CREATE TABLE "McpEmptyResult" (
	id INTEGER NOT NULL,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpEmptyResult_id" ON "McpEmptyResult" (id);

CREATE TABLE "McpGetPromptResult" (
	id INTEGER NOT NULL,
	description TEXT,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpGetPromptResult_id" ON "McpGetPromptResult" (id);

CREATE TABLE "McpHeaderMismatchError" (
	uid INTEGER NOT NULL,
	id TEXT,
	jsonrpc TEXT NOT NULL,
	error_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(error_id) REFERENCES "McpHeaderMismatchErrorError" (id)
);
CREATE INDEX "ix_McpHeaderMismatchError_uid" ON "McpHeaderMismatchError" (uid);

CREATE TABLE "McpInputRequiredResult" (
	id INTEGER NOT NULL,
	"requestState" TEXT,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	"inputRequests_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id),
	FOREIGN KEY("inputRequests_id") REFERENCES "McpInputRequests" (id)
);
CREATE INDEX "ix_McpInputRequiredResult_id" ON "McpInputRequiredResult" (id);

CREATE TABLE "McpJSONRPCErrorResponse" (
	uid INTEGER NOT NULL,
	id TEXT,
	jsonrpc TEXT NOT NULL,
	error_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(error_id) REFERENCES "McpError" (id)
);
CREATE INDEX "ix_McpJSONRPCErrorResponse_uid" ON "McpJSONRPCErrorResponse" (uid);

CREATE TABLE "McpListPromptsResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	"nextCursor" TEXT,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpListPromptsResult_id" ON "McpListPromptsResult" (id);

CREATE TABLE "McpListResourceTemplatesResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	"nextCursor" TEXT,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpListResourceTemplatesResult_id" ON "McpListResourceTemplatesResult" (id);

CREATE TABLE "McpListResourcesResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	"nextCursor" TEXT,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpListResourcesResult_id" ON "McpListResourcesResult" (id);

CREATE TABLE "McpListRootsRequest" (
	id INTEGER NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpListRootsRequestParams" (id)
);
CREATE INDEX "ix_McpListRootsRequest_id" ON "McpListRootsRequest" (id);

CREATE TABLE "McpListToolsResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	"nextCursor" TEXT,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpListToolsResult_id" ON "McpListToolsResult" (id);

CREATE TABLE "McpLoggingMessageNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpLoggingMessageNotificationParams" (id)
);
CREATE INDEX "ix_McpLoggingMessageNotification_id" ON "McpLoggingMessageNotification" (id);

CREATE TABLE "McpPaginatedResult" (
	id INTEGER NOT NULL,
	"nextCursor" TEXT,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpPaginatedResult_id" ON "McpPaginatedResult" (id);

CREATE TABLE "McpProgressNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpProgressNotificationParams" (id)
);
CREATE INDEX "ix_McpProgressNotification_id" ON "McpProgressNotification" (id);

CREATE TABLE "McpPromptListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpNotificationParams" (id)
);
CREATE INDEX "ix_McpPromptListChangedNotification_id" ON "McpPromptListChangedNotification" (id);

CREATE TABLE "McpReadResourceResult" (
	id INTEGER NOT NULL,
	"cacheScope" VARCHAR(7) NOT NULL,
	"resultType" TEXT NOT NULL,
	"ttlMs" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpReadResourceResult_id" ON "McpReadResourceResult" (id);

CREATE TABLE "McpResourceListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpNotificationParams" (id)
);
CREATE INDEX "ix_McpResourceListChangedNotification_id" ON "McpResourceListChangedNotification" (id);

CREATE TABLE "McpResourceUpdatedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpResourceUpdatedNotificationParams" (id)
);
CREATE INDEX "ix_McpResourceUpdatedNotification_id" ON "McpResourceUpdatedNotification" (id);

CREATE TABLE "McpResult" (
	id INTEGER NOT NULL,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpResultMetaObject" (id)
);
CREATE INDEX "ix_McpResult_id" ON "McpResult" (id);

CREATE TABLE "McpSamplingMessage" (
	id INTEGER NOT NULL,
	content TEXT NOT NULL,
	role VARCHAR(9) NOT NULL,
	"McpCreateMessageRequestParams_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpCreateMessageRequestParams_id") REFERENCES "McpCreateMessageRequestParams" (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpSamplingMessage_id" ON "McpSamplingMessage" (id);

CREATE TABLE "McpSubscriptionsAcknowledgedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpSubscriptionsAcknowledgedNotificationParams" (id)
);
CREATE INDEX "ix_McpSubscriptionsAcknowledgedNotification_id" ON "McpSubscriptionsAcknowledgedNotification" (id);

CREATE TABLE "McpSubscriptionsListenResult" (
	id INTEGER NOT NULL,
	"resultType" TEXT NOT NULL,
	_meta_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpSubscriptionsListenResultMetaObject" (id)
);
CREATE INDEX "ix_McpSubscriptionsListenResult_id" ON "McpSubscriptionsListenResult" (id);

CREATE TABLE "McpToolListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "McpNotificationParams" (id)
);
CREATE INDEX "ix_McpToolListChangedNotification_id" ON "McpToolListChangedNotification" (id);

CREATE TABLE "McpUnsupportedProtocolVersionError" (
	uid INTEGER NOT NULL,
	id TEXT,
	jsonrpc TEXT NOT NULL,
	error_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(error_id) REFERENCES "McpUnsupportedProtocolVersionErrorError" (id)
);
CREATE INDEX "ix_McpUnsupportedProtocolVersionError_uid" ON "McpUnsupportedProtocolVersionError" (uid);

CREATE TABLE "McpCreateMessageRequestParams_stopSequences" (
	"McpCreateMessageRequestParams_id" INTEGER,
	"stopSequences" TEXT,
	PRIMARY KEY ("McpCreateMessageRequestParams_id", "stopSequences"),
	FOREIGN KEY("McpCreateMessageRequestParams_id") REFERENCES "McpCreateMessageRequestParams" (id)
);
CREATE INDEX "ix_McpCreateMessageRequestParams_stopSequences_McpCreateMessageRequestParams_id" ON "McpCreateMessageRequestParams_stopSequences" ("McpCreateMessageRequestParams_id");
CREATE INDEX "ix_McpCreateMessageRequestParams_stopSequences_stopSequences" ON "McpCreateMessageRequestParams_stopSequences" ("stopSequences");

CREATE TABLE "McpElicitRequestFormParamsRequestedSchema_required" (
	"McpElicitRequestFormParamsRequestedSchema_id" INTEGER,
	required TEXT,
	PRIMARY KEY ("McpElicitRequestFormParamsRequestedSchema_id", required),
	FOREIGN KEY("McpElicitRequestFormParamsRequestedSchema_id") REFERENCES "McpElicitRequestFormParamsRequestedSchema" (id)
);
CREATE INDEX "ix_McpElicitRequestFormParamsRequestedSchema_required_required" ON "McpElicitRequestFormParamsRequestedSchema_required" (required);
CREATE INDEX "ix_McpElicitRequestFormParamsRequestedSchema_required_McpElicitRequestFormParamsRequestedSchema_id" ON "McpElicitRequestFormParamsRequestedSchema_required" ("McpElicitRequestFormParamsRequestedSchema_id");

CREATE TABLE "McpTitledMultiSelectEnumSchema_default" (
	"McpTitledMultiSelectEnumSchema_id" INTEGER,
	"default" TEXT,
	PRIMARY KEY ("McpTitledMultiSelectEnumSchema_id", "default"),
	FOREIGN KEY("McpTitledMultiSelectEnumSchema_id") REFERENCES "McpTitledMultiSelectEnumSchema" (id)
);
CREATE INDEX "ix_McpTitledMultiSelectEnumSchema_default_McpTitledMultiSelectEnumSchema_id" ON "McpTitledMultiSelectEnumSchema_default" ("McpTitledMultiSelectEnumSchema_id");
CREATE INDEX "ix_McpTitledMultiSelectEnumSchema_default_default" ON "McpTitledMultiSelectEnumSchema_default" ("default");

CREATE TABLE "McpUntitledMultiSelectEnumSchema_default" (
	"McpUntitledMultiSelectEnumSchema_id" INTEGER,
	"default" TEXT,
	PRIMARY KEY ("McpUntitledMultiSelectEnumSchema_id", "default"),
	FOREIGN KEY("McpUntitledMultiSelectEnumSchema_id") REFERENCES "McpUntitledMultiSelectEnumSchema" (id)
);
CREATE INDEX "ix_McpUntitledMultiSelectEnumSchema_default_McpUntitledMultiSelectEnumSchema_id" ON "McpUntitledMultiSelectEnumSchema_default" ("McpUntitledMultiSelectEnumSchema_id");
CREATE INDEX "ix_McpUntitledMultiSelectEnumSchema_default_default" ON "McpUntitledMultiSelectEnumSchema_default" ("default");

CREATE TABLE "McpCompleteResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpCompleteResult" (id)
);
CREATE INDEX "ix_McpCompleteResultResponse_uid" ON "McpCompleteResultResponse" (uid);

CREATE TABLE "McpContentBlock" (
	id INTEGER NOT NULL,
	"McpCallToolResult_id" INTEGER,
	"McpToolResultContent_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpCallToolResult_id") REFERENCES "McpCallToolResult" (id),
	FOREIGN KEY("McpToolResultContent_id") REFERENCES "McpToolResultContent" (id)
);
CREATE INDEX "ix_McpContentBlock_id" ON "McpContentBlock" (id);

CREATE TABLE "McpDiscoverResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpDiscoverResult" (id)
);
CREATE INDEX "ix_McpDiscoverResultResponse_uid" ON "McpDiscoverResultResponse" (uid);

CREATE TABLE "McpJSONRPCResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpResult" (id)
);
CREATE INDEX "ix_McpJSONRPCResultResponse_uid" ON "McpJSONRPCResultResponse" (uid);

CREATE TABLE "McpListPromptsResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpListPromptsResult" (id)
);
CREATE INDEX "ix_McpListPromptsResultResponse_uid" ON "McpListPromptsResultResponse" (uid);

CREATE TABLE "McpListResourceTemplatesResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpListResourceTemplatesResult" (id)
);
CREATE INDEX "ix_McpListResourceTemplatesResultResponse_uid" ON "McpListResourceTemplatesResultResponse" (uid);

CREATE TABLE "McpListResourcesResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpListResourcesResult" (id)
);
CREATE INDEX "ix_McpListResourcesResultResponse_uid" ON "McpListResourcesResultResponse" (uid);

CREATE TABLE "McpListToolsResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpListToolsResult" (id)
);
CREATE INDEX "ix_McpListToolsResultResponse_uid" ON "McpListToolsResultResponse" (uid);

CREATE TABLE "McpMissingRequiredClientCapabilityErrorErrorData" (
	id INTEGER NOT NULL,
	"requiredCapabilities_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("requiredCapabilities_id") REFERENCES "McpClientCapabilities" (id)
);
CREATE INDEX "ix_McpMissingRequiredClientCapabilityErrorErrorData_id" ON "McpMissingRequiredClientCapabilityErrorErrorData" (id);

CREATE TABLE "McpPrompt" (
	id INTEGER NOT NULL,
	description TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"McpListPromptsResult_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpListPromptsResult_id") REFERENCES "McpListPromptsResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id)
);
CREATE INDEX "ix_McpPrompt_id" ON "McpPrompt" (id);

CREATE TABLE "McpRequestMetaObject" (
	id INTEGER NOT NULL,
	mcp_log_level VARCHAR(9),
	mcp_protocol_version TEXT NOT NULL,
	"progressToken" TEXT,
	mcp_client_capabilities_id INTEGER NOT NULL,
	mcp_client_info_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(mcp_client_capabilities_id) REFERENCES "McpClientCapabilities" (id),
	FOREIGN KEY(mcp_client_info_id) REFERENCES "McpImplementation" (id)
);
CREATE INDEX "ix_McpRequestMetaObject_id" ON "McpRequestMetaObject" (id);

CREATE TABLE "McpResource" (
	id INTEGER NOT NULL,
	description TEXT,
	"mimeType" TEXT,
	name TEXT NOT NULL,
	size INTEGER,
	title TEXT,
	uri TEXT NOT NULL,
	"McpListResourcesResult_id" INTEGER,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpListResourcesResult_id") REFERENCES "McpListResourcesResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpResource_id" ON "McpResource" (id);

CREATE TABLE "McpResourceTemplate" (
	id INTEGER NOT NULL,
	description TEXT,
	"mimeType" TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"uriTemplate" TEXT NOT NULL,
	"McpListResourceTemplatesResult_id" INTEGER,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpListResourceTemplatesResult_id") REFERENCES "McpListResourceTemplatesResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpAnnotations" (id)
);
CREATE INDEX "ix_McpResourceTemplate_id" ON "McpResourceTemplate" (id);

CREATE TABLE "McpSubscriptionsListenResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "McpSubscriptionsListenResult" (id)
);
CREATE INDEX "ix_McpSubscriptionsListenResultResponse_uid" ON "McpSubscriptionsListenResultResponse" (uid);

CREATE TABLE "McpTool" (
	id INTEGER NOT NULL,
	description TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"McpCreateMessageRequestParams_id" INTEGER,
	"McpListToolsResult_id" INTEGER,
	_meta_id INTEGER,
	annotations_id INTEGER,
	"inputSchema_id" INTEGER NOT NULL,
	"outputSchema_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpCreateMessageRequestParams_id") REFERENCES "McpCreateMessageRequestParams" (id),
	FOREIGN KEY("McpListToolsResult_id") REFERENCES "McpListToolsResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpMetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "McpToolAnnotations" (id),
	FOREIGN KEY("inputSchema_id") REFERENCES "McpToolInputSchema" (id),
	FOREIGN KEY("outputSchema_id") REFERENCES "McpToolOutputSchema" (id)
);
CREATE INDEX "ix_McpTool_id" ON "McpTool" (id);

CREATE TABLE "McpDiscoverResult_supportedVersions" (
	"McpDiscoverResult_id" INTEGER,
	"supportedVersions" TEXT NOT NULL,
	PRIMARY KEY ("McpDiscoverResult_id", "supportedVersions"),
	FOREIGN KEY("McpDiscoverResult_id") REFERENCES "McpDiscoverResult" (id)
);
CREATE INDEX "ix_McpDiscoverResult_supportedVersions_supportedVersions" ON "McpDiscoverResult_supportedVersions" ("supportedVersions");
CREATE INDEX "ix_McpDiscoverResult_supportedVersions_McpDiscoverResult_id" ON "McpDiscoverResult_supportedVersions" ("McpDiscoverResult_id");

CREATE TABLE "McpReadResourceResult_contents" (
	"McpReadResourceResult_id" INTEGER,
	contents TEXT NOT NULL,
	PRIMARY KEY ("McpReadResourceResult_id", contents),
	FOREIGN KEY("McpReadResourceResult_id") REFERENCES "McpReadResourceResult" (id)
);
CREATE INDEX "ix_McpReadResourceResult_contents_McpReadResourceResult_id" ON "McpReadResourceResult_contents" ("McpReadResourceResult_id");
CREATE INDEX "ix_McpReadResourceResult_contents_contents" ON "McpReadResourceResult_contents" (contents);

CREATE TABLE "McpCallToolRequestParams" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"requestState" TEXT,
	_meta_id INTEGER NOT NULL,
	arguments_id INTEGER,
	"inputResponses_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id),
	FOREIGN KEY(arguments_id) REFERENCES "McpJSONObject" (id),
	FOREIGN KEY("inputResponses_id") REFERENCES "McpInputResponses" (id)
);
CREATE INDEX "ix_McpCallToolRequestParams_id" ON "McpCallToolRequestParams" (id);

CREATE TABLE "McpCompleteRequestParams" (
	id INTEGER NOT NULL,
	ref TEXT NOT NULL,
	_meta_id INTEGER NOT NULL,
	argument_id INTEGER NOT NULL,
	context_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id),
	FOREIGN KEY(argument_id) REFERENCES "McpCompleteRequestParamsArgument" (id),
	FOREIGN KEY(context_id) REFERENCES "McpCompleteRequestParamsContext" (id)
);
CREATE INDEX "ix_McpCompleteRequestParams_id" ON "McpCompleteRequestParams" (id);

CREATE TABLE "McpGetPromptRequestParams" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"requestState" TEXT,
	_meta_id INTEGER NOT NULL,
	arguments_id INTEGER,
	"inputResponses_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id),
	FOREIGN KEY(arguments_id) REFERENCES "McpGetPromptRequestParamsArguments" (id),
	FOREIGN KEY("inputResponses_id") REFERENCES "McpInputResponses" (id)
);
CREATE INDEX "ix_McpGetPromptRequestParams_id" ON "McpGetPromptRequestParams" (id);

CREATE TABLE "McpIcon" (
	id INTEGER NOT NULL,
	"mimeType" TEXT,
	src TEXT NOT NULL,
	theme VARCHAR(5),
	"McpIcons_id" INTEGER,
	"McpImplementation_id" INTEGER,
	"McpPrompt_id" INTEGER,
	"McpResource_id" INTEGER,
	"McpResourceLink_id" INTEGER,
	"McpResourceTemplate_id" INTEGER,
	"McpTool_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpIcons_id") REFERENCES "McpIcons" (id),
	FOREIGN KEY("McpImplementation_id") REFERENCES "McpImplementation" (id),
	FOREIGN KEY("McpPrompt_id") REFERENCES "McpPrompt" (id),
	FOREIGN KEY("McpResource_id") REFERENCES "McpResource" (id),
	FOREIGN KEY("McpResourceLink_id") REFERENCES "McpResourceLink" (id),
	FOREIGN KEY("McpResourceTemplate_id") REFERENCES "McpResourceTemplate" (id),
	FOREIGN KEY("McpTool_id") REFERENCES "McpTool" (id)
);
CREATE INDEX "ix_McpIcon_id" ON "McpIcon" (id);

CREATE TABLE "McpInputResponseRequestParams" (
	id INTEGER NOT NULL,
	"requestState" TEXT,
	_meta_id INTEGER NOT NULL,
	"inputResponses_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id),
	FOREIGN KEY("inputResponses_id") REFERENCES "McpInputResponses" (id)
);
CREATE INDEX "ix_McpInputResponseRequestParams_id" ON "McpInputResponseRequestParams" (id);

CREATE TABLE "McpMissingRequiredClientCapabilityErrorError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "McpMissingRequiredClientCapabilityErrorErrorData" (id)
);
CREATE INDEX "ix_McpMissingRequiredClientCapabilityErrorError_id" ON "McpMissingRequiredClientCapabilityErrorError" (id);

CREATE TABLE "McpPaginatedRequestParams" (
	id INTEGER NOT NULL,
	cursor TEXT,
	_meta_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id)
);
CREATE INDEX "ix_McpPaginatedRequestParams_id" ON "McpPaginatedRequestParams" (id);

CREATE TABLE "McpPromptArgument" (
	id INTEGER NOT NULL,
	description TEXT,
	name TEXT NOT NULL,
	required BOOLEAN,
	title TEXT,
	"McpPrompt_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("McpPrompt_id") REFERENCES "McpPrompt" (id)
);
CREATE INDEX "ix_McpPromptArgument_id" ON "McpPromptArgument" (id);

CREATE TABLE "McpPromptMessage" (
	id INTEGER NOT NULL,
	role VARCHAR(9) NOT NULL,
	"McpGetPromptResult_id" INTEGER,
	content_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("McpGetPromptResult_id") REFERENCES "McpGetPromptResult" (id),
	FOREIGN KEY(content_id) REFERENCES "McpContentBlock" (id)
);
CREATE INDEX "ix_McpPromptMessage_id" ON "McpPromptMessage" (id);

CREATE TABLE "McpReadResourceRequestParams" (
	id INTEGER NOT NULL,
	"requestState" TEXT,
	uri TEXT NOT NULL,
	_meta_id INTEGER NOT NULL,
	"inputResponses_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id),
	FOREIGN KEY("inputResponses_id") REFERENCES "McpInputResponses" (id)
);
CREATE INDEX "ix_McpReadResourceRequestParams_id" ON "McpReadResourceRequestParams" (id);

CREATE TABLE "McpRequestParams" (
	id INTEGER NOT NULL,
	_meta_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id)
);
CREATE INDEX "ix_McpRequestParams_id" ON "McpRequestParams" (id);

CREATE TABLE "McpResourceRequestParams" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	_meta_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id)
);
CREATE INDEX "ix_McpResourceRequestParams_id" ON "McpResourceRequestParams" (id);

CREATE TABLE "McpSubscriptionsListenRequestParams" (
	id INTEGER NOT NULL,
	_meta_id INTEGER NOT NULL,
	notifications_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "McpRequestMetaObject" (id),
	FOREIGN KEY(notifications_id) REFERENCES "McpSubscriptionFilter" (id)
);
CREATE INDEX "ix_McpSubscriptionsListenRequestParams_id" ON "McpSubscriptionsListenRequestParams" (id);

CREATE TABLE "McpCallToolRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpCallToolRequestParams" (id)
);
CREATE INDEX "ix_McpCallToolRequest_uid" ON "McpCallToolRequest" (uid);

CREATE TABLE "McpCompleteRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpCompleteRequestParams" (id)
);
CREATE INDEX "ix_McpCompleteRequest_uid" ON "McpCompleteRequest" (uid);

CREATE TABLE "McpDiscoverRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpRequestParams" (id)
);
CREATE INDEX "ix_McpDiscoverRequest_uid" ON "McpDiscoverRequest" (uid);

CREATE TABLE "McpGetPromptRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpGetPromptRequestParams" (id)
);
CREATE INDEX "ix_McpGetPromptRequest_uid" ON "McpGetPromptRequest" (uid);

CREATE TABLE "McpListPromptsRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpPaginatedRequestParams" (id)
);
CREATE INDEX "ix_McpListPromptsRequest_uid" ON "McpListPromptsRequest" (uid);

CREATE TABLE "McpListResourceTemplatesRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpPaginatedRequestParams" (id)
);
CREATE INDEX "ix_McpListResourceTemplatesRequest_uid" ON "McpListResourceTemplatesRequest" (uid);

CREATE TABLE "McpListResourcesRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpPaginatedRequestParams" (id)
);
CREATE INDEX "ix_McpListResourcesRequest_uid" ON "McpListResourcesRequest" (uid);

CREATE TABLE "McpListToolsRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpPaginatedRequestParams" (id)
);
CREATE INDEX "ix_McpListToolsRequest_uid" ON "McpListToolsRequest" (uid);

CREATE TABLE "McpMissingRequiredClientCapabilityError" (
	uid INTEGER NOT NULL,
	id TEXT,
	jsonrpc TEXT NOT NULL,
	error_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(error_id) REFERENCES "McpMissingRequiredClientCapabilityErrorError" (id)
);
CREATE INDEX "ix_McpMissingRequiredClientCapabilityError_uid" ON "McpMissingRequiredClientCapabilityError" (uid);

CREATE TABLE "McpPaginatedRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpPaginatedRequestParams" (id)
);
CREATE INDEX "ix_McpPaginatedRequest_uid" ON "McpPaginatedRequest" (uid);

CREATE TABLE "McpReadResourceRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpReadResourceRequestParams" (id)
);
CREATE INDEX "ix_McpReadResourceRequest_uid" ON "McpReadResourceRequest" (uid);

CREATE TABLE "McpSubscriptionsListenRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "McpSubscriptionsListenRequestParams" (id)
);
CREATE INDEX "ix_McpSubscriptionsListenRequest_uid" ON "McpSubscriptionsListenRequest" (uid);

CREATE TABLE "McpIcon_sizes" (
	"McpIcon_id" INTEGER,
	sizes TEXT,
	PRIMARY KEY ("McpIcon_id", sizes),
	FOREIGN KEY("McpIcon_id") REFERENCES "McpIcon" (id)
);
CREATE INDEX "ix_McpIcon_sizes_sizes" ON "McpIcon_sizes" (sizes);
CREATE INDEX "ix_McpIcon_sizes_McpIcon_id" ON "McpIcon_sizes" ("McpIcon_id");
