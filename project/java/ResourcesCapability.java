package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Server resources capability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourcesCapability  {

  private boolean listChanged;
  private boolean subscribe;

}