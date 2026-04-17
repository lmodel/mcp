-- # Class: HasMeta Description: Mixin for types that carry a _meta field.
--     * Slot: id
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: HasAnnotations Description: Mixin for types that carry annotations.
--     * Slot: id
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: HasIcons Description: Mixin for types that carry icons.
--     * Slot: id
-- # Class: HasName Description: Mixin for types that carry name and title.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: Annotations Description: Optional annotations for the client. The client can use annotations to inform how objects are used or displayed.
--     * Slot: id
--     * Slot: lastModified Description: The moment the resource was last modified, as an ISO 8601 formatted string.
--     * Slot: priority Description: How important this data is for operating the server. 1 means most important (required), 0 means least important (optional).
-- # Class: Error Description: A JSON-RPC error object.
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A message string.
--     * Slot: data_id Description: Base64-encoded binary data.
-- # Class: InternalError Description: A JSON-RPC error indicating that an internal error occurred on the receiver (-32603).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A message string.
--     * Slot: data_id Description: Base64-encoded binary data.
-- # Class: InvalidParamsError Description: A JSON-RPC error indicating that the method parameters are invalid or malformed (-32602).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A message string.
--     * Slot: data_id Description: Base64-encoded binary data.
-- # Class: InvalidRequestError Description: A JSON-RPC error indicating that the request is not a valid request object (-32600).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A message string.
--     * Slot: data_id Description: Base64-encoded binary data.
-- # Class: MethodNotFoundError Description: A JSON-RPC error indicating that the requested method does not exist or is not available (-32601).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A message string.
--     * Slot: data_id Description: Base64-encoded binary data.
-- # Class: ParseError Description: A JSON-RPC error indicating that invalid JSON was received by the server (-32700).
--     * Slot: id
--     * Slot: code Description: The error type that occurred.
--     * Slot: message Description: A message string.
--     * Slot: data_id Description: Base64-encoded binary data.
-- # Class: URLElicitationRequiredError Description: A response indicating that additional information is required via URL elicitation.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: error_id Description: The error object.
-- # Class: Icon Description: An optionally-sized icon that can be displayed in a user interface.
--     * Slot: id
--     * Slot: src Description: A standard URI pointing to an icon resource.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: theme Description: Optional theme specifier for the icon.
--     * Slot: HasIcons_id Description: Autocreated FK slot
--     * Slot: Implementation_id Description: Autocreated FK slot
--     * Slot: ResourceLink_id Description: Autocreated FK slot
--     * Slot: Resource_id Description: Autocreated FK slot
--     * Slot: ResourceTemplate_id Description: Autocreated FK slot
--     * Slot: Prompt_id Description: Autocreated FK slot
--     * Slot: Tool_id Description: Autocreated FK slot
-- # Class: Implementation Description: Describes the MCP implementation.
--     * Slot: id
--     * Slot: version Description: The version of this implementation.
--     * Slot: description Description: A human-readable description.
--     * Slot: websiteUrl Description: An optional URL of the website for this implementation.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: TextContent Description: Text provided to or from an LLM.
--     * Slot: id
--     * Slot: text Description: Text content.
--     * Slot: type Description: Type discriminator field.
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: ImageContent Description: An image provided to or from an LLM.
--     * Slot: id
--     * Slot: data Description: Base64-encoded binary data.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: type Description: Type discriminator field.
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: AudioContent Description: Audio provided to or from an LLM.
--     * Slot: id
--     * Slot: data Description: Base64-encoded binary data.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: type Description: Type discriminator field.
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: ContentBlock Description: Structured text content block.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: text Description: Text content.
-- # Class: EmbeddedResource Description: The contents of a resource, embedded into a prompt or tool call result.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: resource_id Description: The embedded resource contents (text or blob).
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: ResourceLink Description: A resource that the server is capable of reading, included in a prompt or tool call result.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: description Description: A human-readable description.
--     * Slot: size Description: The size of the raw resource content, in bytes.
--     * Slot: type Description: Type discriminator field.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: ToolUseContent Description: A request from the assistant to call a tool.
--     * Slot: uid
--     * Slot: id Description: A unique identifier for this tool use.
--     * Slot: type Description: Type discriminator field.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: input_id Description: The arguments to pass to the tool.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ToolResultContent Description: The result of a tool use, provided by the user back to the assistant.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: toolUseId Description: The ID of the tool use this result corresponds to.
--     * Slot: isError Description: Whether the tool call ended in an error.
--     * Slot: structuredContent_id Description: An optional JSON object representing structured result of the tool call.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ResourceContents Description: Generic resource contents.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: text Description: Text content.
--     * Slot: blob Description: A base64-encoded string representing binary data.
--     * Slot: ReadResourceResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: TextResourceContents Description: Text resource contents.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: text Description: Text content.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: BlobResourceContents Description: Blob resource contents.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: blob Description: A base64-encoded string representing binary data.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: Resource Description: A known resource that the server is capable of reading.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: description Description: A human-readable description.
--     * Slot: size Description: The size of the raw resource content, in bytes.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: ListResourcesResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: ResourceTemplate Description: A template description for resources available on the server.
--     * Slot: id
--     * Slot: uriTemplate Description: A URI template (RFC 6570) for constructing resource URIs.
--     * Slot: mimeType Description: The MIME type of a resource, if known.
--     * Slot: description Description: A human-readable description.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: ListResourceTemplatesResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Optional metadata object.
--     * Slot: annotations_id Description: Optional annotations for the client.
-- # Class: Root Description: Represents a root directory or file that the server can operate on.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: ListRootsResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: PromptArgument Description: Describes an argument that a prompt can accept.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: required Description: Whether this argument must be provided.
--     * Slot: required_field Description: Whether this argument must be provided.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: Prompt_id Description: Autocreated FK slot
-- # Class: Prompt Description: A prompt or prompt template that the server offers.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: ListPromptsResult_id Description: Autocreated FK slot
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: PromptMessage Description: Describes a message returned as part of a prompt.
--     * Slot: id
--     * Slot: role Description: The role of the sender or recipient.
--     * Slot: GetPromptResult_id Description: Autocreated FK slot
--     * Slot: content_id Description: The content of the prompt message.
-- # Class: PromptReference Description: Identifies a prompt.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: ResourceTemplateReference Description: A reference to a resource or resource template definition.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: uri Description: A resource URI.
-- # Class: ToolAnnotations Description: Additional properties describing a Tool to clients. All properties are hints, not guarantees.
--     * Slot: id
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: destructiveHint Description: If true, the tool may perform destructive updates.
--     * Slot: idempotentHint Description: If true, calling repeatedly with same arguments has no additional effect.
--     * Slot: openWorldHint Description: If true, tool may interact with an open world of external entities.
--     * Slot: readOnlyHint Description: If true, the tool does not modify its environment.
-- # Class: ToolChoice Description: Controls tool selection behavior for sampling requests.
--     * Slot: id
--     * Slot: mode Description: Controls the tool use ability of the model.
-- # Class: ToolExecution Description: Execution-related properties for a tool.
--     * Slot: id
--     * Slot: taskSupport Description: Whether this tool supports task-augmented execution.
-- # Class: MetaObject Description: Metadata object attached to protocol objects.
--     * Slot: id
--     * Slot: progressToken Description: The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.
-- # Class: ArgumentMap Description: Argument object used in prompt and tool calls.
--     * Slot: id
--     * Slot: city Description: City value.
--     * Slot: location Description: Location value.
--     * Slot: language Description: Programming language value.
--     * Slot: framework Description: Framework value.
-- # Class: CompletionArgument Description: Argument descriptor for completion requests.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: value Description: A value string.
-- # Class: CompletionContext Description: Additional context for completion requests.
--     * Slot: id
--     * Slot: arguments_id Description: Arguments for templating.
-- # Class: CompletionData Description: Completion result payload.
--     * Slot: id
--     * Slot: total Description: Total number of items to process (or total progress required), if known.
--     * Slot: hasMore Description: Indicates whether there are additional completion options.
-- # Class: EnumOption Description: Single enumerated option with a machine value and display title.
--     * Slot: id
--     * Slot: const Description: JSON Schema const value.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: SchemaItems Description: JSON Schema items expression used by enum multi-select schemas.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
-- # Class: JsonSchema Description: Restricted JSON Schema object used in MCP payloads.
--     * Slot: id
--     * Slot: schemaUri Description: Optional JSON Schema dialect identifier.
--     * Slot: type Description: Type discriminator field.
--     * Slot: additionalProperties Description: JSON Schema additionalProperties flag.
--     * Slot: minimum Description: Minimum value constraint.
--     * Slot: maximum Description: Maximum value constraint.
--     * Slot: minLength Description: Minimum length constraint.
--     * Slot: maxLength Description: Maximum length constraint.
--     * Slot: format Description: String format constraint.
--     * Slot: description Description: A human-readable description.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: const Description: JSON Schema const value.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: properties_id Description: JSON Schema properties map.
--     * Slot: items_id Description: JSON Schema items definition.
-- # Class: SchemaProperties Description: Named JSON Schema property map used by vendor fixtures.
--     * Slot: id
--     * Slot: name_id Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: email_id Description: Email value.
--     * Slot: age_id Description: Age value.
--     * Slot: city_id Description: City value.
--     * Slot: location_id Description: Location value.
--     * Slot: a_id Description: JSON Schema property for key a.
--     * Slot: b_id Description: JSON Schema property for key b.
--     * Slot: temperature_id Description: Sampling temperature.
--     * Slot: conditions_id Description: Weather conditions description.
--     * Slot: humidity_id Description: Humidity percentage value.
-- # Class: ToolInput Description: Tool input payload.
--     * Slot: id
--     * Slot: city Description: City value.
--     * Slot: location Description: Location value.
-- # Class: StructuredContentData Description: Structured content object returned by tools.
--     * Slot: id
--     * Slot: temperature Description: Sampling temperature.
--     * Slot: conditions Description: Weather conditions description.
--     * Slot: humidity Description: Humidity percentage value.
-- # Class: LogDetails Description: Structured details attached to log data.
--     * Slot: id
--     * Slot: host Description: Host value.
--     * Slot: port Description: Port value.
-- # Class: LogData Description: Structured log data payload.
--     * Slot: id
--     * Slot: error Description: The error object.
--     * Slot: details_id Description: Nested log details object.
-- # Class: ErrorData Description: Structured JSON-RPC error data payload.
--     * Slot: id
--     * Slot: reason Description: An optional string describing the reason.
-- # Class: ElicitationContent Description: Form values returned by an elicitation.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: email Description: Email value.
--     * Slot: age Description: Age value.
-- # Class: URLElicitation Description: URL-based elicitation request payload carried in error data.
--     * Slot: id
--     * Slot: mode Description: The elicitation mode.
--     * Slot: elicitationId Description: The ID of the elicitation.
--     * Slot: message Description: A message string.
--     * Slot: url Description: The URL that the user should navigate to.
--     * Slot: ErrorData_id Description: Autocreated FK slot
-- # Class: ElicitationCapability Description: Client elicitation capability.
--     * Slot: id
-- # Class: SamplingCapability Description: Client sampling capability.
--     * Slot: id
-- # Class: RootsCapability Description: Client roots capability.
--     * Slot: id
--     * Slot: listChanged Description: Whether notifications for list changes are supported.
-- # Class: PromptsCapability Description: Server prompts capability.
--     * Slot: id
--     * Slot: listChanged Description: Whether notifications for list changes are supported.
-- # Class: ResourcesCapability Description: Server resources capability.
--     * Slot: id
--     * Slot: listChanged Description: Whether notifications for list changes are supported.
--     * Slot: subscribe Description: Whether subscribing to resource updates is supported.
-- # Class: ToolsCapability Description: Server tools capability.
--     * Slot: id
--     * Slot: listChanged Description: Whether notifications for list changes are supported.
-- # Class: TaskRequestCapabilities Description: Task request capability map.
--     * Slot: id
--     * Slot: elicitation_id Description: Elicitation capability object.
--     * Slot: sampling_id Description: Sampling capability object.
--     * Slot: tools_id Description: The list of tools.
-- # Class: TasksCapability Description: Task capability object.
--     * Slot: id
--     * Slot: requests_id Description: Task request capabilities.
-- # Class: ExtensionsCapability Description: Server/client extension capability object.
--     * Slot: id
--     * Slot: apps_extension_id Description: Extension capability entry for app mime types.
-- # Class: ExtensionAppCapability Description: Extension payload for app mime type declarations.
--     * Slot: id
-- # Class: Tool Description: Definition for a tool the client can call.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: CreateMessageRequestParams_id Description: Autocreated FK slot
--     * Slot: ListToolsResult_id Description: Autocreated FK slot
--     * Slot: annotations_id Description: Optional additional tool information.
--     * Slot: execution_id Description: Execution-related properties for this tool.
--     * Slot: inputSchema_id Description: A JSON Schema object defining the expected parameters for the tool.
--     * Slot: outputSchema_id Description: An optional JSON Schema object defining the structure of the tool's output.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ModelHint Description: Hints to use for model selection.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: ModelPreferences_id Description: Autocreated FK slot
-- # Class: ModelPreferences Description: The server's preferences for model selection, requested of the client during sampling.
--     * Slot: id
--     * Slot: costPriority Description: How much to prioritize cost when selecting a model (0-1).
--     * Slot: intelligencePriority Description: How much to prioritize intelligence when selecting a model (0-1).
--     * Slot: speedPriority Description: How much to prioritize sampling speed when selecting a model (0-1).
-- # Class: SamplingMessage Description: Describes a message issued to or received from an LLM API.
--     * Slot: id
--     * Slot: role Description: The role of the sender or recipient.
--     * Slot: CreateMessageRequestParams_id Description: Autocreated FK slot
--     * Slot: content_id Description: The message content.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: Task Description: Data associated with a task.
--     * Slot: id
--     * Slot: taskId Description: The task identifier.
--     * Slot: status Description: Current task state.
--     * Slot: createdAt Description: ISO 8601 timestamp when the task was created.
--     * Slot: lastUpdatedAt Description: ISO 8601 timestamp when the task was last updated.
--     * Slot: ttl Description: Actual retention duration from creation in milliseconds, null for unlimited.
--     * Slot: statusMessage Description: Optional human-readable message describing the current task state.
--     * Slot: pollInterval Description: Suggested polling interval in milliseconds.
--     * Slot: ListTasksResult_id Description: Autocreated FK slot
-- # Class: TaskMetadata Description: Metadata for augmenting a request with task execution.
--     * Slot: id
--     * Slot: ttl Description: Actual retention duration from creation in milliseconds, null for unlimited.
-- # Class: RelatedTaskMetadata Description: Metadata for associating messages with a task.
--     * Slot: id
--     * Slot: taskId Description: The task identifier.
-- # Class: ClientCapabilities Description: Capabilities a client may support. Known capabilities are defined here, but this is not a closed set.
--     * Slot: id
--     * Slot: experimental Description: Experimental capability extensions.
--     * Slot: elicitation_id Description: Elicitation capability object.
--     * Slot: extensions_id Description: Implementation-specific extension capabilities.
--     * Slot: roots_id Description: The list of roots.
--     * Slot: sampling_id Description: Sampling capability object.
--     * Slot: tasks_id Description: The list of tasks.
-- # Class: ServerCapabilities Description: Capabilities that a server may support. Known capabilities are defined here, but this is not a closed set.
--     * Slot: id
--     * Slot: experimental Description: Experimental capability extensions.
--     * Slot: extensions_id Description: Implementation-specific extension capabilities.
--     * Slot: prompts_id Description: The list of prompts.
--     * Slot: resources_id Description: The list of resources.
--     * Slot: tools_id Description: The list of tools.
--     * Slot: tasks_id Description: The list of tasks.
-- # Class: StringSchema Description: String schema definition.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: format Description: String format constraint.
--     * Slot: minLength Description: Minimum length constraint.
--     * Slot: maxLength Description: Maximum length constraint.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: NumberSchema Description: Number schema definition.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: minimum Description: Minimum value constraint.
--     * Slot: maximum Description: Maximum value constraint.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: BooleanSchema Description: Boolean schema definition.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: default_value Description: Default boolean value.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: description Description: A human-readable description.
-- # Class: UntitledSingleSelectEnumSchema Description: Single-selection enum without display titles.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: TitledSingleSelectEnumSchema Description: Single-selection enum with display titles for each option.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Class: UntitledMultiSelectEnumSchema Description: Multi-selection enum without display titles.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: minItems Description: Minimum number of items.
--     * Slot: maxItems Description: Maximum number of items.
--     * Slot: items_id Description: JSON Schema items definition.
-- # Class: TitledMultiSelectEnumSchema Description: Multi-selection enum with display titles for each option.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
--     * Slot: minItems Description: Minimum number of items.
--     * Slot: maxItems Description: Maximum number of items.
--     * Slot: items_id Description: JSON Schema items definition.
-- # Class: LegacyTitledEnumSchema Description: Legacy titled enum schema. Use TitledSingleSelectEnumSchema instead.
--     * Slot: id
--     * Slot: type Description: Type discriminator field.
--     * Slot: default Description: Default value for a schema field.
--     * Slot: default_value Description: Default value for a schema field.
--     * Slot: description Description: A human-readable description.
--     * Slot: title Description: Intended for UI and end-user contexts — optimized to be human-readable and easily understood.
-- # Abstract Class: JSONRPCRequest Description: A request that expects a response.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Abstract Class: JSONRPCNotification Description: A notification which does not expect a response.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Abstract Class: JSONRPCResultResponse Description: A successful (non-error) response to a request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
-- # Class: JSONRPCErrorResponse Description: A response to a request that indicates an error occurred.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: error_id Description: The error object.
-- # Class: Result Description: Common result fields.
--     * Slot: id
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CancelledNotificationParams Description: Parameters for a notifications/cancelled notification.
--     * Slot: id
--     * Slot: requestId Description: The ID of a request.
--     * Slot: reason Description: An optional string describing the reason.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ProgressNotificationParams Description: Parameters for a notifications/progress notification.
--     * Slot: id
--     * Slot: progress Description: The progress thus far.
--     * Slot: progressToken Description: The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.
--     * Slot: total Description: Total number of items to process (or total progress required), if known.
--     * Slot: message Description: A message string.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ElicitationCompleteNotificationParams Description: Parameters for a notifications/elicitation/complete notification.
--     * Slot: id
--     * Slot: elicitationId Description: The ID of the elicitation.
-- # Class: LoggingMessageNotificationParams Description: Parameters for a notifications/message notification.
--     * Slot: id
--     * Slot: level Description: The severity of a log message.
--     * Slot: logger Description: An optional name of the logger issuing this message.
--     * Slot: data_id Description: The data to be logged.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ResourceUpdatedNotificationParams Description: Parameters for a notifications/resources/updated notification.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: TaskStatusNotificationParams Description: Parameters for a notifications/tasks/status notification.
--     * Slot: id
--     * Slot: taskId Description: The task identifier.
--     * Slot: status Description: Current task state.
--     * Slot: createdAt Description: ISO 8601 timestamp when the task was created.
--     * Slot: lastUpdatedAt Description: ISO 8601 timestamp when the task was last updated.
--     * Slot: ttl Description: Actual retention duration from creation in milliseconds, null for unlimited.
--     * Slot: statusMessage Description: Optional human-readable message describing the current task state.
--     * Slot: pollInterval Description: Suggested polling interval in milliseconds.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CancelledNotification Description: Notification to indicate that a previously-issued request is being cancelled.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: InitializedNotification Description: Notification sent from the client to the server after initialization has finished.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ProgressNotification Description: Out-of-band notification to inform the receiver of a progress update.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: ResourceListChangedNotification Description: Notification that the list of resources the server can read from has changed.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ResourceUpdatedNotification Description: Notification that a resource has changed and may need to be read again.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: PromptListChangedNotification Description: Notification that the list of prompts the server offers has changed.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ToolListChangedNotification Description: Notification that the list of tools the server offers has changed.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: RootsListChangedNotification Description: Notification from the client that the list of roots has changed.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: LoggingMessageNotification Description: Notification of a log message passed from server to client.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: ElicitationCompleteNotification Description: Notification from the server that an out-of-band elicitation request completed.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: TaskStatusNotification Description: Notification that a task's status has changed.
--     * Slot: id
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: CallToolRequestParams Description: Parameters for a tools/call request.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: arguments_id Description: Arguments to use for the tool call.
--     * Slot: task_id Description: If specified, the caller is requesting task-augmented execution.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: GetPromptRequestParams Description: Parameters for a prompts/get request.
--     * Slot: id
--     * Slot: name Description: Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present).
--     * Slot: arguments_id Description: Arguments to use for templating the prompt.
-- # Class: CompleteRequestParams Description: Parameters for a completion/complete request.
--     * Slot: id
--     * Slot: argument_id Description: The argument's information.
--     * Slot: context_id Description: Optional completion context.
--     * Slot: ref_id Description: A prompt or resource template reference.
-- # Class: ReadResourceRequestParams Description: Parameters for a resources/read request.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
-- # Class: SubscribeRequestParams Description: Parameters for a resources/subscribe request.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
-- # Class: UnsubscribeRequestParams Description: Parameters for a resources/unsubscribe request.
--     * Slot: id
--     * Slot: uri Description: A resource URI.
-- # Class: SetLevelRequestParams Description: Parameters for a logging/setLevel request.
--     * Slot: id
--     * Slot: level Description: The severity of a log message.
-- # Class: InitializeRequestParams Description: Parameters for an initialize request.
--     * Slot: id
--     * Slot: protocolVersion Description: The version of the Model Context Protocol.
--     * Slot: capabilities_id Description: Client capabilities.
--     * Slot: clientInfo_id Description: Information about the client implementation.
-- # Class: CreateMessageRequestParams Description: Parameters for a sampling/createMessage request.
--     * Slot: id
--     * Slot: maxTokens Description: The requested maximum number of tokens to sample.
--     * Slot: systemPrompt Description: An optional system prompt the server wants to use for sampling.
--     * Slot: temperature Description: Sampling temperature.
--     * Slot: includeContext Description: A request to include context from one or more MCP servers.
--     * Slot: modelPreferences_id Description: Model preferences for sampling.
--     * Slot: toolChoice_id Description: Controls how the model uses tools.
--     * Slot: task_id Description: If specified, task-augmented execution.
-- # Class: ElicitRequestFormParams Description: Parameters for a form-mode elicitation request.
--     * Slot: id
--     * Slot: message Description: A message string.
--     * Slot: mode Description: The elicitation mode.
--     * Slot: requestedSchema_id Description: A restricted subset of JSON Schema.
--     * Slot: task_id Description: If specified, task-augmented execution.
-- # Class: ElicitRequestURLParams Description: Parameters for a URL-mode elicitation request.
--     * Slot: id
--     * Slot: elicitationId Description: The ID of the elicitation.
--     * Slot: message Description: A message string.
--     * Slot: mode Description: The elicitation mode.
--     * Slot: url Description: The URL that the user should navigate to.
--     * Slot: task_id Description: If specified, task-augmented execution.
-- # Class: PaginatedRequestParams Description: Common params for paginated requests.
--     * Slot: id
--     * Slot: cursor Description: An opaque token representing the current pagination position. If provided, the server should return results starting after this cursor.
-- # Class: InitializeRequest Description: Request sent from the client to the server when it first connects, asking it to begin initialization.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: PingRequest Description: A ping, issued by either the server or the client, to check that the other party is still alive.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ListResourcesRequest Description: Sent from the client to request a list of resources the server has.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ListResourceTemplatesRequest Description: Sent from the client to request a list of resource templates the server has.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ReadResourceRequest Description: Sent from the client to the server, to read a specific resource URI.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: SubscribeRequest Description: Sent from the client to request resource update notifications.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: UnsubscribeRequest Description: Sent from the client to cancel resource update notifications.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: ListPromptsRequest Description: Sent from the client to request a list of prompts and prompt templates.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: GetPromptRequest Description: Used by the client to get a prompt provided by the server.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: ListToolsRequest Description: Sent from the client to request a list of tools the server has.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: CallToolRequest Description: Used by the client to invoke a tool provided by the server.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: CompleteRequest Description: A request from the client to the server, to ask for completion options.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: SetLevelRequest Description: A request from the client to the server, to enable or adjust logging.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: CreateMessageRequest Description: A request from the server to sample an LLM via the client.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: ListRootsRequest Description: Sent from the server to request a list of root URIs from the client.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: ElicitRequest Description: A request from the server to elicit additional information from the user via the client.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
--     * Slot: params_id Description: JSON-RPC parameters payload.
-- # Class: ListTasksRequest Description: A request to retrieve a list of tasks.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: GetTaskRequest Description: A request to retrieve the state of a task.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: GetTaskPayloadRequest Description: A request to retrieve the result of a completed task.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: CancelTaskRequest Description: A request to cancel a task.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: method Description: The JSON-RPC method name.
-- # Class: InitializeResult Description: The result returned by the server for an initialize request.
--     * Slot: id
--     * Slot: protocolVersion Description: The version of the Model Context Protocol.
--     * Slot: instructions Description: Instructions describing how to use the server and its features.
--     * Slot: capabilities_id Description: Server capabilities.
--     * Slot: serverInfo_id Description: Information about the server implementation.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CallToolResult Description: The result returned by the server for a tools/call request.
--     * Slot: id
--     * Slot: isError Description: Whether the tool call ended in an error.
--     * Slot: structuredContent_id Description: An optional JSON object representing structured result of the tool call.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CompleteResult Description: The result returned by the server for a completion/complete request.
--     * Slot: id
--     * Slot: completion_id Description: The completion result object.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: GetPromptResult Description: The result returned by the server for a prompts/get request.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ListPromptsResult Description: The result returned by the server for a prompts/list request.
--     * Slot: id
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result. If present, there may be more results available.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ListResourcesResult Description: The result returned by the server for a resources/list request.
--     * Slot: id
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result. If present, there may be more results available.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ListResourceTemplatesResult Description: The result returned by the server for a resources/templates/list request.
--     * Slot: id
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result. If present, there may be more results available.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ReadResourceResult Description: The result returned by the server for a resources/read request.
--     * Slot: id
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ListToolsResult Description: The result returned by the server for a tools/list request.
--     * Slot: id
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result. If present, there may be more results available.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ListRootsResult Description: The result returned by the client for a roots/list request.
--     * Slot: id
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CreateMessageResult Description: The result returned by the client for a sampling/createMessage request.
--     * Slot: id
--     * Slot: model Description: The name of the model that generated the message.
--     * Slot: role Description: The role of the sender or recipient.
--     * Slot: stopReason Description: The reason why sampling stopped, if known.
--     * Slot: content_id Description: The message content.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ElicitResult Description: The result returned by the client for an elicitation/create request.
--     * Slot: id
--     * Slot: action Description: The user action in response to the elicitation.
--     * Slot: content_id Description: Structured content block of a message or result.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CreateTaskResult Description: The result returned for a task-augmented request.
--     * Slot: id
--     * Slot: task_id Description: Task data.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: GetTaskPayloadResult Description: The result returned for a tasks/result request.
--     * Slot: id
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: ListTasksResult Description: The result returned for a tasks/list request.
--     * Slot: id
--     * Slot: nextCursor Description: An opaque token representing the pagination position after the last returned result. If present, there may be more results available.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: CancelTaskResult Description: The result returned for a tasks/cancel request.
--     * Slot: id
--     * Slot: taskId Description: The task identifier.
--     * Slot: status Description: Current task state.
--     * Slot: createdAt Description: ISO 8601 timestamp when the task was created.
--     * Slot: lastUpdatedAt Description: ISO 8601 timestamp when the task was last updated.
--     * Slot: ttl Description: Actual retention duration from creation in milliseconds, null for unlimited.
--     * Slot: statusMessage Description: Optional human-readable message describing the current task state.
--     * Slot: pollInterval Description: Suggested polling interval in milliseconds.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: GetTaskResult Description: The result returned for a tasks/get request.
--     * Slot: id
--     * Slot: taskId Description: The task identifier.
--     * Slot: status Description: Current task state.
--     * Slot: createdAt Description: ISO 8601 timestamp when the task was created.
--     * Slot: lastUpdatedAt Description: ISO 8601 timestamp when the task was last updated.
--     * Slot: ttl Description: Actual retention duration from creation in milliseconds, null for unlimited.
--     * Slot: statusMessage Description: Optional human-readable message describing the current task state.
--     * Slot: pollInterval Description: Suggested polling interval in milliseconds.
--     * Slot: _meta_id Description: Optional metadata object.
-- # Class: InitializeResultResponse Description: A successful response from the server for an initialize request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: CallToolResultResponse Description: A successful response from the server for a tools/call request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: CompleteResultResponse Description: A successful response from the server for a completion/complete request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: GetPromptResultResponse Description: A successful response from the server for a prompts/get request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ListPromptsResultResponse Description: A successful response from the server for a prompts/list request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ListResourcesResultResponse Description: A successful response from the server for a resources/list request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ListResourceTemplatesResultResponse Description: A successful response from the server for a resources/templates/list request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ReadResourceResultResponse Description: A successful response from the server for a resources/read request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ListToolsResultResponse Description: A successful response from the server for a tools/list request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ListRootsResultResponse Description: A successful response from the client for a roots/list request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: CreateMessageResultResponse Description: A successful response from the client for a sampling/createMessage request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ElicitResultResponse Description: A successful response from the client for an elicitation/create request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: SetLevelResultResponse Description: A successful response from the server for a logging/setLevel request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: PingResultResponse Description: A successful response for a ping request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: SubscribeResultResponse Description: A successful response for a resources/subscribe request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: UnsubscribeResultResponse Description: A successful response for a resources/unsubscribe request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: CreateTaskResultResponse Description: A successful response for a task-augmented request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: GetTaskResultResponse Description: A successful response for a tasks/get request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: GetTaskPayloadResultResponse Description: A successful response for a tasks/result request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: CancelTaskResultResponse Description: A successful response for a tasks/cancel request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ListTasksResultResponse Description: A successful response for a tasks/list request.
--     * Slot: uid
--     * Slot: id Description: Uniquely identifying ID for a JSON-RPC request.
--     * Slot: jsonrpc Description: JSON-RPC version string.
--     * Slot: result_id Description: JSON-RPC successful result payload.
-- # Class: ClientNotification Description: A union of all notifications that can be sent by a client.
--     * Slot: id
-- # Class: ClientRequest Description: A union of all requests that can be sent by a client.
--     * Slot: id
-- # Class: ClientResult Description: A union of all result types that a client can return.
--     * Slot: id
-- # Class: ServerNotification Description: A union of all notifications that can be sent by a server.
--     * Slot: id
-- # Class: ServerRequest Description: A union of all requests that can be sent by a server.
--     * Slot: id
-- # Class: ServerResult Description: A union of all result types that a server can return.
--     * Slot: id
-- # Class: JSONRPCMessage Description: A union of all JSON-RPC message types (requests, notifications, and responses).
--     * Slot: id
-- # Class: JSONRPCResponse Description: A union of all JSON-RPC response types.
--     * Slot: id
-- # Class: ElicitRequestParams Description: A union of all elicitation request parameter types.
--     * Slot: id
-- # Class: EnumSchema Description: A union of all enum schema types.
--     * Slot: id
-- # Class: SingleSelectEnumSchema Description: A union of single-select enum schema types.
--     * Slot: id
-- # Class: MultiSelectEnumSchema Description: A union of multi-select enum schema types.
--     * Slot: id
-- # Class: PrimitiveSchemaDefinition Description: A union of all primitive schema definition types.
--     * Slot: id
-- # Class: ContentBlockVariants Description: A union of all content block types. Maps to the vendor schema ContentBlock anyOf definition.
--     * Slot: id
-- # Class: SamplingMessageContentBlock Description: A union of content types valid in sampling messages.
--     * Slot: id
-- # Class: Annotations_audience
--     * Slot: Annotations_id Description: Autocreated FK slot
--     * Slot: audience Description: Describes who the intended audience of this object or data is.
-- # Class: Icon_sizes
--     * Slot: Icon_id Description: Autocreated FK slot
--     * Slot: sizes Description: Optional array of strings specifying sizes (WxH format or "any").
-- # Class: ToolResultContent_content
--     * Slot: ToolResultContent_id Description: Autocreated FK slot
--     * Slot: content_id Description: The unstructured result content of the tool use.
-- # Class: CompletionData_values
--     * Slot: CompletionData_id Description: Autocreated FK slot
--     * Slot: values Description: An array of completion values.
-- # Class: SchemaItems_enum
--     * Slot: SchemaItems_id Description: Autocreated FK slot
--     * Slot: enum Description: Array of enum values.
-- # Class: SchemaItems_anyOf
--     * Slot: SchemaItems_id Description: Autocreated FK slot
--     * Slot: anyOf_id Description: JSON Schema anyOf entries.
-- # Class: JsonSchema_required_list
--     * Slot: JsonSchema_id Description: Autocreated FK slot
--     * Slot: required_list Description: JSON Schema required property list.
-- # Class: JsonSchema_oneOf
--     * Slot: JsonSchema_id Description: Autocreated FK slot
--     * Slot: oneOf_id Description: JSON Schema oneOf entries.
-- # Class: JsonSchema_anyOf
--     * Slot: JsonSchema_id Description: Autocreated FK slot
--     * Slot: anyOf_id Description: JSON Schema anyOf entries.
-- # Class: JsonSchema_enum
--     * Slot: JsonSchema_id Description: Autocreated FK slot
--     * Slot: enum Description: Array of enum values.
-- # Class: ExtensionAppCapability_mimeTypes
--     * Slot: ExtensionAppCapability_id Description: Autocreated FK slot
--     * Slot: mimeTypes Description: MIME types supported by an extension capability.
-- # Class: UntitledSingleSelectEnumSchema_enum
--     * Slot: UntitledSingleSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: enum Description: Array of enum values.
-- # Class: UntitledSingleSelectEnumSchema_enum_values
--     * Slot: UntitledSingleSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: enum_values Description: Array of enum values.
-- # Class: TitledSingleSelectEnumSchema_oneOf
--     * Slot: TitledSingleSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: oneOf_id Description: JSON Schema oneOf entries.
-- # Class: UntitledMultiSelectEnumSchema_default
--     * Slot: UntitledMultiSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: default Description: Default value for a schema field.
-- # Class: TitledMultiSelectEnumSchema_default
--     * Slot: TitledMultiSelectEnumSchema_id Description: Autocreated FK slot
--     * Slot: default Description: Default value for a schema field.
-- # Class: LegacyTitledEnumSchema_enum
--     * Slot: LegacyTitledEnumSchema_id Description: Autocreated FK slot
--     * Slot: enum Description: Array of enum values.
-- # Class: LegacyTitledEnumSchema_enum_values
--     * Slot: LegacyTitledEnumSchema_id Description: Autocreated FK slot
--     * Slot: enum_values Description: Array of enum values.
-- # Class: LegacyTitledEnumSchema_enumNames
--     * Slot: LegacyTitledEnumSchema_id Description: Autocreated FK slot
--     * Slot: enumNames Description: Display names for enum values (legacy).
-- # Class: CreateMessageRequestParams_stopSequences
--     * Slot: CreateMessageRequestParams_id Description: Autocreated FK slot
--     * Slot: stopSequences Description: Stop sequences for sampling.
-- # Class: CallToolResult_content
--     * Slot: CallToolResult_id Description: Autocreated FK slot
--     * Slot: content_id Description: A list of content objects that represent the result.

