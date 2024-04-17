n = int(input('Digite um numero inteiro: '))
for c in range(1, n+1):
    s = 0
    for digito in str(c):
        s += int(digito)
    if c % s == 0:
        print(c)
print('Todos os numeros acima são numeros de Harshad, entre 1 e',n)
