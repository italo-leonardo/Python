#Tuplas são imutaveis.
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Refri')
'''print(lanche[0:])'''
#print(len(lanche))
'''for c in lanche:
    print(f'Eu vou comer {c} um ', end='')
    if c == "Suco" or c == 'Refri':
        print('Liquido')
    else:
        print('Solido')'''
#lanche[1] = 'Refrigerate' Não da certo 
'''for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c} é um ', end='')
    if c == 1 or c == 4:
        print('Liquido')
    else:
        print('Solido')
print('Comi muito!!')'''

#print(sorted(lanche)) #Ordenado
#print(lanche) #Normal

'''a = (2, 5, 4)
b = (5, 8, 1, 3)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))'''

pessoa = ('Italo', 22, 'M', 70.36)
del(pessoa) # deleta em python 
pessoa = ('Marcos', 23, 'M', 70.36)
print(pessoa)
pessoa1 = str(input('Nome: ')), int(input('idade: '))
print(pessoa1)
c = pessoa1[1] + 10
print(c)