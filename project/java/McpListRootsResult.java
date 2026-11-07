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
  The result returned by the client for a {@link ListRootsRequestroots/list} request.
This result contains an array of {@link Root} objects, each representing a root directory
or file that the server can operate on.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListRootsResult  {

  private List<McpRoot> roots;


}