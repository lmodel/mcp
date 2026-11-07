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
  The object MCP's `TitledSingleSelectEnumSchema` holds under `oneOf`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpTitledSingleSelectEnumSchemaOneOf  {

  private String title;
  private String const_;


}