import uteis1

num = float(input('Digite o preço: R$'))

print(f'A metade de {(num)} é {uteis1.metade(num, True)}')
print(f'O dobro de {num} é {uteis1.dobro(num, True)}')
print(f'Aumentando 10%, temos {uteis1.aumento(num, 10, True)}')
print(f'Diminuição 10%, temos {uteis1.dimunuir(num, 10, True)}')