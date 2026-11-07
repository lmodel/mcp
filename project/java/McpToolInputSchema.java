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
  A JSON Schema object defining the expected parameters for the tool.

Tool arguments are always JSON objects, so `type: "object"` is required at the root.
Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — including
composition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords
(`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any other
standard validation or annotation keywords.

Property schemas may carry an `x-mcp-header` annotation to mirror the
argument value into an HTTP header on the Streamable HTTP transport. See
the Streamable HTTP transport specification for the validity and
extraction rules.

Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpToolInputSchema  {

  private String type;
  private String schemaDialect;


}