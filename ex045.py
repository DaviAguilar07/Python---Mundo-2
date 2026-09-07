import random
from time import sleep

print('{:=^40}'.format(' Jogo de pedra, papel ou tesoura '))
itens = ('Pedra', 'Papel', 'Tesoura')
jokenpo = int(input('0)Pedra\n1)Papel\n2)Tesoura\n Escolha: '))
escolhacomputador = random.randint(0,2)

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)

print('{:=^40}'.format(''))

if jokenpo == 0 and escolhacomputador == 0:
    print('Empate')
elif jokenpo == 1 and escolhacomputador == 1:
    print('Empate')
elif jokenpo == 2 and escolhacomputador == 2:
    print('Empate')
elif jokenpo == 0 and escolhacomputador == 2 or jokenpo == 1 and escolhacomputador == 0 or jokenpo == 2 and escolhacomputador == 1:
    print('Você ganhou!')
elif escolhacomputador == 0 and jokenpo == 2 or escolhacomputador == 1 and jokenpo == 0 or escolhacomputador == 2 and jokenpo == 1:
    print('O computador ganhou.')

print('O computador escolheu: {}. Você escolheu: {}.'.format(itens[escolhacomputador], itens[jokenpo]))
