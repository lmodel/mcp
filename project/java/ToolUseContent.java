package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A request from the assistant to call a tool.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolUseContent  {

  private String id;
  private String type;
  private String name;
  private ToolInput input;
  private MetaObject meta;

}