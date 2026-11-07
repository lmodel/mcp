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
  Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpNotificationMetaObject extends McpMetaObject {

  private String mcpSubscriptionId;


}