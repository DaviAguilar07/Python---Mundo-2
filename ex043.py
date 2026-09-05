peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura*altura)

print('O seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Peso ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida')
    