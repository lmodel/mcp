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
  An InputRequiredResult sent by the server to indicate that additional input is needed
before the request can be completed.

At least one of `inputRequests` or `requestState` MUST be present.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpInputRequiredResult extends McpResult {

  private McpInputRequests inputRequests;
  private String requestState;


}