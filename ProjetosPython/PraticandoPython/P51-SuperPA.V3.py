print('--GERADOR DE P.A--')
#ENTRADAS
primeiro_termo = int(input('Qual o primeiro termo da P.A? >> '))
razao = int(input('Qual vai ser a razão da P.A? >> '))

#PROCESSAMENTO
qtd_de_termos = 1                               #Quantidade de termos totais
termo1 = primeiro_termo                         #Primeiro termo
mais = 10                                       #Simulação de que foi escolhido 10 termos a mais para ver (pq o programa em si ja mostra 1o termos)
total = 0

while mais != 0:
    total = total + mais
    while qtd_de_termos <= total(10):
        print('{} >> '.format(termo1), end='')
        termo1 += razao
        qtd_de_termos += 1                       #Se chegou neste ponto e não satisfez o qtd_de_termos <= total ele volta pro inicio desse bloco de while
    print('Pausa')
    mais = int(input('Qual termo você gostaria de ver a mais? [se não, digite 0] >> '))

#SAIDAS
print('--TOTAL--')
print('O total final ficou em {} termos'.format(qtd_de_termos))
print('--FIM--')