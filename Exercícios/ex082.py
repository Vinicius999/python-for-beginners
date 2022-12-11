list = []
par = []
impar = []
while True:
    list.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar? [S/N] ').upper().strip()[0]
    if cont == 'N':
        break
for n in list:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'A lista completa é {list}\n'
      f'A lista de pares é {par}\n'
      f'A lista de ímpares é {impar}')

