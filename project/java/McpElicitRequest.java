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
  A request from the server to elicit additional information from the user via the client.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpElicitRequest  {

  private String method;
  private McpElicitRequestParams params;


}