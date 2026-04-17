package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the server for a resources/read request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReadResourceResult extends Result {

  private List<ResourceContents> contents;

}