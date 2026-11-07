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
  A request from the assistant to call a tool.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpToolUseContent  {

  private String id;
  private String name;
  private String type;
  private McpMetaObject meta;
  private McpJSONObject input;


}