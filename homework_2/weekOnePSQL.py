import psycopg2
import psycopg2.extras
from pprint import pprint as pp
from tabulate import tabulate


conn = psycopg2.connect("host=localhost port=5432 dbname=train user=postgres password=password")
cursor = conn.cursor()

"""
    ��������� ������� � ������� ��������:
    CREATE FUNCTION _final_median(anyarray) RETURNS float8 AS $$ 
      WITH q AS
      (
         SELECT val
         FROM unnest($1) val
         WHERE VAL IS NOT NULL
         ORDER BY 1
      ),
      cnt AS
      (
        SELECT COUNT(*) AS c FROM q
      )
      SELECT AVG(val)::float8
      FROM 
      (
        SELECT val FROM q
        LIMIT  2 - MOD((SELECT c FROM cnt), 2)
        OFFSET GREATEST(CEIL((SELECT c FROM cnt) / 2.0) - 1,0)  
      ) q2;
    $$ LANGUAGE SQL IMMUTABLE;

    CREATE AGGREGATE median(anyelement) (
      SFUNC=array_append,
      STYPE=anyarray,
      FINALFUNC=_final_median,
      INITCOND='{}'
    );

"""


query = """
CREATE TABLE IF NOT EXISTS train (
    id INTEGER PRIMARY KEY,
    age INTEGER,
    gender INTEGER,
    height REAL,
    weight REAL,
    ap_hi INTEGER,
    ap_lo INTEGER,
    cholesterol INTEGER,
    gluc INTEGER,
    smoke BOOLEAN,
    alco BOOLEAN,
    active BOOLEAN,
    cardio BOOLEAN
)

"""
cursor.execute(query)
conn.commit()


