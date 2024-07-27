import uteis3
import uteis4
from time import sleep

arq = 'cursoemvideo.txt'

if not uteis4.arquivoExiste(arq):
    uteis3.criarArquivo(arq)

while True:
    resposta = uteis3.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um pessoa.
        uteis3.lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        uteis3.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = uteis3.leiaInt('Idade: ')
        uteis3.cadastar(arq, nome, idade)
    elif resposta == 3:
        #Opção de fecha a programa.
        uteis3.cabecalho('Saindo do sistema.. Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(0.5)