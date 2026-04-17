package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A response indicating that additional information is required via URL elicitation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URLElicitationRequiredError extends JSONRPCErrorResponse {


}