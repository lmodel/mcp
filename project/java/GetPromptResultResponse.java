package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response from the server for a prompts/get request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GetPromptResultResponse extends JSONRPCResultResponse {

  private GetPromptResult result;

}