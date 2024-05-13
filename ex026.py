frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('Há {} "A"s na sua frase'.format(frase.count('A')))
print('O primeiro "A" aparece em {}'.format(frase.find('A')+1))
print('O ultimo "A" aparece em {}'.format(frase.rfind('A')+1))


