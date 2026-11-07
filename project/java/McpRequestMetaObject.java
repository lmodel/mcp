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
  Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpRequestMetaObject extends McpMetaObject {

  private McpClientCapabilities mcpClientCapabilities;
  private McpImplementation mcpClientInfo;
  private String mcpLogLevel;
  private String mcpProtocolVersion;
  private String progressToken;


}