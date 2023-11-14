matrizA = [[0,0], [0,0], [0,0]] 
matrizB = [[0,0], [0,0], [0,0]]  
matrizC = [[0,0], [0,0], [0,0]]       
for i in range (3):
     for j in range(2):
         elementoA = int(input(f"Digite o elemento para matriz A [{i}][{j}]:"))
         matrizA [i][j]= elementoA
     for j in range(2):
        elementoB = int(input(f"Digite o elemento para matriz B [{i}][{j}]:"))
        matrizB [i][j]= elementoB
     for j in range(2):
        matrizC [i][j] = matrizA[i][j]*matrizB[i][j]

print("Matriz MAT A: ")
for linha in matrizA:
    print (linha)  
print("Matriz MAT B: ")
for linha in matrizB:
    print (linha)  

print("Soma da matriz A com a matriz B")
for linha in matrizC:
    print(linha)