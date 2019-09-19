##PARA PESQUISAAR ALGO NO TWITTER VIA PYTHON##
import oauth2
import json
import urllib.parse # SERVE PARA TRANSFORMAR CARACTERES ESPECIAIS EM ESCRITA NORMAL, PARA PODER PESQUISAR OU POSTAR


consumer_key = ''
consumer_secret = ''

token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()
#####################################################################################################################

###POSTART NO TWITTER VIA PYTHON##
import oauth2
import json
import urllib.parse


consumer_key = ''
consumer_secret = ''

token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Novo tweet: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)

print(objeto)
#########################################################################################################################