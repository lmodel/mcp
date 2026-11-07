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
  A successful response from the server for a {@link SubscriptionsListenRequestsubscriptions/listen}
request, sent when the server tears the subscription down gracefully.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionsListenResultResponse extends McpJSONRPCResultResponse {



}