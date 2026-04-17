package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Structured content object returned by tools.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StructuredContentData  {

  private Float temperature;
  private String conditions;
  private Float humidity;

}