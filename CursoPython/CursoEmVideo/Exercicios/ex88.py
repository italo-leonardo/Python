from random import randint
from time import sleep
sena = list()
cop = list()
print('-'*30)
print('     JOGO NA MEGA SENA   ')
print('-'*30)

num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*4 ,f' SORTEANDO {num} JOGOS ','-='*4) 
cont = 0
tot = 1
while tot <= num:
    cont = 0
    while True:
        a  = randint(1, 60)
        if a not in sena:
            sena.append(a)
            cont += 1
        if cont >= 6:
            break
    sena.sort()
    cop.append(sena[:])
    sena.clear()
    tot += 1
for i, l in enumerate(cop):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*4, '< BOA SORTE >', '-='*4) 
