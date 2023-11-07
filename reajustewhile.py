n = 1
while n <=3:
    salario = float(input('Informe o salário atual do colaborador: R$'))

    if salario <= 1500:
     percentual_aumento = 20
    elif salario <= 2000:
     percentual_aumento = 15
    elif salario <= 3000:
     percentual_aumento = 10
    else:
     percentual_aumento = 5

    aumento = (salario*percentual_aumento)/100

    print(f"Salário antes do reajuste: R${salario}")
    print(f"O percentual do aumento aplicado: {percentual_aumento}%")
    print(f"O valor do aumento é de: R${aumento}")   
    print(f"Valor do salário após o aumento: R${salario+aumento}")
    n = n+1