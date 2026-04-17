package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A notification which does not expect a response.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class JSONRPCNotification  {

  private String jsonrpc;
  private String method;

}