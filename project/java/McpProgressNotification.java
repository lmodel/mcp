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
  An out-of-band notification used to inform the receiver of a progress update for a long-running request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpProgressNotification extends McpJSONRPCNotification {



}