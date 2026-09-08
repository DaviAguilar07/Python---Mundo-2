soma = 0
cont = 0
for c in range(0,6):
    num = int(input("Insira um número: "))
    cont += 1
    if(num % 2 == 0):
        soma += num
    else:
        continue
print("Você digitou {} números e a soma de todos os números pares digitados foi: {}".format(cont, soma))
