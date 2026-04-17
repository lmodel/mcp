package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Used by the client to invoke a tool provided by the server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CallToolRequest extends JSONRPCRequest {

  private CallToolRequestParams params;

}