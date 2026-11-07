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
  The result returned by the server for a {@link ListResourcesRequestresources/list} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListResourcesResult extends McpPaginatedResult {

  private String cacheScope;
  private List<McpResource> resources;
  private int ttlMs;


}