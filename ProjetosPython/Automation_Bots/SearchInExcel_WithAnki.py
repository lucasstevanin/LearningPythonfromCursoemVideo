from tkinter import *






def adicionar():

    texto['text'] = 'Palavra: ' + caixa_pesquisa.get()


#Janela
windows = Tk()
windows.title('Searching In Excel')
windows.geometry('400x300+100+50')

#Menu Superior
menu = Menu(windows)
windows.config(menu=menu)

AlterarPlanilha = Menu(menu)
AlterarPlanilha.add_command(label='Planilha 1') #Para add + é só duplicar
AlterarPlanilha.add_command(label='Planilha 2')
menu.add_cascade(label='Alterar Planilha', menu=AlterarPlanilha)

#Barra de Pesquisa
caixa_pesquisa = Entry(windows, font='arial 18')
caixa_pesquisa.pack()


#Textos
texto = Label(windows, text='...', font='arial 14 bold')
texto.pack()            #Para add o widget a janela

#Botões
botao_verificar = Button(windows, text='Verificar',font='arial 8 bold', bg='grey',fg='white',command=adicionar)
#botao_adicionar = Button(windows, text='Adicionar',font='arial 8 bold', bg='grey',fg='white',command=adicionar)
botao_verificar.pack()  #Para add o botão
#botao_adicionar.pack()
#botao_verificar.focus() #Focar no botão de entrada

#Saída
windows.mainloop()      #Ultimo a ser executado no código da janela
