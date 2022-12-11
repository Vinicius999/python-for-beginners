jogadores = list()
jogador = dict()
gols = list()

while True:
    print('-'*40)
    jogador['nome'] = input('Nome do jogador: ')
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    t = 0
    for p in range(part):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
        jogador['gols'] = gols[:]
        t += gols[p]
    jogador['total'] = t
    jogadores.append(jogador.copy())
    gols.clear()
    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Digite somente ¨S¨ ou ¨N¨!')
    if resp[0] == 'N':
        break

print('-='*30)
print(f'{jogadores}')
print('-'*50)
print(f'cod {str("nome"):<16}{str("gols"):<22}{str("total")}')
print('-'*50)

for c, j in enumerate(jogadores):
    print(f' {c}  {j["nome"]:<16}{str(j["gols"]):<22}{str(j["total"]):}')
print('-'*50)

while True:
    j = int(input('Mostrar dados de qual jogador? '))
    if j == '999':
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[j]["nome"]}')
    for k, v in enumerate(jogadores[j]['gols']):
        print(f' => No jogo {k} fez {v} gols.')


