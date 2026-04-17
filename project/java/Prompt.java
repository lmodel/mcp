package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A prompt or prompt template that the server offers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Prompt  {

  private List<PromptArgument> arguments;
  private String description;
  private MetaObject meta;
  private String name;
  private String title;
  private List<Icon> icons;

}