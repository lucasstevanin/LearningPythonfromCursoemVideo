# Sem contar o flag

c = 0
s = 0

while True:
    n = int(input('Digite um número [Para Parar Digite 999]: '))
    if n == 999:  #Flag = objeto de parada
        break
    c += 1
    s += n

print(f'Foram digitados {c} números!')
print(f'A soma dos números foi de {s}!')