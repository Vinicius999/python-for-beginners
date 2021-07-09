r1 = float(input(' Comprimento da reta 1: '))
r2 = float(input(' Comprimento da reta 2: '))
r3 = float(input(' Comprimento da reta 3: '))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    if r1 == r2 == r3:
        print('>> As retas foram um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3:
        print('>> As retas formam um triângulo ESCALENO.')
    else:
        print('>> As retas formar um triângulo ISÓSCELES.')
else:
    print('>> As retas não podem formar um triângulo.')