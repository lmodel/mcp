package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Notification that the list of tools the server offers has changed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolListChangedNotification extends JSONRPCNotification {


}