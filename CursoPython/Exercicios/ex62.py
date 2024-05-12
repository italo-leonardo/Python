primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
pula = 0
guarda = 0
while cont < 3:
    soma = primeiro + pula
    pula += razao
    print(soma, end=" ->")
    guarda = soma
    cont += 1
print("FIM")
pert = int(input("\nQuantos termos a mais deseja ver: "))
while pert > 0:
    if pert != 0:
        cont = 0
        soma = 0
        pula = 0
        while pert > cont:
            pula = razao
            soma = guarda + pula
            print(soma, end=" ->")
            guarda = soma
            cont += 1
    pert = int(input("\nQuantos termos a mais deseja ver: "))
print('FIM DO PROGRAMA')
