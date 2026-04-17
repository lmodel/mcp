package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Capabilities a client may support. Known capabilities are defined here, but this is not a closed set.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ClientCapabilities  {

  private ElicitationCapability elicitation;
  private String experimental;
  private ExtensionsCapability extensions;
  private RootsCapability roots;
  private SamplingCapability sampling;
  private TasksCapability tasks;

}