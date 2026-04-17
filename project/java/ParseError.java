package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error indicating that invalid JSON was received by the server (-32700).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ParseError extends Error {


}