from time import sleep
print(' Os números pares entre 0 e 50 são: \n> ', end='')
for c in range(2, 51):
    print(c if c % 2 == 0 else ', ', end='')
    sleep(0.2)
print('  \033[1;34mFIM !\033[m')