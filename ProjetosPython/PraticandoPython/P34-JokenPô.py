from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 10)
print('PC jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 10)

if pc == 0: # Pc jogou Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('PC Vence!')
    else:
        print('Jogada Inválida!')
elif pc == 1: # PC jogou papel
    if jogador == 0:
        print('PC Vence!')
    elif jogador == 1:
        print('Empate!!')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('Jogada Inválida!')
elif pc == 2: # PC jogou tesoura
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('PC Vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')
