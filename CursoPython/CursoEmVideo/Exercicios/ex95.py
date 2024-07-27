jogado = dict()
jogos = list()
gols = list()
while True:
    jogado.clear()
    jogado['nome'] = str(input('Nome do jogador: '))
    num = int(input(f'Quantas partidas {jogado["nome"]} jogou? '))
    for i in range(0, num):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogado['gols'] = gols[:]
    jogado['total'] = sum(gols)
    gols.clear() 
    jogos.append(jogado.copy())
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == "N":
        break
print('-=' *30)
print('cod ', end='')
for i in jogado.keys():
    print(f'{i:15}', end='')
print()
print('-='*30)
for k, v in enumerate(jogos):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogos):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogos[busca]["nome"]}')
        for i, g in enumerate(jogos[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE')