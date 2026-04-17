/**
* The sender or recipient of messages and data in a conversation.
*/
export enum Role {
    
    /** The assistant role. */
    assistant = "assistant",
    /** The user role. */
    user = "user",
};
/**
* The severity of a log message. Maps to syslog message severities (RFC-5424).
*/
export enum LoggingLevel {
    
    /** Alert severity. */
    alert = "alert",
    /** Critical severity. */
    critical = "critical",
    /** Debug severity. */
    debug = "debug",
    /** Emergency severity. */
    emergency = "emergency",
    /** Error severity. */
    error = "error",
    /** Informational severity. */
    info = "info",
    /** Notice severity. */
    notice = "notice",
    /** Warning severity. */
    warning = "warning",
};
/**
* The status of a task.
*/
export enum TaskStatusEnum {
    
    /** Task was cancelled. */
    cancelled = "cancelled",
    /** Task completed successfully. */
    completed = "completed",
    /** Task failed. */
    failed = "failed",
    /** Task requires additional input. */
    input_required = "input_required",
    /** Task is currently in progress. */
    working = "working",
};
/**
* Context inclusion mode for sampling requests.
*/
export enum IncludeContextEnum {
    
    /** Include context from all servers. */
    allServers = "allServers",
    /** Include no context. */
    none = "none",
    /** Include context from calling server only. */
    thisServer = "thisServer",
};
/**
* User action in response to an elicitation.
*/
export enum ElicitActionEnum {
    
    /** User submitted the form/confirmed the action. */
    accept = "accept",
    /** User dismissed without making an explicit choice. */
    cancel = "cancel",
    /** User explicitly declined the action. */
    decline = "decline",
};
/**
* Controls tool selection behavior for sampling requests.
*/
export enum ToolChoiceModeEnum {
    
    /** Model decides whether to use tools (default). */
    auto = "auto",
    /** Model MUST NOT use any tools. */
    none = "none",
    /** Model MUST use at least one tool before completing. */
    required = "required",
};
/**
* Indicates whether a tool supports task-augmented execution.
*/
export enum TaskSupportEnum {
    
    /** Tool does not support task-augmented execution (default). */
    forbidden = "forbidden",
    /** Tool may support task-augmented execution. */
    optional = "optional",
    /** Tool requires task-augmented execution. */
    required = "required",
};
/**
* Theme specifier for an icon.
*/
export enum IconThemeEnum {
    
    /** Icon designed for a dark background. */
    dark = "dark",
    /** Icon designed for a light background. */
    light = "light",
};
/**
* Number type discriminator.
*/
export enum NumberTypeEnum {
    
    /** Integer type. */
    integer = "integer",
    /** Number type. */
    number = "number",
};
/**
* String format constraints.
*/
export enum StringFormatEnum {
    
    /** Date format. */
    date = "date",
    /** Date-time format. */
    date_time = "date-time",
    /** Email format. */
    email = "email",
    /** URI format. */
    uri = "uri",
};


/**
 * Mixin for types that carry a _meta field.
 */
export interface HasMeta {
    /** Optional metadata object. */
    _meta?: MetaObject,
}


/**
 * Mixin for types that carry annotations.
 */
export interface HasAnnotations {
    /** Optional annotations for the client. */
    annotations?: Annotations,
}


/**
 * Mixin for types that carry icons.
 */
export interface HasIcons {
    /** Optional set of sized icons that the client can display in a user interface. */
    icons?: Icon[],
}


/**
 * Mixin for types that carry name and title.
 */
