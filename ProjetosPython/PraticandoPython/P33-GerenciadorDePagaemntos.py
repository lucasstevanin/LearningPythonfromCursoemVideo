preco = float(input('Preço do Produto: '))
condicao_pagamento = int(input('''--Formas de Pagamentos Disponíveis--
1 - À Vista, Dinheiro / Cheque (10% Desconto)
2 - À Vista, Cartão (5% Desconto)
3 - 2x No Cartão (Preço Normal)
4 - 3x No Cartão (20% Juros)
Opção: '''))

desconto5 = preco - (preco * 0.05)
desconto10 = preco - (preco * 0.10)
juros20 = preco + (preco * 0.20)

if condicao_pagamento == 1:
    print('Total: R${:.2f} (10% de Desconto)'.format(desconto10))
elif condicao_pagamento == 2:
    print('Total: R${:.2f} (5% de Desconto)'.format(desconto5))
elif condicao_pagamento == 3:
    print('Total: R${:.2f}'.format(preco))
elif condicao_pagamento == 4:
    print('Total: R${:.2f} (20% de Juros)'.format(juros20))
else:
    print('Escolha uma Forma de Pagamento Válida!')