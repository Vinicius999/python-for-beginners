list = input('Digite uma expressão: ')
np = 0
for n in list:
    if n in '()':
        np += 1
if np % 2 == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')