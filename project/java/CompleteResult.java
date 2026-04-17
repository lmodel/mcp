package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for a completion/complete request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompleteResult extends Result {

  private CompletionData completion;

}