package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A known resource that the server is capable of reading.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Resource  {

  private String uri;
  private String mimeType;
  private String description;
  private Integer size;
  private MetaObject meta;
  private Annotations annotations;
  private String name;
  private String title;
  private List<Icon> icons;

}