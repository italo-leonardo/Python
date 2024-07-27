'''from random import randint
lista = randint(0,10), randint(0,10),randint(0,10),randint(0,10)
maior = lista[0]
menor = lista[0]
print(f'Os Valores sorteados foram: {lista}')
if lista[0] >= lista[1] and lista[0] >= lista[2] and lista[0] >= lista[3]:
    maior = lista[0]
elif lista[1] >= lista[0] and lista[1] >= lista[2] and lista[1] >= lista[3]:
    maior = lista[1]
elif lista[2] >= lista[0] and lista[2] >= lista[1] and lista[2] >= lista[3]:
    maior = lista[2]
elif lista[3] >= lista[0] and lista[3] >= lista[1] and lista[3] >= lista[2]:
    maior = lista[3]
print(f'O maior valor sorteado foi {maior}')
if lista[0] <= lista[1] and lista[0] <= lista[2] and lista[0] <= lista[3]:
    menor = lista[0]
elif lista[1] <= lista[0] and lista[1] <= lista[2] and lista[1] <= lista[3]:
    menor = lista[1]
elif lista[2] <= lista[0] and lista[2] <= lista[1] and lista[2] <= lista[3]:
    menor = lista[2]
elif lista[3] <= lista[0] and lista[3] <= lista[1] and lista[3] <= lista[2]:
    menor = lista[3]
print(f'O menor valor sorteado foi {menor}')'''
from random import randint

# Gerar uma tupla de valores aleatórios
valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

# Inicializar as variáveis maior e menor com o primeiro valor da tupla
maior = menor = valores[0]

# Encontrar o maior e o menor valor manualmente
for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

# Exibir os resultados
print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
