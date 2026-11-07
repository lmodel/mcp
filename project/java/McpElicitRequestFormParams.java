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
  The parameters for a request to elicit non-sensitive information from the user via a form in the client.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpElicitRequestFormParams  {

  private String message;
  private String mode;
  private McpElicitRequestFormParamsRequestedSchema requestedSchema;


}