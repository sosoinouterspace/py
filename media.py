for _ in range(3):
    nome = input('Informe seu nome:')
    nota1 = float(input(nome+' informe sua primeira nota:'))
    nota2 = float(input(nome+' informe sua segunda nota:'))
    nota3 = float(input(nome+' informe sua terceira nota:'))
    nota4 = float(input(nome+' informe sua quarta nota:'))
    media = (nota1+nota2+nota3+nota4)/4
    print (f'A média do aluno {nome} é {media:.1f}')


