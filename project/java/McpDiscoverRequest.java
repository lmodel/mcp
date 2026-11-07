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
  A request from the client asking the server to advertise its supported
protocol versions, capabilities, and other metadata. Servers **MUST**
implement `server/discover`. Clients **MAY** call it but are not required
to — version negotiation can also happen inline via per-request `_meta`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpDiscoverRequest extends McpJSONRPCRequest {



}