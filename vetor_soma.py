
#Criação dos vetores
vetorA = [] 
vetorB = [0] * 3
vetorC = [] 

#Loop para preencher os vetores
for _ in range(3):
  elemento = int(input(f'Digite o valor na posição {_}:'))
  vetorA.append(elemento)
  
for i in range (3):
  vetorB[i] = int(input(f'Digite o valor na posição {i}:'))

#Loop para somar os vetores
for i in range (len(vetorA)):
  vetorC.append(vetorA[i]+vetorB[i]) 

#Exibir a soma dos vetores
print("Vetor C:", vetorC)