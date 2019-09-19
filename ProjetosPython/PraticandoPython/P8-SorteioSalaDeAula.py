import random

print("--ALUNOS--")
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

alunos = [n1, n2, n3, n4] #Lista
sorteio = random.choice(alunos) #Sorteio de somente um item da lista com .choice

print("O aluno escdlhido foi {}".format(sorteio))