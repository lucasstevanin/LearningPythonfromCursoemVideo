print('===== MAIORES E MENORES VALORES =====')
n1 = int(input('Digite um número: '))
pergunta1 = str(input('Você quer continuar? [S / N]> ')).upper()

pergunta2 = 'S'
c = 1
m = 0
maior = n1
menor = n1

while pergunta2 == 'S':
    n2 = int(input('Digite outro número: '))
    pergunta2 = str(input('Você quer continuar? [S / N]> ')).upper()
    if n1 == 1:
        maior = n1
        menor = n1
    else:
        if n2 > maior:
            maior = n2
        if n2 < menor:
            menor = n2
    n1 += n2
    c += 1
    m = n1 / c

print('========= MÉDIA =========')
print('A média entre todos os valores é {:.2f}'.format(m))
print('='*25)
print()
print('===== MAIOR E MENOR =====')
print('O maior número é {} e o menor é {}'.format(maior, menor))
print('='*25)

