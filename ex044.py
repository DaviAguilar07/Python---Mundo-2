print('{:=^40}'.format(' Varejão '))

valorproduto = float(input('Qual é o valor do produto? R$'))
parcelamento = int(input('Qual a forma de pagamento?\n 1)Á vista dinheiro/cheque\n 2)Á vista no cartão\n 3)2x no cartão\n 4)3x ou mais no cartão\n Escolha: '))


if parcelamento == 1:
    desconto = valorproduto - (valorproduto * 0.1)
    print('O valor da compra é R${:.2f}, com desconto fica R${:.2f}.'.format(valorproduto, desconto))
elif parcelamento == 2:
    descontocartao = valorproduto - (valorproduto * 0.05)
    print('O valor da compra é R${:.2f}, com desconto fica R${:.2f}.'.format(valorproduto, descontocartao))
elif parcelamento == 3:
    desconto2xcartao = valorproduto / 2
    print('O valor da compra é R${:.2f}, a primeira parcela é R${:.2f}.'.format(valorproduto, desconto2xcartao))
elif parcelamento == 4:
    juros3xcartao = valorproduto + (valorproduto * 0.2)
    valorjuros = (valorproduto * 0.2)
    escolhaonumdeparcelas = int(input('Escolha quantas parcelas você quer fazer: '))
    parcela3xcartao = juros3xcartao / escolhaonumdeparcelas
    print('O valor da compra é R${:.2f}, com R${:.2f} de juros, fica {:.2f}. A primeira parcela é R${:.2f}.'.format(valorproduto, valorjuros, juros3xcartao, parcela3xcartao))
else:
    print('Escolha inválida.')
