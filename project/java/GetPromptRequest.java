package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Used by the client to get a prompt provided by the server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GetPromptRequest extends JSONRPCRequest {

  private GetPromptRequestParams params;

}