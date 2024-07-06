pessoas = dict()
galera = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = (str(input('Nome: ')))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        op = input('Quer continuar? [S/N] ').upper()
        if op in 'SN':
            break
        print('ERRO! Resposta apenas S ou N.')
    if op == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
