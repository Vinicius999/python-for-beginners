from random import randint
from time import sleep
nc = randint(0, 5)  #Faz o computador "PENSAR"
n = int(input(' Acerte o número que estou pensando de ¨0¨ a ¨5¨: '))  #Jogador tenta pensar
print(' PROCESSANDO...')
sleep(3)   #O computador irá "DORMIR" por 3 segundos
if nc == n:
    print(' CONGRATULATIONS! I was thinking in {}.'.format(n))
else:
    print(' TRY AGAIN! I was thinking in {}.'.format(nc))
