package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Tool input payload.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolInput  {

  private String city;
  private String location;

}