CREATE TABLE "HasIcons" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HasIcons_id" ON "HasIcons" (id);

CREATE TABLE "HasName" (
	id INTEGER NOT NULL,
	name TEXT,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HasName_id" ON "HasName" (id);

CREATE TABLE "Annotations" (
	id INTEGER NOT NULL,
	"lastModified" TEXT,
	priority FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Annotations_id" ON "Annotations" (id);

CREATE TABLE "Implementation" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	description TEXT,
	"websiteUrl" TEXT,
	name TEXT NOT NULL,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Implementation_id" ON "Implementation" (id);

CREATE TABLE "ContentBlock" (
	id INTEGER NOT NULL,
	type TEXT,
	text TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ContentBlock_id" ON "ContentBlock" (id);

CREATE TABLE "PromptReference" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT NOT NULL,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PromptReference_id" ON "PromptReference" (id);

CREATE TABLE "ResourceTemplateReference" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	uri TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResourceTemplateReference_id" ON "ResourceTemplateReference" (id);

CREATE TABLE "ToolAnnotations" (
	id INTEGER NOT NULL,
	title TEXT,
	"destructiveHint" BOOLEAN,
	"idempotentHint" BOOLEAN,
	"openWorldHint" BOOLEAN,
	"readOnlyHint" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolAnnotations_id" ON "ToolAnnotations" (id);

CREATE TABLE "ToolChoice" (
	id INTEGER NOT NULL,
	mode VARCHAR(8),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolChoice_id" ON "ToolChoice" (id);

CREATE TABLE "ToolExecution" (
	id INTEGER NOT NULL,
	"taskSupport" VARCHAR(9),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolExecution_id" ON "ToolExecution" (id);

CREATE TABLE "MetaObject" (
	id INTEGER NOT NULL,
	"progressToken" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MetaObject_id" ON "MetaObject" (id);

CREATE TABLE "ArgumentMap" (
	id INTEGER NOT NULL,
	city TEXT,
	location TEXT,
	language TEXT,
	framework TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ArgumentMap_id" ON "ArgumentMap" (id);

CREATE TABLE "CompletionArgument" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CompletionArgument_id" ON "CompletionArgument" (id);

CREATE TABLE "CompletionData" (
	id INTEGER NOT NULL,
	total FLOAT,
	"hasMore" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CompletionData_id" ON "CompletionData" (id);

CREATE TABLE "EnumOption" (
	id INTEGER NOT NULL,
	const TEXT NOT NULL,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EnumOption_id" ON "EnumOption" (id);

CREATE TABLE "SchemaItems" (
	id INTEGER NOT NULL,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SchemaItems_id" ON "SchemaItems" (id);

CREATE TABLE "JsonSchema" (
	id INTEGER NOT NULL,
	"schemaUri" TEXT,
	type TEXT,
	"additionalProperties" BOOLEAN,
	minimum INTEGER,
	maximum INTEGER,
	"minLength" INTEGER,
	"maxLength" INTEGER,
	format VARCHAR(9),
	description TEXT,
	title TEXT,
	const TEXT,
	"default" TEXT,
	properties_id INTEGER,
	items_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(properties_id) REFERENCES "SchemaProperties" (id),
	FOREIGN KEY(items_id) REFERENCES "SchemaItems" (id)
);
CREATE INDEX "ix_JsonSchema_id" ON "JsonSchema" (id);

CREATE TABLE "SchemaProperties" (
	id INTEGER NOT NULL,
	name_id INTEGER,
	email_id INTEGER,
	age_id INTEGER,
	city_id INTEGER,
	location_id INTEGER,
	a_id INTEGER,
	b_id INTEGER,
	temperature_id INTEGER,
	conditions_id INTEGER,
	humidity_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(name_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(email_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(age_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(city_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(location_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(a_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(b_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(temperature_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(conditions_id) REFERENCES "JsonSchema" (id),
	FOREIGN KEY(humidity_id) REFERENCES "JsonSchema" (id)
);
CREATE INDEX "ix_SchemaProperties_id" ON "SchemaProperties" (id);

CREATE TABLE "ToolInput" (
	id INTEGER NOT NULL,
	city TEXT,
	location TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolInput_id" ON "ToolInput" (id);

CREATE TABLE "StructuredContentData" (
	id INTEGER NOT NULL,
	temperature FLOAT,
	conditions TEXT,
	humidity FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StructuredContentData_id" ON "StructuredContentData" (id);

CREATE TABLE "LogDetails" (
	id INTEGER NOT NULL,
	host TEXT,
	port INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LogDetails_id" ON "LogDetails" (id);

CREATE TABLE "ErrorData" (
	id INTEGER NOT NULL,
	reason TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ErrorData_id" ON "ErrorData" (id);

CREATE TABLE "ElicitationContent" (
	id INTEGER NOT NULL,
	name TEXT,
	email TEXT,
	age INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ElicitationContent_id" ON "ElicitationContent" (id);

CREATE TABLE "ElicitationCapability" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ElicitationCapability_id" ON "ElicitationCapability" (id);

CREATE TABLE "SamplingCapability" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SamplingCapability_id" ON "SamplingCapability" (id);

CREATE TABLE "RootsCapability" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RootsCapability_id" ON "RootsCapability" (id);

CREATE TABLE "PromptsCapability" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PromptsCapability_id" ON "PromptsCapability" (id);

CREATE TABLE "ResourcesCapability" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	subscribe BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResourcesCapability_id" ON "ResourcesCapability" (id);

CREATE TABLE "ToolsCapability" (
	id INTEGER NOT NULL,
	"listChanged" BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolsCapability_id" ON "ToolsCapability" (id);

CREATE TABLE "ExtensionAppCapability" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ExtensionAppCapability_id" ON "ExtensionAppCapability" (id);

CREATE TABLE "ModelPreferences" (
	id INTEGER NOT NULL,
	"costPriority" FLOAT,
	"intelligencePriority" FLOAT,
	"speedPriority" FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ModelPreferences_id" ON "ModelPreferences" (id);

CREATE TABLE "TaskMetadata" (
	id INTEGER NOT NULL,
	ttl INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TaskMetadata_id" ON "TaskMetadata" (id);

CREATE TABLE "RelatedTaskMetadata" (
	id INTEGER NOT NULL,
	"taskId" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RelatedTaskMetadata_id" ON "RelatedTaskMetadata" (id);

CREATE TABLE "StringSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"default" TEXT,
	default_value TEXT,
	description TEXT,
	format VARCHAR(9),
	"minLength" INTEGER,
	"maxLength" INTEGER,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StringSchema_id" ON "StringSchema" (id);

CREATE TABLE "NumberSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"default" INTEGER,
	default_value TEXT,
	description TEXT,
	minimum INTEGER,
	maximum INTEGER,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NumberSchema_id" ON "NumberSchema" (id);

CREATE TABLE "BooleanSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"default" BOOLEAN,
	default_value BOOLEAN,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BooleanSchema_id" ON "BooleanSchema" (id);

CREATE TABLE "UntitledSingleSelectEnumSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"default" TEXT,
	default_value TEXT,
	description TEXT,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_UntitledSingleSelectEnumSchema_id" ON "UntitledSingleSelectEnumSchema" (id);

CREATE TABLE "TitledSingleSelectEnumSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"default" TEXT,
	default_value TEXT,
	description TEXT,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TitledSingleSelectEnumSchema_id" ON "TitledSingleSelectEnumSchema" (id);

CREATE TABLE "LegacyTitledEnumSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"default" TEXT,
	default_value TEXT,
	description TEXT,
	title TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LegacyTitledEnumSchema_id" ON "LegacyTitledEnumSchema" (id);

CREATE TABLE "JSONRPCRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_JSONRPCRequest_uid" ON "JSONRPCRequest" (uid);

CREATE TABLE "JSONRPCNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_JSONRPCNotification_id" ON "JSONRPCNotification" (id);

CREATE TABLE "JSONRPCResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_JSONRPCResultResponse_uid" ON "JSONRPCResultResponse" (uid);

CREATE TABLE "ElicitationCompleteNotificationParams" (
	id INTEGER NOT NULL,
	"elicitationId" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ElicitationCompleteNotificationParams_id" ON "ElicitationCompleteNotificationParams" (id);

CREATE TABLE "InitializedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InitializedNotification_id" ON "InitializedNotification" (id);

CREATE TABLE "ResourceListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResourceListChangedNotification_id" ON "ResourceListChangedNotification" (id);

CREATE TABLE "PromptListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PromptListChangedNotification_id" ON "PromptListChangedNotification" (id);

CREATE TABLE "ToolListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolListChangedNotification_id" ON "ToolListChangedNotification" (id);

CREATE TABLE "RootsListChangedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RootsListChangedNotification_id" ON "RootsListChangedNotification" (id);

CREATE TABLE "ReadResourceRequestParams" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ReadResourceRequestParams_id" ON "ReadResourceRequestParams" (id);

CREATE TABLE "SubscribeRequestParams" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SubscribeRequestParams_id" ON "SubscribeRequestParams" (id);

CREATE TABLE "UnsubscribeRequestParams" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_UnsubscribeRequestParams_id" ON "UnsubscribeRequestParams" (id);

CREATE TABLE "SetLevelRequestParams" (
	id INTEGER NOT NULL,
	level VARCHAR(9) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SetLevelRequestParams_id" ON "SetLevelRequestParams" (id);

CREATE TABLE "PaginatedRequestParams" (
	id INTEGER NOT NULL,
	cursor TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PaginatedRequestParams_id" ON "PaginatedRequestParams" (id);

CREATE TABLE "PingRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_PingRequest_uid" ON "PingRequest" (uid);

CREATE TABLE "ListResourcesRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ListResourcesRequest_uid" ON "ListResourcesRequest" (uid);

CREATE TABLE "ListResourceTemplatesRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ListResourceTemplatesRequest_uid" ON "ListResourceTemplatesRequest" (uid);

CREATE TABLE "ListPromptsRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ListPromptsRequest_uid" ON "ListPromptsRequest" (uid);

CREATE TABLE "ListToolsRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ListToolsRequest_uid" ON "ListToolsRequest" (uid);

CREATE TABLE "ListRootsRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ListRootsRequest_uid" ON "ListRootsRequest" (uid);

CREATE TABLE "ListTasksRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ListTasksRequest_uid" ON "ListTasksRequest" (uid);

CREATE TABLE "GetTaskRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_GetTaskRequest_uid" ON "GetTaskRequest" (uid);

CREATE TABLE "GetTaskPayloadRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_GetTaskPayloadRequest_uid" ON "GetTaskPayloadRequest" (uid);

CREATE TABLE "CancelTaskRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_CancelTaskRequest_uid" ON "CancelTaskRequest" (uid);

CREATE TABLE "ClientNotification" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ClientNotification_id" ON "ClientNotification" (id);

CREATE TABLE "ClientRequest" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ClientRequest_id" ON "ClientRequest" (id);

CREATE TABLE "ClientResult" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ClientResult_id" ON "ClientResult" (id);

CREATE TABLE "ServerNotification" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ServerNotification_id" ON "ServerNotification" (id);

CREATE TABLE "ServerRequest" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ServerRequest_id" ON "ServerRequest" (id);

CREATE TABLE "ServerResult" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ServerResult_id" ON "ServerResult" (id);

CREATE TABLE "JSONRPCMessage" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_JSONRPCMessage_id" ON "JSONRPCMessage" (id);

CREATE TABLE "JSONRPCResponse" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_JSONRPCResponse_id" ON "JSONRPCResponse" (id);

CREATE TABLE "ElicitRequestParams" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ElicitRequestParams_id" ON "ElicitRequestParams" (id);

CREATE TABLE "EnumSchema" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EnumSchema_id" ON "EnumSchema" (id);

CREATE TABLE "SingleSelectEnumSchema" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SingleSelectEnumSchema_id" ON "SingleSelectEnumSchema" (id);

CREATE TABLE "MultiSelectEnumSchema" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MultiSelectEnumSchema_id" ON "MultiSelectEnumSchema" (id);

CREATE TABLE "PrimitiveSchemaDefinition" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PrimitiveSchemaDefinition_id" ON "PrimitiveSchemaDefinition" (id);

CREATE TABLE "ContentBlockVariants" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ContentBlockVariants_id" ON "ContentBlockVariants" (id);

CREATE TABLE "SamplingMessageContentBlock" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SamplingMessageContentBlock_id" ON "SamplingMessageContentBlock" (id);

CREATE TABLE "HasMeta" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_HasMeta_id" ON "HasMeta" (id);

CREATE TABLE "HasAnnotations" (
	id INTEGER NOT NULL,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_HasAnnotations_id" ON "HasAnnotations" (id);

CREATE TABLE "Error" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_Error_id" ON "Error" (id);

CREATE TABLE "InternalError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_InternalError_id" ON "InternalError" (id);

CREATE TABLE "InvalidParamsError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_InvalidParamsError_id" ON "InvalidParamsError" (id);

CREATE TABLE "InvalidRequestError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_InvalidRequestError_id" ON "InvalidRequestError" (id);

CREATE TABLE "MethodNotFoundError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_MethodNotFoundError_id" ON "MethodNotFoundError" (id);

CREATE TABLE "ParseError" (
	id INTEGER NOT NULL,
	code INTEGER NOT NULL,
	message TEXT NOT NULL,
	data_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_ParseError_id" ON "ParseError" (id);

CREATE TABLE "TextContent" (
	id INTEGER NOT NULL,
	text TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_TextContent_id" ON "TextContent" (id);

CREATE TABLE "ImageContent" (
	id INTEGER NOT NULL,
	data TEXT NOT NULL,
	"mimeType" TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_ImageContent_id" ON "ImageContent" (id);

CREATE TABLE "AudioContent" (
	id INTEGER NOT NULL,
	data TEXT NOT NULL,
	"mimeType" TEXT NOT NULL,
	type TEXT NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_AudioContent_id" ON "AudioContent" (id);

CREATE TABLE "ResourceLink" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	"mimeType" TEXT,
	description TEXT,
	size INTEGER,
	type TEXT NOT NULL,
	name TEXT NOT NULL,
	title TEXT,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_ResourceLink_id" ON "ResourceLink" (id);

CREATE TABLE "ToolUseContent" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	name TEXT NOT NULL,
	input_id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(input_id) REFERENCES "ToolInput" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ToolUseContent_uid" ON "ToolUseContent" (uid);

CREATE TABLE "ToolResultContent" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	"toolUseId" TEXT NOT NULL,
	"isError" BOOLEAN,
	"structuredContent_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("structuredContent_id") REFERENCES "StructuredContentData" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ToolResultContent_id" ON "ToolResultContent" (id);

CREATE TABLE "TextResourceContents" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	"mimeType" TEXT,
	text TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_TextResourceContents_id" ON "TextResourceContents" (id);

CREATE TABLE "BlobResourceContents" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	"mimeType" TEXT,
	blob TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_BlobResourceContents_id" ON "BlobResourceContents" (id);

CREATE TABLE "CompletionContext" (
	id INTEGER NOT NULL,
	arguments_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(arguments_id) REFERENCES "ArgumentMap" (id)
);
CREATE INDEX "ix_CompletionContext_id" ON "CompletionContext" (id);

CREATE TABLE "LogData" (
	id INTEGER NOT NULL,
	error TEXT,
	details_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(details_id) REFERENCES "LogDetails" (id)
);
CREATE INDEX "ix_LogData_id" ON "LogData" (id);

CREATE TABLE "URLElicitation" (
	id INTEGER NOT NULL,
	mode TEXT,
	"elicitationId" TEXT,
	message TEXT,
	url TEXT,
	"ErrorData_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ErrorData_id") REFERENCES "ErrorData" (id)
);
CREATE INDEX "ix_URLElicitation_id" ON "URLElicitation" (id);

CREATE TABLE "TaskRequestCapabilities" (
	id INTEGER NOT NULL,
	elicitation_id INTEGER,
	sampling_id INTEGER,
	tools_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(elicitation_id) REFERENCES "ElicitationCapability" (id),
	FOREIGN KEY(sampling_id) REFERENCES "SamplingCapability" (id),
	FOREIGN KEY(tools_id) REFERENCES "ToolsCapability" (id)
);
CREATE INDEX "ix_TaskRequestCapabilities_id" ON "TaskRequestCapabilities" (id);

CREATE TABLE "ExtensionsCapability" (
	id INTEGER NOT NULL,
	apps_extension_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(apps_extension_id) REFERENCES "ExtensionAppCapability" (id)
);
CREATE INDEX "ix_ExtensionsCapability_id" ON "ExtensionsCapability" (id);

CREATE TABLE "ModelHint" (
	id INTEGER NOT NULL,
	name TEXT,
	"ModelPreferences_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ModelPreferences_id") REFERENCES "ModelPreferences" (id)
);
CREATE INDEX "ix_ModelHint_id" ON "ModelHint" (id);

CREATE TABLE "UntitledMultiSelectEnumSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	default_value TEXT,
	description TEXT,
	title TEXT,
	"minItems" INTEGER,
	"maxItems" INTEGER,
	items_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(items_id) REFERENCES "SchemaItems" (id)
);
CREATE INDEX "ix_UntitledMultiSelectEnumSchema_id" ON "UntitledMultiSelectEnumSchema" (id);

CREATE TABLE "TitledMultiSelectEnumSchema" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	default_value TEXT,
	description TEXT,
	title TEXT,
	"minItems" INTEGER,
	"maxItems" INTEGER,
	items_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(items_id) REFERENCES "SchemaItems" (id)
);
CREATE INDEX "ix_TitledMultiSelectEnumSchema_id" ON "TitledMultiSelectEnumSchema" (id);

CREATE TABLE "Result" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_Result_id" ON "Result" (id);

CREATE TABLE "CancelledNotificationParams" (
	id INTEGER NOT NULL,
	"requestId" TEXT,
	reason TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CancelledNotificationParams_id" ON "CancelledNotificationParams" (id);

CREATE TABLE "ProgressNotificationParams" (
	id INTEGER NOT NULL,
	progress FLOAT NOT NULL,
	"progressToken" TEXT NOT NULL,
	total FLOAT,
	message TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ProgressNotificationParams_id" ON "ProgressNotificationParams" (id);

CREATE TABLE "ResourceUpdatedNotificationParams" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ResourceUpdatedNotificationParams_id" ON "ResourceUpdatedNotificationParams" (id);

CREATE TABLE "TaskStatusNotificationParams" (
	id INTEGER NOT NULL,
	"taskId" TEXT NOT NULL,
	status VARCHAR(14) NOT NULL,
	"createdAt" TEXT NOT NULL,
	"lastUpdatedAt" TEXT NOT NULL,
	ttl INTEGER NOT NULL,
	"statusMessage" TEXT,
	"pollInterval" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_TaskStatusNotificationParams_id" ON "TaskStatusNotificationParams" (id);

CREATE TABLE "ElicitationCompleteNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "ElicitationCompleteNotificationParams" (id)
);
CREATE INDEX "ix_ElicitationCompleteNotification_id" ON "ElicitationCompleteNotification" (id);

CREATE TABLE "CallToolRequestParams" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	arguments_id INTEGER,
	task_id INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(arguments_id) REFERENCES "ArgumentMap" (id),
	FOREIGN KEY(task_id) REFERENCES "TaskMetadata" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CallToolRequestParams_id" ON "CallToolRequestParams" (id);

CREATE TABLE "GetPromptRequestParams" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	arguments_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(arguments_id) REFERENCES "ArgumentMap" (id)
);
CREATE INDEX "ix_GetPromptRequestParams_id" ON "GetPromptRequestParams" (id);

CREATE TABLE "CreateMessageRequestParams" (
	id INTEGER NOT NULL,
	"maxTokens" INTEGER NOT NULL,
	"systemPrompt" TEXT,
	temperature FLOAT,
	"includeContext" VARCHAR(10),
	"modelPreferences_id" INTEGER,
	"toolChoice_id" INTEGER,
	task_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("modelPreferences_id") REFERENCES "ModelPreferences" (id),
	FOREIGN KEY("toolChoice_id") REFERENCES "ToolChoice" (id),
	FOREIGN KEY(task_id) REFERENCES "TaskMetadata" (id)
);
CREATE INDEX "ix_CreateMessageRequestParams_id" ON "CreateMessageRequestParams" (id);

CREATE TABLE "ElicitRequestFormParams" (
	id INTEGER NOT NULL,
	message TEXT NOT NULL,
	mode TEXT,
	"requestedSchema_id" INTEGER NOT NULL,
	task_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("requestedSchema_id") REFERENCES "JsonSchema" (id),
	FOREIGN KEY(task_id) REFERENCES "TaskMetadata" (id)
);
CREATE INDEX "ix_ElicitRequestFormParams_id" ON "ElicitRequestFormParams" (id);

CREATE TABLE "ElicitRequestURLParams" (
	id INTEGER NOT NULL,
	"elicitationId" TEXT NOT NULL,
	message TEXT NOT NULL,
	mode TEXT NOT NULL,
	url TEXT NOT NULL,
	task_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(task_id) REFERENCES "TaskMetadata" (id)
);
CREATE INDEX "ix_ElicitRequestURLParams_id" ON "ElicitRequestURLParams" (id);

CREATE TABLE "ReadResourceRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "ReadResourceRequestParams" (id)
);
CREATE INDEX "ix_ReadResourceRequest_uid" ON "ReadResourceRequest" (uid);

CREATE TABLE "SubscribeRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "SubscribeRequestParams" (id)
);
CREATE INDEX "ix_SubscribeRequest_uid" ON "SubscribeRequest" (uid);

CREATE TABLE "UnsubscribeRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "UnsubscribeRequestParams" (id)
);
CREATE INDEX "ix_UnsubscribeRequest_uid" ON "UnsubscribeRequest" (uid);

CREATE TABLE "SetLevelRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "SetLevelRequestParams" (id)
);
CREATE INDEX "ix_SetLevelRequest_uid" ON "SetLevelRequest" (uid);

CREATE TABLE "CallToolResult" (
	id INTEGER NOT NULL,
	"isError" BOOLEAN,
	"structuredContent_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("structuredContent_id") REFERENCES "StructuredContentData" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CallToolResult_id" ON "CallToolResult" (id);

CREATE TABLE "CompleteResult" (
	id INTEGER NOT NULL,
	completion_id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(completion_id) REFERENCES "CompletionData" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CompleteResult_id" ON "CompleteResult" (id);

CREATE TABLE "GetPromptResult" (
	id INTEGER NOT NULL,
	description TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_GetPromptResult_id" ON "GetPromptResult" (id);

CREATE TABLE "ListPromptsResult" (
	id INTEGER NOT NULL,
	"nextCursor" TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ListPromptsResult_id" ON "ListPromptsResult" (id);

CREATE TABLE "ListResourcesResult" (
	id INTEGER NOT NULL,
	"nextCursor" TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ListResourcesResult_id" ON "ListResourcesResult" (id);

CREATE TABLE "ListResourceTemplatesResult" (
	id INTEGER NOT NULL,
	"nextCursor" TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ListResourceTemplatesResult_id" ON "ListResourceTemplatesResult" (id);

CREATE TABLE "ReadResourceResult" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ReadResourceResult_id" ON "ReadResourceResult" (id);

CREATE TABLE "ListToolsResult" (
	id INTEGER NOT NULL,
	"nextCursor" TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ListToolsResult_id" ON "ListToolsResult" (id);

CREATE TABLE "ListRootsResult" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ListRootsResult_id" ON "ListRootsResult" (id);

CREATE TABLE "CreateMessageResult" (
	id INTEGER NOT NULL,
	model TEXT NOT NULL,
	role VARCHAR(9) NOT NULL,
	"stopReason" TEXT,
	content_id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(content_id) REFERENCES "ContentBlock" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CreateMessageResult_id" ON "CreateMessageResult" (id);

CREATE TABLE "ElicitResult" (
	id INTEGER NOT NULL,
	action VARCHAR(7) NOT NULL,
	content_id INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(content_id) REFERENCES "ElicitationContent" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ElicitResult_id" ON "ElicitResult" (id);

CREATE TABLE "GetTaskPayloadResult" (
	id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_GetTaskPayloadResult_id" ON "GetTaskPayloadResult" (id);

CREATE TABLE "ListTasksResult" (
	id INTEGER NOT NULL,
	"nextCursor" TEXT,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ListTasksResult_id" ON "ListTasksResult" (id);

CREATE TABLE "CancelTaskResult" (
	id INTEGER NOT NULL,
	"taskId" TEXT NOT NULL,
	status VARCHAR(14) NOT NULL,
	"createdAt" TEXT NOT NULL,
	"lastUpdatedAt" TEXT NOT NULL,
	ttl INTEGER NOT NULL,
	"statusMessage" TEXT,
	"pollInterval" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CancelTaskResult_id" ON "CancelTaskResult" (id);

CREATE TABLE "GetTaskResult" (
	id INTEGER NOT NULL,
	"taskId" TEXT NOT NULL,
	status VARCHAR(14) NOT NULL,
	"createdAt" TEXT NOT NULL,
	"lastUpdatedAt" TEXT NOT NULL,
	ttl INTEGER NOT NULL,
	"statusMessage" TEXT,
	"pollInterval" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_GetTaskResult_id" ON "GetTaskResult" (id);

CREATE TABLE "Annotations_audience" (
	"Annotations_id" INTEGER,
	audience VARCHAR(9),
	PRIMARY KEY ("Annotations_id", audience),
	FOREIGN KEY("Annotations_id") REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_Annotations_audience_audience" ON "Annotations_audience" (audience);
CREATE INDEX "ix_Annotations_audience_Annotations_id" ON "Annotations_audience" ("Annotations_id");

CREATE TABLE "CompletionData_values" (
	"CompletionData_id" INTEGER,
	"values" TEXT NOT NULL,
	PRIMARY KEY ("CompletionData_id", "values"),
	FOREIGN KEY("CompletionData_id") REFERENCES "CompletionData" (id)
);
CREATE INDEX "ix_CompletionData_values_values" ON "CompletionData_values" ("values");
CREATE INDEX "ix_CompletionData_values_CompletionData_id" ON "CompletionData_values" ("CompletionData_id");

CREATE TABLE "SchemaItems_enum" (
	"SchemaItems_id" INTEGER,
	enum TEXT,
	PRIMARY KEY ("SchemaItems_id", enum),
	FOREIGN KEY("SchemaItems_id") REFERENCES "SchemaItems" (id)
);
CREATE INDEX "ix_SchemaItems_enum_enum" ON "SchemaItems_enum" (enum);
CREATE INDEX "ix_SchemaItems_enum_SchemaItems_id" ON "SchemaItems_enum" ("SchemaItems_id");

CREATE TABLE "SchemaItems_anyOf" (
	"SchemaItems_id" INTEGER,
	"anyOf_id" INTEGER,
	PRIMARY KEY ("SchemaItems_id", "anyOf_id"),
	FOREIGN KEY("SchemaItems_id") REFERENCES "SchemaItems" (id),
	FOREIGN KEY("anyOf_id") REFERENCES "EnumOption" (id)
);
CREATE INDEX "ix_SchemaItems_anyOf_SchemaItems_id" ON "SchemaItems_anyOf" ("SchemaItems_id");
CREATE INDEX "ix_SchemaItems_anyOf_anyOf_id" ON "SchemaItems_anyOf" ("anyOf_id");

CREATE TABLE "JsonSchema_required_list" (
	"JsonSchema_id" INTEGER,
	required_list TEXT,
	PRIMARY KEY ("JsonSchema_id", required_list),
	FOREIGN KEY("JsonSchema_id") REFERENCES "JsonSchema" (id)
);
CREATE INDEX "ix_JsonSchema_required_list_JsonSchema_id" ON "JsonSchema_required_list" ("JsonSchema_id");
CREATE INDEX "ix_JsonSchema_required_list_required_list" ON "JsonSchema_required_list" (required_list);

CREATE TABLE "JsonSchema_oneOf" (
	"JsonSchema_id" INTEGER,
	"oneOf_id" INTEGER,
	PRIMARY KEY ("JsonSchema_id", "oneOf_id"),
	FOREIGN KEY("JsonSchema_id") REFERENCES "JsonSchema" (id),
	FOREIGN KEY("oneOf_id") REFERENCES "EnumOption" (id)
);
CREATE INDEX "ix_JsonSchema_oneOf_JsonSchema_id" ON "JsonSchema_oneOf" ("JsonSchema_id");
CREATE INDEX "ix_JsonSchema_oneOf_oneOf_id" ON "JsonSchema_oneOf" ("oneOf_id");

CREATE TABLE "JsonSchema_anyOf" (
	"JsonSchema_id" INTEGER,
	"anyOf_id" INTEGER,
	PRIMARY KEY ("JsonSchema_id", "anyOf_id"),
	FOREIGN KEY("JsonSchema_id") REFERENCES "JsonSchema" (id),
	FOREIGN KEY("anyOf_id") REFERENCES "EnumOption" (id)
);
CREATE INDEX "ix_JsonSchema_anyOf_anyOf_id" ON "JsonSchema_anyOf" ("anyOf_id");
CREATE INDEX "ix_JsonSchema_anyOf_JsonSchema_id" ON "JsonSchema_anyOf" ("JsonSchema_id");

CREATE TABLE "JsonSchema_enum" (
	"JsonSchema_id" INTEGER,
	enum TEXT,
	PRIMARY KEY ("JsonSchema_id", enum),
	FOREIGN KEY("JsonSchema_id") REFERENCES "JsonSchema" (id)
);
CREATE INDEX "ix_JsonSchema_enum_enum" ON "JsonSchema_enum" (enum);
CREATE INDEX "ix_JsonSchema_enum_JsonSchema_id" ON "JsonSchema_enum" ("JsonSchema_id");

CREATE TABLE "ExtensionAppCapability_mimeTypes" (
	"ExtensionAppCapability_id" INTEGER,
	"mimeTypes" TEXT,
	PRIMARY KEY ("ExtensionAppCapability_id", "mimeTypes"),
	FOREIGN KEY("ExtensionAppCapability_id") REFERENCES "ExtensionAppCapability" (id)
);
CREATE INDEX "ix_ExtensionAppCapability_mimeTypes_ExtensionAppCapability_id" ON "ExtensionAppCapability_mimeTypes" ("ExtensionAppCapability_id");
CREATE INDEX "ix_ExtensionAppCapability_mimeTypes_mimeTypes" ON "ExtensionAppCapability_mimeTypes" ("mimeTypes");

CREATE TABLE "UntitledSingleSelectEnumSchema_enum" (
	"UntitledSingleSelectEnumSchema_id" INTEGER,
	enum TEXT,
	PRIMARY KEY ("UntitledSingleSelectEnumSchema_id", enum),
	FOREIGN KEY("UntitledSingleSelectEnumSchema_id") REFERENCES "UntitledSingleSelectEnumSchema" (id)
);
CREATE INDEX "ix_UntitledSingleSelectEnumSchema_enum_UntitledSingleSelectEnumSchema_id" ON "UntitledSingleSelectEnumSchema_enum" ("UntitledSingleSelectEnumSchema_id");
CREATE INDEX "ix_UntitledSingleSelectEnumSchema_enum_enum" ON "UntitledSingleSelectEnumSchema_enum" (enum);

CREATE TABLE "UntitledSingleSelectEnumSchema_enum_values" (
	"UntitledSingleSelectEnumSchema_id" INTEGER,
	enum_values TEXT,
	PRIMARY KEY ("UntitledSingleSelectEnumSchema_id", enum_values),
	FOREIGN KEY("UntitledSingleSelectEnumSchema_id") REFERENCES "UntitledSingleSelectEnumSchema" (id)
);
CREATE INDEX "ix_UntitledSingleSelectEnumSchema_enum_values_UntitledSingleSelectEnumSchema_id" ON "UntitledSingleSelectEnumSchema_enum_values" ("UntitledSingleSelectEnumSchema_id");
CREATE INDEX "ix_UntitledSingleSelectEnumSchema_enum_values_enum_values" ON "UntitledSingleSelectEnumSchema_enum_values" (enum_values);

CREATE TABLE "TitledSingleSelectEnumSchema_oneOf" (
	"TitledSingleSelectEnumSchema_id" INTEGER,
	"oneOf_id" INTEGER,
	PRIMARY KEY ("TitledSingleSelectEnumSchema_id", "oneOf_id"),
	FOREIGN KEY("TitledSingleSelectEnumSchema_id") REFERENCES "TitledSingleSelectEnumSchema" (id),
	FOREIGN KEY("oneOf_id") REFERENCES "EnumOption" (id)
);
CREATE INDEX "ix_TitledSingleSelectEnumSchema_oneOf_oneOf_id" ON "TitledSingleSelectEnumSchema_oneOf" ("oneOf_id");
CREATE INDEX "ix_TitledSingleSelectEnumSchema_oneOf_TitledSingleSelectEnumSchema_id" ON "TitledSingleSelectEnumSchema_oneOf" ("TitledSingleSelectEnumSchema_id");

CREATE TABLE "LegacyTitledEnumSchema_enum" (
	"LegacyTitledEnumSchema_id" INTEGER,
	enum TEXT,
	PRIMARY KEY ("LegacyTitledEnumSchema_id", enum),
	FOREIGN KEY("LegacyTitledEnumSchema_id") REFERENCES "LegacyTitledEnumSchema" (id)
);
CREATE INDEX "ix_LegacyTitledEnumSchema_enum_LegacyTitledEnumSchema_id" ON "LegacyTitledEnumSchema_enum" ("LegacyTitledEnumSchema_id");
CREATE INDEX "ix_LegacyTitledEnumSchema_enum_enum" ON "LegacyTitledEnumSchema_enum" (enum);

CREATE TABLE "LegacyTitledEnumSchema_enum_values" (
	"LegacyTitledEnumSchema_id" INTEGER,
	enum_values TEXT,
	PRIMARY KEY ("LegacyTitledEnumSchema_id", enum_values),
	FOREIGN KEY("LegacyTitledEnumSchema_id") REFERENCES "LegacyTitledEnumSchema" (id)
);
CREATE INDEX "ix_LegacyTitledEnumSchema_enum_values_LegacyTitledEnumSchema_id" ON "LegacyTitledEnumSchema_enum_values" ("LegacyTitledEnumSchema_id");
CREATE INDEX "ix_LegacyTitledEnumSchema_enum_values_enum_values" ON "LegacyTitledEnumSchema_enum_values" (enum_values);

CREATE TABLE "LegacyTitledEnumSchema_enumNames" (
	"LegacyTitledEnumSchema_id" INTEGER,
	"enumNames" TEXT,
	PRIMARY KEY ("LegacyTitledEnumSchema_id", "enumNames"),
	FOREIGN KEY("LegacyTitledEnumSchema_id") REFERENCES "LegacyTitledEnumSchema" (id)
);
CREATE INDEX "ix_LegacyTitledEnumSchema_enumNames_LegacyTitledEnumSchema_id" ON "LegacyTitledEnumSchema_enumNames" ("LegacyTitledEnumSchema_id");
CREATE INDEX "ix_LegacyTitledEnumSchema_enumNames_enumNames" ON "LegacyTitledEnumSchema_enumNames" ("enumNames");

CREATE TABLE "URLElicitationRequiredError" (
	uid INTEGER NOT NULL,
	id TEXT,
	jsonrpc TEXT NOT NULL,
	error_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(error_id) REFERENCES "Error" (id)
);
CREATE INDEX "ix_URLElicitationRequiredError_uid" ON "URLElicitationRequiredError" (uid);

CREATE TABLE "ResourceContents" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	"mimeType" TEXT,
	text TEXT,
	blob TEXT,
	"ReadResourceResult_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReadResourceResult_id") REFERENCES "ReadResourceResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_ResourceContents_id" ON "ResourceContents" (id);

CREATE TABLE "Resource" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	"mimeType" TEXT,
	description TEXT,
	size INTEGER,
	name TEXT NOT NULL,
	title TEXT,
	"ListResourcesResult_id" INTEGER,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ListResourcesResult_id") REFERENCES "ListResourcesResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "ResourceTemplate" (
	id INTEGER NOT NULL,
	"uriTemplate" TEXT NOT NULL,
	"mimeType" TEXT,
	description TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"ListResourceTemplatesResult_id" INTEGER,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ListResourceTemplatesResult_id") REFERENCES "ListResourceTemplatesResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_ResourceTemplate_id" ON "ResourceTemplate" (id);

CREATE TABLE "Root" (
	id INTEGER NOT NULL,
	uri TEXT NOT NULL,
	name TEXT,
	"ListRootsResult_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ListRootsResult_id") REFERENCES "ListRootsResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_Root_id" ON "Root" (id);

CREATE TABLE "Prompt" (
	id INTEGER NOT NULL,
	description TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"ListPromptsResult_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ListPromptsResult_id") REFERENCES "ListPromptsResult" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_Prompt_id" ON "Prompt" (id);

CREATE TABLE "PromptMessage" (
	id INTEGER NOT NULL,
	role VARCHAR(9) NOT NULL,
	"GetPromptResult_id" INTEGER,
	content_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("GetPromptResult_id") REFERENCES "GetPromptResult" (id),
	FOREIGN KEY(content_id) REFERENCES "ContentBlock" (id)
);
CREATE INDEX "ix_PromptMessage_id" ON "PromptMessage" (id);

CREATE TABLE "TasksCapability" (
	id INTEGER NOT NULL,
	requests_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(requests_id) REFERENCES "TaskRequestCapabilities" (id)
);
CREATE INDEX "ix_TasksCapability_id" ON "TasksCapability" (id);

CREATE TABLE "Tool" (
	id INTEGER NOT NULL,
	description TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"CreateMessageRequestParams_id" INTEGER,
	"ListToolsResult_id" INTEGER,
	annotations_id INTEGER,
	execution_id INTEGER,
	"inputSchema_id" INTEGER NOT NULL,
	"outputSchema_id" INTEGER,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CreateMessageRequestParams_id") REFERENCES "CreateMessageRequestParams" (id),
	FOREIGN KEY("ListToolsResult_id") REFERENCES "ListToolsResult" (id),
	FOREIGN KEY(annotations_id) REFERENCES "ToolAnnotations" (id),
	FOREIGN KEY(execution_id) REFERENCES "ToolExecution" (id),
	FOREIGN KEY("inputSchema_id") REFERENCES "JsonSchema" (id),
	FOREIGN KEY("outputSchema_id") REFERENCES "JsonSchema" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_Tool_id" ON "Tool" (id);

CREATE TABLE "SamplingMessage" (
	id INTEGER NOT NULL,
	role VARCHAR(9) NOT NULL,
	"CreateMessageRequestParams_id" INTEGER,
	content_id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CreateMessageRequestParams_id") REFERENCES "CreateMessageRequestParams" (id),
	FOREIGN KEY(content_id) REFERENCES "ContentBlock" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_SamplingMessage_id" ON "SamplingMessage" (id);

CREATE TABLE "Task" (
	id INTEGER NOT NULL,
	"taskId" TEXT NOT NULL,
	status VARCHAR(14) NOT NULL,
	"createdAt" TEXT NOT NULL,
	"lastUpdatedAt" TEXT NOT NULL,
	ttl INTEGER NOT NULL,
	"statusMessage" TEXT,
	"pollInterval" INTEGER,
	"ListTasksResult_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ListTasksResult_id") REFERENCES "ListTasksResult" (id)
);
CREATE INDEX "ix_Task_id" ON "Task" (id);

CREATE TABLE "JSONRPCErrorResponse" (
	uid INTEGER NOT NULL,
	id TEXT,
	jsonrpc TEXT NOT NULL,
	error_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(error_id) REFERENCES "Error" (id)
);
CREATE INDEX "ix_JSONRPCErrorResponse_uid" ON "JSONRPCErrorResponse" (uid);

CREATE TABLE "LoggingMessageNotificationParams" (
	id INTEGER NOT NULL,
	level VARCHAR(9) NOT NULL,
	logger TEXT,
	data_id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "LogData" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_LoggingMessageNotificationParams_id" ON "LoggingMessageNotificationParams" (id);

CREATE TABLE "CancelledNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "CancelledNotificationParams" (id)
);
CREATE INDEX "ix_CancelledNotification_id" ON "CancelledNotification" (id);

CREATE TABLE "ProgressNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "ProgressNotificationParams" (id)
);
CREATE INDEX "ix_ProgressNotification_id" ON "ProgressNotification" (id);

CREATE TABLE "ResourceUpdatedNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "ResourceUpdatedNotificationParams" (id)
);
CREATE INDEX "ix_ResourceUpdatedNotification_id" ON "ResourceUpdatedNotification" (id);

CREATE TABLE "TaskStatusNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "TaskStatusNotificationParams" (id)
);
CREATE INDEX "ix_TaskStatusNotification_id" ON "TaskStatusNotification" (id);

CREATE TABLE "CompleteRequestParams" (
	id INTEGER NOT NULL,
	argument_id INTEGER NOT NULL,
	context_id INTEGER,
	ref_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(argument_id) REFERENCES "CompletionArgument" (id),
	FOREIGN KEY(context_id) REFERENCES "CompletionContext" (id),
	FOREIGN KEY(ref_id) REFERENCES "PromptReference" (id)
);
CREATE INDEX "ix_CompleteRequestParams_id" ON "CompleteRequestParams" (id);

CREATE TABLE "GetPromptRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "GetPromptRequestParams" (id)
);
CREATE INDEX "ix_GetPromptRequest_uid" ON "GetPromptRequest" (uid);

CREATE TABLE "CallToolRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "CallToolRequestParams" (id)
);
CREATE INDEX "ix_CallToolRequest_uid" ON "CallToolRequest" (uid);

CREATE TABLE "CreateMessageRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "CreateMessageRequestParams" (id)
);
CREATE INDEX "ix_CreateMessageRequest_uid" ON "CreateMessageRequest" (uid);

CREATE TABLE "ElicitRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "ElicitRequestFormParams" (id)
);
CREATE INDEX "ix_ElicitRequest_uid" ON "ElicitRequest" (uid);

CREATE TABLE "CallToolResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "CallToolResult" (id)
);
CREATE INDEX "ix_CallToolResultResponse_uid" ON "CallToolResultResponse" (uid);

CREATE TABLE "CompleteResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "CompleteResult" (id)
);
CREATE INDEX "ix_CompleteResultResponse_uid" ON "CompleteResultResponse" (uid);

CREATE TABLE "GetPromptResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "GetPromptResult" (id)
);
CREATE INDEX "ix_GetPromptResultResponse_uid" ON "GetPromptResultResponse" (uid);

CREATE TABLE "ListPromptsResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ListPromptsResult" (id)
);
CREATE INDEX "ix_ListPromptsResultResponse_uid" ON "ListPromptsResultResponse" (uid);

CREATE TABLE "ListResourcesResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ListResourcesResult" (id)
);
CREATE INDEX "ix_ListResourcesResultResponse_uid" ON "ListResourcesResultResponse" (uid);

CREATE TABLE "ListResourceTemplatesResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ListResourceTemplatesResult" (id)
);
CREATE INDEX "ix_ListResourceTemplatesResultResponse_uid" ON "ListResourceTemplatesResultResponse" (uid);

CREATE TABLE "ReadResourceResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ReadResourceResult" (id)
);
CREATE INDEX "ix_ReadResourceResultResponse_uid" ON "ReadResourceResultResponse" (uid);

CREATE TABLE "ListToolsResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ListToolsResult" (id)
);
CREATE INDEX "ix_ListToolsResultResponse_uid" ON "ListToolsResultResponse" (uid);

CREATE TABLE "ListRootsResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ListRootsResult" (id)
);
CREATE INDEX "ix_ListRootsResultResponse_uid" ON "ListRootsResultResponse" (uid);

CREATE TABLE "CreateMessageResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "CreateMessageResult" (id)
);
CREATE INDEX "ix_CreateMessageResultResponse_uid" ON "CreateMessageResultResponse" (uid);

CREATE TABLE "ElicitResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ElicitResult" (id)
);
CREATE INDEX "ix_ElicitResultResponse_uid" ON "ElicitResultResponse" (uid);

CREATE TABLE "SetLevelResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "Result" (id)
);
CREATE INDEX "ix_SetLevelResultResponse_uid" ON "SetLevelResultResponse" (uid);

CREATE TABLE "PingResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "Result" (id)
);
CREATE INDEX "ix_PingResultResponse_uid" ON "PingResultResponse" (uid);

CREATE TABLE "SubscribeResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "Result" (id)
);
CREATE INDEX "ix_SubscribeResultResponse_uid" ON "SubscribeResultResponse" (uid);

CREATE TABLE "UnsubscribeResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "Result" (id)
);
CREATE INDEX "ix_UnsubscribeResultResponse_uid" ON "UnsubscribeResultResponse" (uid);

CREATE TABLE "GetTaskResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "GetTaskResult" (id)
);
CREATE INDEX "ix_GetTaskResultResponse_uid" ON "GetTaskResultResponse" (uid);

CREATE TABLE "GetTaskPayloadResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "GetTaskPayloadResult" (id)
);
CREATE INDEX "ix_GetTaskPayloadResultResponse_uid" ON "GetTaskPayloadResultResponse" (uid);

CREATE TABLE "CancelTaskResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "CancelTaskResult" (id)
);
CREATE INDEX "ix_CancelTaskResultResponse_uid" ON "CancelTaskResultResponse" (uid);

CREATE TABLE "ListTasksResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "ListTasksResult" (id)
);
CREATE INDEX "ix_ListTasksResultResponse_uid" ON "ListTasksResultResponse" (uid);

CREATE TABLE "ToolResultContent_content" (
	"ToolResultContent_id" INTEGER,
	content_id INTEGER NOT NULL,
	PRIMARY KEY ("ToolResultContent_id", content_id),
	FOREIGN KEY("ToolResultContent_id") REFERENCES "ToolResultContent" (id),
	FOREIGN KEY(content_id) REFERENCES "ContentBlock" (id)
);
CREATE INDEX "ix_ToolResultContent_content_content_id" ON "ToolResultContent_content" (content_id);
CREATE INDEX "ix_ToolResultContent_content_ToolResultContent_id" ON "ToolResultContent_content" ("ToolResultContent_id");

CREATE TABLE "UntitledMultiSelectEnumSchema_default" (
	"UntitledMultiSelectEnumSchema_id" INTEGER,
	"default" TEXT,
	PRIMARY KEY ("UntitledMultiSelectEnumSchema_id", "default"),
	FOREIGN KEY("UntitledMultiSelectEnumSchema_id") REFERENCES "UntitledMultiSelectEnumSchema" (id)
);
CREATE INDEX "ix_UntitledMultiSelectEnumSchema_default_UntitledMultiSelectEnumSchema_id" ON "UntitledMultiSelectEnumSchema_default" ("UntitledMultiSelectEnumSchema_id");
CREATE INDEX "ix_UntitledMultiSelectEnumSchema_default_default" ON "UntitledMultiSelectEnumSchema_default" ("default");

CREATE TABLE "TitledMultiSelectEnumSchema_default" (
	"TitledMultiSelectEnumSchema_id" INTEGER,
	"default" TEXT,
	PRIMARY KEY ("TitledMultiSelectEnumSchema_id", "default"),
	FOREIGN KEY("TitledMultiSelectEnumSchema_id") REFERENCES "TitledMultiSelectEnumSchema" (id)
);
CREATE INDEX "ix_TitledMultiSelectEnumSchema_default_TitledMultiSelectEnumSchema_id" ON "TitledMultiSelectEnumSchema_default" ("TitledMultiSelectEnumSchema_id");
CREATE INDEX "ix_TitledMultiSelectEnumSchema_default_default" ON "TitledMultiSelectEnumSchema_default" ("default");

CREATE TABLE "CreateMessageRequestParams_stopSequences" (
	"CreateMessageRequestParams_id" INTEGER,
	"stopSequences" TEXT,
	PRIMARY KEY ("CreateMessageRequestParams_id", "stopSequences"),
	FOREIGN KEY("CreateMessageRequestParams_id") REFERENCES "CreateMessageRequestParams" (id)
);
CREATE INDEX "ix_CreateMessageRequestParams_stopSequences_CreateMessageRequestParams_id" ON "CreateMessageRequestParams_stopSequences" ("CreateMessageRequestParams_id");
CREATE INDEX "ix_CreateMessageRequestParams_stopSequences_stopSequences" ON "CreateMessageRequestParams_stopSequences" ("stopSequences");

CREATE TABLE "CallToolResult_content" (
	"CallToolResult_id" INTEGER,
	content_id INTEGER NOT NULL,
	PRIMARY KEY ("CallToolResult_id", content_id),
	FOREIGN KEY("CallToolResult_id") REFERENCES "CallToolResult" (id),
	FOREIGN KEY(content_id) REFERENCES "ContentBlock" (id)
);
CREATE INDEX "ix_CallToolResult_content_content_id" ON "CallToolResult_content" (content_id);
CREATE INDEX "ix_CallToolResult_content_CallToolResult_id" ON "CallToolResult_content" ("CallToolResult_id");

CREATE TABLE "Icon" (
	id INTEGER NOT NULL,
	src TEXT NOT NULL,
	"mimeType" TEXT,
	theme VARCHAR(5),
	"HasIcons_id" INTEGER,
	"Implementation_id" INTEGER,
	"ResourceLink_id" INTEGER,
	"Resource_id" INTEGER,
	"ResourceTemplate_id" INTEGER,
	"Prompt_id" INTEGER,
	"Tool_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("HasIcons_id") REFERENCES "HasIcons" (id),
	FOREIGN KEY("Implementation_id") REFERENCES "Implementation" (id),
	FOREIGN KEY("ResourceLink_id") REFERENCES "ResourceLink" (id),
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id),
	FOREIGN KEY("ResourceTemplate_id") REFERENCES "ResourceTemplate" (id),
	FOREIGN KEY("Prompt_id") REFERENCES "Prompt" (id),
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id)
);
CREATE INDEX "ix_Icon_id" ON "Icon" (id);

CREATE TABLE "EmbeddedResource" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	resource_id INTEGER NOT NULL,
	_meta_id INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(resource_id) REFERENCES "ResourceContents" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Annotations" (id)
);
CREATE INDEX "ix_EmbeddedResource_id" ON "EmbeddedResource" (id);

CREATE TABLE "PromptArgument" (
	id INTEGER NOT NULL,
	description TEXT,
	required BOOLEAN,
	required_field BOOLEAN,
	name TEXT NOT NULL,
	title TEXT,
	"Prompt_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Prompt_id") REFERENCES "Prompt" (id)
);
CREATE INDEX "ix_PromptArgument_id" ON "PromptArgument" (id);

CREATE TABLE "ClientCapabilities" (
	id INTEGER NOT NULL,
	experimental TEXT,
	elicitation_id INTEGER,
	extensions_id INTEGER,
	roots_id INTEGER,
	sampling_id INTEGER,
	tasks_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(elicitation_id) REFERENCES "ElicitationCapability" (id),
	FOREIGN KEY(extensions_id) REFERENCES "ExtensionsCapability" (id),
	FOREIGN KEY(roots_id) REFERENCES "RootsCapability" (id),
	FOREIGN KEY(sampling_id) REFERENCES "SamplingCapability" (id),
	FOREIGN KEY(tasks_id) REFERENCES "TasksCapability" (id)
);
CREATE INDEX "ix_ClientCapabilities_id" ON "ClientCapabilities" (id);

CREATE TABLE "ServerCapabilities" (
	id INTEGER NOT NULL,
	experimental TEXT,
	extensions_id INTEGER,
	prompts_id INTEGER,
	resources_id INTEGER,
	tools_id INTEGER,
	tasks_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(extensions_id) REFERENCES "ExtensionsCapability" (id),
	FOREIGN KEY(prompts_id) REFERENCES "PromptsCapability" (id),
	FOREIGN KEY(resources_id) REFERENCES "ResourcesCapability" (id),
	FOREIGN KEY(tools_id) REFERENCES "ToolsCapability" (id),
	FOREIGN KEY(tasks_id) REFERENCES "TasksCapability" (id)
);
CREATE INDEX "ix_ServerCapabilities_id" ON "ServerCapabilities" (id);

CREATE TABLE "LoggingMessageNotification" (
	id INTEGER NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "LoggingMessageNotificationParams" (id)
);
CREATE INDEX "ix_LoggingMessageNotification_id" ON "LoggingMessageNotification" (id);

CREATE TABLE "CompleteRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "CompleteRequestParams" (id)
);
CREATE INDEX "ix_CompleteRequest_uid" ON "CompleteRequest" (uid);

CREATE TABLE "CreateTaskResult" (
	id INTEGER NOT NULL,
	task_id INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(task_id) REFERENCES "Task" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_CreateTaskResult_id" ON "CreateTaskResult" (id);

CREATE TABLE "InitializeRequestParams" (
	id INTEGER NOT NULL,
	"protocolVersion" TEXT NOT NULL,
	capabilities_id INTEGER NOT NULL,
	"clientInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(capabilities_id) REFERENCES "ClientCapabilities" (id),
	FOREIGN KEY("clientInfo_id") REFERENCES "Implementation" (id)
);
CREATE INDEX "ix_InitializeRequestParams_id" ON "InitializeRequestParams" (id);

CREATE TABLE "InitializeResult" (
	id INTEGER NOT NULL,
	"protocolVersion" TEXT NOT NULL,
	instructions TEXT,
	capabilities_id INTEGER NOT NULL,
	"serverInfo_id" INTEGER NOT NULL,
	_meta_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(capabilities_id) REFERENCES "ServerCapabilities" (id),
	FOREIGN KEY("serverInfo_id") REFERENCES "Implementation" (id),
	FOREIGN KEY(_meta_id) REFERENCES "MetaObject" (id)
);
CREATE INDEX "ix_InitializeResult_id" ON "InitializeResult" (id);

CREATE TABLE "CreateTaskResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "CreateTaskResult" (id)
);
CREATE INDEX "ix_CreateTaskResultResponse_uid" ON "CreateTaskResultResponse" (uid);

CREATE TABLE "Icon_sizes" (
	"Icon_id" INTEGER,
	sizes TEXT,
	PRIMARY KEY ("Icon_id", sizes),
	FOREIGN KEY("Icon_id") REFERENCES "Icon" (id)
);
CREATE INDEX "ix_Icon_sizes_sizes" ON "Icon_sizes" (sizes);
CREATE INDEX "ix_Icon_sizes_Icon_id" ON "Icon_sizes" ("Icon_id");

CREATE TABLE "InitializeRequest" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(params_id) REFERENCES "InitializeRequestParams" (id)
);
CREATE INDEX "ix_InitializeRequest_uid" ON "InitializeRequest" (uid);

CREATE TABLE "InitializeResultResponse" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	jsonrpc TEXT NOT NULL,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(result_id) REFERENCES "InitializeResult" (id)
);
CREATE INDEX "ix_InitializeResultResponse_uid" ON "InitializeResultResponse" (uid);
