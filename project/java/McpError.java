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
  The error a JSON-RPC error response carries: a code, a message and any data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpError  {

  private int code;
  private Object data;
  private String message;


}