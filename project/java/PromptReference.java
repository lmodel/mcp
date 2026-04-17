package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Identifies a prompt.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PromptReference  {

  private String type;
  private String name;
  private String title;

}