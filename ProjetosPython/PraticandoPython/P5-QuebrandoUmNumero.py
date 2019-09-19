# COM BIBLIOTECAS OU FUNÇÕES
from math import trunc
numero = float(input('Digite um número: '))
print('O número é {} tem a parte inteira {}'.format
          (numero, trunc(numero)))
print('-'*10)

'''
# SEM IMPORTAR BIBLIOTECAS OU FUNÇÕES
numero = float(input('Digite um número: '))
print('O número é {} tem a parte inteira {}'.format
          (numero, int(numero)))
'''