package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a form-mode elicitation request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitRequestFormParams  {

  private String message;
  private JsonSchema requestedSchema;
  private String mode;
  private TaskMetadata task;

}