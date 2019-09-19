import re
import sqlite3
import tkinter as tk


class ConectarDB:
    def __init__(self):
        self.con = sqlite3.connect('Words_English.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS Words (Anki text, nulo text, '
                            'Dictionary text, nulo0 text)')

    def insert_anki(self, words_anki, nulo):
        try:
            self.cur.execute("INSERT INTO Anki VALUES(?, ?)", (words_anki, nulo))
        except:
            print('Error Adding!')
            self.con.rollback()
        else:
            self.con.commit()
            print('Successfully Added!')

    def insert_dictionary(self, words_dictionary, nulo1):
        try:
            self.cur.execute("INSERT INTO Dictionary VALUES(?, ?)", (words_dictionary, nulo1))
        except:
            print('Error Adding!')
            self.con.rollback()
        else:
            self.con.commit()
            print('Successfully Added!')

    #def search(self, s):
     #   sql = 'SELECT * FROM Anki, Dictionary'
      #  for row in self.cur.execute(sql):
       #     if s in row:
        #        print(f'{row[s]}')
         #       break
          #  else:
           #     break

class Janela(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        #Titulo janela principal
        master.title('Searching Words')

        #Tamanho da janela principal
        master.geometry('400x300+100+50')

        #Instanciando a conexão com banco de dados
        self.banco = ConectarDB()

        #Gerenciador de layout da janela principal
        self.pack()

        #Criando Widgets
        self.criar_widgets()


    def criar_widgets(self):
        #Containers
        frame1 = tk.Frame(self)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

        #Caixa de Pesquisa
        self.entry_word = tk.Entry(frame1, font='arial 18')
        self.entry_word.pack()

        #Textos
        texts = tk.Label(frame1, text='...', font='arial 14 bold')
        texts.pack()

        #def search(self, s):
         #   sql = 'SELECT * FROM Anki, Dictionary'
          #  for row in self.cur.execute(sql):
           #     if s in row:
            #        print(f'{row[s]}')
             #       break
              #  else:
               #     break
        #Botões
        button_check = tk.Button(frame1, text='Add Anki', font='arial 8 bold', bg='black', fg='white',command=self.search2)
        button_check.pack()

        self.con = sqlite3.connect('Words_English.db')
        self.cur = self.con.cursor()
    def search2(self):
            sql = 'SELECT * FROM Anki, Dictionary'
            for row in self.cur.execute(sql):
                if self.entry_word.get() in row:
                    print(f'{row}')
                    break
                else:
                    break




root = tk.Tk()
app = Janela(master=root)
app.mainloop()

