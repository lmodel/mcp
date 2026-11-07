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
  Sent from the server to request a list of root URIs from the client. Roots allow
servers to ask for specific directories or files to operate on. A common example
for roots is providing a set of repositories or directories a server should operate
on.

This request is typically used when the server needs to understand the file system
structure or access specific locations that the client has permission to read from.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpListRootsRequest  {

  private String method;
  private McpListRootsRequestParams params;


}