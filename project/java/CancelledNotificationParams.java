package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a notifications/cancelled notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CancelledNotificationParams  {

  private String requestId;
  private String reason;
  private MetaObject meta;

}