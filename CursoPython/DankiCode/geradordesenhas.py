#maiusculas e minusculas
#simbolos e espacos

'''
Security = chave
5ecut1ty = senha

'''

chave = input('Digite a base da sua senha: ')

senha = ''

for letra in chave:
    if letra in 'Aa': senha = senha + '10'
    elif letra in 'Bb': senha = senha + '11'
    elif letra in 'Cc': senha = senha + '12'
    elif letra in 'Dd': senha = senha + '13'
    elif letra in 'Ee': senha = senha + '14'
    elif letra in 'Ff': senha = senha + '#'
    elif letra in 'Rr': senha = senha + '$'
    else: senha = senha + letra
print(senha)
    