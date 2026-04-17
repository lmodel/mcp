package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Sent from the client to the server, to read a specific resource URI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReadResourceRequest extends JSONRPCRequest {

  private ReadResourceRequestParams params;

}