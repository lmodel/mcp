package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Metadata for associating messages with a task.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedTaskMetadata  {

  private String taskId;

}