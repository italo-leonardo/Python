valores = []
mai = 0 
men = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite o valor para a Posição {i}: ')))
    if i == 0:
        mai = men = valores[i]
    else:
        if valores[i] > mai:
            mai = valores[i]
        if valores[i] < men:
            men = valores[i]
print(f'Você digitou os valotes {valores}')
print(f'O maior valor digitado foi {mai} na posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} na posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
