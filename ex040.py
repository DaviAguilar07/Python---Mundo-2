nota1 = float(input('Qual o valor da primeira nota: '))
nota2 = float(input('Qual o valor da segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado com {:.2f} de média.'.format(media))
elif media >= 5:
    print('Recuperação com {:.2f} de média.'.format(media))
else:
    print('Reprovado com {:.2f} de média.'.format(media))
