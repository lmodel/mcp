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
  A prompt or prompt template that the server offers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpPrompt extends McpBaseMetadata {

  private McpMetaObject meta;
  private List<McpPromptArgument> arguments;
  private String description;
  private List<McpIcon> icons;


}