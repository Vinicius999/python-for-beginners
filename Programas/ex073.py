brasil = 'Atlético-MG', 'Vasco', 'Internacional', 'Bahia', 'Atlético-PR',\
         'Grêmio', 'Atlético-GO', 'Santos', 'Fluminense', 'Sport', 'São Paulo',\
         'Flamengo', 'Palmeiras', 'Botafogo','Bragantino-SP', 'Corithians', 'Goiás', \
         'Ceará', 'Fortaleza', 'Coritiba'
print('-='*30,f'\nTimes do Brasileirão: {brasil}\n', '-='*30)
print(f'Os 5 primeiros são: {brasil[:5]}\n','-='*30)
print(f'Os 4 últimos são: {brasil[-4:]}\n', '-='*30)
print(f'Times em ordem alfabética: {sorted(brasil)}\n', '-='*30)
print(f'O Flamengo está na {brasil.index("Flamengo")+1}ª posição.')
