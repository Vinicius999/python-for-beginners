quant = s = 0
while True:
    n = int(input(' Digite o  número (999 para parar): '))
    if n == 999:
        break
    quant += 1
    s += n
print(f' A soma dos {quant} valores deu {s}')
