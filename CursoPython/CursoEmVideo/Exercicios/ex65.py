perg = "S"
cont = soma = media = maior = menor= 0
while perg in "Ss":
    num = float(input("Digite um número: "))
    perg = input("Quer continuar? [S/N] ")
    cont +=1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f"Você digitou {cont} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
