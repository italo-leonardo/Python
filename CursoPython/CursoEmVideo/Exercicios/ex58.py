'''from random import randint
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
    print(f"Vc acertou na tentativa numero {erro}")'''

from random import randint
computador = randint(0, 10)
print("-=+" *20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=+" *20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print('Menos... Tenta mais uma vez.')
print(f"Acertou com {palpites} palpites!")