import requests
from json import loads  #importa só uma função dessa biblioteca
import datetime  #import a biblioteca inteira
import time

while True:
    requisicao = requests.get('https://api.hgbrasil.com/finance')
    cotacao = loads(requisicao.text)

    print('##COTAÇÃO##', datetime.datetime.now())
    print('Dólar:',cotacao['results']['currencies']['USD']['buy'])
    print('Euro:',cotacao['results']['currencies']['BTC']['buy'])
    print('Bitcoin:',cotacao['results']['currencies']['EUR']['buy'])
    time.sleep(3)
    print()
