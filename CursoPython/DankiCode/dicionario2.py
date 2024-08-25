dicio = {"nome": "Italo", "ano": 2001, "valor_logico": True}
print(dicio)

dicio['nome'] = 'Marcos'
print(dicio)

dicio.update({'nome': 'Ana'})
print(dicio)

dicio['idade'] = 22 # adiconar novos valores
print(dicio)

dicio.update({'estado': 'Sao Paulo'})
print(dicio)

"""dicio.popitem() # remove o ultimo valor da lista
print(dicio)

dicio.pop('nome')
print(dicio)

dicio.clear()
print(dicio)"""

'''for x, y in dicio.items():
    print(x, y)'''

dicio2 = dicio.copy()
print(dicio2)

dicio3 = dict(dicio)
print(dicio3)


