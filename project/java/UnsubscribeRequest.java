package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Sent from the client to cancel resource update notifications.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UnsubscribeRequest extends JSONRPCRequest {

  private UnsubscribeRequestParams params;

}