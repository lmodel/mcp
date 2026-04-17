package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Structured text content block.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContentBlock  {

  private String type;
  private String text;

}