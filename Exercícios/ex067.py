while True:
    n = int(input(' Quer ver a tabuada de que valor? '))
    print('-'*30)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n:^2}x {cont:^2} = {n*cont}')
    print('-'*30)
print(' >> PROGRAMA TABUADA ECERRADO!')