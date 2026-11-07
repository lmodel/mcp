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
  Common params for resource-related requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResourceRequestParams extends McpRequestParams {

  private URI uri;


}