valordacasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempoprestaçao = int(input('Em quantos anos você pretende pagar a casa? '))


prestaçaoanual = (valordacasa / tempoprestaçao)
prestaçaomensal = (prestaçaoanual / 12)


valormaximodeprestaçao = (salario * 0.30)

if prestaçaomensal > valormaximodeprestaçao:
    print('Não será possível fazer o financiamento.')
else:
    print('O financiamento foi liberado.')
