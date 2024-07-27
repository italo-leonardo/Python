valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
        op = input('Que continuar? [S/N]').upper()
        if op == 'S':
            continue
        else:
            break 
    else:
        print('Valor duplicado! Não vou adiconar...')
        op = input('Que continuar? [S/N]').upper()
        if op == 'S':
            continue
        else:
            break 
        
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')

