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
  MCP's `StringSchema`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpStringSchema  {

  private String default_;
  private String description;
  private String format;
  private Integer maxLength;
  private Integer minLength;
  private String title;
  private String type;


}