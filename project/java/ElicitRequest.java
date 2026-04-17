package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A request from the server to elicit additional information from the user via the client.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitRequest extends JSONRPCRequest {

  private ElicitRequestFormParams params;

}