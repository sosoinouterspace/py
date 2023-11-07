vetor1 = []
vetor2 = []
vetor_diferença = []
vetor_soma = []
vetor_mult = []


for i in range (10):
    vetor1 = int (input(f"Digite um número {i+1}:"))
    vetor2 = int (input(f"Digite um número {i+1}:"))
for _ in range (len(vetor1)):
    vetor_diferença [i] = (vetor1 [i]-vetor2[i])
    vetor_soma [i]= (vetor1 [i]+vetor2[i])   
    vetor_mult [i]= (vetor1 [i]*vetor2[i]) 

print('Vetor 1:', vetor1)
print("Vetor :", vetor2)
print('A diferença dos dois vetores:', vetor_diferença)
print('A soma dos dois vetores:', vetor_soma)
print('A multiplicação dos dois vetores', vetor_mult)

