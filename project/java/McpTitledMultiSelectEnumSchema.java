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
  Schema for multiple-selection enumeration with display titles for each option.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpTitledMultiSelectEnumSchema  {

  private List<String> default_;
  private String description;
  private McpTitledMultiSelectEnumSchemaItems items;
  private Integer maxItems;
  private Integer minItems;
  private String title;
  private String type;


}