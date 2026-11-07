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
  A template description for resources available on the server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResourceTemplate extends McpBaseMetadata {

  private String description;
  private McpMetaObject meta;
  private McpAnnotations annotations;
  private List<McpIcon> icons;
  private String mimeType;
  private String uriTemplate;


}