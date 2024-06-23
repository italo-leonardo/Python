num = int(input())
cid = ''
des = [[61, 'Brasilia'], [71, 'Salvador'],
[11, 'Sao Paulo'], [21, 'Rio de Janeiro'],
[32, 'Juiz de Fora'], [19, 'Campinas'], 
[27, 'Vitoria'], [31, 'Belo Horizonte']]

for d in des:
    if num == d[0]:
       cid = d[1]

if cid != '':
    print(cid)
else:
    print('DDD nao cadastrado caso')
    
        