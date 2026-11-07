package example;

/* metamodel_version: 1.12.0 */
/* version: 2026-07-28 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Parameters for a `sampling/createMessage` request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpCreateMessageRequestParams  {

  private String includeContext;
  private int maxTokens;
  private List<McpSamplingMessage> messages;
  private McpJSONObject metadata;
  private McpModelPreferences modelPreferences;
  private List<String> stopSequences;
  private String systemPrompt;
  private Float temperature;
  private McpToolChoice toolChoice;
  private List<McpTool> tools;


}