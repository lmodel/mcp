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
  A field of an elicitation form that takes a number or an integer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpNumberSchema  {

  private String description;
  private String title;
  private Float default_;
  private Float maximum;
  private Float minimum;
  private String kind;


}