vel = float(input('Qual a velocidade atual do carro: '))
veloc = (vel - 80) * 7
if vel <= 80:
    print('Obrigado por seguir as leis de transito!')
else:
    print('Voce passou {} km/h a mais que o permitido, a multa foi de R${}'.format(vel-80, veloc))
