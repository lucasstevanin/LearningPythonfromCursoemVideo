import sqlite3
from time import sleep

connection = sqlite3.connect('Customer_List.db')
c = connection.cursor()

#SQL
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Register (Name text,'
              'Telephone varchar, Age varchar, Email text)')

create_table()

def insert(n, t, i, e):
    c.execute("INSERT INTO Register VALUES(?, ?, ?, ?)",
              (n, t, i, e))
    connection.commit()


def search(s):
    sql = 'SELECT * FROM Register WHERE Name = ?'
    for row in c.execute(sql, (s, )):
        print(row)


find = int(input('1.Register User\n2.Search\n-> '))
print()

if find == 1:
    try:
        print('Costumer Base')
        sleep(1)
        n = str(input('Name: ')).title()
        t = int(input('Telephone: '))
        i = int(input('Age: '))
        e = str(input('Email: '))

        insert(n, t, i, e)

    except:
        print('Error Registering!')
    else:
        print('Successful Registration!')

elif find == 2:
    try:
        print('Search Client!')
        sleep(1)
        s = str(input('Client Name: '))
        search(s)
    except:
        print('Client Not Found!')
    else:
        print('...')


