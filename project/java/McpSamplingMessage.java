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
  Describes a message issued to or received from an LLM API.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpSamplingMessage  {

  private McpMetaObject meta;
  private String content;
  private String role;


}