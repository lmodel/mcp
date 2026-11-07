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
  MCP's `NumberSchema`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpNumberSchema  {

  private Float default_;
  private String description;
  private Float maximum;
  private Float minimum;
  private String title;
  private String type;


}