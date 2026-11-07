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
  Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
{@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionsListenResultMetaObject extends McpResultMetaObject {

  private String mcpSubscriptionId;


}