export interface HasName {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * Optional annotations for the client. The client can use annotations to inform how objects are used or displayed.
 */
export interface Annotations {
    /** Describes who the intended audience of this object or data is. */
    audience?: string,
    /** The moment the resource was last modified, as an ISO 8601 formatted string. */
    lastModified?: string,
    /** How important this data is for operating the server. 1 means most important (required), 0 means least important (optional). */
    priority?: number,
}


/**
 * A JSON-RPC error object.
 */
export interface Error {
    /** The error type that occurred. */
    code: number,
    /** Base64-encoded binary data. */
    data?: ErrorData,
    /** A message string. */
    message: string,
}


/**
 * A JSON-RPC error indicating that an internal error occurred on the receiver (-32603).
 */
export interface InternalError extends Error {
}


/**
 * A JSON-RPC error indicating that the method parameters are invalid or malformed (-32602).
 */
export interface InvalidParamsError extends Error {
}


/**
 * A JSON-RPC error indicating that the request is not a valid request object (-32600).
 */
export interface InvalidRequestError extends Error {
}


/**
 * A JSON-RPC error indicating that the requested method does not exist or is not available (-32601).
 */
export interface MethodNotFoundError extends Error {
}


/**
 * A JSON-RPC error indicating that invalid JSON was received by the server (-32700).
 */
export interface ParseError extends Error {
}


/**
 * A response indicating that additional information is required via URL elicitation.
 */
export interface URLElicitationRequiredError extends JSONRPCErrorResponse {
}


/**
 * An optionally-sized icon that can be displayed in a user interface.
 */
export interface Icon {
    /** A standard URI pointing to an icon resource. */
    src: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** Optional array of strings specifying sizes (WxH format or "any"). */
    sizes?: string[],
    /** Optional theme specifier for the icon. */
    theme?: string,
}


/**
 * Describes the MCP implementation.
 */
export interface Implementation extends HasName, HasIcons {
    /** The version of this implementation. */
    version: string,
    /** A human-readable description. */
    description?: string,
    /** An optional URL of the website for this implementation. */
    websiteUrl?: string,
}


/**
 * Text provided to or from an LLM.
 */
export interface TextContent extends HasMeta, HasAnnotations {
    /** Text content. */
    text: string,
    /** Type discriminator field. */
    type: string,
}


/**
 * An image provided to or from an LLM.
 */
export interface ImageContent extends HasMeta, HasAnnotations {
    /** Base64-encoded binary data. */
    data: string,
    /** The MIME type of a resource, if known. */
    mimeType: string,
    /** Type discriminator field. */
    type: string,
}


/**
 * Audio provided to or from an LLM.
 */
export interface AudioContent extends HasMeta, HasAnnotations {
    /** Base64-encoded binary data. */
    data: string,
    /** The MIME type of a resource, if known. */
    mimeType: string,
    /** Type discriminator field. */
    type: string,
}


/**
 * Structured text content block.
 */
export interface ContentBlock {
    /** Type discriminator field. */
    type?: string,
    /** Text content. */
    text?: string,
}


/**
 * The contents of a resource, embedded into a prompt or tool call result.
 */
export interface EmbeddedResource extends HasMeta, HasAnnotations {
    /** Type discriminator field. */
    type: string,
    /** The embedded resource contents (text or blob). */
    resource: ResourceContents,
}


/**
 * A resource that the server is capable of reading, included in a prompt or tool call result.
 */
export interface ResourceLink extends HasMeta, HasAnnotations, HasName, HasIcons {
    /** A resource URI. */
    uri: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** A human-readable description. */
    description?: string,
    /** The size of the raw resource content, in bytes. */
    size?: number,
    /** Type discriminator field. */
    type: string,
}


/**
 * A request from the assistant to call a tool.
 */
export interface ToolUseContent extends HasMeta {
    /** A unique identifier for this tool use. */
    id: string,
    /** Type discriminator field. */
    type: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name: string,
    /** The arguments to pass to the tool. */
    input: ToolInput,
}


/**
 * The result of a tool use, provided by the user back to the assistant.
 */
export interface ToolResultContent extends HasMeta {
    /** The unstructured result content of the tool use. */
    content: ContentBlock[],
    /** Type discriminator field. */
    type: string,
    /** The ID of the tool use this result corresponds to. */
    toolUseId: string,
    /** Whether the tool call ended in an error. */
    isError?: boolean,
    /** An optional JSON object representing structured result of the tool call. */
    structuredContent?: StructuredContentData,
}


/**
 * Generic resource contents.
 */
export interface ResourceContents extends HasMeta {
    /** A resource URI. */
    uri: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** Text content. */
    text?: string,
    /** A base64-encoded string representing binary data. */
    blob?: string,
}


/**
 * Text resource contents.
 */
export interface TextResourceContents extends HasMeta {
    /** A resource URI. */
    uri: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** Text content. */
    text: string,
}


/**
 * Blob resource contents.
 */
export interface BlobResourceContents extends HasMeta {
    /** A resource URI. */
    uri: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** A base64-encoded string representing binary data. */
    blob: string,
}


/**
 * A known resource that the server is capable of reading.
 */
export interface Resource extends HasMeta, HasAnnotations, HasName, HasIcons {
    /** A resource URI. */
    uri: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** A human-readable description. */
    description?: string,
    /** The size of the raw resource content, in bytes. */
    size?: number,
}


/**
 * A template description for resources available on the server.
 */
export interface ResourceTemplate extends HasMeta, HasAnnotations, HasName, HasIcons {
    /** A URI template (RFC 6570) for constructing resource URIs. */
    uriTemplate: string,
    /** The MIME type of a resource, if known. */
    mimeType?: string,
    /** A human-readable description. */
    description?: string,
}


/**
 * Represents a root directory or file that the server can operate on.
 */
export interface Root extends HasMeta {
    /** A resource URI. */
    uri: string,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name?: string,
}


/**
 * Describes an argument that a prompt can accept.
 */
export interface PromptArgument extends HasName {
    /** A human-readable description. */
    description?: string,
    /** Whether this argument must be provided. */
    required?: boolean,
    /** Whether this argument must be provided. */
    required_field?: boolean,
}


/**
 * A prompt or prompt template that the server offers.
 */
export interface Prompt extends HasMeta, HasName, HasIcons {
    /** A list of arguments to use for templating the prompt. */
    arguments?: PromptArgument[],
    /** A human-readable description. */
    description?: string,
}


/**
 * Describes a message returned as part of a prompt.
 */
export interface PromptMessage {
    /** The content of the prompt message. */
    content: ContentBlock,
    /** The role of the sender or recipient. */
    role: string,
}


/**
 * Identifies a prompt.
 */
export interface PromptReference extends HasName {
    /** Type discriminator field. */
    type: string,
}


/**
 * A reference to a resource or resource template definition.
 */
export interface ResourceTemplateReference {
    /** Type discriminator field. */
    type: string,
    /** A resource URI. */
    uri: string,
}


/**
 * Additional properties describing a Tool to clients. All properties are hints, not guarantees.
 */
export interface ToolAnnotations {
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
    /** If true, the tool may perform destructive updates. */
    destructiveHint?: boolean,
    /** If true, calling repeatedly with same arguments has no additional effect. */
    idempotentHint?: boolean,
    /** If true, tool may interact with an open world of external entities. */
    openWorldHint?: boolean,
    /** If true, the tool does not modify its environment. */
    readOnlyHint?: boolean,
}


/**
 * Controls tool selection behavior for sampling requests.
 */
export interface ToolChoice {
    /** Controls the tool use ability of the model. */
    mode?: string,
}


/**
 * Execution-related properties for a tool.
 */
export interface ToolExecution {
    /** Whether this tool supports task-augmented execution. */
    taskSupport?: string,
}


/**
 * Metadata object attached to protocol objects.
 */
export interface MetaObject {
    /** The progress token which was given in the initial request, used to associate this notification with the request that is proceeding. */
    progressToken?: string,
}


/**
 * Argument object used in prompt and tool calls.
 */
export interface ArgumentMap {
    /** City value. */
    city?: string,
    /** Location value. */
    location?: string,
    /** Programming language value. */
    language?: string,
    /** Framework value. */
    framework?: string,
}


/**
 * Argument descriptor for completion requests.
 */
export interface CompletionArgument {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name: string,
    /** A value string. */
    value: string,
}


/**
 * Additional context for completion requests.
 */
export interface CompletionContext {
    /** Arguments for templating. */
    arguments?: ArgumentMap,
}


/**
 * Completion result payload.
 */
export interface CompletionData {
    /** An array of completion values. */
    values: string[],
    /** Total number of items to process (or total progress required), if known. */
    total?: number,
    /** Indicates whether there are additional completion options. */
    hasMore?: boolean,
}


/**
 * Single enumerated option with a machine value and display title.
 */
export interface EnumOption {
    /** JSON Schema const value. */
    const: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * JSON Schema items expression used by enum multi-select schemas.
 */
export interface SchemaItems {
    /** Type discriminator field. */
    type?: string,
    /** Array of enum values. */
    enum?: string[],
    /** JSON Schema anyOf entries. */
    anyOf?: EnumOption[],
}


/**
 * Restricted JSON Schema object used in MCP payloads.
 */
export interface JsonSchema {
    /** Optional JSON Schema dialect identifier. */
    schemaUri?: string,
    /** Type discriminator field. */
    type?: string,
    /** JSON Schema properties map. */
    properties?: SchemaProperties,
    /** JSON Schema required property list. */
    required_list?: string[],
    /** JSON Schema additionalProperties flag. */
    additionalProperties?: boolean,
    /** Minimum value constraint. */
    minimum?: number,
    /** Maximum value constraint. */
    maximum?: number,
    /** Minimum length constraint. */
    minLength?: number,
    /** Maximum length constraint. */
    maxLength?: number,
    /** String format constraint. */
    format?: string,
    /** A human-readable description. */
    description?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
    /** JSON Schema oneOf entries. */
    oneOf?: EnumOption[],
    /** JSON Schema anyOf entries. */
    anyOf?: EnumOption[],
    /** JSON Schema items definition. */
    items?: SchemaItems,
    /** Array of enum values. */
    enum?: string[],
    /** JSON Schema const value. */
    const?: string,
    /** Default value for a schema field. */
    default?: string,
}


/**
 * Named JSON Schema property map used by vendor fixtures.
 */
export interface SchemaProperties {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name?: JsonSchema,
    /** Email value. */
    email?: JsonSchema,
    /** Age value. */
    age?: JsonSchema,
    /** City value. */
    city?: JsonSchema,
    /** Location value. */
    location?: JsonSchema,
    /** JSON Schema property for key a. */
    a?: JsonSchema,
    /** JSON Schema property for key b. */
    b?: JsonSchema,
    /** Sampling temperature. */
    temperature?: JsonSchema,
    /** Weather conditions description. */
    conditions?: JsonSchema,
    /** Humidity percentage value. */
    humidity?: JsonSchema,
}


/**
 * Tool input payload.
 */
export interface ToolInput {
    /** City value. */
    city?: string,
    /** Location value. */
    location?: string,
}


/**
 * Structured content object returned by tools.
 */
export interface StructuredContentData {
    /** Sampling temperature. */
    temperature?: number,
    /** Weather conditions description. */
    conditions?: string,
    /** Humidity percentage value. */
    humidity?: number,
}


/**
 * Structured details attached to log data.
 */
export interface LogDetails {
    /** Host value. */
    host?: string,
    /** Port value. */
    port?: number,
}


/**
 * Structured log data payload.
 */
export interface LogData {
    /** The error object. */
    error?: string,
    /** Nested log details object. */
    details?: LogDetails,
}


/**
 * Structured JSON-RPC error data payload.
 */
export interface ErrorData {
    /** An optional string describing the reason. */
    reason?: string,
    /** URL elicitation entries included in error data. */
    elicitations?: URLElicitation[],
}


/**
 * Form values returned by an elicitation.
 */
export interface ElicitationContent {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name?: string,
    /** Email value. */
    email?: string,
    /** Age value. */
    age?: number,
}


/**
 * URL-based elicitation request payload carried in error data.
 */
export interface URLElicitation {
    /** The elicitation mode. */
    mode?: string,
    /** The ID of the elicitation. */
    elicitationId?: string,
    /** A message string. */
    message?: string,
    /** The URL that the user should navigate to. */
    url?: string,
}


/**
 * Client elicitation capability.
 */
export interface ElicitationCapability {
}


/**
 * Client sampling capability.
 */
export interface SamplingCapability {
}


/**
 * Client roots capability.
 */
export interface RootsCapability {
    /** Whether notifications for list changes are supported. */
    listChanged?: boolean,
}


/**
 * Server prompts capability.
 */
export interface PromptsCapability {
    /** Whether notifications for list changes are supported. */
    listChanged?: boolean,
}


/**
 * Server resources capability.
 */
export interface ResourcesCapability {
    /** Whether notifications for list changes are supported. */
    listChanged?: boolean,
    /** Whether subscribing to resource updates is supported. */
    subscribe?: boolean,
}


/**
 * Server tools capability.
 */
export interface ToolsCapability {
    /** Whether notifications for list changes are supported. */
    listChanged?: boolean,
}


/**
 * Task request capability map.
 */
export interface TaskRequestCapabilities {
    /** Elicitation capability object. */
    elicitation?: ElicitationCapability,
    /** Sampling capability object. */
    sampling?: SamplingCapability,
    /** The list of tools. */
    tools?: ToolsCapability,
}


/**
 * Task capability object.
 */
export interface TasksCapability {
    /** Task request capabilities. */
    requests?: TaskRequestCapabilities,
}


/**
 * Server/client extension capability object.
 */
export interface ExtensionsCapability {
    /** Extension capability entry for app mime types. */
    apps_extension?: ExtensionAppCapability,
}


/**
 * Extension payload for app mime type declarations.
 */
export interface ExtensionAppCapability {
    /** MIME types supported by an extension capability. */
    mimeTypes?: string[],
}


/**
 * Definition for a tool the client can call.
 */
export interface Tool extends HasMeta, HasName, HasIcons {
    /** Optional additional tool information. */
    annotations?: ToolAnnotations,
    /** Execution-related properties for this tool. */
    execution?: ToolExecution,
    /** A human-readable description. */
    description?: string,
    /** A JSON Schema object defining the expected parameters for the tool. */
    inputSchema: JsonSchema,
    /** An optional JSON Schema object defining the structure of the tool's output. */
    outputSchema?: JsonSchema,
}


/**
 * Hints to use for model selection.
 */
export interface ModelHint {
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name?: string,
}


/**
 * The server's preferences for model selection, requested of the client during sampling.
 */
export interface ModelPreferences {
    /** How much to prioritize cost when selecting a model (0-1). */
    costPriority?: number,
    /** How much to prioritize intelligence when selecting a model (0-1). */
    intelligencePriority?: number,
    /** How much to prioritize sampling speed when selecting a model (0-1). */
    speedPriority?: number,
    /** Optional hints to use for model selection. */
    hints?: ModelHint[],
}


/**
 * Describes a message issued to or received from an LLM API.
 */
export interface SamplingMessage extends HasMeta {
    /** The message content. */
    content: ContentBlock,
    /** The role of the sender or recipient. */
    role: string,
}


/**
 * Data associated with a task.
 */
export interface Task {
    /** The task identifier. */
    taskId: string,
    /** Current task state. */
    status: string,
    /** ISO 8601 timestamp when the task was created. */
    createdAt: string,
    /** ISO 8601 timestamp when the task was last updated. */
    lastUpdatedAt: string,
    /** Actual retention duration from creation in milliseconds, null for unlimited. */
    ttl: number,
    /** Optional human-readable message describing the current task state. */
    statusMessage?: string,
    /** Suggested polling interval in milliseconds. */
    pollInterval?: number,
}


/**
 * Metadata for augmenting a request with task execution.
 */
export interface TaskMetadata {
    /** Actual retention duration from creation in milliseconds, null for unlimited. */
    ttl?: number,
}


/**
 * Metadata for associating messages with a task.
 */
export interface RelatedTaskMetadata {
    /** The task identifier. */
    taskId: string,
}


/**
 * Capabilities a client may support. Known capabilities are defined here, but this is not a closed set.
 */
export interface ClientCapabilities {
    /** Elicitation capability object. */
    elicitation?: ElicitationCapability,
    /** Experimental capability extensions. */
    experimental?: string,
    /** Implementation-specific extension capabilities. */
    extensions?: ExtensionsCapability,
    /** The list of roots. */
    roots?: RootsCapability,
    /** Sampling capability object. */
    sampling?: SamplingCapability,
    /** The list of tasks. */
    tasks?: TasksCapability,
}


/**
 * Capabilities that a server may support. Known capabilities are defined here, but this is not a closed set.
 */
export interface ServerCapabilities {
    /** Experimental capability extensions. */
    experimental?: string,
    /** Implementation-specific extension capabilities. */
    extensions?: ExtensionsCapability,
    /** The list of prompts. */
    prompts?: PromptsCapability,
    /** The list of resources. */
    resources?: ResourcesCapability,
    /** The list of tools. */
    tools?: ToolsCapability,
    /** The list of tasks. */
    tasks?: TasksCapability,
}


/**
 * String schema definition.
 */
export interface StringSchema {
    /** Type discriminator field. */
    type: string,
    /** Default value for a schema field. */
    default?: string,
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** String format constraint. */
    format?: string,
    /** Minimum length constraint. */
    minLength?: number,
    /** Maximum length constraint. */
    maxLength?: number,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * Number schema definition.
 */
export interface NumberSchema {
    /** Type discriminator field. */
    type: string,
    /** Default value for a schema field. */
    default?: number,
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** Minimum value constraint. */
    minimum?: number,
    /** Maximum value constraint. */
    maximum?: number,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * Boolean schema definition.
 */
export interface BooleanSchema {
    /** Type discriminator field. */
    type: string,
    /** Default value for a schema field. */
    default?: boolean,
    /** Default boolean value. */
    default_value?: boolean,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
    /** A human-readable description. */
    description?: string,
}


/**
 * Single-selection enum without display titles.
 */
export interface UntitledSingleSelectEnumSchema {
    /** Type discriminator field. */
    type: string,
    /** Array of enum values. */
    enum?: string[],
    /** Array of enum values. */
    enum_values?: string[],
    /** Default value for a schema field. */
    default?: string,
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * Single-selection enum with display titles for each option.
 */
export interface TitledSingleSelectEnumSchema {
    /** Type discriminator field. */
    type: string,
    /** JSON Schema oneOf entries. */
    oneOf?: EnumOption[],
    /** Default value for a schema field. */
    default?: string,
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * Multi-selection enum without display titles.
 */
export interface UntitledMultiSelectEnumSchema {
    /** Type discriminator field. */
    type: string,
    /** JSON Schema items definition. */
    items?: SchemaItems,
    /** Default value for a schema field. */
    default?: string[],
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
    /** Minimum number of items. */
    minItems?: number,
    /** Maximum number of items. */
    maxItems?: number,
}


/**
 * Multi-selection enum with display titles for each option.
 */
export interface TitledMultiSelectEnumSchema {
    /** Type discriminator field. */
    type: string,
    /** JSON Schema items definition. */
    items?: SchemaItems,
    /** Default value for a schema field. */
    default?: string[],
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
    /** Minimum number of items. */
    minItems?: number,
    /** Maximum number of items. */
    maxItems?: number,
}


/**
 * Legacy titled enum schema. Use TitledSingleSelectEnumSchema instead.
 */
export interface LegacyTitledEnumSchema {
    /** Type discriminator field. */
    type: string,
    /** Array of enum values. */
    enum?: string[],
    /** Array of enum values. */
    enum_values?: string[],
    /** Display names for enum values (legacy). */
    enumNames?: string[],
    /** Default value for a schema field. */
    default?: string,
    /** Default value for a schema field. */
    default_value?: string,
    /** A human-readable description. */
    description?: string,
    /** Intended for UI and end-user contexts — optimized to be human-readable and easily understood. */
    title?: string,
}


/**
 * A request that expects a response.
 */
export interface JSONRPCRequest {
    /** Uniquely identifying ID for a JSON-RPC request. */
    id: string,
    /** JSON-RPC version string. */
    jsonrpc: string,
    /** The JSON-RPC method name. */
    method: string,
}


/**
 * A notification which does not expect a response.
 */
export interface JSONRPCNotification {
    /** JSON-RPC version string. */
    jsonrpc: string,
    /** The JSON-RPC method name. */
    method: string,
}


/**
 * A successful (non-error) response to a request.
 */
export interface JSONRPCResultResponse {
    /** Uniquely identifying ID for a JSON-RPC request. */
    id: string,
    /** JSON-RPC version string. */
    jsonrpc: string,
}


/**
 * A response to a request that indicates an error occurred.
 */
export interface JSONRPCErrorResponse {
    /** Uniquely identifying ID for a JSON-RPC request. */
    id?: string,
    /** JSON-RPC version string. */
    jsonrpc: string,
    /** The error object. */
    error: Error,
}


/**
 * Common result fields.
 */
export interface Result extends HasMeta {
}


/**
 * Parameters for a notifications/cancelled notification.
 */
export interface CancelledNotificationParams extends HasMeta {
    /** The ID of a request. */
    requestId?: string,
    /** An optional string describing the reason. */
    reason?: string,
}


/**
 * Parameters for a notifications/progress notification.
 */
export interface ProgressNotificationParams extends HasMeta {
    /** The progress thus far. */
    progress: number,
    /** The progress token which was given in the initial request, used to associate this notification with the request that is proceeding. */
    progressToken: string,
    /** Total number of items to process (or total progress required), if known. */
    total?: number,
    /** A message string. */
    message?: string,
}


/**
 * Parameters for a notifications/elicitation/complete notification.
 */
export interface ElicitationCompleteNotificationParams {
    /** The ID of the elicitation. */
    elicitationId: string,
}


/**
 * Parameters for a notifications/message notification.
 */
export interface LoggingMessageNotificationParams extends HasMeta {
    /** The data to be logged. */
    data: LogData,
    /** The severity of a log message. */
    level: string,
    /** An optional name of the logger issuing this message. */
    logger?: string,
}


/**
 * Parameters for a notifications/resources/updated notification.
 */
export interface ResourceUpdatedNotificationParams extends HasMeta {
    /** A resource URI. */
    uri: string,
}


/**
 * Parameters for a notifications/tasks/status notification.
 */
export interface TaskStatusNotificationParams extends HasMeta {
    /** The task identifier. */
    taskId: string,
    /** Current task state. */
    status: string,
    /** ISO 8601 timestamp when the task was created. */
    createdAt: string,
    /** ISO 8601 timestamp when the task was last updated. */
    lastUpdatedAt: string,
    /** Actual retention duration from creation in milliseconds, null for unlimited. */
    ttl: number,
    /** Optional human-readable message describing the current task state. */
    statusMessage?: string,
    /** Suggested polling interval in milliseconds. */
    pollInterval?: number,
}


/**
 * Notification to indicate that a previously-issued request is being cancelled.
 */
export interface CancelledNotification extends JSONRPCNotification {
    /** JSON-RPC parameters payload. */
    params: CancelledNotificationParams,
}


/**
 * Notification sent from the client to the server after initialization has finished.
 */
export interface InitializedNotification extends JSONRPCNotification {
}


/**
 * Out-of-band notification to inform the receiver of a progress update.
 */
export interface ProgressNotification extends JSONRPCNotification {
    /** JSON-RPC parameters payload. */
    params: ProgressNotificationParams,
}


/**
 * Notification that the list of resources the server can read from has changed.
 */
export interface ResourceListChangedNotification extends JSONRPCNotification {
}


/**
 * Notification that a resource has changed and may need to be read again.
 */
export interface ResourceUpdatedNotification extends JSONRPCNotification {
    /** JSON-RPC parameters payload. */
    params: ResourceUpdatedNotificationParams,
}


/**
 * Notification that the list of prompts the server offers has changed.
 */
export interface PromptListChangedNotification extends JSONRPCNotification {
}


/**
 * Notification that the list of tools the server offers has changed.
 */
export interface ToolListChangedNotification extends JSONRPCNotification {
}


/**
 * Notification from the client that the list of roots has changed.
 */
export interface RootsListChangedNotification extends JSONRPCNotification {
}


/**
 * Notification of a log message passed from server to client.
 */
export interface LoggingMessageNotification extends JSONRPCNotification {
    /** JSON-RPC parameters payload. */
    params: LoggingMessageNotificationParams,
}


/**
 * Notification from the server that an out-of-band elicitation request completed.
 */
export interface ElicitationCompleteNotification extends JSONRPCNotification {
    /** JSON-RPC parameters payload. */
    params: ElicitationCompleteNotificationParams,
}


/**
 * Notification that a task's status has changed.
 */
export interface TaskStatusNotification extends JSONRPCNotification {
    /** JSON-RPC parameters payload. */
    params: TaskStatusNotificationParams,
}


/**
 * Parameters for a tools/call request.
 */
export interface CallToolRequestParams extends HasMeta {
    /** Arguments to use for the tool call. */
    arguments?: ArgumentMap,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name: string,
    /** If specified, the caller is requesting task-augmented execution. */
    task?: TaskMetadata,
}


/**
 * Parameters for a prompts/get request.
 */
export interface GetPromptRequestParams {
    /** Arguments to use for templating the prompt. */
    arguments?: ArgumentMap,
    /** Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title is not present). */
    name: string,
}


/**
 * Parameters for a completion/complete request.
 */
export interface CompleteRequestParams {
    /** The argument's information. */
    argument: CompletionArgument,
    /** Optional completion context. */
    context?: CompletionContext,
    /** A prompt or resource template reference. */
    ref: PromptReference,
}


/**
 * Parameters for a resources/read request.
 */
export interface ReadResourceRequestParams {
    /** A resource URI. */
    uri: string,
}


/**
 * Parameters for a resources/subscribe request.
 */
export interface SubscribeRequestParams {
    /** A resource URI. */
    uri: string,
}


/**
 * Parameters for a resources/unsubscribe request.
 */
export interface UnsubscribeRequestParams {
    /** A resource URI. */
    uri: string,
}


/**
 * Parameters for a logging/setLevel request.
 */
export interface SetLevelRequestParams {
    /** The severity of a log message. */
    level: string,
}


/**
 * Parameters for an initialize request.
 */
export interface InitializeRequestParams {
    /** Client capabilities. */
    capabilities: ClientCapabilities,
    /** Information about the client implementation. */
    clientInfo: Implementation,
    /** The version of the Model Context Protocol. */
    protocolVersion: string,
}


/**
 * Parameters for a sampling/createMessage request.
 */
export interface CreateMessageRequestParams {
    /** The requested maximum number of tokens to sample. */
    maxTokens: number,
    /** Messages for sampling. */
    messages: SamplingMessage[],
    /** Model preferences for sampling. */
    modelPreferences?: ModelPreferences,
    /** An optional system prompt the server wants to use for sampling. */
    systemPrompt?: string,
    /** Sampling temperature. */
    temperature?: number,
    /** A request to include context from one or more MCP servers. */
    includeContext?: string,
    /** Stop sequences for sampling. */
    stopSequences?: string[],
    /** Tools that the model may use during generation. */
    tools?: Tool[],
    /** Controls how the model uses tools. */
    toolChoice?: ToolChoice,
    /** If specified, task-augmented execution. */
    task?: TaskMetadata,
}


/**
 * Parameters for a form-mode elicitation request.
 */
export interface ElicitRequestFormParams {
    /** A message string. */
    message: string,
    /** A restricted subset of JSON Schema. */
    requestedSchema: JsonSchema,
    /** The elicitation mode. */
    mode?: string,
    /** If specified, task-augmented execution. */
    task?: TaskMetadata,
}


/**
 * Parameters for a URL-mode elicitation request.
 */
export interface ElicitRequestURLParams {
    /** The ID of the elicitation. */
    elicitationId: string,
    /** A message string. */
    message: string,
    /** The elicitation mode. */
    mode: string,
    /** The URL that the user should navigate to. */
    url: string,
    /** If specified, task-augmented execution. */
    task?: TaskMetadata,
}


/**
 * Common params for paginated requests.
 */
export interface PaginatedRequestParams {
    /** An opaque token representing the current pagination position. If provided, the server should return results starting after this cursor. */
    cursor?: string,
}


/**
 * Request sent from the client to the server when it first connects, asking it to begin initialization.
 */
export interface InitializeRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: InitializeRequestParams,
}


/**
 * A ping, issued by either the server or the client, to check that the other party is still alive.
 */
export interface PingRequest extends JSONRPCRequest {
}


/**
 * Sent from the client to request a list of resources the server has.
 */
export interface ListResourcesRequest extends JSONRPCRequest {
}


/**
 * Sent from the client to request a list of resource templates the server has.
 */
export interface ListResourceTemplatesRequest extends JSONRPCRequest {
}


/**
 * Sent from the client to the server, to read a specific resource URI.
 */
export interface ReadResourceRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: ReadResourceRequestParams,
}


/**
 * Sent from the client to request resource update notifications.
 */
export interface SubscribeRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: SubscribeRequestParams,
}


/**
 * Sent from the client to cancel resource update notifications.
 */
export interface UnsubscribeRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: UnsubscribeRequestParams,
}


/**
 * Sent from the client to request a list of prompts and prompt templates.
 */
export interface ListPromptsRequest extends JSONRPCRequest {
}


/**
 * Used by the client to get a prompt provided by the server.
 */
export interface GetPromptRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: GetPromptRequestParams,
}


/**
 * Sent from the client to request a list of tools the server has.
 */
export interface ListToolsRequest extends JSONRPCRequest {
}


/**
 * Used by the client to invoke a tool provided by the server.
 */
export interface CallToolRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: CallToolRequestParams,
}


