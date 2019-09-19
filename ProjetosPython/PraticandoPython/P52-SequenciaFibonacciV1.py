#SEQUENCIA DE FIBONACCI TEM COMO PADRÃO O COMEÇO COM 0, 1


print('-=-=-= GERADOR DE SEQUÊNCIA FIBONACCI -=-=-=')
p1 =  int(input('Escolha o primeiro elemento da Sequência de Fibonacci -> '))
print('-=' * 20)

soma = 0
qtd_elementos = 1
listadeelementos = [0, 1]
c = 4
soma2 = (listadeelementos[0]) + (listadeelementos[1])
listadeelementos.append(soma2)

while c <= p1:
    soma = int(listadeelementos[-1]) + int(listadeelementos[-2])
    listadeelementos.append(soma)
    c += 1

print('-=-=-=-=-=-= SUA SEQUÊNCIA! -=-=-=-=-=-=')
print((listadeelementos), '> Pausa')
print('-=' * 20)
print('>>SEQUÊNCIA FIBONACCI FINALIZADA!!<<')
