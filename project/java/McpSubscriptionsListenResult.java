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
  The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
request, signalling that the subscription has ended gracefully (for example,
during server shutdown). Because the listen stream is long-lived, this result
is sent only when the server tears the subscription down; an abrupt transport
close carries no response. The result body is otherwise empty.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionsListenResult extends McpResult {



}