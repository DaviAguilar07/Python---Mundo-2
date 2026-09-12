primeiro = int(input("Insira o primeiro termo da progressão artimética: "))
razao = int(input("Insira a razão da PA: "))
contador = 1
termo = primeiro

while contador <= 10:
    print(" {} ->".format(termo), end = "")
    termo += razao
    contador += 1

print("FIM\n")
