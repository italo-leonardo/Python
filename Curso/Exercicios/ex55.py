maior = 0
for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    menor = peso
    if peso > maior:
        maior = peso
print(maior)

