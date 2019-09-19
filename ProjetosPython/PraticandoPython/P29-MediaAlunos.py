n1 = float(input('Qual foi a sua 1ª nota? '))
n2 = float(input('Qual foi a sua 2ª nota? '))

media = (n1 + n2) / 2

if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
elif media >= 7.0:
    print('APROVADO!')