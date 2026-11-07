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
  A resource's contents as text.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpTextResourceContents extends McpResourceContents {

  private String text;


}