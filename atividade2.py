vetor_original=[]
tamanho=int(input("Digite o tamanho do vetor:"))

#Leitura dos elementos inteiros e positivos
for i in range (tamanho):
    elementos = int(input(f"Digite o elemento{i+1}:"))
    vetor_original.append(elementos)

#Inicializando o segundo vetor
vetor_multiplicado=[]

#Aplicação das regras de transformação
for i in range(tamanho):
    if i %2==0:
        #indice par:multiplicar o elemento por 2
        novo_elemento= vetor_original[i]*2
    else:
        #indice ímpar: multiplicar o elemento por 3 
        novo_elemento= vetor_original[i]*3
    vetor_multiplicado.append(novo_elemento)
#Imprimir os dois vetores
print("Vetor original:", vetor_original)
print("Vetortransformado:", vetor_multiplicado)