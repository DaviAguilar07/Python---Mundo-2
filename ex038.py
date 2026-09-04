num1 = float(input('Digite um número inteiro: '))
num2 = float(input('Digite um número inteiro: '))

if num1 > num2:
    print('O {:.2f} é maior que {:.2f}'.format(num1, num2))
elif num2 > num1:
    print('O {:.2f} é maior que {:.2f}'.format(num2, num1))
else:
    print('Os dois números são iguais.')
