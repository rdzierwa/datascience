import sqlite3
import io


def kopia_bezpieczenstwa(db_name):
    conn = sqlite3.connect(db_name)
    with io.open(db_name + '.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    print('Kopia zapasowa została wykonana pomyślnie.')
    print('Zapisano jako CodeBrainers_dump.sql')
    conn.close()
    print('Kopia zapasowa została wykonana pomyślnie.')
    print(f'Zapisano jako {db_name}.sql')


conn = sqlite3.connect('codebrainers.db')
data = conn.cursor()
data2 = conn.cursor()

# data.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')
# data.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT2',100,35.14)")
t = data.execute(
    "SELECT * FROM stocks")  # bez commita INSERT NIE PÓJDZIE DO BAZY ALE MOŻESZ ZROBIć selecta z tych danych które chcemy zapisać,
# w pamięci robi insert do wirtualnego obiektu
# conn.commit()
#
# values =[('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# data.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)',values)
# conn.commit()
#print(t.fetchall())
#print(data.execute('SELECT sqlite_version();').fetchall())
# interdump() -> funkcja do pobrania całej bazy danych i zapisania na dysk  do pliku sql!!! UWAGA czyta linijka po linijce i tak trzeba zapisywać.


def exception_on_database():
    try:
        data.execute("INSERT INTO stocks2 VALUES ('2006-01-05','BUY','RHAT23',100,35.14)")
    except sqlite3.Error as err:
        print(err)
    finally:
        conn.commit()
        conn.close()


def create_database():
    data.execute('CREATE TABLE users(login VARCHAR(8) NOT NULL, name VARCHAR(40) NOT NULL, phone_no VARCHAR(15));')
    t = data.execute('select * from sqlite_schema')
    print(t.fetchall())


def list_data_from_table():
    """data - jeden kursor data2 - drugi kursor lub po prostu zapytanie na połączeniu"""
    table = (data.execute('select name from sqlite_schema  WHERE type = "table" GROUP BY name;').fetchall())
    for name_table in table:
         print(f"Rekordy z tabeli: {name_table[0]}")
         print(data.execute('SELECT * FROM ' + name_table[0]).fetchall())


list_data_from_table()






conn.close()
