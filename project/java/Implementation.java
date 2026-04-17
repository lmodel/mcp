package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Describes the MCP implementation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Implementation  {

  private String version;
  private String description;
  private String websiteUrl;
  private String name;
  private String title;
  private List<Icon> icons;

}