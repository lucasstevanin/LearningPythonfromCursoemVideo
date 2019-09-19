distancia = float(input('Qual a distância da sua viagem (KM)? '))

if distancia <= 200.00:
    passagem = 0.50 * distancia
    print('O preço da passagem irá ficar em {:.2f}'.format(passagem))
else:
    passagem_longa = 0.45 * distancia
    print('O preço da passagem irá ficar em {:.2f}'.format(passagem_longa))