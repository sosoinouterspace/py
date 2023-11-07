while True:
    valor_compra = float(input("Informe o valor da compra:"))
    if valor_compra <= 1500.00:
        percentual_desconto = 5
    elif valor_compra <= 2000.00:
        percentual_desconto = 10
    elif valor_compra <= 3000.00:
        percentual_desconto = 15
    else:
        percentual_desconto = 20
    desconto = (valor_compra*percentual_desconto)/10
    print('O valor da compra antes do desconto: R$', valor_compra)
    print('O percentual de desconto aplicado:', percentual_desconto,'%' )
    print('o valor do desconto é de: R$', desconto)
    print('O valor a ser pago após o desconto: R$', (valor_compra-desconto))
    
    continuar = input('Deseja continuar? (s/n):')
    if continuar.lower() != 's':
        break