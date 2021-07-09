n_ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',\
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', \
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre ¨0¨ e ¨20¨: '))
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um númeor entre ¨0¨ e ¨20¨: '))
    print(f'Você digitou o número ¨{n_ext[n]}¨')
    sn = input('Quer continuar? ').upper()
    if sn[0] == 'N':
        break
print('Programa encerrado. Volte sempre!')