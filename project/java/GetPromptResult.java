package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for a prompts/get request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GetPromptResult extends Result {

  private String description;
  private List<PromptMessage> messages;

}