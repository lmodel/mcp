package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Boolean schema definition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BooleanSchema  {

  private String type;
  private boolean default;
  private boolean defaultValue;
  private String title;
  private String description;

}