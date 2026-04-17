package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Single-selection enum with display titles for each option.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TitledSingleSelectEnumSchema  {

  private String type;
  private List<EnumOption> oneOf;
  private String default;
  private String defaultValue;
  private String description;
  private String title;

}