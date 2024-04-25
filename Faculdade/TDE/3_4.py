contador = 0
primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
quinto = 0
pessoa = 'a'
dias = 0
while True:
    print('_'*63)
    print("Menu Principal")
    print('1 = Cadastrar')
    print('2 = Acervo')
    print('3 = Reservar') 
    print('4 = Renovar')
    print('5 = devolver')
    op = int(input("Escolha uma opção: "))
    if op == 1:
        #Cadastramento de livro
        while True:
            print('_'*50)
            print('  C A D A S T R A M E N T O   D E   L I V R O S')
            print('-'*50)
            if op == 1:
             livro1 = input('Digite o titulo do livro: ')
             primeiro = livro1
             contador += 1
             print(f'{livro1} foi cadastrado com sucesso!\n')
             print('1 = Voltar ao menu princiapl\n2 = Cadastrar mais um livro')
             caminho = int(input('Digite o número referente a ação desejada: '))
            if caminho == 1:
                break
            elif caminho == 2:
                livro2 = input('Digite o titulo do livro: ')
                segundo = livro2
                contador += 1
                print(f'{livro2} foi cadastrado com sucesso!\n')
                print('1 = Voltar ao menu princiapal\n2 = Cadastrar mais um livro')
                caminho2 = int(input('Digite p número referente a ação desejada: '))
            if caminho2 == 1:
                break
            elif caminho2 == 2:
                livro3 = input('Digite o titulo do livro: ')
                terceiro = livro3
                contador += 1
                print(f'{livro3} foi cadastrado com sucesso!\n')
                print('1 = Voltar ao menu principal\n2 = Cadastrar mais um livro')
                caminho3 = int(input('Digite o número referente a ação desejada: '))
            if caminho3 == 1:
                break
            elif caminho3 == 2:
                livro4 = input('Digite o titulo do livro: ')
                quarto = livro4
                contador += 1
                print(f'{livro4} foi cadastrado com sucesso!\n')
                print('1 = Voltar ao menu principal\n2 = Cadastrar mais um livro')
                caminho4 = int(input('Digite o número referente a ação desejada: '))
            if caminho4 == 1:
                break
            elif caminho4 == 2:
                livro5 = input('Digite o titulo do livro: ')
                quinto = livro5
                contador += 1
                print(f'{livro5} foi cadastrado com sucesso!\n')
                print('1 = Fechar o programa\n2 = voltar ao menu principal')
                caminho5 = int(input('Digite o número referente a ação desejada: '))
            if caminho5 == 1: 
                print('Volte sempre!')
                exit()
            elif caminho5 == 2:
                break      
    elif op == 2:
        #Vizualizar acervo
        while True:
            print('_'*50)
            print('                   A C E R V O')
            print('-'*50)
            if contador == 0:
             print('Nenhum livro cadastrado, o acervo está vazio!') 
             print('1 = Fechar o programa\n2 = voltar ao menu principal')
             opção = int(input('Digite o número referentea ação desejada: '))
             if opção == 1:
                print('Volte sempre!')
                exit()
             elif opção == 2:
                break  
            if contador == 1:
                print(livro1)
            if contador == 2:
                print(livro1)
                print(livro2)
            if contador == 3:
                print(livro1)
                print(livro2)
                print(livro3)
            if contador == 4:
                print(livro1)
                print(livro2)
                print(livro3)
                print(livro4)
            if contador >= 5:
                print(livro1)
                print(livro2)
                print(livro3)
                print(livro4)
                print(livro5)                
            print('1 = Fechar o programa\n2 = voltar ao menu principal')
            caminho = int(input('Digite o número referente a ação desejada: '))
            if caminho == 1: 
             print('Volte sempre!')
             exit()
            elif caminho == 2:
             break      
                 
           
    elif op == 3:
        while True:
            #reservar livro
            print('ATENÇÃO! as resevas tem um prazo pré estabelecido de 7 dias, se você ao fim deste prazo não renovar ou devolver\no livro, será sobrado uma taxa de R$1,00 por dia de atraso!')
            nome = input('Digite seu nome: ')
            pessoa = nome
            if contador == 0:
                print('Sem livros no sistema.')
                print('1 = Fechar o programa\n2 = voltar ao menu principal')
                caminho = int(input('Digite o número referentea ação desejada: '))
                if caminho == 1:
                    print('Volte sempre!')
                    exit()
                elif caminho == 2:
                    break       
            elif contador == 1:    
             print(livro1)
            elif contador == 2: 
             print(f'1 = {livro1}\n2 = {livro2}')
            elif contador == 3: 
             print(f'1 = {livro1}\n2 = {livro2}\n3 = {livro3}')
            elif contador == 4:  
             print(f'1 = {livro1}\n2 = {livro2}\n3 = {livro3}\n4 = {livro4}')
            elif contador == 5:  
             print(f'1 = {livro1}\n2 = {livro2}\n3 = {livro3}\n4 = {livro4}\n5 = {livro5}')
            reserva = int(input('Digite o número referente ao titulo desejado: '))
            if reserva == 1:
                print(f'{livro1} reservado para {nome} por 7 dias, boa leitura!')
                print('1 = Fechar o programa\n2 = voltar ao menu principal')
                caminho = int(input('Digite o número referentea ação desejada: '))
                if caminho == 1:
                    print('Volte sempre!')
                    exit()
                elif caminho == 2:
                    break 
            elif reserva == 2:
                print(f'{livro2} reservado para {nome} por 7 dias, boa leitura!')
                print('1 = Fechar o programa\n2 = voltar ao menu principal')
                caminho = int(input('Digite o número referentea ação desejada: '))
                if caminho == 1:
                    print('Volte sempre!')
                    exit()
                elif caminho == 2:
                    break
            elif reserva == 3:
                print(f'{livro3} reservado para {nome} por 7 dias, boa leitura!')
                print('1 = Fechar o programa\n2 = voltar ao menu principal')
                caminho = int(input('Digite o número referentea ação desejada: '))
                if caminho == 1:
                    print('Volte sempre!')
                    exit()
                elif caminho == 2:
                    break
            elif reserva == 4:
                print(f'{livro4} reservado para {nome} por 7 dias, boa leitura!')
                print('1 = Fechar o programa\n2 = voltar ao menu principal')
                caminho = int(input('Digite o número referentea ação desejada: '))
                if caminho == 1:
                    print('Volte sempre!')
                    exit()
                elif caminho == 2:
                    break
            elif reserva == 5:
                print(f'{livro5} reservado para {nome} por 7 dias, boa leitura!')
                print('1 = fechar o programa\n2 = voltar ao menu principal')
                caminho = int(input('Digite o número referente a ação desejada: '))
                if caminho == 1:
                    print('Volte sempre')
                    exit()
                elif caminho == 2:
                    break                
                
    else:
        print('_'*63)
        print('\nATENÇÃO: Digite um número relacionado a uma das opçõs do menu!')