package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A reference to a resource or resource template definition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceTemplateReference  {

  private String type;
  private String uri;

}