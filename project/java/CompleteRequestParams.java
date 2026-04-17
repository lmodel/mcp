package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a completion/complete request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompleteRequestParams  {

  private CompletionArgument argument;
  private CompletionContext context;
  private PromptReference ref;

}