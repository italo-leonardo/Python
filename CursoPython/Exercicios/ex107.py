import uteis1

num = float(input('Digite o preço: R$'))

print(f'A metade de R${num} é R${uteis1.metade(num)}')
print(f'O dobro de R${num} é R${uteis1.dobro(num)}')
print(f'Aumentando 10%, temos R${uteis1.aumento(num)}')
print(f'Diminuição 10%, temos R${uteis1.dimunuir(num)}')