lista = []
lista_par = []
lista_imap = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
            lista_par.append(num)
    else:
        lista_imap.append(num)
    op = input('Quer continuar [S/N]: ').upper()
    if op != 'S':
        break
        
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_imap}')
    

