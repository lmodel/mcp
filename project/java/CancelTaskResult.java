package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned for a tasks/cancel request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CancelTaskResult extends Result {

  private String taskId;
  private String status;
  private String createdAt;
  private String lastUpdatedAt;
  private int ttl;
  private String statusMessage;
  private Integer pollInterval;

}