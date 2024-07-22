import uteis1

num = float(input('Digite o preço: R$'))

print(f'A metade de {uteis1.moeda(num)} é {uteis1.moeda(uteis1.metade(num))}')
print(f'O dobro de {num} é {uteis1.moeda(uteis1.dobro(num))}')
print(f'Aumentando 10%, temos {uteis1.moeda(uteis1.aumento(num, 10))}')
print(f'Diminuição 10%, temos {uteis1.moeda(uteis1.dimunuir(num, 10))}')