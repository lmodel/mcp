package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for a resources/list request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListResourcesResult extends Result {

  private String nextCursor;
  private List<Resource> resources;

}