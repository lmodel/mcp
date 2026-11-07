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
  A response to a request that indicates an error occurred.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpJSONRPCErrorResponse  {

  private McpError error;
  private String id;
  private String jsonrpc;


}