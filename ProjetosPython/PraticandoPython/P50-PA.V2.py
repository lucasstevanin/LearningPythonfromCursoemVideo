p1 = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))

termo = p1      #Primeiro Termo
count = 1       #Contador de termos

while count <= 10:                          #Enquanto a qtd de termos for menor que 10
    print('{} -> '.format(termo), end='')   #Print dos termos conforme a razão
    termo += razao                          #Pega o 1ª termo e soma a razão
    count += 1                              #com isso vai add mais 1 termo no contador de termos
print('Fim')