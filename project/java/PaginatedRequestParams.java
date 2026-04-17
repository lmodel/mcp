package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Common params for paginated requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PaginatedRequestParams  {

  private String cursor;

}