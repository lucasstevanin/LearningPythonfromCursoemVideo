from random import randint

c = 0
print('--- JOGO DO PAR OU IMPAR ---')
computador = randint(0, 11)
while True:
    jogador = int(input('Digite um número: '))
    p_i = str(input('Par ou Impar? [P/I]> ')).upper()
    print(f'O computador escolheu {computador}!')
    soma = computador + jogador
    if p_i == 'I' and soma % 2 != 0 or p_i == 'P' and soma % 2 == 0:
        print('Você Ganhou!!')
        c += 1
        print()
    else:
        print('Você PERDEU!')
        print(f'Vitórias Consecutivas {c}!')
        print()
        break

