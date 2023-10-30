vetora = [0]*3
vetorb = [0]*3
vetorc = [0]*3
for i in range(3):
    vetora[i]= int(input(f"Digite o valor da posição {i}:"))
    vetorb[i]= int(input(f"Digite o valor da posição {i}:"))
    vetorc[i]=vetora[i]+vetorb[i]
print("Vetor digitado:", vetora)
print("Vetor digitado:", vetorb)
print("Vetor que corresponde à soma dos vetores", vetorc)