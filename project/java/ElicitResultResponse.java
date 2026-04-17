package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response from the client for an elicitation/create request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitResultResponse extends JSONRPCResultResponse {

  private ElicitResult result;

}