package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Structured JSON-RPC error data payload.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ErrorData  {

  private String reason;
  private List<URLElicitation> elicitations;

}