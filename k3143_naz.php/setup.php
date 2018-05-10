<?php

include 'config.php'; 

$query ="CREATE TABLE IF NOT EXISTS company (
id_company int(10) NOT NULL AUTO_INCREMENT,
lisence varchar(255) NOT NULL,
director varchar(255) NOT NULL,
PRIMARY KEY (id_company))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO company VALUES ('2145', 'T5843', 'Новиков Д.А.'), ('3462', 'G1001', 'Шевцов Е.Н.'),
('4653', 'N4563', 'Сергеев И.Н.'),('7311', 'B3928', 'Александров К.Д.'), ('9865', 'Y2415', 'Рамазанов А.А.')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS crew (
id_crew int(10) NOT NULL AUTO_INCREMENT,
num_members varchar(255) NOT NULL,
PRIMARY KEY (id_crew))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO crew VALUES ('2336', '4'), ('4567', '4') ";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS time (
date_time_code int(10) NOT NULL AUTO_INCREMENT,
date_time_ar datetime NOT NULL,
date_time_lan datetime NOT NULL,
PRIMARY KEY (date_time_code))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO time VALUES ('455', '2018-04-21 14:15:00', '2018-04-21 21:00:00'), 
('653', '2018-04-21 10:28:00', '2018-04-21 14:47:00'), ('670', '2018-04-21 17:45:00', '2018-04-21 19:59:00'), 
('899', '2018-04-21 09:00:00', '2018-04-21 23:55:00'), ('933', '2018-04-21 16:30:00', '2018-04-21 22:15:00')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS transit_landing (
number_of_tl int(10) NOT NULL AUTO_INCREMENT,
date_time_tl datetime NOT NULL,
date_time_ta datetime NOT NULL,
landing_point varchar(255) NOT NULL,
PRIMARY KEY (number_of_tl))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO transit_landing VALUES ('123', '2018-04-21 14:15:00', '2018-04-21 21:00:00', 'Хельсинки'), 
('653', '2018-04-21 10:28:00', '2018-04-21 14:47:00', 'Мюнхен'), ('670', '2018-04-21 17:45:00', '2018-04-21 19:59:00', 'Дубаи')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
$query ="CREATE TABLE IF NOT EXISTS route (
route_number int(10) NOT NULL AUTO_INCREMENT,
departure_point varchar(255) NOT NULL,
arrival_point varchar(255) NOT NULL,
route_lenght int(10) NOT NULL,
PRIMARY KEY (route_number))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO route VALUES ('25', 'Рим', 'Сочи', '2560'), ('56', 'Архангельск', 'Уфа', '3470'),
('77', 'Москва', 'Лос-Анджелес', '5930'), ('87', 'Нижний Новгород', 'Санкт-Петербург', '2800'), ('90', 'Новосибирск', 'Иркутск', '1290')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
 

$query ="CREATE TABLE IF NOT EXISTS plane_type (
model_number int(10) NOT NULL AUTO_INCREMENT,
mark varchar(255) NOT NULL,
num_of_pl int(10) NOT NULL,
speed int(10) NOT NULL,
PRIMARY KEY (model_number))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO plane_type VALUES ('453', 'Boeing', '230', '900'), ('473', 'Boeing', '300', '850'),
('477', 'Airbus', '284', '950'), ('555', 'Fiat', '190', '1000'), 
('584', 'Boeing', '215', '900'), ('675', 'Boeing', '245', '950'),
('766', 'Airbus', '277', '900'), ('900', 'Airbus', '314', '800')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
 
$query ="CREATE TABLE IF NOT EXISTS plane (
plane_number int(10) NOT NULL AUTO_INCREMENT,
id_company int(10) NOT NULL,
model_number int(10) NOT NULL,
id_crew int(10) NOT NULL,
repairs varchar(255) NOT NULL,
PRIMARY KEY (plane_number),
FOREIGN KEY (id_company) REFERENCES company (id_company),
FOREIGN KEY (id_crew) REFERENCES crew (id_crew),
FOREIGN KEY (model_number) REFERENCES plane_type (model_number))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO plane VALUES ('345', '2145', '584', '4567', 'no'), ('627', '2145', '900', '4567', 'no'),
('672', '3462', '675', '2336', 'no'), ('782', '4653', '477', '2336', 'no'), 
('783', '2145', '453', '2336', 'yes'), ('788', '7311', '555', '4567', 'no')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
 
