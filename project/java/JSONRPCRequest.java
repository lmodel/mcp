package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A request that expects a response.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class JSONRPCRequest  {

  private String id;
  private String jsonrpc;
  private String method;

}