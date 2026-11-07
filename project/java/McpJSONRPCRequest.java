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
  A request that expects a response.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpJSONRPCRequest extends McpRequest {

  private String identifier;
  private String jsonrpc;


}