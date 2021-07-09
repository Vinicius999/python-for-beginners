num = [list(), list()]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()
print('-='*20)
print(f'Os valores pares digitados foram {num[0]}\n'
      f'Os valores ímpares digitados foram {num[1]}')
