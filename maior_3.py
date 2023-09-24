n1 = float(input('Informe o primeiro número:'))
n2 = float(input("Informe o segundo número:"))
n3 = float(input("Informe o terceiro número:"))

maior = n1
menor = n1

if n2 > maior:
    maior =n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior =n3
elif n3 < menor:
    menor = n3

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')