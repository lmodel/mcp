package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A request from the server to sample an LLM via the client.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreateMessageRequest extends JSONRPCRequest {

  private CreateMessageRequestParams params;

}