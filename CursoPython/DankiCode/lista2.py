lista = ['carro', 'barco', 'aviao']
print(lista)

'''for x in range(len(lista)):
    print(x, lista[x]) 

texto = 'meunome@gmail.com'
lista2 = list(texto)
print(lista2)

texto = texto.split('@')
print(texto)'''

'''lista.append('moto') # adicionar elemento na lista
print(lista)

lista.append(['bicicleta', 'navio'])
print(lista)'''
 
'''lista.insert(0, 'bicicleta') #inserie valores entre index
print(lista)'''

lista.extend(['bicicleta', 'navio']) # pdoe adixionar varios valores dentro da lista
print(lista)

for x in range(len(lista)):
    print(x, lista[x]) 
