package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Number schema definition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NumberSchema  {

  private String type;
  private Integer default;
  private String defaultValue;
  private String description;
  private Integer minimum;
  private Integer maximum;
  private String title;

}