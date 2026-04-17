package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a notifications/tasks/status notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaskStatusNotificationParams  {

  private String taskId;
  private String status;
  private String createdAt;
  private String lastUpdatedAt;
  private int ttl;
  private String statusMessage;
  private Integer pollInterval;
  private MetaObject meta;

}