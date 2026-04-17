package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Capabilities that a server may support. Known capabilities are defined here, but this is not a closed set.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ServerCapabilities  {

  private String experimental;
  private ExtensionsCapability extensions;
  private PromptsCapability prompts;
  private ResourcesCapability resources;
  private ToolsCapability tools;
  private TasksCapability tasks;

}