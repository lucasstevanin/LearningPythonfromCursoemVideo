n1 = str(input('Digite um numero: '))
n2 = str(input('Digite um numero: '))
n3 = str(input('Digite um numero: '))

#maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

#menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))