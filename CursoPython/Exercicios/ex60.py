n = int(input("Digite um número: "))
salva = n
fato = 1
print(f'Canculando {n}! = ')
while salva > 0:
    print(f'{salva}', end='')
    print('x' if salva > 1 else '=', end='')
    fato *= salva
    salva -= 1
print(fato)


