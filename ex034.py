sal_i = float(input('Digite o seu salário atual: '))
if sal_i > 1250.00:
    print('O seu novo salário é de R${}'.format(sal_i * 110/100))
else:
    print('O seu novo salário é de R${}'.format(sal_i * 115/100))
