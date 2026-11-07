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
  The result returned by the server for a {@link DiscoverRequestserver/discover} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpDiscoverResult extends McpCacheableResult {

  private McpServerCapabilities capabilities;
  private String instructions;
  private List<String> supportedVersions;


}