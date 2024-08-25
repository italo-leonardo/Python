'''Lista: Colecao ordenada, mutavel e que permite valores duplicados
Tuplas: Colecao ordenada, imutavel e que permite valores duplicados
Dicionarios: Colecao nao ordenada, mutavel e que nao permite valores duplicados'''


dicio = {"chavel": "Italo", "chave2": 2001, "chave3": True}

dicionario = {
    "nome": 'Pedro',
    "idade": 20,
    "nacionalidade": 'brasileiro'
}

print(dicionario)

print(dicionario["idade"])

print(dicionario.get('nome'))

print(dicionario.keys()) # retorna as chaves 

print(len(dicionario))

print(dicionario.values()) # retorna os valores das keys = (chave).

if 'idade' in dicionario:
    print('A chave idade existe')

print(dicionario.items())