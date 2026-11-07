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
  Optional annotations for the client. The client can use annotations to inform how objects are used or displayed
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpAnnotations  {

  private List<String> audience;
  private String lastModified;
  private Float priority;


}