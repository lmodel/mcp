package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification that a resource has changed and may need to be read again.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceUpdatedNotification extends JSONRPCNotification {

  private ResourceUpdatedNotificationParams params;

}