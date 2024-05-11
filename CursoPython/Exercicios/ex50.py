s = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0: # verificar se o numero é par.
        s += n # fazer a soma dos numeros pares.
print(s)
