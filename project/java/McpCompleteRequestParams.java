package example;

/* metamodel_version: 1.12.0 */
/* version: 2026-07-28 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Parameters for a `completion/complete` request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpCompleteRequestParams extends McpRequestParams {

  private McpCompleteRequestParamsContext context;
  private McpCompleteRequestParamsArgument argument;
  private String ref;


}