num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digit o último número: ')))
print(f'Você digitou os números {num}')
print(f'O número ¨9¨ aparece {num.count(9)} vezes.')
if 3 not in num:
    print('O valor ¨3¨ não foi digitado nenhuma vez. ')
else:
    print(f'O valor ¨3¨ foi o {(num.index(3)+1)}º valor digitado.')
print('Os números pares foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



