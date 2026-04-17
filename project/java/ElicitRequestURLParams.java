package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a URL-mode elicitation request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitRequestURLParams  {

  private String elicitationId;
  private String message;
  private String mode;
  private String url;
  private TaskMetadata task;

}