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
  Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionsAcknowledgedNotificationParams extends McpNotificationParams {

  private McpSubscriptionFilter notifications;


}