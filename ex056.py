somaidade = 0
maioridade = 0
nomevelho = ''
mulhernova = 0


for pessoas in range(1, 5):
    print("----{}° pessoa-----\n".format(pessoas))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    somaidade += idade

    if pessoas == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhernova += 1

idademedia = somaidade / 4

print("-----Análise dos resultados-----\n")
print("A média de idade é {} anos.\n".format(idademedia))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridade, nomevelho))
print("Tem {} mulheres com menos de 20 anos.".format(mulhernova))
