n = int(input('Digite um numero: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n')
print('O numero {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('È por isso que ele é PRIMO!')
else:
    print('È por isso que ele Não é PRIMO!')

       