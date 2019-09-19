from sqlite3 import connect
from tkinter import *

connection = connect('Words_English.db')
c = connection.cursor()


c.execute('CREATE TABLE IF NOT EXISTS Words (Anki text, nulo text, Dictionary text, nulo0 text)')
c.close()
connection.commit()
connection.close()


#SQL
def insert_anki():
    connection = connect('Words_English.db')
    c = connection.cursor()
    c.execute("INSERT INTO Anki VALUES(?, ?)", (words_anki.get(), nulo.get()))
    c.close()
    connection.commit()
    connection.close()
def insert_dictionary():
    connection = connect('Words_English.db')
    c = connection.cursor()
    c.execute("INSERT INTO Dictionary VALUES(?, ?)", (words_dictionary.get(), nulo1.get()))
    c.close()
    connection.commit()
    connection.close()

def search():
    connection = connect('Words_English.db')
    c = connection.cursor()
    sql = 'SELECT * FROM Anki, Dictionary'
    for row in c.execute(sql):
        if s.get() in row:
            texto['text'] = 'Já Tem!!'                     #f'\033[1;32m{s.get()}'
            #print(f'\033[1;32m{s.get()}')

        else:
            texto['text'] = 'Não Tem!!'                    #f'\033[1;31m{s.get()}'
            #print(f'\033[1;31m{s.get()}')


###############################################################
master = Tk()
master.title('Searching Words')
master.geometry('400x300+100+50')

menu = Menu(master)
master.config(menu=menu)

words_anki = words_dictionary = StringVar()
nulo = nulo1 = StringVar()
s = Entry(master, textvariable=words_anki, font='arial 30')#BARRA DE PESQUISA
s = Entry(master, textvariable=words_dictionary)
s.pack()

texto = Label(master, text='...', font='arial 14 bold')
texto.pack()

botao_anki = Button(master, text='Add Anki',font='arial 8 bold',command=insert_anki)
botao_dict = Button(master, text='Add Dict',font='arial 8 bold',command=insert_dictionary)
botao_search = Button(master, text='Search',font='arial 8 bold',command=search)
botao_anki.pack(padx=0, pady=10)
botao_dict.pack(padx=0, pady=10)
botao_search.pack(padx=0, pady=10)

master.mainloop()



'''
if find == 1:
    try:
        print('Anki')
        words_anki = str(input('Add Word: '))
        nulo = '-'
        insert_anki(words_anki, nulo)
    except:
        print('Error Adding!')
    else:
        print('Successfully Added!')

elif find == 2:
    try:
        print('Dictionary')
        words_dictionary = str(input('Add Word: '))
        nulo1 = '-'
        insert_dictionary(words_dictionary, nulo1)
    except:
        print('Error Adding!')
    else:
        print('Successfully Added!')

elif find == 3:
    try:
        print('Check')
        s = str(input('Check Word: '))
        search(s)
    except:
        print(f'\033[1;31m{s}')
    else:
        print(f'\033[1;32m{s}')
'''
