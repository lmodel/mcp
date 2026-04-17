package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Represents a root directory or file that the server can operate on.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Root  {

  private String uri;
  private String name;
  private MetaObject meta;

}