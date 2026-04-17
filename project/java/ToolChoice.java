package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Controls tool selection behavior for sampling requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolChoice  {

  private String mode;

}