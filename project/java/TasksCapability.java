package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Task capability object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TasksCapability  {

  private TaskRequestCapabilities requests;

}