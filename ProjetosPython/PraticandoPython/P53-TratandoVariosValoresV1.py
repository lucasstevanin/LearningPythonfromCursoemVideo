#999 é o flag (não atribuir ele a soma) não vale como dado
c = 0
soma = 0
n = int(input('Digite um número [Para para digite 999]> '))

while n != 999:
    c += 1
    soma += n
    n = int(input('Digite outro número [Para para digite 999]> '))

print('Foram digitados {} números'.format(c))
print('A soma dos números digitados é {}'.format(soma))
print('Fim')