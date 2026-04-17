package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Text resource contents.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TextResourceContents  {

  private String uri;
  private String mimeType;
  private String text;
  private MetaObject meta;

}