<html>
<body>
	<form action = 'search.php' method = 'get'>
	<table>
	<tr><th><i>Значение:</i></th></tr>
	<tr><td>ФИО сотрудника: <input name = 'input_1' type = 'text' value='<?=@$_GET['input_1']?>'></td></tr>
	<tr><td>Номер самолета: <input name = 'input_2' type = 'text' value='<?=@$_GET['input_2']?>'></td></tr>
	</table>
	<br/>
	<input type = 'submit' name = 'button'>
	</form>
</body>
</html>
<?php

include 'config.php';

if(isset($_GET['button']))
{
	$input_1 = strtr(trim($_GET['input_1']), '*', '%');
	$input_2 = strtr(trim($_GET['input_2']), '*', '%');

	$query = "SELECT workers.fio, plane.plane_number, plane_type.speed
FROM (plane_type INNER JOIN (crew INNER JOIN plane ON crew.id_crew = plane.id_crew) ON plane_type.model_number = plane.model_number)
INNER JOIN workers ON crew.id_crew = workers.id_crew
WHERE plane_type.speed > 950 AND workers.fio LIKE '%$input_1%' ";
	
	if (!empty($input_2)) {
			$query .= "AND plane.plane_number LIKE '%$input_2%' ";
        
	}
	
	
$result = mysqli_query($link, $query);
echo "<table border = 1 align=center><tr><td>ФИО сотрудника</td><td>Номер самолета</td><td>Скорость самолета</td></tr>";
while($row = mysqli_fetch_array($result)) 
{

echo "<tr><td>".$row['fio']."</td><td>".$row['plane_number']."</td><td>".$row['speed']."</td></tr>";
}
echo "</table>";

mysqli_close($link);
}

?>