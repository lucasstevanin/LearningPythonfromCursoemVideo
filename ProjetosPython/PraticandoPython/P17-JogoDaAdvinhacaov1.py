from random import randint

computador = randint(0, 5)
numero = int(input('Escolha um número de 0 a 5: '))

print('O número escolhido foi {}, veja se acertou abaixo:'
      .format(computador))

if numero == computador:
    print('Parabéns você acertou!')
else:
    print('Que pena, tente novamente!')

