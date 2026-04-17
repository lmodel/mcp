package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result of a tool use, provided by the user back to the assistant.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolResultContent  {

  private List<ContentBlock> content;
  private String type;
  private String toolUseId;
  private boolean isError;
  private StructuredContentData structuredContent;
  private MetaObject meta;

}