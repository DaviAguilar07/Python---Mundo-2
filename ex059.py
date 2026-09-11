num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
opçao = 0
soma = 0
multiplicar = 1

while opçao != 5:
    opçao = int(input(" [1]Soma\n [2]Multiplicar\n [3]Maior\n [4]Novos números\n [5]Sair do programa\n Escolha: "))
    if opçao == 1:
        soma = num1 + num2
        print("A soma é {}\n".format(soma))

    elif opçao == 2:
        multiplicar = num1 * num2
        print("A multiplicação é {}\n".format(multiplicar))

    elif opçao == 3:
        if num1 > num2:
            print("O {} é maior que {}\n".format(num1, num2))

        elif num2 > num1:
            print("O {} é maior que {}\n".format(num2, num1))

        else: print("Os números são iguais.\n")

    elif opçao == 4:
        num1 = int(input("Digite a troca do primeiro número: "))
        num2 = int(input("Digite a troca do segundo número: "))
    else:
        print("Opção inválida.\n")
