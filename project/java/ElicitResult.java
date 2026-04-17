package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  The result returned by the client for an elicitation/create request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElicitResult extends Result {

  private String action;
  private ElicitationContent content;

}