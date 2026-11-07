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
  Returned when the request's protocol version is unknown to the server or
unsupported (e.g., a known experimental or draft version the server has
chosen not to implement). For HTTP, the response status code MUST be
`400 Bad Request`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpUnsupportedProtocolVersionError extends McpJSONRPCErrorResponse {



}