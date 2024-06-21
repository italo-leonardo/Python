num = [2, 5 ,9 , 1]
num[2] = 10 # subistituir valores da lista
num.append(7) #Adicionar valores a lista
num.sort(reverse=True) # deixar a lista em ordem
num.insert(1,10) # Inserir valores entra valores
num.pop() # remove o valor
if 8 in num:
    num.remove(8) # remove valores procurando do inicio a lista apenas um
else:
    print('Não achei o valor!')
print(num)
print(f'Essa lista tem {len(num)} elementos. ')

'''valores = []
valores.append(int(input('Digite um valor: ')))
valores.append(9)
valores.append(4)
valores.sort(reverse=True)

for v in valores:
    print(f'{v}...', end='')
print()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')'''

'''a = [2, 3, 4, 7]
b = a[:] # Gerando uma copia a lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''