package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification sent from the client to the server after initialization has finished.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InitializedNotification extends JSONRPCNotification {


}