package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A ping, issued by either the server or the client, to check that the other party is still alive.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PingRequest extends JSONRPCRequest {


}