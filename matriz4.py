matrizA = [[0,0], [0,0]] 
soma = 0
for i in range (2):
     for j in range(2):
         elementoA = int(input(f"Digite o elemento para matriz A [{i}][{j}]:"))
         matrizA [i][j]= elementoA
         if i == j:
          soma = soma + elementoA

print("Matriz MAT A: ") 
for linha in matrizA:
    print (linha)  
print("Soma da diagonal da Matriz A: ", soma)