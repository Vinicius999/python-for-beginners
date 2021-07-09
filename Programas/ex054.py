from datetime import date
ma = 0
me = 0
for c in range(1, 8):
    nasc = int(input(' Ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - nasc >= 18:
        ma += 1
    else:
        me += 1
print('-'*37)
print(' MENORES DE 18: {}\n MAIORES DE 18: {}'.format(me, ma))

