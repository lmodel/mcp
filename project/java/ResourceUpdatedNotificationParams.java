package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Parameters for a notifications/resources/updated notification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceUpdatedNotificationParams  {

  private String uri;
  private MetaObject meta;

}