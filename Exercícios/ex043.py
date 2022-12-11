peso = float(input(' Peso [Kg]: '))
altura = float(input(' Altura [metros]:' ))
imc = peso/(altura**2)
if imc < 18.5:
    print(' IMC = {:.1f} > Abaixo do peso'.format(imc))
elif imc < 25:
    print(' IMC = {:.1f} > Peso ideal'.format(imc))
elif imc < 30:
    print(' IMC = {:.1f} > Sobrepeso'.format(imc))
elif imc < 40:
    print(' IMC = {:.1f} > Obesidade'.format(imc))
else:
    print(' IMC = {:.1f} > Obesidade Mórbida'.format(imc))