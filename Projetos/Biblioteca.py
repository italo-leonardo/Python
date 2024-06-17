livro1 = livro2 = livro3 = livro4 = livro5 = None
reserva_livro1 = reserva_livro2 = reserva_livro3 = reserva_livro4 = reserva_livro5 = 0
pessoa_livro1 = pessoa_livro2 = pessoa_livro3 = pessoa_livro4 = pessoa_livro5 = None

def exibir_menu():
    print('===== Menu Principal =====')
    print('1. Cadastrar livros')
    print('2. Acervo')
    print('3. Reservar')
    print('4. Renovar')
    print('5. Devolver')
    print('6. passar dia')
    print('0. Sair')

def passar_dias():
    global reserva_livro1,reserva_livro2,reserva_livro3,reserva_livro4,reserva_livro5
    if reserva_livro1 > 0 :
        reserva_livro1 -= 1
    if reserva_livro2 > 0 :
        reserva_livro2 -= 1
    if reserva_livro3 > 0 : 
        reserva_livro3 -= 1
    if reserva_livro4 > 0 : 
        reserva_livro4 -= 1
    if reserva_livro5 > 0 : 
        reserva_livro5 -= 1
    return reserva_livro1, reserva_livro2, reserva_livro3, reserva_livro4, reserva_livro5

def cadastrar_livro():
    global livro1, livro2, livro3, livro4, livro5
    print("-"*30)
    print("     CADASTRO DE LIVROS    ")
    print("-"*30)
    if livro1 is None:
        livro1 = input('Digite o título do primeiro livro: ')
        print("Cadastor realizado com sucesso !")
    elif livro2 is None:
        livro2 = input('Digite o título do segundo livro: ')
        print("Cadastor realizado com sucesso !")
    elif livro3 is None:
        livro3 = input('Digite o título do terceiro livro: ')
        print("Cadastor realizado com sucesso !")
    elif livro4 is None:
        livro4 = input('Digite o título do quarto livro: ')
        print("Cadastor realizado com sucesso !")
    elif livro5 is None:
        livro5 = input('Digite o título do quinto livro: ')
        print("Cadastor realizado com sucesso !")
    else:
        print('Capacidade máxima de livros cadastrados atingida.')

def exibir_acervo():
    global reserva_livro1, reserva_livro2, reserva_livro3, reserva_livro4, reserva_livro5
    print('\nAcervo:')
    if livro1:
        print(f'- {livro1} {f"(Indisponível, restam {reserva_livro1} dia(s))" if reserva_livro1 > 0 else "(Disponível)"}')
    if livro2:
        print(f'- {livro2} {f"(Indisponível, restam {reserva_livro2} dia(s))" if reserva_livro2 > 0 else "(Disponível)"}')
    if livro3:
        print(f'- {livro3} {f"(Indisponível, restam {reserva_livro3} dia(s))" if reserva_livro3 > 0 else "(Disponível)"}')
    if livro4:
        print(f'- {livro4} {f"(Indisponível, restam {reserva_livro4} dia(s))" if reserva_livro4 > 0 else "(Disponível)"}')
    if livro5:
        print(f'- {livro5} {f"(Indisponível, restam {reserva_livro5} dia(s))" if reserva_livro5 > 0 else "(Disponível)"}')

def reservar_livro():
    global livro1, livro2, livro3, livro4, livro5
    global reserva_livro1, reserva_livro2, reserva_livro3, reserva_livro4, reserva_livro5
    global pessoa_livro1, pessoa_livro2, pessoa_livro3, pessoa_livro4, pessoa_livro5
    titulo = input('Digite o título do livro que deseja reservar: ')
    if titulo == livro1 and reserva_livro1 == 0:
        pessoa_livro1 = input('Digite seu nome: ')
        reserva_livro1 = 7
        print(f'O livro {livro1} foi reservado com sucesso para {pessoa_livro1} por 7 dias.')
    elif titulo == livro2 and reserva_livro2 == 0:
        pessoa_livro2 = input('Digite seu nome: ')
        reserva_livro2 = 7  
        print(f'O livro {livro2} foi reservado com sucesso para {pessoa_livro2} por 7 dias.')
    elif titulo == livro3 and reserva_livro3 == 0:
        pessoa_livro3 = input('Digite seu nome: ')
        reserva_livro3 = 7
        print(f'O livro {livro3} foi reservado com sucesso para {pessoa_livro3} por 7 dias.')
    elif titulo == livro4 and reserva_livro4 == 0:
        pessoa_livro4 = input('Digite seu nome: ')
        reserva_livro4 = 7
        print(f'O livro {livro4} foi reservado com sucesso para {pessoa_livro4} por 7 dias.')
    elif titulo == livro5 and reserva_livro5 == 0:
        pessoa_livro5 = input('Digite seu nome: ')
        reserva_livro5 = 7
        print(f'O livro {livro5} foi reservado com sucesso para {pessoa_livro5} por 7 dias.')
    else:
        print(f'Livro indisponível ou não encontrado.')

