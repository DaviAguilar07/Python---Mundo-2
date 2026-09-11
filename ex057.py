sexo = str(input("Qual o seu sexo [M/F]? ")).upper()[0].strip()

while sexo not in ['M', 'F']:
    sexo = str(input("Qual o seu sexo [M/F]? Insira novamente: ")).upper()[0].strip()

if sexo == 'M':
    print("Masculino\n")
elif sexo == 'F':
    print("Feminino\n")
