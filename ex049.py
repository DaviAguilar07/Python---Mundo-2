num = int(input('Insira um número que você queira descobrir a tabuada (tabuada de 1 a 10): '))

for c in range(1,11):
    print('{} x {} = {}'.format(num, c, c*num))

