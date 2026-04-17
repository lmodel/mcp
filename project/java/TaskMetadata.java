package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Metadata for augmenting a request with task execution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaskMetadata  {

  private Integer ttl;

}