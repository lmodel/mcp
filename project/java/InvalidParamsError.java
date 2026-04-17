package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error indicating that the method parameters are invalid or malformed (-32602).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InvalidParamsError extends Error {


}