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
  An optional JSON Schema object defining the structure of the tool's output returned in
the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpToolOutputSchema  {

  private String schemaDialect;


}