d = float(input(' Distância total da viagem [km]: '))
print(' Valor da passagem: R${:.2f}'.format(d*0.5) if d <= 200 else ' Valor da passagem: R${:.2f}'.format(d*0.45))
