package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Describes a message issued to or received from an LLM API.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SamplingMessage  {

  private ContentBlock content;
  private String role;
  private MetaObject meta;

}