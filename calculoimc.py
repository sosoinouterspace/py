nome = 'Sofia Sacramenta'
peso = 56.0
altura = 1.60
imc = peso/(altura*altura)

#print (nome, 'tem' , altura, 'de altura,')
#print('pesa', peso, 'quilos e seu imc é {:.1f}'.format(imc))

"f-strings"
linha1 = f'{nome} tem  {altura:.2f} de altura,'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)




