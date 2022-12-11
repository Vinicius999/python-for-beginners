list = []
while True:
    n = int(input('Digite um valor: '))
    if n in list:
        print('Valor duplicado! Não vou adicionar...')
    else:
        list.append(n)
        print('Valor adicionado com sucesso...')
    cond = input('Quer continuar? [S/N] ').upper().strip()[0]
    if cond == 'N':
        break
list.sort()
print('-'*50)
print(f'Você digitou os valores {list}')
