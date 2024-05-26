n = int(input("Digite um numero [999 para parar]: "))
soma = cont = 0
while n != 999:
    if n != 999:
        soma += n
    n = int(input("Digite um numero [999 para parar]: "))
    cont += 1
print(f"Você digitou {cont} e a soma entre eles foi {soma}.")