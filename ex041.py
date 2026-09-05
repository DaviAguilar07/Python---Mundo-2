from datetime import date

anodenascimento = int(input('Insira o ano em que você nasceu: '))
idade = (date.today().year - anodenascimento)

if idade <= 9:
    print('Você é um atleta mirim.')
elif idade <= 14:
    print('Você é um atleta infantil.')
elif idade <= 19:
    print('Você é um atleta júnior.')
elif idade <= 25:
    print('Você é um atleta sênior.')
else:
    print('Você é um atleta master.')
    