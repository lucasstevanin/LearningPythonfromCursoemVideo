from random import randint

tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
sorteio = sorted(tupla)

print(tupla)
print(f'O maior numero é {sorteio[-1]}')
print(f'O menor numero é {sorteio[0]}')




