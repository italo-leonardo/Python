aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['Media'] = float(input(f'Média de {aluno['nome']}: '))
print(f'O Nome é igual a {aluno["nome"]}')
print(f'A Média é igual a {aluno["Media"]}')
if aluno['Media'] >= 7.0:
    print('Situação é igual a Aprovada')
    aluno['situacao'] = str('Aprovado')
else:
    print('Situação é igual a Reprovado')
    aluno['situacao'] = str('Reprovado')
print(aluno)