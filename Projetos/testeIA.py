def ponto():
    print('-=' * 15)

def arredondar(media):
    prime_decimal = int(media * 10) % 10
    cont = 0
    if 2 <= prime_decimal <= 5:
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
    return media + (cont / 10)

disciplina = input('Digite o nome da Disciplina: ')
av1 = float(input('Digite seu nota da AV1: '))
av2 = float(input('Digite seu nota da AV2: '))
tde1 = float(input('Digite seu nota do TDE1: '))
tde2 = float(input('Digite seu nota do TDE2: '))
tde3 = float(input('Digite seu nota do TDE3: '))
tde4 = float(input('Digite seu nota do TDE4: '))

media = (av1 * 0.4) + (av2 * 0.4) + (0.05 * (tde1 + tde2 + tde3 + tde4))
media_final = arredondar(media)

ponto()
print(f'{"SIMULADOR DE NOTAS":^30}')
ponto()
print()

print(f'Média calculada: {media:.10f}'.split('.')[0] + '.' + f'{media:.10f}'.split('.')[1][0])

if media_final >= 7.0:
    print(f'Você está aprovado(a) em {disciplina} com a média {str(media_final).split(".")[0]}.{str(media_final).split(".")[1][0]}.')
elif 4.0 <= media_final < 7.0:
    print(f'Boa sorte na AVF de {disciplina}, sua média foi {str(media_final).split(".")[0]}.{str(media_final).split(".")[1][0]}.')
    print('Você precisa de 4.0 na prova para ser aprovado(a)!')
else:
    print(f'Reprovado(a) com média {str(media_final).split(".")[0]}.{str(media_final).split(".")[1][0]}.')
    print(f'Você está devendo {disciplina} agora!')

