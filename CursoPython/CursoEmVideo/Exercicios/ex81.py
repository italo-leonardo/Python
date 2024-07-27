lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    op = input('Quer continuar? [S/N]').upper()
    if op != 'S':
        break
print(f'Você digitou {len(lista)} alementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem descrecente são {lista}')
'''for v in lista:
    if v == 5:
        print('O Valor 5 faz parte da lista na posição :')
        break
    else:
        if v == num and num != 5:
            print('Valor 5 não se encontra na lista:')'''
if 5 in lista:
    print('O Valor 5 faz parte da lista na posição :')
else:
    print('Valor 5 não se encontra na lista:')