package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification of a log message passed from server to client.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LoggingMessageNotification extends JSONRPCNotification {

  private LoggingMessageNotificationParams params;

}