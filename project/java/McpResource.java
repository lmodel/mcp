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
  A known resource that the server is capable of reading.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResource extends McpBaseMetadata {

  private McpMetaObject meta;
  private McpAnnotations annotations;
  private String description;
  private List<McpIcon> icons;
  private String mimeType;
  private Integer size;
  private URI uri;


}