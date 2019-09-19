while True:
    print('#CONVERSOR DE TEMPERATURA#')
    temperatura = float(input('Temperatura em ºC: '))
    fahrenheit = (temperatura * 1.8) + 32

    print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(temperatura, fahrenheit))
    print('-' * 10)