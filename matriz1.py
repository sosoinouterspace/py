linhas = 3
colunas = 3

mat = []

for i in range (linhas):
    linha = []
    for j in range (colunas):
        valor = int(input(f"Digite o valor para mat [{i}][{j}]:"))
        linha.append(valor)
    mat.append(linha)

print ("Matriz mat:")
for linha in mat:
    print(linha)                   