frase = str(input("Escreva uma frase e veja se ela é um palíndromo: ")).strip().upper()

palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1] #Macete do Python, de fatiamento.

print("A frase é {} e o inverso dela é {}".format(junto, inverso))

            #for frase in range(len(junto) - 1, -1, -1) Também daria certo
if(junto == inverso):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
