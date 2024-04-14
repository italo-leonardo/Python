maior = 0
menor = 99999
for c in range(0, 3):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        peso = menor
print(maior)
print(menor)

