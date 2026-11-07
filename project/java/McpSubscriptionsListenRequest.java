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
  Sent from the client to open a long-lived channel for receiving notifications
outside the context of a specific request. Replaces the previous HTTP GET
endpoint and ensures consistent behavior between HTTP and STDIO.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSubscriptionsListenRequest extends McpJSONRPCRequest {



}