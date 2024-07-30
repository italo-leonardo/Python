'''
do while
Codigo para adivinhar um numero
'''

p = 5
n = 9

while bool(p) is True:
    print('Qual o numero correto? ')
    p = int(input())
    if p == n:
        print('Parabens voce acertou!')
        break
    else:
        print('Voce errou')
