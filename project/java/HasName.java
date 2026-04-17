package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Mixin for types that carry name and title.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasName  {

  private String name;
  private String title;

}