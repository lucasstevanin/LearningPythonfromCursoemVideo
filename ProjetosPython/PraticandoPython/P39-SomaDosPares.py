soma = 0
for i in range(0, 6):
    n = int(input('Escolha um número: '))
    if n % 2 == 0:
        soma += n
    else:
        print('Números ímpares não entram na soma!!!')

print('A soma final é {}'.format(soma))

