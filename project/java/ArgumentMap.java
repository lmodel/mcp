package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Argument object used in prompt and tool calls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArgumentMap  {

  private String city;
  private String location;
  private String language;
  private String framework;

}