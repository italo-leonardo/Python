"""primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
pula = 0
guarda = 0
termos = 0
while cont < 10:
    soma = primeiro + pula
    pula += razao
    print(soma, end=" ->")
    guarda = soma
    cont += 1
    termos +=1 
print("PAUSA")
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
            termos +=1
    print("PAUSA")
    pert = int(input("\nQuantos termos a mais deseja ver: "))
print(f'Progressão finalizada com {termos} termos mostrados.')"""

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
pula = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        soma = primeiro + pula
        pula += razao
        print(soma, end=" ->")
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostra a mais? "))
print(f'Progressão finalizada com {total} termos mostrados.')
