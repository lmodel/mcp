package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a logging/setLevel request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SetLevelRequestParams  {

  private String level;

}