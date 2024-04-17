n = int(input('Digite um número: '))
for num in range(1, n+1):
    if num > 1:
        for c in range(2, num):
            if (num % c) == 0:
                break
        else:
            print(num)
print('Todos os numeros acima são os números primos entre 1 e',n)