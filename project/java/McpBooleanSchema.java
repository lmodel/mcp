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
  A field of an elicitation form that takes true or false.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpBooleanSchema  {

  private String description;
  private String title;
  private String type;
  private Boolean default_;


}