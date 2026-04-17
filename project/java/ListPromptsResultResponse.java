package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response from the server for a prompts/list request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListPromptsResultResponse extends JSONRPCResultResponse {

  private ListPromptsResult result;

}