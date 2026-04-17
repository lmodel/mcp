package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Single-selection enum without display titles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UntitledSingleSelectEnumSchema  {

  private String type;
  private List<String> enum;
  private List<String> enumValues;
  private String default;
  private String defaultValue;
  private String description;
  private String title;

}