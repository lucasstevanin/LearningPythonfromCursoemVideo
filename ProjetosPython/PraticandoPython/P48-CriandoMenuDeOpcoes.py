n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('----------------------')

n = 0
while n != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] ADD NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    print()
    n = int(input('Escolha uma opção: '))
    print('---------------------')
    if n == 1:
        print('--SOMA--')
        soma = n1 + n2
        print('O resultado da SOMA é {}'.format(soma))
        print('---------------------')

    if n == 2:
        print('--MULTIPLICAÇÃO--')
        multiplicacao = n1 * n2
        print('O resultado da MULTIPLICAÇÃO é {}'.format(multiplicacao))
        print('---------------------')

    if n == 3:
        print('--MAIOR NÚMERO--')
        maior = 0
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('O MAIOR NÚMERO é {}'.format(maior))
        print('---------------------')

    if n == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print('----------------------')

print('Programa Finalizado!')