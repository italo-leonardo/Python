#maiusculas e minusculas
#simbolos e espacos

'''
Security = chave
5ecut1ty = senha

'''

chave = input('Digite a base da sua senha: ')

senha = ''

for letra in chave:
    if letra in 'Aa': senha = senha + '0'
    elif letra in 'Bb': senha = senha + '1'
    elif letra in 'Cc': senha = senha + '2'
    elif letra in 'Dd': senha = senha + '8'
    elif letra in 'Ee': senha = senha + '4'
    elif letra in 'Ff': senha = senha + '#'
    elif letra in 'Rr': senha = senha + '$'
    elif letra in ' ': senha = senha + '_'
    else: senha = senha + letra
print(senha)
    