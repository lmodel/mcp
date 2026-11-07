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
  The result returned by the client for a {@link CreateMessageRequestsampling/createMessage} request.
The client should inform the user before returning the sampled message, to allow them
to inspect the response (human in the loop) and decide whether to allow the server to see it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpCreateMessageResult extends McpSamplingMessage {

  private String model;
  private String stopReason;


}