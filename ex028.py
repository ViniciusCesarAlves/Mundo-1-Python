import random, time
num = random.randint(0, 5)
print('Venha brincar comigo!')
print('Adivinhe o número em que estou pensando!')
print('Um minuto, deixe-me pensar mais um pouco!')
print('(Pensando...)')
time.sleep(3)
escolha = int(input('Adivinhe o número entre 0 e 5:'))
print('O numero escolhido pelo computador foi {} e o seu foi {}'.format(num, escolha))
if escolha == num:
    print('VOCE GANHOU O JOGO!')
else:
    print('Eu ganhei!')
print(40*"-")
