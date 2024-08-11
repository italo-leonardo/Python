'''tupla = ('item1', 'item2', 'item3', 'item1')
lista = ['item1', 'item2', 'item3']
print(tupla)
print(type(tupla))
print(type(lista))'''

#print(tupla[2])

#print(tupla.count('item1')) # verificar quantas vezes um item se repete

"""tupla = ('item3', 'item4', 'verde')
print(tupla)"""

'''tupla = (3, 5.9, True, 'item')
print(tupla)
print(type(tupla))
lista = list(tupla)
print(lista)
print(type(lista))'''

'''tupla = ('item1', )
tupla2 = ('a', 'b')

tupla = tupla * 3
print(tupla)

for v in tupla:
    print(v)'''

tupla = ('item1', 'item2', 'item3', 'item1')
'''(x, y, z, p) = tupla
print(x)
print(y)
print(z)
print(p)'''
(x, *y, z) = tupla
print('X:', x)
print('Y:', y)
print('Z:', z)