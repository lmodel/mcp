package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Structured details attached to log data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogDetails  {

  private String host;
  private Integer port;

}