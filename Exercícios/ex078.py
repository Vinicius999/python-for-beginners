list = list()
for c in range(0, 5):
    list.append(int(input(f'Digite um valor a posição {c}: ')))
print('=-'*25)
print(f'Você digitou os valores: {list}')
print(f'O maior valor digitado foi {max(list)} nas posições ', end='')
for p, c in enumerate(list):
    if c >= max(list):
        print(f'{p}...', end=' ')
print(f'\nO menor valor digitado foi {min(list)} nas posições ', end='')
for p, c in enumerate(list):
    if c <= min(list):
        print(f'{p}...', end=' ' )
print(' ')