def devolver_livro():
    global reserva_livro1, reserva_livro2, reserva_livro3, reserva_livro4, reserva_livro5
    titulo = input('Digite o título do livro que deseja devolver: ')
    dias_com_o_livro = int(input('Quantos dias você ficou com o livro? '))
    if titulo == livro1 and reserva_livro1 > 0:
        if dias_com_o_livro > 7:
            multa = dias_com_o_livro - 7
            print(f'O livro {livro1} está atrasado. Multa de R$ {multa} pelo atraso.')
        else:
            print('Obrigado por devolver o livro no prazo!')
        reserva_livro1 = 0
    elif titulo == livro2 and reserva_livro2 > 0:
        if dias_com_o_livro > 7:
            multa = dias_com_o_livro - 7
            print(f'O livro "{livro2}" está atrasado. Multa de R$ {multa} pelo atraso.')
        else:
            print('Obrigado por devolver o livro no prazo!')
        reserva_livro2 = 0
    elif titulo == livro3 and reserva_livro3 > 0:
        if dias_com_o_livro > 7:
            multa = dias_com_o_livro - 7
            print(f'O livro {livro3} está atrasado. Multa de R$ {multa} pelo atraso.')
        else:
            print('Obrigado por devolver o livro no prazo!')
        reserva_livro3 = 0
    elif titulo == livro4 and reserva_livro4 > 0:
        if dias_com_o_livro > 7:
            multa = dias_com_o_livro - 7
            print(f'O livro {livro4} está atrasado. Multa de R$ {multa} pelo atraso.')
        else:
            print('Obrigado por devolver o livro no prazo!')
        reserva_livro4 = 0
    elif titulo == livro5 and reserva_livro5 > 0:
        if dias_com_o_livro > 7:
            multa = dias_com_o_livro - 7
            print(f'O livro {livro5} está atrasado. Multa de R$ {multa} pelo atraso.')
        else:
            print('Obrigado por devolver o livro no prazo!')
        reserva_livro5 = 0
    else:
        print('Este livro não está reservado ou não foi encontrado.')

def renovar_reserva():
    global reserva_livro1, reserva_livro2, reserva_livro3, reserva_livro4, reserva_livro5
    titulo = input('Digite o título do livro que deseja renovar a reserva: ')
    if titulo == livro1 and reserva_livro1 > 0:
        if 1 <= reserva_livro1 <= 3:
            reserva_livro1 = 7
            print(f'A reserva do livro {livro1} foi renovada por mais 7 dias.')
        else:
            print('A renovação só pode ser feita de 1 a 3 dias antes do fim da reserva.')
    elif titulo == livro2 and reserva_livro2 > 0:
        if 1 <= reserva_livro2 <= 3:
            reserva_livro2 = 7
            print(f'A reserva do livro {livro2} foi renovada por mais 7 dias.')
        else:
            print('A renovação só pode ser feita de 1 a 3 dias antes do fim da reserva.')
    elif titulo == livro3 and reserva_livro3 > 0:
        if 1 <= reserva_livro3 <= 3:
            reserva_livro3 = 7
            print(f'A reserva do livro {livro3} foi renovada por mais 7 dias.')
        else:
            print('A renovação só pode ser feita de 1 a 3 dias antes do fim da reserva.')
    elif titulo == livro4 and reserva_livro4 > 0:
        if 1 <= reserva_livro4 <= 4:
            reserva_livro4 = 7
            print(f'A reserva do livro {livro4} foi renovada por mais 7 dias.')
    elif titulo == livro5 and reserva_livro5 > 0:
        if 1 <= reserva_livro5 <= 4:
            reserva_livro5 = 7
            print(f'A reserva do livro {livro5} foi renovada por mais 7 dias.')
        else:
            print('A renovação só pode ser feita de 1 a 4 dias antes do fim da reserva.')
    else:
        print('Não há reserva para este livro ou livro não encontrado.')
       
while True:
    exibir_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
      while True:  
        cadastrar_livro()
        continuar = input('Deseja cadastrar outro livro? S / N ')
        if continuar == 'N' or continuar == 'n':
            break
        elif continuar == 'S' or continuar == 's':
            cadastrar_livro() 
            continuar = input('Deseja cadastrar outro livro? S / N ')
        if continuar == 'N' or continuar == 'n':
            break
        elif continuar == 'S' or continuar == 's':
            cadastrar_livro()
            continuar = input('Deseja cadastrar outro livro? S / N ')
        if continuar == 'N' or continuar == 'n':
            break
        elif continuar == 'S' or continuar == 's':
            cadastrar_livro()
            continuar = input('Deseja cadastrar outro livro? S / N  ')
        if continuar == 'N' or continuar == 'n':
            break
        elif continuar == 'S' or continuar == 's':
            cadastrar_livro()
            print('Você cadastrou 5 livros, acervo cheio!\n1 = voltar ao MENU\n2 = Encerrar o programa')
            opcao = int(input('Digite o número referente a opção desejada: '))
            if opcao == 1:
                break
            elif opcao == 2:
                exit()
                
    elif opcao == '2':
      while True:  
        exibir_acervo()
        print('1 = voltar ao MENU\n2 = Encerrar o programa')
        opcao = int(input('Digite o número referente a opção desejada: '))
        if opcao == 1:
            break
        elif opcao == 2:
            exit()
    elif opcao == '3':
      while True:  
        exibir_acervo()
        reservar_livro()
        print('1 = voltar ao MENU\n2 = Encerrar o programa')
        opcao = int(input('Digite o número referente a opção desejada: '))
        if opcao == 1:
            break
        elif opcao == 2:
            exit()
    elif opcao == '4':
       while True: 
        renovar_reserva()
        print('1 = voltar ao MENU\n2 = Encerrar')
        opcao = int(input('Digite o número referente a opção desejada: '))
        if opcao == 1:
            break
        elif opcao == 2:
            exit()
    elif opcao == '5':
       while True: 
        devolver_livro()
        print('1 = voltar ao MENU\n2 = Encerrar o programa')
        opcao = int(input('Digite o número referente a opção desejada: '))
        if opcao == 1:
            break
        elif opcao == 2:
            exit()
    elif opcao == '6':
        passar_dias()
        print(passar_dias())       
    elif opcao == '0':
        print('Você encerrou o programa!')
        break
    else:
        print('Opção inválida, tente novamente, Escolha uma opção válida do menu.')

#Antonio Alison Deodato Silva e Ítalo Leonardo Coelho Oliveira.