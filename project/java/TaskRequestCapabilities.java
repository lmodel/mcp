package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Task request capability map.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaskRequestCapabilities  {

  private ElicitationCapability elicitation;
  private SamplingCapability sampling;
  private ToolsCapability tools;

}