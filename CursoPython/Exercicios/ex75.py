lista = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
lista2 = 0
cont9 = cont3 = 0

for valor in lista:
    if valor == 9:
        cont9 += 1
    if valor % 2 == 0:
        lista2 += valor

print(f'Você digitou os valores: {lista}')
print(f'O valor 9 apareceu {cont9} vezes')
print(f'O valor 3 {cont3}')
print(f'Os valores pares digitados foram {lista2}')
