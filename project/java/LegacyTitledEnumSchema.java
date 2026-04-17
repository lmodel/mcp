package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Legacy titled enum schema. Use TitledSingleSelectEnumSchema instead.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LegacyTitledEnumSchema  {

  private String type;
  private List<String> enum;
  private List<String> enumValues;
  private List<String> enumNames;
  private String default;
  private String defaultValue;
  private String description;
  private String title;

}