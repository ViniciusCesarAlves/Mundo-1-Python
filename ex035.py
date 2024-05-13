a1 = float(input('Primeiro lado: '))
a2 = float(input('Segundo lado: '))
a3 = float(input('Terceiro lado: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')
