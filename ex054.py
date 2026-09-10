from datetime import date
somamenor = 0
somamaior = 0
for nascimento in range (1, 8):
    anodenasc = int(input("Qual a data de nascimento da pessoa {}?".format(nascimento)))
    idade = (date.today().year - anodenasc)
    if(idade < 18):
        somamenor += 1
    else:
        somamaior += 1
print("A quantidade de pessoas que não atingiram a maior idade são: {}. E as pessoas que já atingiram a maior idade são: {}".format(somamenor, somamaior))
