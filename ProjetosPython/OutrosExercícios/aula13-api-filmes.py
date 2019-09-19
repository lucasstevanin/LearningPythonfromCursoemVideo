
#PESQUISA DE FILMES E A PAGINA QUE ESTAO
#NÃO ESTA FUNCIONANDO PQ ACHO QUE O SITE NAO FUNCIONA MAIS
import requests
import json


def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?t=Interstellar&r=json' + titulo)
        dicionario = (req.text)
        return dicionario
    except:
        print('Erro De Entrada')
        return None


def printardetalhes(filme):
    print('Titulo: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Nota: ', filme['imdbRating'])


sair = False
while not sair:
    op = input('Escreva o nome do filme que procura ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo..')
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print('Filme não encontrado')
        else:
            printardetalhes(filme)


