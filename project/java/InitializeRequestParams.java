package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for an initialize request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InitializeRequestParams  {

  private ClientCapabilities capabilities;
  private Implementation clientInfo;
  private String protocolVersion;

}