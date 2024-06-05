preco = total = totmil = menor = cont = 0
resp = barato = ""
while True:
    print('-'*30)
    print('LOJA SUPER BERATÃO')
    print('-'*30)
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
        barato = nome
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if resp == "N":
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')
