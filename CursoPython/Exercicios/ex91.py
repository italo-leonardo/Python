from random import randint
lista = list()
print('Valores sorteados:')
for n in range(1, 5):
    jogadores = dict()
    num = randint(0, 10)
    jogadores['jogador'] = int(n)
    jogadores['tirou'] = int(num)
    lista.append(jogadores.copy())
    print(f'O jogador {n} tirou {num}')
print('Ranking dos Jogadores:')
for v in lista:
    print(f'O {v}')
