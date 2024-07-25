import uteis3
import uteis4
from time import sleep

arq = 'cursoemvideo.txt'

if not uteis4.arquivoExiste(arq):
    uteis3.criarArquivo(arq)

while True:
    resposta = uteis3.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        uteis3.lerArquivo(arq)
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        uteis3.cabecalho('Saindo do sistema.. Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(0.5)