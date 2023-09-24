salario = float(input('Informe seu salário atual:'))

if salario <= 1500:
    percentual_aumento = 20
elif salario <= 2000:
    percentual_aumento = 15
elif salario <= 3000:
    percentual_aumento = 10
else:
    percentual_aumento = 5
    
   