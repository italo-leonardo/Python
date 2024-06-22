def ponto():
    print('-='*15)

disciplina = str(input('Digite o nome da Disciplina: '))
av1 = float(input('Digite seu nota da AV1: '))
av2 = float(input('Digite seu nota da AV2: '))
tde1 = float(input('Digite seu nota do TDE1: '))
tde2 = float(input('Digite seu nota do TDE2: '))
tde3 = float(input('Digite seu nota do TDE3: '))
tde4 = float(input('Digite seu nota do TDE4: '))

media = ((av1 * 0.4) + (av2 * 0.4)) + (0.05 * (tde1 + tde2 + tde3 + tde4) ) 

ponto()
print(f'{"SIMULADOR DE NOTAS":^30}')
ponto()
print()
if media >= 7.0:
    print(f'Voçê esta aprovoda em {disciplina} com a media {media:.1f}.')
elif media >= 4 and media < 7:
    print(f'Boa sorte na AVF de {disciplina} sua media foi {media:.1f}.')
    print('Precisa de 4.0 na prova para ser aprovado!!')
else:
    print(f'Reprovado com media {media:.1f}.')
    print(f'Esta devendo {disciplina} agora!.')
