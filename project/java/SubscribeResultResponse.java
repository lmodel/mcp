package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response for a resources/subscribe request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SubscribeResultResponse extends JSONRPCResultResponse {

  private Result result;

}