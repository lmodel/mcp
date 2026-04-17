package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Audio provided to or from an LLM.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AudioContent  {

  private String data;
  private String mimeType;
  private String type;
  private MetaObject meta;
  private Annotations annotations;

}