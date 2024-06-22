def ponto():
    print('-='*15)

cont = 0
disciplina = str(input('Digite o nome da Disciplina: '))
av1 = float(input('Digite seu nota da AV1: '))
av2 = float(input('Digite seu nota da AV2: '))
tde1 = float(input('Digite seu nota do TDE1: '))
tde2 = float(input('Digite seu nota do TDE2: '))
tde3 = float(input('Digite seu nota do TDE3: '))
tde4 = float(input('Digite seu nota do TDE4: '))

media = ((av1 * 0.4) + (av2 * 0.4)) + (0.05 * (tde1 + tde2 + tde3 + tde4) )
media_dois = media % 10   
prime_decimal = int(media * 10) % 10

if prime_decimal >= 2 and prime_decimal <= 5:
    while prime_decimal != 5:
        prime_decimal += 1
        cont += 1
elif prime_decimal >= 7:
    while prime_decimal != 10:
        prime_decimal += 1
        cont += 1
    prime_decimal /= 10
else: 
    prime_decimal -= 1
    cont -= 1
media_final = media_dois + (cont / 10)
    

ponto()
print(f'{"SIMULADOR DE NOTAS":^30}')
ponto()
print()
print(media)
if media_final >= 7.0:
    print(f'Voçê esta aprovoda em {disciplina} com a media {media_final:.1f}.')
elif media_final >= 4.0 and media_final < 7:
    print(f'Boa sorte na AVF de {disciplina} sua media foi {media_final:.1f}.')
    print('Precisa de 4.0 na prova para ser aprovado!!')
else:
    print(f'Reprovado com media {media_final:.1f}.')
    print(f'Esta devendo {disciplina} agora!.')
