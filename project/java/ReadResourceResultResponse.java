package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response from the server for a resources/read request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReadResourceResultResponse extends JSONRPCResultResponse {

  private ReadResourceResult result;

}