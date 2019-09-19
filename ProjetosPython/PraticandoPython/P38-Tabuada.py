n = int(input('Escolha o nº da tabuada que deseja ver: '))

for i in range(0, 11):
    mult = n*i
    print('{} x {} = {}'.format(n, i, mult))
print('FIM')