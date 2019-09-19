from tkinter import *
import sqlite3 as db

connection = db.connect('Teste.db')
c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS datadict(dict text, nulo0)")
c.close()
connection.commit()
connection.close()

def put_anki():
    try:
        connection = db.connect('Teste.db')
        c = connection.cursor()
        c.execute("INSERT INTO data VALUES(?, ?)",(anki.get(), nulo.get()))
        c.close()
        connection.commit()
        connection.close()
    except:
        print('Error!!')
    else:
        print('Sucesso!!')

def put_dict():
    try:
        connection = db.connect('Teste.db')
        c = connection.cursor()
        c.execute("INSERT INTO datadict VALUES(?, ?)",(dict.get(), nulo0.get()))
        c.close()
        connection.commit()
        connection.close()
    except:
        print('Error!!')
    else:
        print('Sucesso!!')

def search(s):
    try:
        connection = db.connect('Teste.db')
        c = connection.cursor()
        sql = 'SELECT * FROM data, datadict'
        for row in c.execute(sql):
            if s in row:
                print(f'{row[s]}')
                break
            else:
                break
    except:
        print(f'\033[1;31m{s}')
    else:
        print(f'\033[1;32m{s}')

#GUI
master = Tk()

anki = dict = StringVar()
nulo = nulo0 = StringVar()

#barra de pesquisa
#Label(master, text='Anki: ').grid(row=0, column=0)#ESCRITA ANTES DA BARRA DE PESQUISA
s = Entry(master, textvariable=anki).grid(row=0, column=2)#BARRA DE PESQUISA
s = Entry(master, textvariable=dict)
search(s)

#Label(master, text='Dict: ').grid(row=1, column=0)#ESCRITA ANTES DA BARRA DE PESQUISA
#Entry(master, textvariable=dict).grid(row=1, column=1)

#Botão add anki
Button(master, text='Add Anki',command=put_anki).grid(row=3, column=1)
Button(master, text='Add Dict',command=put_dict).grid(row=3, column=2)
Button(master, text='Search',command=search).grid(row=3, column=3)

mainloop()