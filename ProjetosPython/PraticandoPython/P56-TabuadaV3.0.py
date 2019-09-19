while True:
    n = int(input('Digite o número da tabuada que deseja ver: '))
    print('-'*12)
    if n < 0:
        break
    for i in range(0, 11):
        tabuada = n * i
        print(f'{n} x {i} = {tabuada}')
    print('-'*12)

print('Tabuada Finalizada!!')