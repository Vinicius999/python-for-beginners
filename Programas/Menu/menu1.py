from time import sleep


def menu(menu1):
    while True:
        try:
            menuPr()
            op = int(input(f'\033[32m{menu1}\033[m'))
        except:
            print('\033[31mERRO! Por favor, digite um número inteiro válido\033[m')
        else:
            if op == 3:
                printf('Saindo do sistea...Até logo!')
                sleep(2)
                break
            printf(str(f'Opção {op}'))


def menuPr():
    printf(str('MENU PRINCIPAL'))
    print('\033[32m1 - \033[36mVer pessoas cadastradas\033[m')
    print('\033[32m2 - \033[36mCadastrar nova Pessoa\033[m')
    print('\033[32m3 - \033[36mSair do Sistema\033[m')
    print('-' * 45)


'''def option(opt):
    if opt == 1:'''




def printf(opt):
    print('-' * 45)
    print(f'{opt:^45}')
    print('-' * 45)