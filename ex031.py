km = float(input('Quantos KMs será a sua viagem? Digite os kms usando .: '))
ate200 = km * 0.50
mais200 = km * 0.45
if km <= 200:
    print('A sua passagem ficará R${}!'.format(ate200))
else:
    print('A sua passagem custará R${}!'.format(mais200))
print(' ')
