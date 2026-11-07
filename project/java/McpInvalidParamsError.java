package example;

/* metamodel_version: 1.12.0 */
/* version: 2026-07-28 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error indicating that the method parameters are invalid or malformed.

In MCP, this error is returned in various contexts when request parameters fail validation:

- **Tools**: Unknown tool name or invalid tool arguments
- **Prompts**: Unknown prompt name or missing required arguments
- **Pagination**: Invalid or expired cursor values
- **Logging**: Invalid log level
- **Elicitation**: Server requests an elicitation mode not declared in client capabilities
- **Sampling**: Missing tool result or tool results mixed with other content
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpInvalidParamsError extends McpError {



}