# Здесь БД создается заного если не существует, поэтому все жданные перетираются
from psycopg2.extensions import AsIs
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Создание переменной для соединения с БД
con = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', password='tatutatu123')

# Создание БД python_db (обратить внимание, "тире" в названии быть не должно, только знаки подчеркивания)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
db_name = "python_db"
db_table = "people"

# Просто так БД удалить нельзя, если она используется кем-то, поэтому:
# cur.execute(f"REVOKE CONNECT ON DATABASE {db_name} FROM public")
cur.execute(f"SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '{db_name}'")
cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
cur.execute(f"CREATE DATABASE {db_name}")
# Закрыть соединение с БД
con.close()

# Открываем уже новое соединение с созданной БД
con = psycopg2.connect(dbname='python_db', user='postgres', host='localhost', password='tatutatu123')
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age TEXT, gender TEXT)")
result = cur.execute(f"SELECT * FROM {db_table};")
print(result)

#  Создаем словарь
mydict = ({'name': 'Vasya', 'age': '20', 'gender': 'male'},
          {'name': 'Katya', 'age': '25', 'gender': 'female'},
          {'name': 'Petr', 'age': '21', 'gender': 'male'})

# Заполняем БД
cur.executemany(f"""INSERT INTO {db_table}(name,age,gender) VALUES (%(name)s, %(age)s, %(gender)s)""", mydict)

