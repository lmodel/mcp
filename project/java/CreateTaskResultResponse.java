package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response for a task-augmented request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreateTaskResultResponse extends JSONRPCResultResponse {

  private CreateTaskResult result;

}