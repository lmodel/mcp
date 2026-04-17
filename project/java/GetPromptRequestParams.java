package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a prompts/get request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GetPromptRequestParams  {

  private ArgumentMap arguments;
  private String name;

}