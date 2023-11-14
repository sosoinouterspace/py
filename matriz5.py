matrizA = [[0,0], [0,0], [0,0]] 
soma_linha = []
for i in range (3):
     soma = 0
     for j in range(2):
         elemento= int(input(f"Digite o elemento para matriz A [{i}][{j}]:"))
         matrizA [i][j]= elemento
         soma = soma + elemento
     soma_linha.append(soma)
         
         
print("Matriz MAT A: ") 
for linha in matrizA:
    print (linha)  
print("A soma das linhas da Matriz A: ", soma_linha)