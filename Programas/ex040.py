n1 = float(input(' 1ª nota: '))
n2 = float(input(' 2ª nota: '))
n3 = float(input(' 3ª nota: '))
m = (n1+n2+n3)/3
if m < 5:
    print('Sua média: {:.1f}\n > \033[1;31mREPROVADO\033[m'.format(m))
elif 5 <= m < 7:
    print('Sua média: {:.1f}\n > \033[1;33mRECUPERAÇÃO\033[m'.format(m))
elif m >= 7:
    print('Sua média: {:.1f}\n > \033[1;34mAPROVADO\033[m'.format(m))
