matriz = []
spar = stc = masl = 0

for n in range(0, 3):
    matriz.append(int(input(f'Digite um valor para [0, {n}]: ')))
for n in range(0, 3):
    matriz.append(int(input(f'Digite um valor para [1, {n}]: ')))
for n in range(0, 3):
    matriz.append(int(input(f'Digite um valor para [2, {n}]: ')))

print('-='*22)
for n, t in enumerate(matriz):
    print(f'[{t:^5}]', end='')
    if n == 2 or n == 5 or n == 8:
        print('')
        stc += t
    if t % 2 == 0:
        spar += t
    if 3 <= n <= 5:
        if t > masl:
            masl = t

print('-='*22)
print(f'A soma dos valores pares é {spar}\n'
      f'A soma dos valores da terceira coluna é {stc}\n'
      f'O maior valor da segunda linha é {masl}')

