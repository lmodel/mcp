package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Mixin for types that carry a _meta field.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasMeta  {

  private MetaObject meta;

}