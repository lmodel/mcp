package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the client for a sampling/createMessage request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreateMessageResult extends Result {

  private ContentBlock content;
  private String model;
  private String role;
  private String stopReason;

}