/**
 * A request from the client to the server, to ask for completion options.
 */
export interface CompleteRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: CompleteRequestParams,
}


/**
 * A request from the client to the server, to enable or adjust logging.
 */
export interface SetLevelRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: SetLevelRequestParams,
}


/**
 * A request from the server to sample an LLM via the client.
 */
export interface CreateMessageRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: CreateMessageRequestParams,
}


/**
 * Sent from the server to request a list of root URIs from the client.
 */
export interface ListRootsRequest extends JSONRPCRequest {
}


/**
 * A request from the server to elicit additional information from the user via the client.
 */
export interface ElicitRequest extends JSONRPCRequest {
    /** JSON-RPC parameters payload. */
    params: ElicitRequestFormParams,
}


/**
 * A request to retrieve a list of tasks.
 */
export interface ListTasksRequest extends JSONRPCRequest {
}


/**
 * A request to retrieve the state of a task.
 */
export interface GetTaskRequest extends JSONRPCRequest {
}


/**
 * A request to retrieve the result of a completed task.
 */
export interface GetTaskPayloadRequest extends JSONRPCRequest {
}


/**
 * A request to cancel a task.
 */
export interface CancelTaskRequest extends JSONRPCRequest {
}


/**
 * The result returned by the server for an initialize request.
 */
