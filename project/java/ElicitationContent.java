package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Form values returned by an elicitation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitationContent  {

  private String name;
  private String email;
  private Integer age;

}