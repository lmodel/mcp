package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a notifications/progress notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProgressNotificationParams  {

  private float progress;
  private String progressToken;
  private Float total;
  private String message;
  private MetaObject meta;

}