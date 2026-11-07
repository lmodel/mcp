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
  Common params for paginated requests.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpPaginatedRequestParams extends McpRequestParams {

  private String cursor;


}