n = int(input(' Digite um número: '))
x = int(input(' [1] para BINÁRIO\n [2] para OCTAL\n [3] para HEXADECIMAL\n >>> Escolha: '))
if x == 1:
    print(' Convertido para BINÁRIO: {}'.format(bin(n)[2:]))
elif x == 2:
    print(' Convertido para OCTAL: {}'.format(oct(n)[2:]))
elif x == 3:
    print(' Convertido para HEXADECIMAL: {}'.format(hex(n)[2:]))
else:
    print(' Opção inválida.')
