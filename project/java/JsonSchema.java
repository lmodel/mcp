package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Restricted JSON Schema object used in MCP payloads.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class JsonSchema  {

  private String schemaUri;
  private String type;
  private SchemaProperties properties;
  private List<String> requiredList;
  private boolean additionalProperties;
  private Integer minimum;
  private Integer maximum;
  private Integer minLength;
  private Integer maxLength;
  private String format;
  private String description;
  private String title;
  private List<EnumOption> oneOf;
  private List<EnumOption> anyOf;
  private SchemaItems items;
  private List<String> enum;
  private String const;
  private String default;

}