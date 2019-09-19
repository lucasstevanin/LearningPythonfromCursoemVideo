while True:

    preco_produto = float(input('Preço do produto: R$ '))
    desconto = float(input('Desconto de %: '))
    preco_desconto = preco_produto - (preco_produto * desconto/100)

    print('O preço do produto é de R${:.2f}, e com desconto de {:.0f}% vai ficar R${:.2f} '.format
          (preco_produto, desconto, preco_desconto))
    print('-' * 10)




