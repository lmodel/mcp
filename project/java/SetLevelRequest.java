package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A request from the client to the server, to enable or adjust logging.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SetLevelRequest extends JSONRPCRequest {

  private SetLevelRequestParams params;

}