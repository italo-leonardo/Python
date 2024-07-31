'''
Descobrir se um numero eh primo

'''

n = int(input('Digite um numero: '))

if n > 1:
    for x in range(2, n):
        if n % 2 == 0:
            print('Esse nao eh um numero primo')
            break
    else:
        print('Esse numero eh primo')
else:
    print('Esse numero nao eh primo')