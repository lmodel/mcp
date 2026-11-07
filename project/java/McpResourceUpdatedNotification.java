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
  A notification from the server to the client, informing it that a resource has changed and may need to be read again. This is only sent for resources the client opted in to via the `resourceSubscriptions` field of a {@link SubscriptionsListenRequestsubscriptions/listen} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResourceUpdatedNotification extends McpJSONRPCNotification {



}