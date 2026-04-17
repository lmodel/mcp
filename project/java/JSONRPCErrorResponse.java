package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A response to a request that indicates an error occurred.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class JSONRPCErrorResponse  {

  private String id;
  private String jsonrpc;
  private Error error;

}