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
  Hints to use for model selection.

Keys not declared here are currently left unspecified by the spec and are up
to the client to interpret.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpModelHint  {

  private String name;


}