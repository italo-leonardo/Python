soma = 0
while True:
    cont = int(input("Digite um valor: "))
    if cont == 999:
        break
    soma += cont
print(f"A soma de todos os valores é {soma}")