package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Metadata object attached to protocol objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MetaObject  {

  private String progressToken;

}