km = float(input('Quantos kms rodou com o carro alugado? Kms: '))
dias = float(input('Quantos dias ficou com o carro? Dias:'))
pkm = 0.15 * km
pdias = 60 * dias
print('O carro ficará R${}, sendo R${} de quilometragem e R${} de dias alugados'.format(pkm+pdias, pkm, pdias))
