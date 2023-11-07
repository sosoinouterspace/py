vetor1 = []
vetor2 = []
vetor_diferença = []
vetor_soma = []
vetor_mult = []


for i in range (10):
    elemento = int (input(f"Digite o elemento {i+1} para o vetor 1:"))
    vetor1.append(elemento)

for i in range (10):
    elemento2 = int (input(f"Digite o elemento {i+1} para o vetor 2:"))
    vetor2.append(elemento2)

for i in range (len(vetor1)):
    vetor_diferença.append(vetor1 [i] - vetor2[i])
    vetor_soma.append(vetor2 [i]+vetor2[i])
    vetor_mult.append(vetor1 [i]*vetor2[i]) 

print('Vetor 1:', vetor1)
print("Vetor :", vetor2)
print('A diferença dos dois vetores:', vetor_diferença)
print('A soma dos dois vetores:', vetor_soma)
print('A multiplicação dos dois vetores', vetor_mult)

