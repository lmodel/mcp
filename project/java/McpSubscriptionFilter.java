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
  The set of notification types a client may opt in to on a
{@link SubscriptionsListenRequestsubscriptions/listen} request.

Each notification type is **opt-in**; the server **MUST NOT** send
notification types the client has not explicitly requested here.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionFilter  {

  private Boolean promptsListChanged;
  private List<String> resourceSubscriptions;
  private Boolean resourcesListChanged;
  private Boolean toolsListChanged;


}