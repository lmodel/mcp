package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The contents of a resource, embedded into a prompt or tool call result.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EmbeddedResource  {

  private String type;
  private ResourceContents resource;
  private MetaObject meta;
  private Annotations annotations;

}