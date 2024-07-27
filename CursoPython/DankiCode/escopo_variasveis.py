#Escopo de variaves

"""
as variaveis globais

as veriaveis locais
"""

x = 5 

def funcao():
    x = 3
    print(f'Valor de variavel local: {x}')

funcao()
print(f'Valor de variavel global: {x}')