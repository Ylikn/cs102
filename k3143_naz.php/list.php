<?php

include 'config.php';

$query = "SELECT reys.reys_number, num_of_pl - number_tickets AS free_pl
          FROM plane_type INNER JOIN (reys INNER JOIN flight ON reys.reys_number = flight.reys_number) ON plane_type.model_number = flight.model_number
          WHERE reys.reys_number)='11' ";

$res = mysqli_query($link, $query);
 echo "<table border=1 align=center>
<tr>
<td>Номер рейса</td><td>Количество свободных мест</td>
</tr>";

while($row = mysqli_fetch_array($res))
{
echo "<tr>
<td>".$row['reys_number']."</td><td>".$row['free_pl']."</td>
</tr>";
}
echo "</table>";

mysqli_close($link);
?>
