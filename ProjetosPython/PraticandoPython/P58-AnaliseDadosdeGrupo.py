maioresdeidade = 0
homens = 0
mulheresmenos20 = 0
sexo = ''

while True:
    idade = int(input('Sua idade: '))

    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper()

    pergunta = str(input('Quer continuar? [S/N]: ')).upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('Quer continuar? [S/N]: ')).upper()

    if idade > 18:
        maioresdeidade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulheresmenos20 += 1
    if pergunta == 'N':
        break

print(f'Há {maioresdeidade} pessoas maiores de 18 anos!')
print(f'Há {homens} homens cadastrados!!')
print(f'Há {mulheresmenos20} mulheres que tem menos de 20 anos!!')