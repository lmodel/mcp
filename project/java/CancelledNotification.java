package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification to indicate that a previously-issued request is being cancelled.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CancelledNotification extends JSONRPCNotification {

  private CancelledNotificationParams params;

}