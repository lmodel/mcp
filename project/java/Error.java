package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  A JSON-RPC error object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Error  {

  private int code;
  private ErrorData data;
  private String message;

}