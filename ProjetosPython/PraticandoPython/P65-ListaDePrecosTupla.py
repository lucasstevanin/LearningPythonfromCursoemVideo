produtos = ('Leite', 2,
            'Pão', 3,
            'Ovo', 5,
            'Margarina', 1)



print('='*27)
print(f'{"Preços":^27}')
print('='*27)

for pos in range(0, len(produtos)):             #Range(0, qtd de elementos da tupla)
    if pos % 2 == 0:                            #Se posição for par
        print(f'{produtos[pos]:.<20}', end='')  #Mostrar o produto da posição de numero par
    else:                                       #Senão
        print(f'R${produtos[pos]:>5.2f}')       #Mostrar o produto do restante das posições




''' #Jeito Mais Trabalhoso
print(f'{produtos[0]:.<20}R${produtos[1]}')
print(f'{produtos[2]:.<20}R${produtos[3]}')
print(f'{produtos[4]:.<20}R${produtos[5]}')
print(f'{produtos[6]:.<20}R${produtos[7]}')
'''
