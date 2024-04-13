n = int(input('Digite um numero: '))
s = 0
for c in range(1, 11):
    s = c * n
    print('{} * {} = {}'.format(c, n, s))  