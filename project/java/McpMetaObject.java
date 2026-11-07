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
  Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

Valid keys have two segments:

**Prefix:**
- Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
- Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
- Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
- Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

**Name:**
- Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
- Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class McpMetaObject  {



}