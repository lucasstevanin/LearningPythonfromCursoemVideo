from random import shuffle

print("--ALUNOS--")
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

alunos = [n1, n2, n3, n4]
shuffle(alunos)

print('A ordem de apresentação será: ')
print(alunos)