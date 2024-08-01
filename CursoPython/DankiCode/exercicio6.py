for x in range(5):
    n = int(input('Digite um numero: '))
    if x == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'O manior valor eh {maior}')
print(f'O menor valor eh {menor}')
