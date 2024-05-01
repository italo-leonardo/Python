def verifica_sinal(numero):
    if numero > 0:
        return True
    else:
        return False

if verifica_sinal(int(input("Digite um valor: "))):
    print("É POSITIVO")
else:
    print("È NEGATIVO")