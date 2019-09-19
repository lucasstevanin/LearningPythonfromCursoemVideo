from random import randint

tentativas = 0
numero = 0

computador = randint(0, 11)
while numero != computador:
    numero = int(input('Tente advinhar o número que estou pensando de 0 - 10: '))
    tentativas += 1

print('O número escolhido foi {}, e você precisou de {} tentativas:'
      .format(computador, tentativas))

