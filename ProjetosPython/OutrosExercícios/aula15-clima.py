import requests
import json

while True:
    cidade = input('Onde você mora? ')
    requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&APPID=c975bcb4d9fdadc4ee9d877fa2608a4d')

    tempo = json.loads(requisicao.text)

    temperaturac = tempo['main']['temp'] - 273.15


    print('Tempo:',tempo['weather'][0]['description'])
    print('Temperatura: {:.2f}'.format(temperaturac), 'ºC')
    print('-' * 20)
