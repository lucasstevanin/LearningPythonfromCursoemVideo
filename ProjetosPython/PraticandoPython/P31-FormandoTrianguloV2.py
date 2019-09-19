r1 = float(input('Digite um tamanho para a reta 1: '))
r2 = float(input('Digite um tamanho para a reta 2: '))
r3 = float(input('Digite um tamanho para a reta 3: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com as medidas {}, {}, {}, você consegue formar'
          ' um triângulo!'.format(r1, r2, r3))

    if r1 == r2 == r3:
        print('Tipo: Triângulo Equilátero.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Tipo: Triângulo Isósceles.')
    elif r1 != r2 != r3:
        print('Tipo: Triângulo Escaleno.')
else:
    print('Você não pode formar um triângulo com essas medidas!')