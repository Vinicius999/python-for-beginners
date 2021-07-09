from math import radians, sin, cos, tan
a = float(input(' Angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(' Seno: {:.3f};\n Cosseno: {:.3f};\n Tangente: {:.3f}.'.format(s, c, t))
