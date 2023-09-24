p1 = float(input('Informe o preço do primeiro produto:'))
p2 = float(input('Informe o preço do segundo produto:'))
p3 = float(input('Informe o preço do terceiro produto:'))

if p1 <= p2 and p1 <= p3:
    menor_preco = p1
elif p2 <= p3:
    menor_preco = p2
else:
    menor_preco = p3

if p1 >= p2 and p1 >= p3:
 maior_preco = p1
elif p2 >= p3:
 maior_preco = p2
else:
 maior_preco = p3

print(f"Preço do primeiro produto: R${p1:.2f}")
print(f"Preço do segundo produto: R${p2:.2f}") 
print(f"Preço do terceiro produto: R${p3:.2f}")
print(f"O menor preço dos produtos é: R${menor_preco:.2f}")   
print(f"O maior preço dos produtos é: R${maior_preco:.2f}")   