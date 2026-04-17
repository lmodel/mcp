package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error indicating that an internal error occurred on the receiver (-32603).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InternalError extends Error {


}