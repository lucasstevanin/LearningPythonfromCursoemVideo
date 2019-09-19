print('-=' * 10,'Empréstimo','-=' * 10)
valor_da_casa = float(input('Valor da Casa:R$ '))
parcelas_casa = int(input('Em quanto anos você quer pagar a sua casa? '))
salario = float(input('Seu Salário:R$ '))


porcentagem_salario = salario * 0.30
prestacao_mensal = valor_da_casa / (parcelas_casa * 12)

print('Sua prestação mensal será de R${:.2f}!'.format(prestacao_mensal))

if prestacao_mensal <= porcentagem_salario:
    print('Seu Empréstimo Foi Aprovado!')
elif prestacao_mensal > porcentagem_salario:
    print('Seu Empréstimo Foi Negado!')
print('-=' * 26)

