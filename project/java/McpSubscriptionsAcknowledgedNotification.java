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
  Sent by the server to acknowledge that a
{@link SubscriptionsListenRequestsubscriptions/listen} subscription has been
established and to report which notification types it agreed to honor.

This notification MUST be the first message the server sends carrying the
subscription's ID in `io.modelcontextprotocol/subscriptionId`. The server MUST
NOT send any notification on the subscription before acknowledging it. On
stdio, where every subscription shares one channel, this ordering is defined
per subscription ID and not per channel: messages belonging to other
subscriptions MAY be interleaved before it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionsAcknowledgedNotification extends McpJSONRPCNotification {



}