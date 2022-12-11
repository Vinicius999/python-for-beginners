v = float(input(' Velocidade do carro [km/h]: '))
if v > 80:
    print(' Você foi multado em R${:.2f}'.format((v-80)*7))
