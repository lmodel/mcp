package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Structured log data payload.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogData  {

  private String error;
  private LogDetails details;

}