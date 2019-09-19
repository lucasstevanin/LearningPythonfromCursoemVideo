numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')


for i in range(0, len(numeros)):
    n = int(input('Escolha um número de 0 a 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente Novamente e escolha um número de 0 a 20: '))
    print(f'{numeros[n]}')
    print('-'*10)
