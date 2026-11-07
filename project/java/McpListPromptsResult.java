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
  The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListPromptsResult extends McpPaginatedResult {

  private String cacheScope;
  private List<McpPrompt> prompts;
  private int ttlMs;


}