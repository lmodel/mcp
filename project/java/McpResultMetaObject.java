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
  Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpResultMetaObject extends McpMetaObject {

  private McpImplementation mcpServerInfo;


}