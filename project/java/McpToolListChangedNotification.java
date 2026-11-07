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
  An optional notification from the server to the client, informing it that the list of tools it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `toolsListChanged` filter field.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpToolListChangedNotification extends McpJSONRPCNotification {



}