from OutrosExercícios.twitter import Twitter

consumer_key = ''                  ## INSERIR KEYS PARA FUNCIONAR ##
consumer_secret = ''
token_key = ''
token_secret = ''

twitter = Twitter (consumer_key, consumer_secret, token_key, token_secret)

twitter.tweet() ### Parapostar algo (SÓ A MENSAGEM)

twitter.search() ## PARA PROCURAR POR ALGO NO TWITTER   # 2 PARAMETROS (ASSUNTO, LÍNGUA)