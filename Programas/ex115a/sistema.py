from ex115a.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
        sleep(1)
    elif resposta == 2:
        cabecalho('Opção 2')
        sleep(1)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)

