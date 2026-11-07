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
  Describes the MCP implementation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpImplementation extends McpBaseMetadata {

  private String description;
  private String version;
  private List<McpIcon> icons;
  private URI websiteUrl;


}