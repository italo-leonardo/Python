num = [[], []]
valor = 0
for n in range(0, 7):
    valor = int(input(f'Digite o {n+1}ª. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' *30)
num[0].sort()
num[1].sort()
print(f'Todos os valores pares são: {num[0]}')
print(f'Todos os valores impares são: {num[1]}')

