from math import sin, cos, tan, radians
a = int(input('Qual ângulo quer ter as informações? : '))

seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('sen = {:.2f} \ncos = {:.2f} \ntan = {:.2f}'.format(seno, cosseno, tangente))
