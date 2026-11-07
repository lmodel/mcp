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
  Base interface for metadata with name (identifier) and title (display name) properties.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpBaseMetadata  {

  private String name;
  private String title;


}