$query ="CREATE TABLE IF NOT EXISTS reys (
reys_number int(10) NOT NULL AUTO_INCREMENT,
date_time_code int(10) NOT NULL,
route_number int(10) NOT NULL,
number_tickets int(10) NOT NULL,
PRIMARY KEY (reys_number),
FOREIGN KEY (date_time_code) REFERENCES time (date_time_code),
FOREIGN KEY (route_number) REFERENCES route (route_number))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO reys VALUES ('11', '933', '25', '210'), ('12', '670', '87', '180'),
('13', '455', '56', '205'), ('14', '899', '77', '23'), ('15', '653', '87', '159')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS num_tl (
com_code int(10) NOT NULL AUTO_INCREMENT,
number_of_tl int(10) NOT NULL,
reys_number int(10) NOT NULL,
PRIMARY KEY (com_code),
FOREIGN KEY (number_of_tl) REFERENCES transit_landing (number_of_tl),
FOREIGN KEY (reys_number) REFERENCES reys (reys_number))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO num_tl VALUES ('10', '123', '14'), ('11', '653', '15'), ('12', '670', '11')";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
 
$query ="CREATE TABLE IF NOT EXISTS workers (
id_workers int(10) NOT NULL AUTO_INCREMENT,
fio varchar(255) NOT NULL,
age int(10) NOT NULL,
education varchar(255) NOT NULL,
work_experience varchar(255) NOT NULL,
passport int(20) NOT NULL,
post varchar(255) NOT NULL,
id_crew int(10) NOT NULL,
admission varchar(255) NOT NULL,
id_company int(10) NOT NULL,
PRIMARY KEY (id_workers),
FOREIGN KEY (id_crew) REFERENCES crew (id_crew),
FOREIGN KEY (id_company) REFERENCES company (id_company))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO workers VALUES 
('2574', 'Кулаков А.П.', '49', 'Высшее', '27', '4009 677382', 'Второй пилот', '4567', 'yes', '2145'),
('3822', 'Лешков П.М.', '51', 'Высшее', '16', '4014 784529', 'Штурман', '4567', 'yes', '2145'),
('1536', 'Петров М.С.', '47', 'Высшее', '5', '4034 745632', 'Командир корабля', '4567', 'yes', '2145'),
('3433', 'Петрова Ю.О.', '36', 'Высшее', '5', '4034 786324', 'Стюардесса', '4567', 'yes', '2145'),
('7908', 'Петров Н.Д.', '52', 'Высшее', '21', '4013 727428', 'Второй пилот', '4567', 'yes', '2145'),
('5311', 'Таганова Е.А.', '32', 'Среднее специальное', '3', '4012 878029', 'Стюардесса', '4567', 'no', '2145')";

if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
 
$query ="CREATE TABLE IF NOT EXISTS flight (
flight_code int(10) NOT NULL AUTO_INCREMENT,
id_company int(10) NOT NULL,
model_number int(10) NOT NULL,
id_crew int(10) NOT NULL,
date_time_code int(10) NOT NULL,
route_number int(10) NOT NULL,
reys_number int(10) NOT NULL,
plane_number int(10) NOT NULL,
PRIMARY KEY (flight_code),
FOREIGN KEY (id_company) REFERENCES company (id_company),
FOREIGN KEY (model_number) REFERENCES plane_type (model_number),
FOREIGN KEY (id_crew) REFERENCES crew (id_crew),
FOREIGN KEY (date_time_code) REFERENCES time (date_time_code),
FOREIGN KEY (route_number) REFERENCES route (route_number),
FOREIGN KEY (reys_number) REFERENCES reys (reys_number),
FOREIGN KEY (plane_number) REFERENCES plane (plane_number))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO flight VALUES ('1', '2145', '453', '2336', '455', '25', '11', '627'), ('2', '3462', '675', '2336', '455', '25', '14', '345'),
('3', '4653', '555', '2336', '455', '25', '14', '627'), ('4', '7311', '900', '4567', '899', '77', '12', '782') ";
if (mysqli_query($link, $sql)) {
echo "Created successfully<br>";
} else {
echo "Error creating <br>" . mysqli_error($link);
}
 
mysqli_close($link);
?>
