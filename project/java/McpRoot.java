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
  Represents a root directory or file that the server can operate on.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpRoot  {

  private McpMetaObject meta;
  private String name;
  private URI uri;


}