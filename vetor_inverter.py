vetor_original = []
vetor_invertido = []

tamanho = int(input("Digite o tamanho do vetor:"))
for i in range (tamanho):
    elemento = int(input(f"Digite o elemento {i+1}"))
    vetor_original.append (elemento)

#Criar um segundo vetor com elementos na orndem invertida
for i in range(tamanho):
    vetor_invertido.append (vetor_original[tamanho-i-1])

#Imrpimir os dois vetores
print("Vetor Original:", vetor_original)
print('Vetor Invetido:', vetor_invertido)