package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Blob resource contents.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BlobResourceContents  {

  private String uri;
  private String mimeType;
  private String blob;
  private MetaObject meta;

}