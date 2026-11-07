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
  Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpClientCapabilities  {

  private McpClientCapabilitiesElicitation elicitation;
  private McpClientCapabilitiesExperimental experimental;
  private McpClientCapabilitiesExtensions extensions;
  private McpClientCapabilitiesRoots roots;
  private McpClientCapabilitiesSampling sampling;


}