from datetime import date

ano_nascimento = int(input('Que ano você nasceu? '))

ano_atual = date.today()
idade = ano_atual.year - ano_nascimento

print('''---CLASSIFICAÇÃO-CATEGORIA---
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER
-----------------------------''')
print('Você pertence a categoria:')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')