frutas = ('abacaxi', 'melancia', 'banana', 'kiwi', 'jabuticaba',
          'tangerina', 'limão','morango', 'melao', 'maca', 'laranja')


for palavra in frutas:              #Analisa cada elemento da tupla frutas
    print(f'\nNa palavra {palavra}, as vogais são: ', end='')
    for letra in palavra:           #Pega cada letra da palavra analisada
        if letra in 'aeiou':        #Vê se essa letra é 'aeiou'
            print(letra, end='')    #Mostra essas letras (vogais)




