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
  The result returned by the server for a {@link ListToolsRequesttools/list} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListToolsResult extends McpPaginatedResult {

  private String cacheScope;
  private List<McpTool> tools;
  private int ttlMs;


}