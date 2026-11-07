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
  Schema for the array items.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpUntitledMultiSelectEnumSchemaItems  {

  private String type;
  private List<String> enum_;


}