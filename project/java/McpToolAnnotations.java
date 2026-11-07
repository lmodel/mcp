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
  Additional properties describing a {@link Tool} to clients.

NOTE: all properties in `ToolAnnotations` are **hints**.
They are not guaranteed to provide a faithful description of
tool behavior (including descriptive properties like `title`).

Clients should never make tool use decisions based on `ToolAnnotations`
received from untrusted servers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpToolAnnotations  {

  private String title;
  private Boolean destructiveHint;
  private Boolean idempotentHint;
  private Boolean openWorldHint;
  private Boolean readOnlyHint;


}