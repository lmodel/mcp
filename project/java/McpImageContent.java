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
  An image provided to or from an LLM.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpImageContent  {

  private String type;
  private McpMetaObject meta;
  private McpAnnotations annotations;
  private String data;
  private String mimeType;


}