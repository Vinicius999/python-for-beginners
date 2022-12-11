pessoas = list()
dados = dict()
tidade = 0

while True:
    dados['nome'] = input('Nome: ')
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas ¨M¨ ou ¨F¨')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    tidade += dados['idade']
    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()
        if resp[0] in 'SN':
            break
        print('ERRO! Responda apenas ¨S¨ ou ¨N¨')
    if resp == 'N':
        break

print(f'- O grupo tem {len(pessoas)} pessoas.\n'
      f'- A média de idade é de {tidade/len(pessoas):.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for s, v in enumerate(pessoas):
    if pessoas[s]['sexo'] == 'F':
        print(f'{v["nome"]}', end=' ')
print()
print('Pessoas que estão acima da média: ')
for s, v in enumerate(pessoas):
    for k, va in v.items():
        if v['idade'] > (tidade/len(pessoas)):
            print(f'{k} = {va}', end='; ')
    print()
print(' <<< ENCERRADO >>> ')

