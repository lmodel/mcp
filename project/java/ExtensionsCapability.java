package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Server/client extension capability object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExtensionsCapability  {

  private ExtensionAppCapability appsExtension;

}