primeiro = int(input("Insira o primeiro termo da progressão artimética: "))
razao = int(input("Insira a razão da PA: "))
cont = 1
termo = primeiro
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} ->".format(termo), end = "")
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print("Progressão finalizada com {} termos mostrados.\n".format(total)) 
