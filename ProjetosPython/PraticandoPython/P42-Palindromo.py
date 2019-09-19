frase = str(input('Insira uma frase ou palavra: ')).replace(' ','')
fraseinvertida = frase[::-1]

if frase == fraseinvertida:
    print('É Palindromo!')
else:
    print('Não é Palindromo!!')