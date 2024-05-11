n = 0
sexo = input("Digite seu SEXO [M/F]: ").upper()
while n != 1:
    if sexo == "M":
        print("Você é um HOMEM")
        n = 1
        print("FIM")
    if sexo == "F":
        print("Voê é uma MULHER")
        n = 1
        print("FIM")
    if sexo != "M" and sexo != "F":
        print("Volar digitado errado: ")
        sexo = input("Digite seu SEXO [M/F]: ").upper()

