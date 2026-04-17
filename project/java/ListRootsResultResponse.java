package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A successful response from the client for a roots/list request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListRootsResultResponse extends JSONRPCResultResponse {

  private ListRootsResult result;

}