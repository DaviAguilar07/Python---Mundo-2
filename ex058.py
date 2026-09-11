from random import randint
from time import sleep
jogadas = 0

print("-----Jogo de advinhação-----\n")
print("O computador está escolhendo um número de 1 a 10.\n")
sleep(1)
sleep(1)
sleep(1)
computador = randint(1, 10)

jogador = int(input("Qual o número que o computador escolheu? "))

while jogador != computador:
    jogador = int(input("Tente acertar mais uma vez: "))
    jogadas += 1

print("Você acertou em {} tentativas.\n".format(jogadas))

