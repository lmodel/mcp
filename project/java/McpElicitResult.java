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
  The result returned by the client for an {@link ElicitRequestelicitation/create} request.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpElicitResult  {

  private String action;
  private McpElicitResultContent content;


}