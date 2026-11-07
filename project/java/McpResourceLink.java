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
  A resource that the server is capable of reading, included in a prompt or tool call result.

Note: resource links returned by tools are not guaranteed to appear in the results of {@link ListResourcesRequestresources/list} requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResourceLink extends McpResource {

  private String kind;


}