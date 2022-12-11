def  leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print('\033[31mPor favor, digite um número inteiro!\033[m')
            continue
        else:
            return num
            break


def linha():
    print('-' * 42)

def cabecalho(msg):
    linha()
    print(f'{str(msg):^42}')
    linha()


def menu(msg):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for op in msg:
        print(f'{c} - {op}')
        c += 1
    linha()
    opc = leiaInt('\033[32mSua opção:\033[m')
    return opc