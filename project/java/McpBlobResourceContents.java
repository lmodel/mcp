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
  A resource's contents as binary data, given as base64 text.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpBlobResourceContents extends McpResourceContents {

  private String blob;


}