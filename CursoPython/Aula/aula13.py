'''p = int(6/3)
for c in range(10, 1, -p):
    print(c)
print('FIM')'''

'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''

'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0
p = 1 
for c in range(0 , 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {} e p = {}'.format(s, p))