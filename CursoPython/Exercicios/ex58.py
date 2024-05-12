from random import randint, random
pensar = randint(0, 10)
n = 0
erro= 1
valor = 0
print("-=+" *20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=+" *20)
while n != 1:
    valor = int(input("Digite um numero de 0 a 10: "))
    if valor == pensar:
        print(f"Parabéns o numero era {valor}")
        n = 1
    else:
        print("Voce não acertou tente novamente: ")
        erro += 1
if erro == 1:
    print("Vc acertou de primeira!")
else:
    print(f"Vc acertou na tentativa numero {erro}")