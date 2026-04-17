package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error indicating that the requested method does not exist or is not available (-32601).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MethodNotFoundError extends Error {


}