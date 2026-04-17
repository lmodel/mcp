package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response for a tasks/cancel request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CancelTaskResultResponse extends JSONRPCResultResponse {

  private CancelTaskResult result;

}