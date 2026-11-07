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
  MCP's `BooleanSchema`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpBooleanSchema  {

  private String description;
  private String title;
  private Boolean default_;
  private String kind;


}