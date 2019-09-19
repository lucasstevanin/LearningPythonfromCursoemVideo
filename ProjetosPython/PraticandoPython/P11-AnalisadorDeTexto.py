nome = str(input('Qual o seu nome? '))

# DEIXAR TUDO MAIUSCULO
print(nome.upper())
# DEIXAR TUDO MINUSCULO
print(nome.lower())
# CONTAR QUANTAS LETRAS TEM SEM OS ESPAÇOS DO COMEÇO E FINAL
print(int(len(nome.strip())))
# PARA CONTAR QUANTAS LETRAS TEM NO 1º NOME
dividido = nome.split()
print(len(dividido[0]))