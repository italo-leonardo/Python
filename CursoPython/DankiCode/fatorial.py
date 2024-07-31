'''
Como achar o fatorial de um numero
'''
fat = 1

n = int(input('Insira um numero: '))

if n < 0:
    print('Nao existe fatorial de numeros negastivos')
elif n == 0:
    print(f'O fatorial de {n} eh 1')
else:
    for x in range(1, n+1):
        fat = fat * x
print(f'O fatorial de {n} eh {fat}')