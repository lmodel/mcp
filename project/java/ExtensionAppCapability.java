package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Extension payload for app mime type declarations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExtensionAppCapability  {

  private List<String> mimeTypes;

}