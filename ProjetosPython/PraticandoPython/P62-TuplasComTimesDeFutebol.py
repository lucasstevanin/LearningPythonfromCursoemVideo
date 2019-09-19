classificacao = ('Santos','Flamengo','Palmeiras','Atlético-MG','São Paulo','Corinthians','Internacional','Athletico-PR',
                 'Botafogo','Bahia','Ceara','Goias','Gremio','Fortaleza','Vasco','Cruzeiro','Chapecoense','Fluminense',
                 'CSA','Avaí')

print('-='*20)
print(f'Os 5 primeiros colocados são: {classificacao[:5]}')
print('-='*20)
print(f'Os ultimos 4 colocados da tabela são: {classificacao[-4:]}')
print('-='*20)
print(f'Times em ordem: {sorted(classificacao)}')
print('-='*20)
print(f'Chapecoense está na {classificacao.index("Chapecoense")}ª posição')
print('-='*20)