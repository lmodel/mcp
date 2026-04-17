package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the client for a roots/list request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListRootsResult extends Result {

  private List<Root> roots;

}