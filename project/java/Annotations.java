package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Optional annotations for the client. The client can use annotations to inform how objects are used or displayed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Annotations  {

  private List<String> audience;
  private String lastModified;
  private Float priority;

}