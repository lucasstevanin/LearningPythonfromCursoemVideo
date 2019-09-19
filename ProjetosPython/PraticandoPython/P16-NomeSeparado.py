nome = str(input('Qual seu nome completo? ')).title().split()

nome1 = nome[0]
nomeult = nome[-1]

print('Primeiro nome é {}\n'
      'Último nome é {}'.format(nome1, nomeult))