export interface InitializeResult extends Result {
    /** Server capabilities. */
    capabilities: ServerCapabilities,
    /** The version of the Model Context Protocol. */
    protocolVersion: string,
    /** Information about the server implementation. */
    serverInfo: Implementation,
    /** Instructions describing how to use the server and its features. */
    instructions?: string,
}


/**
 * The result returned by the server for a tools/call request.
 */
export interface CallToolResult extends Result {
    /** A list of content objects that represent the result. */
    content: ContentBlock[],
    /** Whether the tool call ended in an error. */
    isError?: boolean,
    /** An optional JSON object representing structured result of the tool call. */
    structuredContent?: StructuredContentData,
}


/**
 * The result returned by the server for a completion/complete request.
 */
export interface CompleteResult extends Result {
    /** The completion result object. */
    completion: CompletionData,
}


/**
 * The result returned by the server for a prompts/get request.
 */
export interface GetPromptResult extends Result {
    /** A human-readable description. */
    description?: string,
    /** The prompt messages. */
    messages: PromptMessage[],
}


/**
 * The result returned by the server for a prompts/list request.
 */
export interface ListPromptsResult extends Result {
    /** An opaque token representing the pagination position after the last returned result. If present, there may be more results available. */
    nextCursor?: string,
    /** The list of prompts. */
    prompts: Prompt[],
}


