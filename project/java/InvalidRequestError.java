package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error indicating that the request is not a valid request object (-32600).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InvalidRequestError extends Error {


}