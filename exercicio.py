matrizA = [[0,0],[0,0],[0,0]]
matrizB = [[0,0],[0,0],[0,0]]
matrizC = [[0,0],[0,0],[0,0]]

for i in range (3):
    for j in range (2):
     elemento = int(input(f"Digite os elementos da matriz A [{i}][{j}]: "))
     matrizA[i][j]=elemento
for i in range (3):
    for j in range (2):    
     elemento = int(input(f"Digite os elementos da matriz B [{i}][{j}]: "))
     matrizB[i][j]=elemento
    for j in range (2):
     matrizC [i][j] = matrizA[i][j]-matrizB[i][j]

print ("Matriz A:")
for linha in matrizA:
   print (linha)
print ("Matriz B:")
for linha in matrizB:
   print (linha) 
print ("Matriz C:")
for linha in matrizC:
   print (linha) 