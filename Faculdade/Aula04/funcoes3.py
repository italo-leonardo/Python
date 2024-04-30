def linha(quantidade, texto):
    for i in range(quantidade):
        print(texto, end="")
    print("")

print("AULA DE LAB. PROGRAMAÇÃO")
linha(int(input("Digite um valor:")), "@")
print("PROF. CAETANO")
linha(15, "*")
print("AULA NA UNIFAP")
linha(20, "$")