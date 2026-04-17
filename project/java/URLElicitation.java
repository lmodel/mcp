package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  URL-based elicitation request payload carried in error data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URLElicitation  {

  private String mode;
  private String elicitationId;
  private String message;
  private String url;

}