maior = 0
menor = 0
for c in range(1, 4):
    peso = float(input(f'Digite o {c}º peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é {maior}Kg")
print(f"O menor peso é {menor}Kg")

