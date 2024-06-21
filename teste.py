h, hf = map(int, input().split())
d = 0
if h >= hf:
    for i in range(h, 24 + hf):
        d += 1
else:
    for i in range(h, hf - h + 2):
        d += 1
print(f'O JOGO DUROU {d} HORA(S)')