with open('mlbootcamp5_train.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')

    # Skip the header row

    next(reader)
   for row in reader:
        cursor.execute(
            "INSERT INTO train VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

conn.commit()




def fetch_all(cursor):
    colnames = [desc[0] for desc in cursor.description]
    records = cursor.fetchall()
    return [{colname: value for colname, value in zip(colnames, record)} for record in records]




"""
cursor.execute("")
records = cursor.fetchall()
print(records)

"""


""" 1.������� ������ � ������ ������������ � ���� ������ ������? """

cursor.execute(
   """
   select gender, AVG(height), COUNT(gender) AS ammount
   from train
   group by gender

   """
   )
print('������� 1')
print(tabulate(fetch_all(cursor), "keys", "psql"))




""" 2. ��� � ������� ���� ���������, ��� ����������� �������� � ������� ��� �������? """

cursor.execute(

    """
    select count(alco) from train where gender = '1' and alco = '1'
    select count(alco) from train where gender = '2' and alco = '1'  
    """
)
print('������� 2')
print(tabulate(fetch_all(cursor), "keys", "psql"))



""" 3.�� ������� ��� (����������, round) ������� ������� ����� ������ ������, ��� �������
    ������� ����� ������ (�� ������� ����, �� ���� �������� ������)? """

cursor.execute(
    """
    select (((select count(smoke) from train where gender = '2' and smoke = '1')/(select count(gender) from train where
    gender = '2'))/((select count(smoke) from train where smoke = '1' and gender = '1')/(select count(gender) from train where
    gender = '1'))) from train limit 1;
    """
 )
 print('������� 3')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 4.� ��� ����� ���������� �������? �� ������� ������� (��������) ���������� ��������� ��������
    �������� ������� � ���������? """

cursor.execute(
    """
    select distinct abs(
        (select median(age) / 30 from train where smoke='1') - \
        (select median(age) / 30 from train where smoke='0')
    )::int as difference
    from train
    """
) 
print('������� 4')
print(tabulate(fetch_all(cursor), "keys", "psql"))




""" 5.  1. �������� ����� ������� age_years � ������� � �����, �������� �� ����� (round).
       ��� ������� ������� �������� ������� ������ �� 60 �� 64 ��� ������������.
        2. ��������� ������ ���������� �� ������� � � ����� ������ ����������. ����������� �������� �� ��������
       � �������� �������� cholesterol ���������: 4 �����/� -> 1, 5-7 �����/� -> 2, 8 �����/� -> 3.
        3. ���������� 2 ���������� ������� ������ �������� �� 60 �� 64 ��� ������������:
       ������ � ������� ������������ ��������� ������ ������ 120 �� ��.��. � ������������� ����������� � 4 �����/�,
       � ������ � � ������� ������������ ��������� �� 160 (������������) �� 180 �� ��.��. (�� ������������)
       � ������������� ����������� � 8 �����/�.
       �� ������� ��� (����������, round) ���������� ���� ������� ����� (�������� �������� ��������, cardio)
       � ���� ���� �����������?
       """

cursor.execute(
    """
    select(select avg(cardio) from train where gender = '2' and age >= 60365 and age <= 64365 and smoke = '1' and ap_hi >= 160 and 
    ap_hi < 180 and cholesterol = '1') / (select avg(cardio) from train where gender = '2' and age >= 21900 and age <= 64*365
    and smoke = '1' and ap_hi < 120 and cholesterol = '1') from train limit 1
    """
)
print('������� 5')
print(tabulate(fetch_all(cursor), "keys", "psql"))



""" 6. ��������� ����� ������� � BMI (Body Mass Index). ��� ����� ���� ��� � �����������
    �������� �� ������� ����� � ������. ����������� ��������� �������� BMI �� 18.5 �� 25.
    ������� ������ �����������:
    1. ��������� BMI �� ������� ��������� �����.
    2. � ������ � ������� BMI ����, ��� � ������.
    3. � �������� � ������� BMI ����, ��� � �������.
    4. � �������� �������� � �������� ������ � ������� BMI ����� � �����,
       ��� � �������� �������� � �������� ������.
"""
cursor.execute(
    """
   select median(weight / (height / 100) ^ 2) as m_BMI from train
    """
)
print('������� 6.1')
print(tabulate(fetch_all(cursor), "keys", "psql"))

cursor.execute(
    """
    select (select avg(weight) from train where gender = '1' )/(select avg(pow(height/100,2)) from train where gender = '1' ) 
    from train limit 1 
    select (select avg(weight) from train where gender = '2' )/(select avg(pow(height/100,2)) from train where gender = '2' )
    from train limit 1 
    """
)
print('������� 6.2')
print(tabulate(fetch_all(cursor), "keys", "psql"))  

cursor.execute(
    """
    select (select avg(weight) from train where cardio = '1' )/(select avg(pow(height/100,2)) from train where cardio = '1' ) 
    from train limit 1 
    select (select avg(weight) from train where cardio = '0' )/(select avg(pow(height/100,2)) from train where cardio = '0' ) 
    from train limit 1 
    """
)
print('������� 6.3')
print(tabulate(fetch_all(cursor), "keys", "psql"))  

cursor.execute(
    """
    select (select avg(weight) from train where cardio = '0' and gender = '2' and alco = '0' )/(select avg(pow(height/100,2)) 
    from train where cardio = '0' and gender = '2' and alco = '0' ) from train limit 1 
    select (select avg(weight) from train where cardio = '0' and gender = '1' and alco = '0' )/(select avg(pow(height/100,2)) 
    from train
    where cardio = '0' and gender = '1' and alco = '0' ) from train limit 1 
    """
)
print('������� 6.4')
print(tabulate(fetch_all(cursor), "keys", "psql"))  


"""" 7. ������������ ��������� �������� ��������� (������� ��� �������� � ������):
    1. ��������� ������ �������� ������������� �������� ������ ���� ��������.
    2. ���� ������ ������ 2.5%-���������� ��� ������ ������ 97.5%-����������.
       (����������� pd.Series.quantile, ���� �� ������, ��� ��� ����� � ����������)
    3. ��� ������ ������ 2.5%-���������� ��� ������ ������ 97.5%-����������.
    ������� ��������� ������ (����������, round) �� ���������? """

cursor.execute(
    """
    select count(height) as all, PERCENTILE_CONT(0.025) within group (ORDER BY height) as h_25,
    PERCENTILE_CONT(0.975) within group (ORDER BY height) as h_975, PERCENTILE_CONT(0.025) within group (ORDER BY weight) as w_25,
    PERCENTILE_CONT(0.975) within group (ORDER BY weight) as w_975
    from train limit 1 
    """"
)
print('������� 7, ��������')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" ������� �������� , ��� � ������������ ��� ������� ������ ���� � ��� ������ ��������������� ��������� ������������ :
    150 <= ���� <=180
    51 <= ��� <= 108
    """

cursor.execute(
    """
    select distinct ( 100 - ((select distinct count(*) * 100 from train where ap_hi >= ap_lo and height >= 150 
    and height <= 180 and weight >= 51 AND weight <= 108) / (select count(*) from train ))) as answer from train
    """
 )
print('������� 7, �����')
print(tabulate(fetch_all(cursor), "keys", "psql"))