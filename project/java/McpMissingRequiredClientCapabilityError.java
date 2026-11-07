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
  Returned when processing a request requires a capability the client did not
declare in `clientCapabilities`. For HTTP, the response status code MUST be
`400 Bad Request`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpMissingRequiredClientCapabilityError extends McpJSONRPCErrorResponse {



}