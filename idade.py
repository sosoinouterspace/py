

maior_18 = 0
soma_idade = 0

for _ in range(10):
    idade = int(input("Digite sua idade:"))
    soma_idade = soma_idade + idade
    if idade >= 18:
      maior_18 = maior_18+1

media_idade = soma_idade/10

print ("O número de pessoas com mais de 18 anos:", maior_18)
print ("A média de idade entre essas pessoas é de:", media_idade)
