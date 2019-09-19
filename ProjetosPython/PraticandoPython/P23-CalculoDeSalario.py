salario = float(input('Quanto você ganha? '))

if salario > 1250.00:
    salario = salario + (salario * 0.10)
    print('Seu novo salário será de R${}'.format(salario))

else:
    salario = salario + (salario * 0.15)
    print('Seu novo saláro será de R${}'.format(salario))