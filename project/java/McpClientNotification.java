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
  This notification is sent by the client to indicate that it is cancelling a request it previously issued.

On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

This notification indicates that the result will be unused, so any associated processing SHOULD cease.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpClientNotification extends McpCancelledNotification {



}