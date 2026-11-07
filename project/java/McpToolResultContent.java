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
  The result of a tool use, provided by the user back to the assistant.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpToolResultContent  {

  private McpMetaObject meta;
  private List<McpContentBlock> content;
  private Boolean isError;
  private Object structuredContent;
  private String toolUseId;
  private String kind;


}