/**
 * The result returned by the server for a resources/list request.
 */
export interface ListResourcesResult extends Result {
    /** An opaque token representing the pagination position after the last returned result. If present, there may be more results available. */
    nextCursor?: string,
    /** The list of resources. */
    resources: Resource[],
}


/**
 * The result returned by the server for a resources/templates/list request.
 */
export interface ListResourceTemplatesResult extends Result {
    /** An opaque token representing the pagination position after the last returned result. If present, there may be more results available. */
    nextCursor?: string,
    /** The list of resource templates. */
    resourceTemplates: ResourceTemplate[],
}


/**
 * The result returned by the server for a resources/read request.
 */
export interface ReadResourceResult extends Result {
    /** The resource contents. */
    contents: ResourceContents[],
}


/**
 * The result returned by the server for a tools/list request.
 */
export interface ListToolsResult extends Result {
    /** An opaque token representing the pagination position after the last returned result. If present, there may be more results available. */
    nextCursor?: string,
    /** The list of tools. */
    tools: Tool[],
}


/**
 * The result returned by the client for a roots/list request.
 */
export interface ListRootsResult extends Result {
    /** The list of roots. */
    roots: Root[],
}


/**
 * The result returned by the client for a sampling/createMessage request.
 */
export interface CreateMessageResult extends Result {
    /** The message content. */
    content: ContentBlock,
    /** The name of the model that generated the message. */
    model: string,
    /** The role of the sender or recipient. */
    role: string,
    /** The reason why sampling stopped, if known. */
    stopReason?: string,
}


