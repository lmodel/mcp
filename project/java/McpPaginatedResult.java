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
  A result that holds a page of a list, and the cursor of the next page.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpPaginatedResult extends McpResult {

  private String nextCursor;


}