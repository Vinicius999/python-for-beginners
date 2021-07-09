p = s = q = 0
print('{:-^35}'.format(' Digite 999 para PARAR '))
while p != 999:
    p = int(input(' Digite um número: '))
    if p != 999:
        s += p
        q += 1
    else:
        print('> A soma dos {} valores digitados totaliza {}'.format(q, s))
