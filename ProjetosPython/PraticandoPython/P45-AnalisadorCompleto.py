mais_velho = str(0)
somaidade = 0
mulheres_menos_d20 = 0

for dados in range(1, 5):
    print('-=-=-= {}ª Pessoa -=-=-='.format(dados))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo, M ou F: '))
    somaidade += idade
    media_idade = somaidade / 4

    if dados == 1:
        mais_velho = str(idade)
    else:
        if sexo == 'm' and 'idade' > mais_velho:
            mais_velho = nome

    if sexo == 'f' and idade < 20:
        mulheres_menos_d20 += 1

print('--RESULTADOS--')
print('A média de idade do grupo é {} anos!'.format(media_idade))
print('O mais velho dos homens é o: {}'.format(mais_velho))
print('Há {} mulheres menores de 20 anos de idade!'.format(mulheres_menos_d20))