/**
 * The result returned by the client for an elicitation/create request.
 */
export interface ElicitResult extends Result {
    /** The user action in response to the elicitation. */
    action: string,
    /** Structured content block of a message or result. */
    content?: ElicitationContent,
}


/**
 * The result returned for a task-augmented request.
 */
export interface CreateTaskResult extends Result {
    /** Task data. */
    task: Task,
}


/**
 * The result returned for a tasks/result request.
 */
export interface GetTaskPayloadResult extends Result {
}


/**
 * The result returned for a tasks/list request.
 */
export interface ListTasksResult extends Result {
    /** An opaque token representing the pagination position after the last returned result. If present, there may be more results available. */
    nextCursor?: string,
    /** The list of tasks. */
    tasks: Task[],
}


/**
 * The result returned for a tasks/cancel request.
 */
export interface CancelTaskResult extends Result, HasMeta {
    /** The task identifier. */
    taskId: string,
    /** Current task state. */
    status: string,
    /** ISO 8601 timestamp when the task was created. */
    createdAt: string,
    /** ISO 8601 timestamp when the task was last updated. */
    lastUpdatedAt: string,
    /** Actual retention duration from creation in milliseconds, null for unlimited. */
    ttl: number,
    /** Optional human-readable message describing the current task state. */
    statusMessage?: string,
    /** Suggested polling interval in milliseconds. */
    pollInterval?: number,
}


