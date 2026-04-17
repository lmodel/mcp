package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Text provided to or from an LLM.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TextContent  {

  private String text;
  private String type;
  private MetaObject meta;
  private Annotations annotations;

}