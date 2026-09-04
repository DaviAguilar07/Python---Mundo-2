from datetime import date
anodenasc = int(input('Informe sua data de nascimento: '))
anoatual = date.today().year
idade = date.today().year - anodenasc

if idade == 18:
    print('Este é o ano exato para fazer o alistamento militar.')
elif idade < 18:
    tempoquefalta = 18 - idade
    print('Você fará o alistamento militar daqui {} ano(s).'.format(tempoquefalta))
    anoalistar = tempoquefalta + anoatual
    print('Você irá se alistar em {}.'.format(anoalistar))
else:
    tempoquesobra = idade - 18
    print('Você deveria ter se alistado há {} ano(s).'.format(tempoquesobra))
    anoalistei =  anoatual - tempoquesobra
    print('Você se alistou em {}.'.format(anoalistei))
