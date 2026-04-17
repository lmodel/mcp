package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Sent from the client to request a list of resources the server has.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListResourcesRequest extends JSONRPCRequest {


}