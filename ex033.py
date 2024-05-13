a1 = int(input('Primeiro valor: '))
a2 = int(input('Segundo valor: '))
a3 = int(input('Terceiro valor: '))
if a1 > a2 > a3:
    print('O maior número é {} e o menor é {}'.format(a1, a3))
elif a1 > a3 > a2:
    print('O maior número é {} e o menor é {}'.format(a1, a2))
elif a2 > a1 > a3:
    print('O maior número é {} e o menor é {}'.format(a2, a3))
elif a2 > a3 > a1:
    print('O maior número é {} e o menor é {}'.format(a2, a1))
elif a3 > a1 > a2:
    print('O maior número é {} e o menor é {}'.format(a3, a2))
elif a3 > a2 > a1:
    print('O maior número é {} e o menor é {}'.format(a3, a1))
else:
    print('Todos os números são iguais!')
