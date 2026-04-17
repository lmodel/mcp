package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  String schema definition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StringSchema  {

  private String type;
  private String default;
  private String defaultValue;
  private String description;
  private String format;
  private Integer minLength;
  private Integer maxLength;
  private String title;

}