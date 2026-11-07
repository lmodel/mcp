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
  A successful (non-error) response to a request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpJSONRPCResultResponse  {

  private String identifier;
  private String jsonrpc;
  private McpResult result;


}