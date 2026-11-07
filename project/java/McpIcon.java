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
  An optionally-sized icon that can be displayed in a user interface.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpIcon  {

  private String mimeType;
  private List<String> sizes;
  private URI src;
  private String theme;


}