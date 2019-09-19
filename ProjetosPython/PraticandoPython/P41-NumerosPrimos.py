

n = int(input('Escolha um número: '))
m = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(end='')
        m += 1
    else:
        print(end='')
    print('{} '.format(i), end='')
print('\nO numero {} foi divisivel {} vezes'.format(n, m))
if m == 2:
    print('È Primo!')
else:
    print('NÂO é Primo!!')