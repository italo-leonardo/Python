def linha():
    print('-='*15)

futebol = ('Botafogo', 'Flamengo', 'Bahia', 'Athletico-PR', 'Palmeiras', 'São Paulo', 'Bragantino', 'Cruzeiro', 'Atlético-MG', 'Internacional', 'Juventude', 'Fortaleza', 'Atlético-GO', 'Cuiabá', 'Vasco', 'Corinthians', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória')
linha()
print(f'Lista de Times do Brasileirão: {futebol}')
linha()
print(f'Os 5 primeiros são: {futebol[0:5]}')
linha()
print(f'Os 4 últimos são: {futebol[16:20]}')
linha()
print(f'Times em ordem alfabética: {sorted(futebol)}')
linha()
for p in range(0, len(futebol)):
    if p == 5:
        print(f'O São Paulo está na {p}ª posição')
        break
linha()
print('O Chapecoense não esta na tabela de 2024.')