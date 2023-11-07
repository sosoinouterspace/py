
while True:
    nome = input('Informe seu nome:')
    nota1 = float(input(nome+' informe sua primeira nota:'))
    nota2 = float(input(nome+' informe sua segunda nota:'))
    nota3 = float(input(nome+' informe sua terceira nota:'))
    nota4 = float(input(nome+' informe sua quarta nota:'))
    freq = float(input(nome+' informe o percentual de frequência:'))
    media = (nota1+nota2+nota3+nota4)/4

    if media>= 7 and freq>=75:
        print(f'O aluno {nome} foi aprovado com média {media:.1f} e percentual de freqûencia de {freq} %')
    elif media >=5 and freq>=50:
        print(f'O aluno {nome} está em recuperação com {media:.1f} e percentual de freqûencia de {freq} %')
        notarec= float(input(nome+' informe a nota da recuperação:'))
        novamedia = (media+notarec)/2
        print(f'A nova média do aluno {nome} é {novamedia:.1f}')
        if novamedia>=6:
            print('O aluno' , nome , 'foi aprovado após a recuperação')
        else:
            print('O aluno foi reprovado após a recuperação')

    else:
        print(f'O aluno {nome} foi reprovado com média {media:.1f} e percentual de freqûencia de {freq} %') 


    continuar = input('Deseja continuar? (s/n):')
    if continuar.lower() != 's':
        break