t = int(input(' Quer ver a tabuada de qual número? '))
print('-'*12, 'TABUADA DO {}'.format(t), 12*'-')
for c in range(1, 10+1):
    print('    {} + {:^2} = {} '.format(t, c, t+c))
