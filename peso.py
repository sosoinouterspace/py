
soma_peso = 0
sobrepeso = 0 
for _ in range(10):
   peso = float(input("Informe seu peso em kg:"))
   altura = float(input("Informe sua altura:")) 
   
   soma_peso = soma_peso+peso

   if peso > 100.00 and altura < 1.70:
     sobrepeso = sobrepeso+1

media_peso = soma_peso/10

print (f"O número de pessoas com peso acima de 100Kg e altura menor que 1,70 m: {sobrepeso}")
print (f"A média de peso entre essas pessoas é de: {media_peso:.2f}")
     
 