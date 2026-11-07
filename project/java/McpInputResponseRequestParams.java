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
  Parameters a client request may carry: its responses to an input-required result's requests, and the state the server returned.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpInputResponseRequestParams extends McpRequestParams {

  private McpInputResponses inputResponses;
  private String requestState;


}