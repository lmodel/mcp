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
  Identifies a prompt.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpPromptReference extends McpBaseMetadata {

  private String type;


}