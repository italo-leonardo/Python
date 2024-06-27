'''dados = dict()
dados = {'nome':'pedro','idade':25}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
print(dados)
del dados['idade'] # Eliminar elementos
print(dados)'''

'''filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
}
print(filme.values()) # Retorna os valores
print(filme.keys()) # Retorna as chaves ou ID
print(filme.items()) # Retorna valores e chaves
for k, v in filme.items():
    print(f'O {k} é {v} ')'''

'''locadora = [{'titulo':'Star Wars', 'ano':1977, 'didreto':'Georde Lucas'},
            {'titulo':'Avengers', 'ano':2012, 'didreto':'Joss Whedon'},
            {'titulo':'Matrix', 'ano':1999, 'didreto':'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[0].values())
print(locadora[2].items())'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())  
for k in pessoas.keys():
    print(k)
print('-='*30)
for v in pessoas.values():
    print(v)
print('-='*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)
del pessoas['sexo']
pessoas['nome'] = 'Italo' # Modificar valores
pessoas['peso'] = 75.6 # adicionar valores
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[1]['uf'])'''

brasil = list()
for c in range(0, 3):
    estado = dict()
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print(len(brasil))
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')