package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Describes a message returned as part of a prompt.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PromptMessage  {

  private ContentBlock content;
  private String role;

}