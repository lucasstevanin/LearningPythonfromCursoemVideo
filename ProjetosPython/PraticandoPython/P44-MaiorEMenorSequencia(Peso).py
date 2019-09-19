maior_peso = 0
menor_peso = 0

for peso in range(1, 6):
    p = float(input('Peso da {}ª pessoa: '.format(peso)))
    if peso == 1:       #nesse caso indica que o primeiro
        maior_peso = p  #peso é o maior e menor ao mesmo tempo
        menor_peso = p
    else:
        if p > maior_peso:
            maior_peso = p
        elif p < menor_peso:
            menor_peso = p

print('O maior peso é {}KG e o menor é {}KG'.format(maior_peso, menor_peso))