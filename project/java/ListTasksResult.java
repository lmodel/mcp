package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned for a tasks/list request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListTasksResult extends Result {

  private String nextCursor;
  private List<Task> tasks;

}