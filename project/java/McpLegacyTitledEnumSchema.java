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
  Use {@link TitledSingleSelectEnumSchema} instead.
This interface will be removed in a future version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpLegacyTitledEnumSchema  {

  private String default_;
  private String description;
  private List<String> enum_;
  private List<String> enumNames;
  private String title;
  private String type;


}