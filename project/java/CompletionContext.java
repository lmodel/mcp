package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Additional context for completion requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompletionContext  {

  private ArgumentMap arguments;

}