package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a resources/read request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReadResourceRequestParams  {

  private String uri;

}