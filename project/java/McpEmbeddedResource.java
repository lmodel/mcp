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
  The contents of a resource, embedded into a prompt or tool call result.

It is up to the client how best to render embedded resources for the benefit
of the LLM and/or the user.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpEmbeddedResource  {

  private McpMetaObject meta;
  private McpAnnotations annotations;
  private String resourceContents;
  private String kind;


}