package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Named JSON Schema property map used by vendor fixtures.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SchemaProperties  {

  private JsonSchema name;
  private JsonSchema email;
  private JsonSchema age;
  private JsonSchema city;
  private JsonSchema location;
  private JsonSchema a;
  private JsonSchema b;
  private JsonSchema temperature;
  private JsonSchema conditions;
  private JsonSchema humidity;

}