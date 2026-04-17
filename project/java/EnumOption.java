package None;

/* metamodel_version: 1.7.0 */
/* version: draft */
import java.util.List;
import lombok.*;

/**
  Single enumerated option with a machine value and display title.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnumOption  {

  private String const;
  private String title;

}