primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
pula = 0
while cont < 10:
    soma = primeiro + pula
    pula += razao
    print(soma, end=" ->")
    cont += 1
print("FIM")