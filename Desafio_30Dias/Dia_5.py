def ler_nota():
    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            return nota
        else:
            print("nota invalida")

def calcular_media():
    nota1 = ler_nota()
    nota2 = ler_nota()
    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")

def novo_calculo():
    while True:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 1 or x == 2:
            return x
        else:
            continue

while True:
    calcular_media()
    if novo_calculo() == 2:
        break
