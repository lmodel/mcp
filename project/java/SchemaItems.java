package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  JSON Schema items expression used by enum multi-select schemas.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SchemaItems  {

  private String type;
  private List<String> enum;
  private List<EnumOption> anyOf;

}