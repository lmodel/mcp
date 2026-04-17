package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  An optionally-sized icon that can be displayed in a user interface.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Icon  {

  private String src;
  private String mimeType;
  private List<String> sizes;
  private String theme;

}