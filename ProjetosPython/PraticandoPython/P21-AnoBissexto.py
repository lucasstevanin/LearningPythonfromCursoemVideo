while True:
    print('-=-' * 20)
    print('Ano Bissexto')
    print('-=-' * 20)

    ano = int(input('Digite um ano:' ))

    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print('Ano é bissexto!')
    else:
        print('Ano não é bissexto!')
    print('-' * 50)
    print()