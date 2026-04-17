package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification from the server that an out-of-band elicitation request completed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitationCompleteNotification extends JSONRPCNotification {

  private ElicitationCompleteNotificationParams params;

}