package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a resources/unsubscribe request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UnsubscribeRequestParams  {

  private String uri;

}