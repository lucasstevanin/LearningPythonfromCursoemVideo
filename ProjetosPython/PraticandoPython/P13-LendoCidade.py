cidade = str(input('Qual o nome da sua cidade? '))

# QUER DIZER SE A PALAVRA 'SANTO' ESTIVER DENTRO DA VARIAVEL CIDADE
# ELE VA FAZER UM SPLIT E PEGAR A PRIMEIRA PALAVRA, RETORNANDO TRUE OR FALSE
print('Santo' in cidade.split()[0])
