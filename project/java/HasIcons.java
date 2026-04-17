package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Mixin for types that carry icons.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasIcons  {

  private List<Icon> icons;

}