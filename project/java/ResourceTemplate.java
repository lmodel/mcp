package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A template description for resources available on the server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceTemplate  {

  private String uriTemplate;
  private String mimeType;
  private String description;
  private MetaObject meta;
  private Annotations annotations;
  private String name;
  private String title;
  private List<Icon> icons;

}