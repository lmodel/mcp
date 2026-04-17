package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for a prompts/list request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListPromptsResult extends Result {

  private String nextCursor;
  private List<Prompt> prompts;

}