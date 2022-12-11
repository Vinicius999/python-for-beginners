def leiaInt(msg=''):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
            break
        except:
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
        else:
            return num


def leiaFloat(msg=0):
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
            break
        except:
            print('\033[31mERRO! Por favor, digite um número real válido!\033[m')
        else:
            return num


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')






'''def leiaInt(msg):
    """
    -> Valida entradas numéricas do tipo inteiro.
    :param msg: (opcional) Mensagem que será exibida na tela para entrada do valor numérico.
    :return: O valor numérico recebido como caractere transdormado em numérico.
    """
    print('\n', '-' * 30, sep='')
    ok = False
    valor = 0
    while True:
        num = input(msg)
        if num.replace('-', '').isnumeric():
            ok = True
            valor = int(num)
        else:
            print(('\033[31mERRO! Digite um núero inteiro válido!\033[m'))
        if ok:
            break
    return valor'''
