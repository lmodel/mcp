package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response from the server for a tools/call request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CallToolResultResponse extends JSONRPCResultResponse {

  private CallToolResult result;

}