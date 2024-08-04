lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 4, 5, 10]
print(lista2)

lista3 = [2.3, 4.5, 1.0]
print(lista3)

lista6 = lista2 + lista3
print(lista6 )

lista4 = [True, False]
print(lista4)

lista5 = [True, 'chicago', 2.5, False, 5]
print(lista5)

print(type(lista5))
print(lista5[0])
print(lista5[-1])

#Slicing
print(lista5[::]) # mostra todos os dados da lista
print(lista5[1: ]) # contaguem se inicia depois de index marcado
print(lista5[:3]) # retorna do comeco da lista ate o index -1
print(lista5[1:3]) # retonar o index escolhido ate o index final -1
print(lista5[0:5:2]) # retonar o index escolhodo pulando de 2

nome5 = 'Terra'
print(nome5[::])
print(nome5[2:4])

print(len(lista6)) # len ver tamanho da lista

# Funcoes que so pode ser utilizado com tidos de dados numerocos
print(lista6)
print(sum(lista6)) # soma dos valores numericos das listas
print(max(lista6)) # maior valor da lista
print(min(lista6)) # menor valor da lista

nome = 'Curso de Python'
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list(nome)
print(lista8)

elemento = 43
if elemento in lista7:
    print('Esta na lista')
else:
    print('Nao esta na lista')