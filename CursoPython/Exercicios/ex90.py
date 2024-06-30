aluno = dict()
aluno['Nome'] = str(input('Nome:'))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7.0:
    aluno['Situacao'] = str('Aprovado')
else:
    aluno['Situacao'] = str('Reprovado')
print('-='*30)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')