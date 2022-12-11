pessoas = list()
dados = list()
maisp = list()
menosp = list()
map = mep = 0

while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    teste = input('Quer continuar? [S/N]').upper().strip()[0]
    if teste in 'Nn':
        break

for c, p in enumerate(pessoas):
    if c == 0:
        maisp.append(p[0])
        menosp.append(p[0])
        map = mep = p[1]
    elif p[1] >= map:
        if p[1] > map:
            maisp.clear()
        map = p[1]
        maisp.append(p[0])
    elif p[1] <= mep:
        if p[1] < mep:
            menosp.clear()
        mep = p[1]
        menosp.append(p[0])
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {map:.2f}kg. Peso de {maisp}')
print(f'O menor peso foi {mep:.2f}kh. Peso de {menosp}')