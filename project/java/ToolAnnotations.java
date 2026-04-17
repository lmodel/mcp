package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Additional properties describing a Tool to clients. All properties are hints, not guarantees.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolAnnotations  {

  private String title;
  private boolean destructiveHint;
  private boolean idempotentHint;
  private boolean openWorldHint;
  private boolean readOnlyHint;

}