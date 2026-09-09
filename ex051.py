print("-----Progressão aritmética-----")
primeiro = int(input("Qual vai ser o primeiro termo dessa progressão aritmética? "))
razao = int(input("Qual vai ser a razão dessa progressão aritmética? "))
enesimo = primeiro + (10 - 1) * razao

for c in range(primeiro, enesimo + razao, razao):
    print("{} ".format(c), end =" ")
print("-> Fim")
