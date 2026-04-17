package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Request sent from the client to the server when it first connects, asking it to begin initialization.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InitializeRequest extends JSONRPCRequest {

  private InitializeRequestParams params;

}