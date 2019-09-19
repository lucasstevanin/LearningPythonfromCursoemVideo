while True:

    salario = float(input('Salário Atual:R$ '))
    reajuste_salarial = float(input('Aumento de:% '))
    salario_final = salario + (salario * reajuste_salarial/100)

    print('O Salário  é de R${:.2f} por mês, e com o reajuste de {:.0f}% vai para R${:.2f} por mês '.format
          (salario, reajuste_salarial, salario_final))
    print('-' * 10)