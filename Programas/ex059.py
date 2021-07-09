n1 = int(input('  1º valor: '))
n2 = int(input('  2º valor: '))
op = 0
s = 0
while op != 5:
    op = int(input(' [1]Somar\n [2]Multiplicar \n [3]Maior \n [4]Novos números\n [5]Sair do programa\n >>Sua Escolha: '))
    if op == 1:
        print(' Soma: {}'.format(n1 + n2))
    elif op == 2:
        print(' Produto: {}'.format(n1 * n2))
    elif op == 3:
        if n1 > n2:
            print(' Maior valor: {}'.format(n1))
        elif n1 < n2:
            print(' Maior valor: {}'.format(n2))
        else:
            print(' Valores iguais.')
    elif op == 4:
        n1 = int(input('  1º valor: '))
        n2 = int(input('  2º valor: '))
    print('-'*20)
print(' >> FIM!')