/**
 * The result returned for a tasks/get request.
 */
export interface GetTaskResult extends Result, HasMeta {
    /** The task identifier. */
    taskId: string,
    /** Current task state. */
    status: string,
    /** ISO 8601 timestamp when the task was created. */
    createdAt: string,
    /** ISO 8601 timestamp when the task was last updated. */
    lastUpdatedAt: string,
    /** Actual retention duration from creation in milliseconds, null for unlimited. */
    ttl: number,
    /** Optional human-readable message describing the current task state. */
    statusMessage?: string,
    /** Suggested polling interval in milliseconds. */
    pollInterval?: number,
}


/**
 * A successful response from the server for an initialize request.
 */
export interface InitializeResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: InitializeResult,
}


/**
 * A successful response from the server for a tools/call request.
 */
export interface CallToolResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: CallToolResult,
}


/**
 * A successful response from the server for a completion/complete request.
 */
export interface CompleteResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: CompleteResult,
}


/**
 * A successful response from the server for a prompts/get request.
 */
export interface GetPromptResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: GetPromptResult,
}


/**
 * A successful response from the server for a prompts/list request.
 */
export interface ListPromptsResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ListPromptsResult,
}


/**
 * A successful response from the server for a resources/list request.
 */
export interface ListResourcesResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ListResourcesResult,
}


