
grupo1 = 0
grupo2 = 0 
grupo3 = 0
grupo4 = 0
grupo5 = 0
for _ in range(15):
    idade = float(input("Digite sua idade:"))
    
    if idade <= 15:
      grupo1 = grupo1 +1
    elif idade <=30:
     grupo2 = grupo2+1
    elif idade <=45:
     grupo3 = grupo3+1
    elif idade <=60:
     grupo4 = grupo4+1
    else:
     grupo5 = grupo5+1

print ("O número de pessoas de até 15 anos:", grupo1)
print ("O número de pessoas entre 16 e 30 anos:", grupo2 )
print ("O número de pessoas entre 31 e 45 anos:", grupo3)
print ("O número de pessoas entre 46 e 60 anos:", grupo4)
print ("O número de pessoas acima de 60 anos:", grupo5)

