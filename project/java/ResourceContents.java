package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Generic resource contents.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceContents  {

  private String uri;
  private String mimeType;
  private String text;
  private String blob;
  private MetaObject meta;

}