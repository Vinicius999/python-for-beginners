alt = float(input(' Altura da parede [m]: '))
lar = float(input(' Largura da parede [m]: '))
area = alt * lar
tinta = area / 2
print(' A área da parede é {} m² e será necessário {} l de tinta para pintá-la.'.format(area, tinta))
