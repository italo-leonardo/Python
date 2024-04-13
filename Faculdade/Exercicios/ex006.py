idade = int(input("Digite seu idade: "))

if idade <= 12:
    print("Criança")
if idade >= 13 and idade <= 19:
    print("Adolescente")
if idade >= 20 and idade <= 59:
    print("Adulto")
if idade >= 60:
    print("idoso")