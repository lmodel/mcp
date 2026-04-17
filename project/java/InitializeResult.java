package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for an initialize request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InitializeResult extends Result {

  private ServerCapabilities capabilities;
  private String protocolVersion;
  private Implementation serverInfo;
  private String instructions;

}