'''lista = ['a', 'b', 'c']
lista2 = [1, 2, 3]'''

'''lista = lista + lista2
print(lista)'''

'''lista.extend(lista2)
print(lista)'''

'''for x in lista2:
    lista.append(x)

print(lista)'''

lista = ['a', 'b', 'c']
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.append('d')
print(lista)
print(lista2)