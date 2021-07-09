r1 = float(input(' comprimento de r1: '))
r2 = float(input(' comprimento de r2: '))
r3 = float(input(' comprimento de r3: '))
if abs(r2-r3) < r1 < r2+r3 or abs(r1-r3) < r2 < r1+r3 or abs(r1-r2) < r3 < r1+r2:
    print(' r1, r2 e r3 PODEM FORMAR um triâncgulo!')
else:
    print(' r1, r2 e r3 NÃO PODEM FORMAR um triângulo!')
