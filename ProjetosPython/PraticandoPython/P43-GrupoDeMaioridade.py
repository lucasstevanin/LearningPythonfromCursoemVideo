from datetime import date
anoatual = date.today().year
maioridade = 0
menores = 0

for i in range(1, 8):
    a = int(input('Qual o seu ano de nascimento? '))
    idade = anoatual - a
    if idade >= 21:
        maioridade += 1
    elif idade < 21:
        menores += 1

print('{} NÃO atingiram a maioridade e {} JÁ atingiram a maioridade!!'.format(menores, maioridade))

