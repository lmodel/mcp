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
  Definition for a tool the client can call.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpTool extends McpBaseMetadata {

  private McpMetaObject meta;
  private McpToolAnnotations annotations;
  private String description;
  private List<McpIcon> icons;
  private McpToolInputSchema inputSchema;
  private McpToolOutputSchema outputSchema;


}