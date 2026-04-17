package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification from the client that the list of roots has changed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RootsListChangedNotification extends JSONRPCNotification {


}