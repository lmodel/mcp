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
  Parameters for a {@link ProgressNotificationnotifications/progress} notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpProgressNotificationParams extends McpNotificationParams {

  private String message;
  private float progress;
  private String progressToken;
  private Float total;


}