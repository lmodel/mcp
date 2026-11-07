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
  Present if the client supports sampling from an LLM.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpClientCapabilitiesSampling  {

  private McpJSONObject contextInfo;
  private McpJSONObject tools;


}