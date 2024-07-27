def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor um número inteiro válido.\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor um número real válido\033[m')
            continue 
        else:
            return n   

num = leiaInt('Digite um valor inteiro: ')
flu = leiaFloat('Digite um valor real: ')
print(f'O valor interio foi {num} e o valor real {flu}.')
