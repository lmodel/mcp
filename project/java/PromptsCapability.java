package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Server prompts capability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PromptsCapability  {

  private boolean listChanged;

}