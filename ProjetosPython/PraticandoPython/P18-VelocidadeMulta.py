velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80.00:
    multa = (velocidade * 7.00) - 560.00
    print('Você foi multado por excesso de velocidade. O preço'
          ' a pagar é R${:.2f}'.format(multa))
else:
    print('Você passou na velocidade média. Aproveite a viagem!')

