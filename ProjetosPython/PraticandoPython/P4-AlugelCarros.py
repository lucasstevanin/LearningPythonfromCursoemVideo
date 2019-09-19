while True:
    print('#ALUGUEL DE CARROS#')
    dias = float(input('Dias Alugados: '))
    quilometros = float(input("KM's Rodados com o carro: "))

    preço_dia = (dias * 60) + (0.15 * quilometros)
    print('O total a pagar é de R${:.2f}'.format(preço_dia))
    print('-' * 10)