/**
 * A successful response from the server for a resources/templates/list request.
 */
export interface ListResourceTemplatesResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ListResourceTemplatesResult,
}


/**
 * A successful response from the server for a resources/read request.
 */
export interface ReadResourceResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ReadResourceResult,
}


/**
 * A successful response from the server for a tools/list request.
 */
export interface ListToolsResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ListToolsResult,
}


/**
 * A successful response from the client for a roots/list request.
 */
export interface ListRootsResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ListRootsResult,
}


/**
 * A successful response from the client for a sampling/createMessage request.
 */
export interface CreateMessageResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: CreateMessageResult,
}


/**
 * A successful response from the client for an elicitation/create request.
 */
export interface ElicitResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ElicitResult,
}


/**
 * A successful response from the server for a logging/setLevel request.
 */
export interface SetLevelResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result?: Result,
}


/**
 * A successful response for a ping request.
 */
export interface PingResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result?: Result,
}


/**
 * A successful response for a resources/subscribe request.
 */
export interface SubscribeResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result?: Result,
}


/**
 * A successful response for a resources/unsubscribe request.
 */
export interface UnsubscribeResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result?: Result,
}


/**
 * A successful response for a task-augmented request.
 */
export interface CreateTaskResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: CreateTaskResult,
}


/**
 * A successful response for a tasks/get request.
 */
export interface GetTaskResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: GetTaskResult,
}


/**
 * A successful response for a tasks/result request.
 */
export interface GetTaskPayloadResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: GetTaskPayloadResult,
}


/**
 * A successful response for a tasks/cancel request.
 */
export interface CancelTaskResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: CancelTaskResult,
}


/**
 * A successful response for a tasks/list request.
 */
export interface ListTasksResultResponse extends JSONRPCResultResponse {
    /** JSON-RPC successful result payload. */
    result: ListTasksResult,
}


/**
 * A union of all notifications that can be sent by a client.
 */
export interface ClientNotification {
}


/**
 * A union of all requests that can be sent by a client.
 */
export interface ClientRequest {
}


/**
 * A union of all result types that a client can return.
 */
export interface ClientResult {
}


/**
 * A union of all notifications that can be sent by a server.
 */
export interface ServerNotification {
}


/**
 * A union of all requests that can be sent by a server.
 */
export interface ServerRequest {
}


/**
 * A union of all result types that a server can return.
 */
export interface ServerResult {
}


/**
 * A union of all JSON-RPC message types (requests, notifications, and responses).
 */
export interface JSONRPCMessage {
}


/**
 * A union of all JSON-RPC response types.
 */
export interface JSONRPCResponse {
}


/**
 * A union of all elicitation request parameter types.
 */
export interface ElicitRequestParams {
}


/**
 * A union of all enum schema types.
 */
export interface EnumSchema {
}


/**
 * A union of single-select enum schema types.
 */
export interface SingleSelectEnumSchema {
}


/**
 * A union of multi-select enum schema types.
 */
export interface MultiSelectEnumSchema {
}


/**
 * A union of all primitive schema definition types.
 */
export interface PrimitiveSchemaDefinition {
}


/**
 * A union of all content block types. Maps to the vendor schema ContentBlock anyOf definition.
 */
export interface ContentBlockVariants {
}


/**
 * A union of content types valid in sampling messages.
 */
export interface SamplingMessageContentBlock {
}



