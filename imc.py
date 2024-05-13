p = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura? '))
imc = p / (alt * alt)
if imc < 16:
    print('O seu imc é de {}. Voce está na magreza grave!'.format(imc))
elif imc >= 16 and imc <= 16.9:
    print('O seu imc é de {}. Voce está na magreza moderada!'.format(imc))
elif imc >= 17 and imc <= 18.5:
    print('O seu imc é de {}. Voce está na magreza leve!'.format(imc))
else:
    print('O seu imc é de {}. Está bem!'.format(imc))
