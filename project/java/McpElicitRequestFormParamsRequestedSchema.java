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
  A restricted subset of JSON Schema.
Only top-level properties are allowed, without nesting.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpElicitRequestFormParamsRequestedSchema  {

  private String schemaDialect;
  private McpElicitRequestFormParamsRequestedSchemaProperties properties;
  private List<String> requiredNames;
  private String kind;


}