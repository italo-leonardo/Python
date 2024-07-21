def jogo(nome='desconhecido', gol=0):
    print(f'O jogador {nome} fex {gol} gol(s) no campeonato.')

nome = str(input('Digite sue nome: '))
num = str(input('Número de Gol(S): '))
if num.isnumeric():
    num = int(num)
else:
    num = 0
if nome.strip() == '':
    jogo(gol=num)
else:
    jogo(nome, num)