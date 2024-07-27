jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for n in range(0, part):
    gols.append(int(input(f'    Quantos gols na partida {n}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols) # sum formula para fazer soma.
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Total de {jogador["total"]} gols!!!')