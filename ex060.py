num = int(input("Insira um número para saber o valor do seu fatorial.\n"))
contador = num
fatorial = 1

print(f"{num}! = ", end="")  # início da expressão

while contador > 0:
    print(f"{contador}", end=" ")
    print("x " if contador > 1 else "= ", end="")
    fatorial *= contador
    contador -= 1

print(f"{fatorial}")
