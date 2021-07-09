list = []
while True:
    list.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar? [S/N] ').upper().strip()[0]
    if cont in 'Nn':
        break
list.sort(reverse=True)
print('-='*25)
print(f'Voce digitou {len(list)} elementos.\n'
      f'Os valores em ordem decrescente são {list}')
if 5 in list:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')