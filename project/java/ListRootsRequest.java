package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Sent from the server to request a list of root URIs from the client.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListRootsRequest extends JSONRPCRequest {


}