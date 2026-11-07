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
  Text provided to or from an LLM.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpTextContent  {

  private String type;
  private McpMetaObject meta;
  private McpAnnotations annotations;
  private String text;


}