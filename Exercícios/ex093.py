jogador = dict()
gols = list()
t = 0

jogador['nome'] = input('Nome: ')
part = int(input(f'Quanats partidas {jogador["nome"]} jogou? '))

for p in range(part):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = gols[:]
    t += gols[p]
jogador['total'] = t
print('-='*30)
print(f'{jogador}')
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for p, g in enumerate(gols):
    print(f' => Na partida {p}, fez {g} gols.')
print(f'Foi um total de {t} gols.')

