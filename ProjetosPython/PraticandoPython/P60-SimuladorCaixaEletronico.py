#Com cédulas de 50, 20, 10 e 1 #OBS: Fiz com de 100 tambem
#Informar quantas cédula de cada valor serão entregues

print('='*30)
print('{:^30}'.format('CAIXA ELETRÔNICO (24 HRS)'))
print('='*30)
m = c = d = u = 0
milhar = centena = dezena10 = dezena20 = unidade = 0

while True:
    valor_sacado = input('Qual o valor a ser sacado? R$ ')
    if int(valor_sacado) >= 1000:
        m = valor_sacado[-4]
    if int(valor_sacado) >= 100:
        c = valor_sacado[-3]
    if int(valor_sacado) >= 10:
        d = valor_sacado[-2]
    u = valor_sacado[-1]
    mult_milhar = (int(m) * 1000)
    if mult_milhar >= 100:
        milhar = mult_milhar / 100              #notas de 100
    centena = (int(c) * 100 / 50)               #notas de 50
    mult_dezena = (int(d) * 10)                 #notas de 20
    resto = mult_dezena - (mult_dezena - 10)
    if mult_dezena >= 20:
        dezena20 = mult_dezena // 20
    if mult_dezena % 20 != 0:
            dezena10 = resto / 10               #notas de 10
    unidade = (int(u) * 1) / 1                  #notas de 1
    pergunta = str(input('Deseja Realizar Alguma Outra Operação? [S / N] ')).upper()
    if pergunta == 'N':
        break
print()
print('=== SEU DINHEIRO ===')
print(f'Vão ser {milhar:.0f} notas de R$100\n'
      f'{centena:.0f} notas de R$50\n'
      f'{dezena20:.0f} notas de R$20\n'
      f'{dezena10:.0f} notas de R$10\n'
      f'{unidade:.0f} notas de R$1\n')

'''
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''

