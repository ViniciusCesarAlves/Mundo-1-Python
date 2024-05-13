import math
cat1 = float(input('Cateto oposto: '))
cat2 = float(input('Cateto adjacente: '))
hip = math.sqrt((cat1**2 + cat2**2))
print('A hipotenusa vai medir {}'.format(hip))
