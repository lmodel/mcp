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
  A field of an elicitation form that takes text.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpStringSchema  {

  private String description;
  private String title;
  private String type;
  private String default_;
  private String format;
  private Integer maxLength;
  private Integer minLength;


}