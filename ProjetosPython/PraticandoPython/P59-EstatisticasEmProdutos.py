total = maisde1000 = menor = cont = 0
produtomaisbarato = ''

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$ '))
    pergunta = str(input('Quer Continuar: [S/N] ')).upper()

    total += preco
    if preco > 1000:
        maisde1000 += 1

    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        produtomaisbarato = nome

    if pergunta == 'N':
        break

print(f'Total',total)
print(f'produtos mais caros que 1000 ->', maisde1000)
print(f'produto mais barato', produtomaisbarato)

