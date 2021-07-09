from time import sleep
c = ('\033[m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[7m')


def manual(com):
    título(f'Acessando o manual com \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)



while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = (input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        manual(comando)
título('ATÉ LOGO', 1)