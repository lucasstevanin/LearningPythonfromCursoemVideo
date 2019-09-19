n1 = int(input('Escolha um número:'))
n2 = int(input('Escolha outro número:'))

if n1 > n2:
    print('O {} é maior!'.format(n1))
elif n2 > n1:
    print('O {} é maior!'.format(n2))
elif n1 == n1:
    print('Não existe valor maior, {} e {} são iguais!'.format(n1, n2))
