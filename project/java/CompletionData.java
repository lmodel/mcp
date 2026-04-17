package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Completion result payload.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompletionData  {

  private List<String> values;
  private Float total;
  private boolean hasMore;

}