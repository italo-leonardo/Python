n1 = int(input("Digite um numero: "))
n2 = int(input("Digite segundo numero: "))
n3 = int(input("Digite terceiro numero: "))
menor = n1

if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

print("O menor numero é", menor)