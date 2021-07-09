list = list()
cond = '/'
c = 0

while True:
    list.append([])
    list[c].append(input('Nome: '))
    list[c].append([float(input('Nota 1: ')),
                    float(input('Nota 2: '))])
    while cond not in 'NS':
        cond = input('Quer continuar? [S/N] ').upper().strip()
    if cond == 'N':
        break
    cond = '/'
    c += 1

print('-'*40)
print('nº  NOME               MEDIA')
print('-'*30)
for c, cond in enumerate(list):
    print(f'{c:<4}{cond[0]:<20}{((cond[1][0] + cond[1][1]) / 2)}')

while True:
    print('-' * 40)
    c = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if c == 999:
        break
    print(f'Notas de {list[c][0]} são {list[c][1]}')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>>')





