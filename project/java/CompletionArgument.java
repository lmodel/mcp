package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Argument descriptor for completion requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompletionArgument  {

  private String name;
  private String value;

}