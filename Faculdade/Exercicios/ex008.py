n1 = int(input("Digite um numero: "))
n2 = int(input("Digite segundo numero: "))
n3 = int(input("Digite terceiro numero: "))
maior = n1

if maior < n2:
    maior = n2
if maior < n3:
    maior = n3

print("O maior numero é", maior)

