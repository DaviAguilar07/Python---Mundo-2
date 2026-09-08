soma = 0
cont = 0
print('Números divisiveis por 3 de 1 a 500: \n')
for c in range(1, 501, 2):
    if(c % 3 == 0):
        # print('{} '.format(c), end = '')
        cont = cont + 1
        soma = soma + c
print('A quantidade dos valores é {} e a soma de todos os valores é {}'.format(cont ,soma))
