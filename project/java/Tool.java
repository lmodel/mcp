package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Definition for a tool the client can call.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Tool  {

  private ToolAnnotations annotations;
  private ToolExecution execution;
  private String description;
  private JsonSchema inputSchema;
  private JsonSchema outputSchema;
  private MetaObject meta;
  private String name;
  private String title;
  private List<Icon> icons;

}