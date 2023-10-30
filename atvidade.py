vetororiginal = [] 
vetorinvertido = []

tamanho=int(input("Informe o tamanho do vetor :"))
for i in range(tamanho):
    elemento=int(input(f"Informe o elemento {i + 1}:"))
    vetororiginal.append(elemento)
for i in range(tamanho):
    vetorinvertido.append(vetororiginal[ tamanho -i-1 ])

print("O valor original é ",vetororiginal)
print("O valor invertido  é ",vetorinvertido)