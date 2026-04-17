package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful (non-error) response to a request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class JSONRPCResultResponse  {

  private String id;
  private String jsonrpc;

}