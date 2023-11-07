vetorA = [0] * 3
vetorB = [0] * 3
vetorC = [0] * 3

for i in range(3):
    vetorA [i] = int(input(f'Digite o valor da posição {i} do vetor A:'))
    vetorB [i] = int(input(f'Digite o valor da posição {i} do vetor B:'))
    vetorC [i] =  vetorA[i] + vetorB[i]
    
print('Vetor digitado:', vetorA)    
print('Vetor digitado:', vetorB)     
print('Soma do vetor A com o vetor B:',vetorC)  