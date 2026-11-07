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
  The submitted form data, only present when action is `"accept"` and mode was `"form"`.
Contains values matching the requested schema.
Omitted for out-of-band mode responses.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpElicitResultContent  {



}