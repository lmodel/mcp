package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for a tools/call request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CallToolResult extends Result {

  private List<ContentBlock> content;
  private boolean isError;
  private StructuredContentData structuredContent;

}