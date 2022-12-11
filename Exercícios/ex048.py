s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s = s + c
print(' A soma dos {} múltiplos de 3, ímpares, de 1 a 500 é igual a \033[1;31m{}\033[m!'.format(cont, s))
