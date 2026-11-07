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
  Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpServerCapabilities  {

  private McpJSONObject completions;
  private McpServerCapabilitiesExperimental experimental;
  private McpServerCapabilitiesExtensions extensions;
  private McpJSONObject logging;
  private McpServerCapabilitiesPrompts prompts;
  private McpServerCapabilitiesResources resources;
  private McpServerCapabilitiesTools tools;


}