package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Multi-selection enum without display titles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UntitledMultiSelectEnumSchema  {

  private String type;
  private SchemaItems items;
  private List<String> default;
  private String defaultValue;
  private String description;
  private String title;
  private Integer minItems;
  private Integer maxItems;

}