def linha(quantidade=15, texto="*"):
    for i in range(quantidade):
        print(texto, end="")
    print("")

print("AULA DE LAB. PROGRAMAÇÃO")
linha(int(input("Digite um valor:")), input("Digite um texto: "))
print("PROF. CAETANO")
linha(15)
print("AULA NA UNIFAP")
linha(20, "$")
print("AULA DA TERÇA")
linha()