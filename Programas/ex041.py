from datetime import date
nasc = int(input(' Ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print(' O atleta tem {} anos: \033[1;32mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print(' O atleta tem {} anos: \033[1;35mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print(' O atleta tem {} anos: \033[1;36mJÚNIOR\033[m'.format(idade))
elif idade <= 20:
    print(' O atleta tem {} anos: \033[1;31mSÊNIOR\033[m'.format(idade))
else:
    print(' Acima de 20 anos: \033[1;31mMASTER\033[m'.format(idade))
