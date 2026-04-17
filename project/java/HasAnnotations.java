package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Mixin for types that carry annotations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasAnnotations  {

  private Annotations annotations;

}