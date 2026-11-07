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
  Optional MCP extensions that the client supports. Keys are extension identifiers
(e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values are
per-extension settings objects. An empty object indicates support with no settings.

Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
mandatory prefix.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpClientCapabilitiesExtensions  {



}