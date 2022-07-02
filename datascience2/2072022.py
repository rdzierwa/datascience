from asyncio import constants
from enum import Enum
import math
from math import pi



class Figura:

    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError
class Kolo(Figura):

    color = "Niebieski"
    
    def __init__(self, promien):
        super().__init__()
        self.promien = promien

    def obwod(self):
        return f'Obwód to: {2 * pi * self.promien}'

    def pole(self):
        return f'Pole koła to {pi * self.promien ** 2}'

    def show(self, color = color):
        print (f'prostokąt jest {color}')


class Kwadrat(Kolo):

    def __init__(self, a, b, promien):
        super().__init__(promien)
        self.a = a
        self.b = b

    def pole_kola(self):
        return f'{super().pole()}'

    def pole(self):
        return f'{self.a * self.b}'

# kolo = Kolo(5)
# print(kolo.obwod())
# print(kolo.pole())

# kw = Kwadrat(4,5,10)

# print(kw.pole_kola())
# print(kw.pole())

# kolo = Kolo(5)
# kolo.color = 'ROŻ'
# print(kolo.color)
# kolo.show()

class Test():
    COLOR = 'NIEBIESKI'
    def __init__(self) -> None:
        pass
        
    def show(self, color = COLOR):
        return (f'Mamy kolor {color} {id(Test)}')
    def show2(self):
        return (f'Bez coloru {id(Test)}')

# t1 = Test()
# t1.COLOR = 'ZIELONY'
# print (t1.COLOR)
# print (t1.show())
# print (t1.COLOR)
# print (t1.show2())
import sqlite3
import os

BASE = f'{os.getcwd()}/pythonprojects/datascience/datascience2/'
url_sql = f'{BASE}library_db.db'
url_sql2 = f'{BASE}CodeBrainers.db'
#print(url_sql)
url_sql2 = f'datascience2/CodeBrainers.db'

def run_execute(sql):
    try:
        return cur.execute(sql).fetchall()
    except Exception as Error:
        return Error
con = sqlite3.connect(url_sql2)
cur = con.cursor()

sql2 = "SELECT * FROM authors"
sql1 = "SELECT sqlite_version()"
sql3 = "SELECT * FROM Product"
sql_show_table = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
create_tabel = """CREATE TABLE Users(
                    login VARCHAR(8) NOT NULL, 
                    name VARCHAR(40) NOT NULL, 
                    phone_no VARCHAR(15)
                )"""
drop_city_table = "DROP TABLE IF EXISTS  City;"
create_table_city = """ CREATE TABLE City(
                            id SMALLINT,
                            name VARCHAR(30) NOT NULL, 
                            city VARCHAR(35) NOT NULL
                        )
                    """
sql_count = " SELECT COUNT(id) FROM City"
sql_insert_data_city = " INSERT INTO City VALUES (?,?,?)"
sql_insert_one_data_city = "INSERT INTO City VALUES (((SELECT MAX(id) FROM CITY)+1),?,?)"
data = run_execute(create_table_city)
con.commit()
print(run_execute(sql_count)[0][0])
#data_to_city = [
 #       (5001, 'Piotr Nowak','Warszawa'),
 #       (5002, 'Anna Kowalska','Kraków'),
  #      (5003, 'Krzysztof Wiśniewski','Łódź'),
  #      (5004, 'Maria Wójcik','Kraków'),
  #      (5005, 'Andrzej Kowalczyk','Wrocław')
#]
#cur.executemany(sql_insert_data_city,data_to_city)
#con.commit()
name = str(input('Podaj imię i nazwisko:'))
city = str(input('Podaj miasto:'))
cur.execute(sql_insert_one_data_city,(name,city))
con.commit()
print(run_execute(sql_count)[0][0])

print(data)

con.close()




