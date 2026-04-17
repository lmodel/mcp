package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The server's preferences for model selection, requested of the client during sampling.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ModelPreferences  {

  private Float costPriority;
  private Float intelligencePriority;
  private Float speedPriority;
  private List<ModelHint> hints;

}