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
  The contents of a specific resource or sub-resource.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResourceContents  {

  private McpMetaObject meta;
  private String mimeType;
  private URI uri;


}