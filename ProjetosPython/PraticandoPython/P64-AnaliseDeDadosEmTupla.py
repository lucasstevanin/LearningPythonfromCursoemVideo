n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha um numero: '))
n3 = int(input('Escolha um numero: '))
n4 = int(input('Escolha um numero: '))

tupla = (n1, n2, n3, n4)
lista = []

for n in tupla:
    if n % 2 == 0:
        lista.append(n)

print(f'Ha {tupla.count(9)} número(s) 9 dentro da tupla!')
if 3 in tupla:
    print(f'O primeiro número 3 foi digitado na {tupla.index(3)+1}ª posição!')
else:
    print(f'Não foi encontrado o numero 3 dentro da tupla!')
print(f'Os numeros pares foram {lista}!')

