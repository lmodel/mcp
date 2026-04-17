package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Describes an argument that a prompt can accept.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PromptArgument  {

  private String description;
  private boolean required;
  private boolean requiredField;
  private String name;
  private String title;

}