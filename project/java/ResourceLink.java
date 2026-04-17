package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A resource that the server is capable of reading, included in a prompt or tool call result.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceLink  {

  private String uri;
  private String mimeType;
  private String description;
  private Integer size;
  private String type;
  private MetaObject meta;
  private Annotations annotations;
  private String name;
  private String title;
  private List<Icon> icons;

}