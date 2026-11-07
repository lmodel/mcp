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
  The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListResourceTemplatesResult extends McpPaginatedResult {

  private String cacheScope;
  private List<McpResourceTemplate> resourceTemplates;
  private int ttlMs;


}