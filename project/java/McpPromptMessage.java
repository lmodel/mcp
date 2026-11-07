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
  Describes a message returned as part of a prompt.

This is similar to {@link SamplingMessage}, but also supports the embedding of
resources from the MCP server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpPromptMessage  {

  private McpContentBlock content;
  private String role;


}