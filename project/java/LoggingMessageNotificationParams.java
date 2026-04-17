package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a notifications/message notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LoggingMessageNotificationParams  {

  private LogData data;
  private String level;
  private String logger;
  private MetaObject meta;

}