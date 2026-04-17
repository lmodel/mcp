package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A request from the client to the server, to ask for completion options.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompleteRequest extends JSONRPCRequest {

  private CompleteRequestParams params;

}