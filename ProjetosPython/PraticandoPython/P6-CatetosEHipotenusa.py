from math import hypot
CO = float(input('Valor do cateto oposto: '))
CA = float(input('Valor do cateto adjacente: '))
HIP = hypot(CA, CO)
print('A hipotenusa vai medir {:.2f}'.format(HIP))

print('-' * 20)

cateto_oposto = float(input('Cateto Oposto: '))
cateto_adjacente = float(input('Cateto Adjacente: '))
hip = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hip))