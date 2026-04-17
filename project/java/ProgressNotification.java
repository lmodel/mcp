package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Out-of-band notification to inform the receiver of a progress update.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProgressNotification extends JSONRPCNotification {

  private ProgressNotificationParams params;

}