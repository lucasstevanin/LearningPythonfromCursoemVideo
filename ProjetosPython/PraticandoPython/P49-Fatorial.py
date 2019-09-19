n = int(input('Escolha um número e veja seu fatorial: '))

c = n                                           # c vai ser o numero escolhido em n
f = 1                                           # f vai ser o ultimo numero do fatorial ,ou seja, 1

while c > 0:                                    # enquanto o c for maior que 0
    print('{}'.format(c), end='')               #vai mostrar o numero escolhido em n
    print(' x ' if c > 1 else ' = ', end='')    # colocar o simbolo de 'x' e '=' conforme a regra
    c -= 1                                      # subtrair do c -1 e atribuir esse valor a c
    f *= c                                      #pegar o f multiplicar por c  atribuir esse valor a f
print('{}'.format(f))                           #printar o f