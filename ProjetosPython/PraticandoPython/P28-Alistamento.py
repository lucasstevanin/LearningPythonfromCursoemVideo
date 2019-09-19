from datetime import date

ano_de_nascimento = int(input('Que ano você nasceu? '))

data_atual = date.today()
idade =  int(data_atual.year - ano_de_nascimento) - 18
ano_da_maioridade = int(data_atual.year - 18)

if ano_de_nascimento > ano_da_maioridade:
    print('Ainda não está na hora de se alistar, volte'
          ' daqui a {} ano(s)!'.format(abs(idade)))
elif ano_de_nascimento == ano_da_maioridade:
    print('Está no ano de se alistar amigão!!\n'
          'BOA SORTE!!')
elif ano_de_nascimento < ano_da_maioridade:
    print('Parece que você perdeu o ano de alistamento!\n'
          'Está atrasado {} ano(s)'.format(idade))