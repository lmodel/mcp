package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a tools/call request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CallToolRequestParams  {

  private ArgumentMap arguments;
  private String name;
  private TaskMetadata task;
  private MetaObject meta;

}