from random import randint #Gerar numero aleatorio.
print("-="*20)
print("VAMOS JOGAR PAR OU IMPAR")
print("-="*20)
cont = 0
opcao = ''
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 11)
    soma = jogador + computador
    opcao = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    while opcao not in "PI":
        opcao = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o Computador {computador}. Total de {soma} ", end="")
    print("DEU PAR" if soma % 2 == 0 else "DEU IMPAR")
    if opcao == "P":
        if soma % 2 == 0:
            print("Vocẽ VENCEU")
            cont += 1
        else:
            print("Você PERDEU!")
            break
    elif opcao == "I":
        if soma % 2 == 1:
            print("Vocẽ VENCEU")
            cont += 1
        else:
            print("Você PERDEU!")
            break
    print("vamos jogar novamente...")
print(f"GAME OVER! você venceu {cont} vezes.")
