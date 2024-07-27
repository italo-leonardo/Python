'''pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''

'''teste= list()
teste.append('Italo')
teste.append(22)
galera = list()
galera.append(teste[:]) #Copia os dados para outra lista [:]
teste[0] = 'jhuly'
teste[1] = 20
galera.append(teste[:])
print(galera)'''

'''pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # limpar dados

print(f'Dado: {dado}')
print(f'Galera: {galera}')

totmai = totmeno = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade>')
        totmeno += 1
print(f'Tem {totmai} maior de idade')
print(f'Tem {totmeno} menor de idade')
