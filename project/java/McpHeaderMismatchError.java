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
  Returned when a server rejects a request because the values in the HTTP
headers do not match the corresponding values in the request body, or
because required headers are missing or malformed. For HTTP, the response
status code MUST be `400 Bad Request`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpHeaderMismatchError extends McpJSONRPCErrorResponse {



}