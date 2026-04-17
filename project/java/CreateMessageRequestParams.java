package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a sampling/createMessage request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreateMessageRequestParams  {

  private int maxTokens;
  private List<SamplingMessage> messages;
  private ModelPreferences modelPreferences;
  private String systemPrompt;
  private Float temperature;
  private String includeContext;
  private List<String> stopSequences;
  private List<Tool> tools;
  private ToolChoice toolChoice;
  private TaskMetadata task;

}