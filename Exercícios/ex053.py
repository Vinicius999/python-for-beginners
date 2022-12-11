f = input(' Digite uma frase para saber se é um palíndromo: ').upper().strip()
f = f.replace(' ', '')
inv = f[::-1]
print(' O inverso de ¨{}¨ é ¨{}¨'.format(f, inv))
print('>Temos um palíndromo' if f == inv else '>Não é um palíndromo')