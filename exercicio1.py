matriz = [[0,0],[0,0],[0,0]]
soma = 0
for i in range (3):
    for j in range (2):
        elemento = int(input(f"Digite os elementos da matriz [{i}][{j}]:"))
        matriz [i][j] = elemento
        soma = soma + elemento

print ('Matriz:')
for linha in matriz:
    print(linha)

print(f'A soma da matriz é: {soma}')