n = int(input('Digite um número: '))
b = int(input('1-binario\n'
              '2-octal\n'
              '3-hexadecimal\n'
              'Escolha a base de conversão:'))

if b == 1:
    print('O número {} em binário ficará {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('O número {} em octal ficará {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('O número {} em hexadecimal ficará {}'.format(n, hex(n)[2:]))
else:
    print('Digite um número de base válida!!')

from random import choice

while True:
    usuario = input('Pedra, Papel, Tesoura\n'
                    'Escolha: ')

    escolhas_possiveis = ['Pedra', 'Papel', 'Tesoura']
    escolha_do_pc = choice(escolhas_possiveis)

    if usuario == 1:
        print('Pedra')
    elif usuario == 2:
        print('Papel')
    elif usuario == 3:
        print('Tesoura')

    if 'Pedra' in usuario and 'Pedra' in escolha_do_pc:
        print('Empate!')
    print('-' * 50)
