package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification that a task's status has changed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaskStatusNotification extends JSONRPCNotification {

  private TaskStatusNotificationParams params;

}