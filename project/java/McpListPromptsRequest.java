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
  Sent from the client to request a list of prompts and prompt templates the server has.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListPromptsRequest extends McpPaginatedRequest {



}